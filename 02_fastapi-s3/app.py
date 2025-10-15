# upload_file은 로컬에 있는 파일을 경로로 업로드하는 함수고, upload_fileobj는 바이트스트림으로 읽어서 바로 업로드하는 메서드

from fastapi import FastAPI, UploadFile, File, HTTPException, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
import boto3
import os
import logging

load_dotenv()

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
BUCKET_NAME = os.getenv("BUCKET_NAME")
AWS_DEFAULT_REGION = os.getenv("AWS_DEFAULT_REGION")

s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=AWS_DEFAULT_REGION,
)

app = FastAPI()
# templates = Jinja2Templates(directory="templates")

@app.post("/upload_rest")
async def upload_file_rest(file: UploadFile = File(...), key: str | None = None):
    """
    POST multipart/form-data로 파일을 업로드하면 S3에 저장합니다.
    (옵션) key 파라미터로 S3 키 지정 가능. 지정하지 않으면 uploads/{원본파일명}
    """
    bucket = BUCKET_NAME
    s3_key = key or f"uploads/{file.filename}"

    try:
        # 업로드 전에 파일 포인터를 처음으로 이동
        file.file.seek(0)
        # content type 전달하려면 ExtraArgs 사용
        s3_client.upload_fileobj(
            Fileobj=file.file,
            Bucket=bucket,
            Key=s3_key,
            ExtraArgs={"ContentType": file.content_type} if file.content_type else None,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        await file.close()

    return {"bucket": bucket, "key": s3_key, "filename": file.filename, "content_type": file.content_type}


# @app.get("/")
# async def form(request: Request):
#     # 업로드 폼 렌더링
#     return templates.TemplateResponse("index.html", {"request": request})


# @app.post("/upload")
# async def upload_file(request: Request, file: UploadFile = File(...), key: str | None = None):
#     """
#     multipart/form-data로 받은 파일을 S3에 upload_fileobj로 바로 업로드하고,
#     템플릿에 결과를 렌더링합니다.
#     """
#     bucket = BUCKET_NAME
#     s3_key = key or f"uploads/{file.filename}"

#     try:
#         # 업로드 전에 파일 포인터를 처음으로 이동
#         file.file.seek(0)

#         extra_args = {}
#         if file.content_type:
#             extra_args["ContentType"] = file.content_type

#         # upload_fileobj 호출 (ExtraArgs 있을 때만 전달)
#         if extra_args:
#             s3_client.upload_fileobj(Fileobj=file.file, Bucket=bucket, Key=s3_key, ExtraArgs=extra_args)
#         else:
#             s3_client.upload_fileobj(Fileobj=file.file, Bucket=bucket, Key=s3_key)

#         # 가능한 경우 presigned URL 생성 (읽기용, 1시간 유효)
#         url = None
#         try:
#             url = s3_client.generate_presigned_url(
#                 "get_object",
#                 Params={"Bucket": bucket, "Key": s3_key},
#                 ExpiresIn=3600,
#             )
#         except Exception:
#             url = f"https://{bucket}.s3.amazonaws.com/{s3_key}"

#         # 버전 ID 확인 시도 (버전 관리 활성화된 경우)
#         version_id = None
#         try:
#             resp = s3_client.list_object_versions(Bucket=bucket, Prefix=s3_key)
#             versions = resp.get("Versions", [])
#             for v in versions:
#                 if v.get("IsLatest"):
#                     version_id = v.get("VersionId")
#                     break
#         except Exception:
#             version_id = None

#         result = {
#             "bucket": bucket,
#             "key": s3_key,
#             "file": file.filename,
#             "version_id": version_id,
#             "url": url,
#         }
#         return templates.TemplateResponse("index.html", {"request": request, "result": result})

#     except Exception as e:
#         logging.exception("S3 업로드 실패")
#         error = str(e)
#         return templates.TemplateResponse("index.html", {"request": request, "error": error})
#     finally:
#         await file.close()