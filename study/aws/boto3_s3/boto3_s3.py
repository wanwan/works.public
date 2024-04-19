#!/usr/bin/python

import boto3

# Let's use Amazon S3 
s3 = boto3.resource('s3')

my_bucket = s3.Bucket('wanwanbucket3')
print(my_bucket.name)

for bucket in my_bucket.objects.all():
	print(bucket.key)

with open('test.txt', 'rb') as data:
	my_bucket.put_object(Key='test.txt', Body=data)
