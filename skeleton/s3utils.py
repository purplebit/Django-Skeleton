import os
from datetime import datetime
from skeleton.settings import AWS_STORAGE_BUCKET_NAME
from storages.backends.s3boto import S3BotoStorage
from django.utils.functional import SimpleLazyObject

StaticRootS3BotoStorage = lambda: S3BotoStorage(location='static')

# For media uploads:
S3URL = 'https://s3.amazonaws.com/'
S3Bucket = AWS_STORAGE_BUCKET_NAME
S3BucketBasePath = '/media/'

def stripBaseURL(url):
    if url == "":
        return url
    parts = url.split(S3URL + S3Bucket + S3BucketBasePath)
    if len(parts) != 2 or parts[0] != '':
        raise Exception('stripBaseURL: Illegal baseURL sent')
    return parts[1]

def addBaseURL(url):
    if url == "":
        return url
    return S3URL + S3Bucket + S3BucketBasePath + url
