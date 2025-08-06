import os
import time
import random
import pandas as pd
from roboflow import Roboflow

# Replace with your Roboflow API key
ROBOFLOW_API_KEY = "xxx"

# Initialize the Roboflow client
rf = Roboflow(api_key=ROBOFLOW_API_KEY)

# Validate the API key
try:
    workspaces = rf.workspace().projects()
    print(f"API key validation successful! Found {len(workspaces)} projects.")
except Exception as e:
    print(f"API key validation failed: {e}")
    exit(1)

# Read the CSV file
df = pd.read_csv('roboflow-datasets.csv')

# Iterate through each data link and download
for dataset_url in df['Data Href']:
    try:
        # Extract dataset identifiers
        parts = dataset_url.strip('/').split('/')
        if len(parts) >= 2:
            workspace_name = parts[-2]
            dataset_name = parts[-1]
        else:
            print(f"Skipping invalid dataset URL: {dataset_url}")
            continue

        # Corresponding save path
        download_location = f"D:/roboflow/{dataset_name}"
        os.makedirs(download_location, exist_ok=True)

        print(f"Downloading: {dataset_name} to {download_location}")

        # Get the project and version
        project = rf.workspace(workspace_name).project(dataset_name)

        # Attempt to get the latest version
        try:
            versions = project.versions()
            if not versions:
                print(f"Dataset {dataset_name} has no available versions.")
                continue
            latest_version = versions[-1]['version']
            print(f"Downloading version: {latest_version}")
            dataset = project.version(latest_version).download("voc", location=download_location)
        except Exception as e:
            print(f"Failed to get the latest version, attempting to download version 1: {e}")
            dataset = project.version(1).download("voc", location=download_location)

        # Validate the download results
        files = os.listdir(download_location)
        if len(files) == 0:
            print(f"❌ {dataset_name} download resulted in an empty folder.")
        else:
            print(f"✅ {dataset_name} download completed, file count: {len(files)}")

    except Exception as e:
        print(f"❌ Download failed: {dataset_name} - Error: {str(e)}")

    # Random sleep
    wait_time = random.randint(1, 5)
    print(f"Resting for {wait_time} seconds before continuing...")
    time.sleep(wait_time)

print("All datasets downloaded!")
