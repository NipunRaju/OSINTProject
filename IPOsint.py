import requests

def check_ip_abuse(ip_address, api_key):
    url = f'https://api.abuseipdb.com/api/v2/check?ipAddress={ip_address}'
    headers = {'Key': api_key}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            result = response.json()
            return result
        else:
            return f"Error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"Error: {e}"

def main():
    api_key = "d5b3021029d35717f2869d8117f761b9f15bde9a5f6dd7959d4e4147a2cdb279108106f4b4573ef5" 
    ip_address = input("Enter the IP address to check: ")

    result = check_ip_abuse(ip_address, api_key)
    print(result)

if __name__ == "__main__":
    main()