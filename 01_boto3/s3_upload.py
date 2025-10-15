# s3_upload.py

# 실습1. 신짱구.png를 같은 key로 업로드 후 버전 확인
# 실습2. 신짱구.png를 jjanggu.png로 업로드 후 버전 확인, 기존에 띄워둔 EC2 서버의 HTTP 주소 확인

# pip install boto3
# File Upload
# file_name = Upload한 파일이 저장된 위치를 지정한다, 상대 경로는 실행하는 코드를 기준으로 한다
# bucket = 업로드 할 버킷의 이름을 지정한다
# key = 업로드 되어 버킷에서 해당 파일이 가질 키를 지정한다
import boto3
from dotenv import load_dotenv
import os

# .env 파일 로드
load_dotenv()

# AWS S3 버킷 사용
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
BUCKET_NAME = os.getenv("BUCKET_NAME")
AWS_DEFAULT_REGION = os.getenv("AWS_DEFAULT_REGION")
AWS_STORAGE_OVERRIDE = False  # 기존의 파일을 덮어쓰는 것을 허용할지 여부를 결정


file_name = './jjanggu.png'
bucket = BUCKET_NAME 
key = 'uploads/test.png'

# Upload the file

#자격 증명 
s3_client = boto3.client(
's3',
aws_access_key_id=AWS_ACCESS_KEY,
aws_secret_access_key=AWS_SECRET_KEY,
region_name=AWS_DEFAULT_REGION
)
res = s3_client.upload_file(file_name, bucket, key)