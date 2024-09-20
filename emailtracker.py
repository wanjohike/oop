# python prog to check Email aaccounts across services
# install holehe module
import subprocess
def check_email(email):
    result = subprocess.run(['holehe', email],capture_output = True, text =True)
    return result.stdout

email = input('Énter Your Email:')
response = check_email(email)
print(response)
