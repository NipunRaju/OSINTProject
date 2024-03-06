import requests
import sys

def get_ip_details(api_key, user_ip):
    api_url = f"https://ipqualityscore.com/api/json/ip/{api_key}/{user_ip}"
    
    try:
        response = requests.get(api_url)
        data = response.json()
        return data
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == '__main__':
 
    user_ip = sys.argv[1]


    api_key = 'kRh1Af6lyk0uknJih0JwMGM6CnqJ9OKS'

    result = get_ip_details(api_key, user_ip)

    if result and 'proxy' in result and 'vpn' in result and 'organization' in result and 'is_crawler' in result:
        print("\nSelected Details:")
        print(f"Proxy: {result['proxy']}")
        print(f"VPN: {result['vpn']}")
        print(f"Organization: {result['organization']}")
        print(f"Is Crawler: {result['is_crawler']}")
        print(f"Latitude: {result.get('latitude', 'N/A')}")
        print(f"Longitude: {result.get('longitude', 'N/A')}")
    else:
        print("Failed to retrieve IP details.")