import requests
import sys

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
    ip_address = sys.argv[1]

    result = check_ip_abuse(ip_address, api_key)
    
    if result:
        ip_data = result.get('data', {})
        ipAddress = ip_data.get('ipAddress')
        isPublic = ip_data.get('isPublic')
        ipVersion = ip_data.get('ipVersion')
        isWhitelisted = ip_data.get('isWhitelisted')
        abuseConfidenceScore = ip_data.get('abuseConfidenceScore')
        countryCode = ip_data.get('countryCode')
        usageType = ip_data.get('usageType')
        isp = ip_data.get('isp')
        domain = ip_data.get('domain')
        hostnames = ip_data.get('hostnames', [])
        isTor = ip_data.get('isTor')
        totalReports = ip_data.get('totalReports')
        numDistinctUsers = ip_data.get('numDistinctUsers')
        lastReportedAt = ip_data.get('lastReportedAt')

        print("IP Address:", ipAddress)
        print("Is Public:", isPublic)
        print("IP Version:", ipVersion)
        print("Is Whitelisted:", isWhitelisted)
        print("Abuse Confidence Score:", abuseConfidenceScore)
        print("Country Code:", countryCode)
        print("Usage Type:", usageType)
        print("ISP:", isp)
        print("Domain:", domain)
        print("Hostnames:", hostnames)
        print("Is Tor:", isTor)
        print("Total Reports:", totalReports)
        print("Number of Distinct Users:", numDistinctUsers)
        print("Last Reported At:", lastReportedAt)
    else:
        print("No data available for the provided IP address.")

if __name__ == "__main__":
    main()
