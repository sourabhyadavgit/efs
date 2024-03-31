import boto3
import os

# Define the mount point of the EFS volume
efs_mount_point = '/mnt/efs'

def lambda_handler(event, context):
    # Initialize S3 client
    s3 = boto3.client('s3')

    # Set the bucket name and file key
    bucket_name = 'your-bucket-name'
    file_key = 'path/to/your/file.txt'  # Replace with the actual file key

    # Set the local file path within the mounted EFS directory
    local_file_path = os.path.join(efs_mount_point, 'downloaded_file.txt')

    try:
        # Download file from S3 to the local file path
        s3.download_file(bucket_name, file_key, local_file_path)

        # Perform operations on the downloaded file if needed
        # For example, you can read the contents of the file
        with open(local_file_path, 'r') as file:
            file_contents = file.read()
            print("Contents of the downloaded file:", file_contents)

        return {
            'statusCode': 200,
            'body': 'File downloaded successfully'
        }
    except Exception as e:
        print("Error:", e)
        return {
            'statusCode': 500,
            'body': 'Error downloading file from S3'
        }
