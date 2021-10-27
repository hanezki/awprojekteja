from google.cloud import storage

storage_client = storage.Client()

#list buckets
def list_buckets():
    buckets = storage_client.list_buckets()

    for bucket in buckets:
        print(bucket.name)

def create_bucket(bucket_name):
    bucket = storage_client.bucket(bucket_name)
    bucket.storage_class = "COLDLINE"
    new_bucket = storage_client.create_bucket(bucket, location="us")

    print(f"Created bucket {new_bucket.name} in {new_bucket.location} with storage class {new_bucket.storage_class}")

create_bucket("juukeli")