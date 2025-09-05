import requests
import time

# List of URLs to scan
urls = [
    "https://skillsforall.com",
    "https://www.google.com",
    "https://www.github.com",
    "https://kyglhyutdf.com"  # Example invalid URL
]

def scan_url(url):
    try:
        start = time.time()
        response = requests.get(url, timeout=5)
        elapsed = time.time() - start
        print(f"[+] {url} - Status: {response.status_code}, Time: {elapsed:.2f}s")
    except requests.exceptions.RequestException as e:
        print(f"[-] {url} - Error: {e}")

def main():
    print("=== Simple URL Scanner ===\n")
    for url in urls:
        scan_url(url)

if __name__ == "__main__":
    main()
