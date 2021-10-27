from google.cloud import storage

def list_buckets():
    storage_client = storage.Client()
    buckets = storage_client.list_buckets()

    for bucket in buckets:
        print(bucket.name)

list_buckets()