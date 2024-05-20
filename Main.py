import requests
import base64

# Replace with your GitHub repository details
REPO_OWNER = 'repo_owner'
REPO_NAME = 'repo_name'
FILE_PATH = 'path/to/your/file'
BRANCH = 'main'  # or whatever branch you want to fetch from

# GitHub API URL for the file
url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{FILE_PATH}?ref={BRANCH}"

# Make the request to the GitHub API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    file_content_base64 = response.json()['content']
    
    # Decode the Base64 content
    file_content = base64.b64decode(file_content_base64).decode('utf-8')
    
    # Save the decoded content to a variable
    decoded_file_content = file_content
    
    # Print or use the content as needed
    print(decoded_file_content)
else:
    print(f"Failed to fetch the file: {response.status_code}")
    print(response.json())
