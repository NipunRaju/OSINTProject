import subprocess
import sys

def run_proxy_osint():
    subprocess.run([sys.executable, "ProxyOSINT.py"])

def run_email_osint():
    subprocess.run([sys.executable, "emailosint.py"])

def run_account_compromise():
    subprocess.run([sys.executable, "accountcompromise.py"])

def run_ip_osint():
    subprocess.run([sys.executable, "IPOsint.py"])

def run_username_osint():
    subprocess.run([sys.executable, "usernameosint.py"])

def main():
    while True:
        print("Select an option:")
        print("1. Run Proxy OSINT")
        print("2. Run Email OSINT")
        print("3. Run Account Compromise")
        print("4. Run IP OSINT")
        print("5. Run Username OSINT")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            run_proxy_osint()
        elif choice == "2":
            run_email_osint()
        elif choice == "3":
            run_account_compromise()
        elif choice == "4":
            run_ip_osint()
        elif choice == "5":
            run_username_osint()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
