import uuid
import ibm_boto3
from ibm_botocore.client import Config
from ibm_botocore.exceptions import ClientError


def log_done():
    print("DONE!\n")

def log_client_error(e):
    print("CLIENT ERROR: {0}\n".format(e))

def log_error(msg):
    print("UNKNOWN ERROR: {0}\n".format(msg))

def get_uuid():
    return str(uuid.uuid4().hex)

# Retrieve the list of available buckets
def get_buckets():
    print("Retrieving list of buckets")
    try:
        bucket_list = cos_cli.list_buckets()
        for bucket in bucket_list["Buckets"]:
            print("Bucket Name: {0}".format(bucket["Name"]))
        
        log_done()
    except ClientError as be:
        log_client_error(be)
    except Exception as e:
        log_error("Unable to retrieve list buckets: {0}".format(e))

# Retrieve the list of contents for a bucket
def get_bucket_contents(bucket_name):
    print("Retrieving bucket contents from: {0}".format(bucket_name))
    try:
        file_list = cos_cli.list_objects(Bucket=bucket_name)
        for file in file_list.get("Contents", []):
            print("Item: {0} ({1} bytes).".format(file["Key"], file["Size"]))
        else:
            print("Bucket {0} has no items.".format(bucket_name))
        log_done()
    except ClientError as be:
        log_client_error(be)
    except Exception as e:
        log_error("Unable to retrieve bucket contents: {0}".format(e))

# Retrieve a particular item from the bucket
def get_item(bucket_name, item_name):
    print("Retrieving item from bucket: {0}, key: {1}".format(bucket_name, item_name))
    try:
        file = cos_cli.get_object(Bucket=bucket_name, Key=item_name)
        file1 = open("static/"+item_name,"wb")
        a = file.get('Body').read()
        file1.write(a)
        log_done()
        return 1
    except ClientError as be:
        log_client_error(be)
    except Exception as e:
        log_error("Unable to retrieve file contents for {0}:\n{1}".format(item_name, e))

# Constants for IBM COS values
COS_ENDPOINT = "https://s3.jp-tok.cloud-object-storage.appdomain.cloud" # example: https://s3.us-south.cloud-object-storage.appdomain.cloud
COS_API_KEY_ID = "o9uWNKIq0BU2ub8q92Qz4HydRJ_E0W9Rg6LM8XtQaMQI" # example: xxxd12V2QHXbjaM99G9tWyYDgF_0gYdlQ8aWALIQxXx4
COS_AUTH_ENDPOINT = "https://iam.cloud.ibm.com/identity/token"
COS_SERVICE_CRN = "crn:v1:bluemix:public:cloud-object-storage:global:a/bbb49d14dbaa4bb58c65afb8f4ac3c67:5f2526fc-cb8c-45da-94aa-a2a6dfc9be8f::"
# example: crn:v1:bluemix:public:cloud-object-storage:global:a/xx999cd94a0dda86fd8eff3191349999:9999b05b-x999-4917-xxxx-9d5b326a1111::
COS_STORAGE_CLASS = "Smart Tier" # example: us-south-standard

# Create client connection
cos_cli = ibm_boto3.client("s3",
    ibm_api_key_id=COS_API_KEY_ID,
    ibm_service_instance_id=COS_SERVICE_CRN,
    ibm_auth_endpoint=COS_AUTH_ENDPOINT,
    config=Config(signature_version="oauth"),
    endpoint_url=COS_ENDPOINT
)

# *** Main Program ***
def main():
    try:
        new_bucket_name = "py.bucket." + get_uuid()
        new_text_file_name = "py_file_" + get_uuid() + ".txt"
        new_text_file_contents = "This is a test file from Python code sample!!!"
        new_large_file_name = "py_large_file_" + get_uuid() + ".bin"
        new_large_file_size = 1024 * 1024 * 20 

        get_buckets()

        get_bucket_contents("assignment3-image-storage")

        get_item("assignment3-image-storage", "Screenshot (30).png")
        get_item("assignment3-image-storage", "Screenshot (32).png")
        get_item("assignment3-image-storage", "Screenshot (34).png")
        get_item("assignment3-image-storage", "Screenshot (44).png")
        get_item("assignment3-image-storage", "Screenshot (31).png")
        get_item("assignment3-image-storage", "cssfromcloudstorage.css")

    except Exception as e:
        log_error("Main Program Error: {0}".format(e))

if __name__ == "__main__":
    main()
