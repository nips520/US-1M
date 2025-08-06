import os
import json
import re
import base64
import csv
import requests
from urllib.parse import urlparse

# File path
base_path = 'C:/Users/namae/Downloads/figshare/json_index/'

# Define unit conversion mapping
unit_mapping = {
    'kB': 1e3,
    'MB': 1e6,
    'GB': 1e9,
    'TB': 1e12
}

def parse_size(size_str):
    """Convert size_str to bytes"""
    match = re.match(r'(\d+(\.\d+)?)\s*(kB|MB|GB|TB)', size_str)
    if match:
        size, _, unit = match.groups()
        return float(size) * unit_mapping[unit]
    return 0

def is_size_valid(size):
    """Check if size is greater than or equal to 1MB"""
    return size >= 1e6  # 1 MB in bytes

def is_description_valid(description):
    """Check if description starts with 'Sheet' or 'Table'"""
    return not (description.startswith("Sheet") or description.startswith("Table"))

def encode_image(image_url):
    """Convert image URL to base64 encoding"""
    response = requests.get(image_url)
    if response.status_code == 200:
        return base64.b64encode(response.content).decode('utf-8')
    else:
        print(f"Error fetching image from URL: {image_url}")
        return None

def get_pic_url(url):
    """Extract the last segment from the URL and construct a new pic_url"""
    parsed_url = urlparse(url)
    last_segment = parsed_url.path.split('/')[-1]  # Get the last part
    return f"{url}/preview/{last_segment}/preview.jpg"

def collect_data(base_path):
    """Collect size_str, source, x_filename, and description data"""
    size_list = []
    source_list = []
    x_filename_list = []
    description_list = []
    url_list = []
    pic_url_list = []  # New list to store image URLs

    for root, _, files in os.walk(base_path):
        for file in files:
            if file == 'durl_info.txt':
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    try:
                        data = json.load(f)

                        # Extract description
                        description = data.get('discription', 'no description')  # Collect description data
                        url = data.get('url', 'no url')  # Collect URL data

                        # Extract url_infos
                        for info in data.get('url_infos', []):
                            size_str = info.get('size_str', '0kB')
                            source = info.get('source', 'unknown')
                            x_filename = info.get('x_filename', 'unknown')

                            size = parse_size(size_str)
                            if is_size_valid(size):  # Only keep data greater than or equal to 1 MB
                                # Further check description
                                if is_description_valid(description):
                                    size_list.append(size)
                                    source_list.append(source)
                                    x_filename_list.append(x_filename)
                                    description_list.append(description)  # Add description to the list
                                    url_list.append(url)  # Add URL to the list
                                    pic_url_list.append(get_pic_url(url))  # Add pic_url to the list

                    except json.JSONDecodeError:
                        print(f"Error decoding JSON in file: {file_path}")

    return size_list, source_list, x_filename_list, description_list, url_list, pic_url_list

def sort_and_save(size_list, source_list, url_list, pic_url_list, output_file='E:/sorted_data.csv'):
    """Sort by size_list and save corresponding source, url, and pic_url to a CSV file"""
    # Create a list to combine size, source, url, and pic_url
    combined_data = list(zip(size_list, source_list, url_list, pic_url_list))

    # Sort data by size in descending order
    sorted_data = sorted(combined_data, key=lambda x: x[0], reverse=True)

    # Save to CSV file
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        # Write data without headers
        for size, source, url, pic_url in sorted_data:
            size_in_gb = size / unit_mapping['GB']  # Convert bytes to GB
            writer.writerow([size_in_gb, source, url, pic_url])  # Write data

if __name__ == '__main__':
    size_list, source_list, x_filename_list, description_list, url_list, pic_url_list = collect_data(base_path)
    sort_and_save(size_list, source_list, url_list, pic_url_list)
