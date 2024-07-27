import requests

url = "https://go.dev/dl/go1.22.4.linux-amd64.tar.gz"

response = requests.head(url, allow_redirects=True)

if response.status_code == 200:
    if "Content-Disposition" in response.headers:
        # If the response has a Content-Disposition header, it's likely a file
        print(f"{url} is a file")
    elif "Content-Type" in response.headers and response.headers["Content-Type"].startswith("text/"):
        # If the response has a Content-Type header with a text type, it's likely a webpage
        print(f"{url} is a webpage")
    else:
        print(f"{url} is neither a file nor a webpage")
else:
    print(f"Error: {response.status_code}")

# wget https://github.com/MehrdadDw/ScriptsP/raw/main/checkAccess.py && chmod +x checkAccess.py && ./checkAccess.py

