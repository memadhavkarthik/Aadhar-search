import os
from flask import Flask, render_template, request, redirect, url_for
import boto3

app = Flask(__name__)

# AWS S3 configuration
S3_BUCKET = 'aadhardemo'
S3_REGION = 'US East (Ohio) us-east-2'

# AWS credentials (ensure these are set in your environment or provide them directly)
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')

# Configure AWS S3 client
s3_client = boto3.client('s3',
                         aws_access_key_id=AWS_ACCESS_KEY_ID,
                         aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                         region_name=S3_REGION)


@app.route('/')
def index():
  return render_template('upload.html')


@app.route('/upload', methods=['POST'])
def upload():
  if 'file' not in request.files:
    return redirect(url_for('index'))

  file = request.files['file']
  if file.filename == '':
    return redirect(url_for('index'))

  # Upload the file to S3 bucket
  s3_client.upload_fileobj(file, S3_BUCKET, file.filename)

  return 'File uploaded successfully'


if __name__ == '__main__':
  app.run()
