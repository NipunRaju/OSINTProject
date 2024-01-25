import requests
import argparse
import sys

def get_parameters():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--Email", dest="Email", help="Enter the email address")
    options = parser.parse_args()
    if not options.Email:
        print("[-] Please specify Email, use --help for more info")
        sys.exit(1)  # Exit with a non-zero code to indicate an error
    return options

def RED(message):
    print("\033[91m{}\033[0m".format(message))

def maildb(emailaddress):
    if "@" in emailaddress and (".com" in emailaddress or ".in" in emailaddress):
        domain = emailaddress.split('@')[1]
        print("Domain:", domain)
        req = requests.get("https://api.hunter.io/v2/domain-search?domain=" + domain + "&api_key=8a3262f9f876aa2aeb81dec505da6790c09ce8be")
        print("API Response Status Code:", req.status_code)
        print("API Response Content:", req.text)

        try:
            j = req.json()
            if 'data' in j and 'emails' in j['data']:
                print("[+] Breaching from " + emailaddress + "...\n")
                for i in range(len(j['data']['emails'])):
                    print("Email ID   :", j['data']['emails'][i]['value'])
                    print("First Name :", j['data']['emails'][i]['first_name'])
                    print("Last Name  :", j['data']['emails'][i]['last_name'])
                    if j['data']['emails'][i]['position'] is not None:
                        print("Position   :", j['data']['emails'][i]['position'])
                    if j['data']['emails'][i]['linkedin'] is not None:
                        print("Linkedin   :", j['data']['emails'][i]['linkedin'])
                    if j['data']['emails'][i]['twitter'] is not None:
                        print("Twitter    :", j['data']['emails'][i]['twitter'])
                    print()
            else:
                print("No emails found in the API response.")
        except Exception as e:
            RED("Error parsing API response: {}".format(str(e)))
    else:
        RED("Error: Invalid Email Address")

def main():
    options = get_parameters()
    mail = options.Email
    maildb(mail)

if __name__ == "__main__":
    main()