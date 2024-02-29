import requests
import os

API_KEY_FILE = "securitytrails_api_key.txt"

def get_api_key():
    if os.path.exists(API_KEY_FILE):
        with open(API_KEY_FILE, 'r') as file:
            return file.read().strip()
    else:
        api_key = input("Enter your SecurityTrails API key: ")
        with open(API_KEY_FILE, 'w') as file:
            file.write(api_key)
        return api_key

def get_subdomains(api_key, domain):
    url = f"https://api.securitytrails.com/v1/domain/{domain}/subdomains"
    headers = {"APIKEY": api_key}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        subdomains = data.get('subdomains', [])
        return subdomains
    else:
        print(f"Failed to retrieve subdomains: {response.status_code}")
        return []

def write_subdomains_to_file(subdomains, domain, output_file):
    with open(output_file, 'w') as file:
        for subdomain in subdomains:
            full_subdomain = f"{subdomain}.{domain}"
            file.write(full_subdomain + '\n')
    print(f"Subdomains written to {output_file}")

def main():
    api_key = get_api_key()
    domain = input("Enter the domain for which you want to collect subdomains: ")
    output_file = input("Enter the name of the output file: ")
    
    subdomains = get_subdomains(api_key, domain)
    if subdomains:
        write_subdomains_to_file(subdomains, domain, output_file)
    else:
        print("No subdomains found.")

if __name__ == "__main__":
    main()
