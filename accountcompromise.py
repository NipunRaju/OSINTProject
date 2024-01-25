import requests

def leak_check_api(api_key, email):
    base_url = "https://leakcheck.io/api/public"
    endpoint = f"{base_url}?key={api_key}&check={email}"

    try:
        response = requests.get(endpoint)
        response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)

        print("[+] Raw API Response:")
        print(response.text)

        result = response.json()
        return result

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def main():
    api_key = "e5ac9c54442f1d10baaaf70648ce3dbe637c1f53"
    email = input("Enter the email address to check for compromises: ")

    result = leak_check_api(api_key, email)

    if result is not None:
        print("[+] Results:")
        print(result)
    else:
        print("[-] An error occurred or no results were found.")

if __name__ == "__main__":
    main()
