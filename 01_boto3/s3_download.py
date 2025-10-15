# s3_download.py

# File Download
# file_name = Download한 파일이 저장될 위치를 지정한다, 상대 경로는 실행하는 코드를 기준으로 한다
# bucket = 다운로드 할 버킷의 이름을 지정한다
# key = 다운로드 할 객체를 지정한다, image폴더 안의 파일을 가져온다
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



file_name = './신짱구2.png'
bucket =  BUCKET_NAME 
key ='uploads/test.png'


# Download the file
s3_client = boto3.client(
's3',
aws_access_key_id=AWS_ACCESS_KEY,
aws_secret_access_key=AWS_SECRET_KEY,
region_name=AWS_DEFAULT_REGION
)
s3_client.download_file(bucket, key, file_name)