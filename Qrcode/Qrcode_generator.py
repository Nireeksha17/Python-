#generating Qr Code filecreation inside the S3 bucket.
import qrcode
import image
import os
import boto3
from dotenv import load_dotenv
import s3fs


load_dotenv()
access_key = os.getenv("ACCESS_KEY")
secret_key = os.getenv("SECRET_KEY")



qr = qrcode.QRCode(
    version = 17,
    box_size= 10,
    border=10

)


data = "https://www.linkedin.com/in/nireekshapk/" # you can give a URL or a Plane text inside the quotes for Qr code creation

qr.add_data(data)
qr.make(fit=True)
image = qr.make_image(fill = "black",back_color = "white",)
image.save("test_qr.png")

s3 = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key)

s3.upload_file('E:/gitprojects/python/qr_generator/test_qr.png', 'finalbucket1forp1', 'test_qr.png')


