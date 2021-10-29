import json
import urllib.request
from  google.cloud import storage

def avaa_tiedosto():
    tiedosto = urllib.request.urlopen("https://2ri98gd9i4.execute-api.us-east-1.amazonaws.com/dev/academy-checkpoint2-json")
    tiedot_data = json.loads(tiedosto.read())
    parametri_data = []
    for data in tiedot_data['items']:
        if not data['parameter']:
            continue

        parametri_data.append(data['parameter'])
    return parametri_data

def talleta(tiedosto: list):
        with open("checkpoint.txt", "w") as f:
            for item in tiedosto:
                f.write(item + "\n")

def create_bucket():

    bucket_name = "khcheckpoint_bucket"

    storage_client = storage.Client()

    bucket = storage_client.create_bucket(bucket_name)
    print(f"Bucket with name {bucket_name} has been created")

def filein_bucket():

    bucket_infile = "checkpoint.txt"
    bucket_name_infile = "checkpoint1"

    storage_client = storage.Client()

    bucket = storage_client.get_bucket("khcheckpoint_bucket")
    blob = bucket.blob(bucket_name_infile)
    blob.upload_from_filename(bucket_infile)

    print(f"File {bucket_infile} has been upload to {bucket}")


def main():
    koko_data = avaa_tiedosto()
    talleta(koko_data)

    create_bucket()
    filein_bucket()

if __name__ == "__main__":
    main()