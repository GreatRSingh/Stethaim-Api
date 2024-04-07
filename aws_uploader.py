import boto3

# Let's use Amazon S3
#s3 = boto3.resource('s3')

# Print out bucket names
#for bucket in s3.buckets.all():
#    print(bucket.name)

# Upload a new file
#with open('test.jpg', 'rb') as data:
#    s3.Bucket('my-bucket').put_object(Key='test.jpg', Body=data)

s3 = boto3.resource('s3')

def upload_file(file_name):
    with open(f'data/{file_name}', 'rb') as data:
        s3.Bucket('stethaim').put_object(Key=f'{file_name}', Body=data)
