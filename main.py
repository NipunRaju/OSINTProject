from flask import Flask, render_template, request
import subprocess
import sys

app = Flask(__name__)

def run_proxy_osint(ip_address):
    # Execute ProxyOSINT.py script with the provided IP address
    result = subprocess.run([sys.executable, "ProxyOSINT.py", ip_address], capture_output=True, text=True)
    return result.stdout

def run_email_osint(email_address):
    # Execute emailosint.py script with the provided email address
    result = subprocess.run([sys.executable, "emailosint.py", email_address], capture_output=True, text=True)
    return result.stdout

def run_account_compromise(account_name):
    # Execute accountcompromise.py script with the provided account name
    result = subprocess.run([sys.executable, "accountcompromise.py", account_name], capture_output=True, text=True)
    return result.stdout

def run_ip_osint(ip_address):
    # Execute IPOsint.py script with the provided IP address
    result = subprocess.run([sys.executable, "IPOsint.py", ip_address], capture_output=True, text=True)
    return result.stdout

def run_username_osint(username):
    # Execute usernameosint.py script with the provided username
    result = subprocess.run([sys.executable, "usernameosint.py", username], capture_output=True, text=True)
    return result.stdout

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run/<command>', methods=['POST'])
def run_command(command):
    if command == 'proxy_osint':
        ip_address = request.form['proxy_ip_address']
        result = run_proxy_osint(ip_address)
        return render_template('index.html', message='Proxy OSINT executed successfully', result=result)
    elif command == 'email_osint':
        email_address = request.form['email_address']
        result = run_email_osint(email_address)
        return render_template('index.html', message='Email OSINT executed successfully', result=result)
    elif command == 'account_compromise':
        account_name = request.form['account_name']
        result = run_account_compromise(account_name)
        return render_template('index.html', message='Account Compromise executed successfully', result=result)
    elif command == 'ip_osint':
        ip_address = request.form['ip_address']
        result = run_ip_osint(ip_address)
        return render_template('index.html', message='IP OSINT executed successfully', result=result)
    elif command == 'username_osint':
        username = request.form['username']
        result = run_username_osint(username)
        return render_template('index.html', message='Username OSINT executed successfully', result=result)
    elif command == 'exit':
        return 'Exiting...'
    else:
        return 'Invalid command'

if __name__ == '__main__':
    app.run(debug=True)
