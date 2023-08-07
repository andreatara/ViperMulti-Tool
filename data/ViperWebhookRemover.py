# Modules importation
import time
import os
try:
    from colorama import Fore, init
except:
    os.system("py -m pip install colorama")
    from colorama import Fore, init
try:
    import requests
except:
    os.system("py -m pip install requests")
    import requests

init()
os.system("title Viper W-Deleter / Made by Tara")

print("""
      ██╗   ██╗██╗██████╗ ███████╗██████╗     ██╗    ██╗      ██████╗ ███████╗███╗   ███╗ ██████╗ ██╗   ██╗███████╗██████╗ 
      ██║   ██║██║██╔══██╗██╔════╝██╔══██╗    ██║    ██║      ██╔══██╗██╔════╝████╗ ████║██╔═══██╗██║   ██║██╔════╝██╔══██╗
      ██║   ██║██║██████╔╝█████╗  ██████╔╝    ██║ █╗ ██║█████╗██████╔╝█████╗  ██╔████╔██║██║   ██║██║   ██║█████╗  ██████╔╝
      ╚██╗ ██╔╝██║██╔═══╝ ██╔══╝  ██╔══██╗    ██║███╗██║╚════╝██╔══██╗██╔══╝  ██║╚██╔╝██║██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
       ╚████╔╝ ██║██║     ███████╗██║  ██║    ╚███╔███╔╝      ██║  ██║███████╗██║ ╚═╝ ██║╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
        ╚═══╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝     ╚══╝╚══╝       ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝ ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝
      """)
print("ENTER FULL SCREEN OR ASCII ART WON'T WORK\n\n")

webhook = input("Enter the webhook to delete : ")
content = input("Enter Message: ")
r2 = requests.post(webhook, json={"content": content})

def delete():
    requests.delete(webhook)
    check = requests.get(webhook)
    if check.status_code == 404:
        print("\n Webhook succesfully deleted")
        os.system("pause >nul") 
        input("Click enter to close: ")
        exit()
    elif check.status_code == 200:
        print("\n Failed to delete the webhook")
        os.system("pause >nul")

test = requests.get(webhook)
if test.status_code == 404:
    print("\n The webhook is invalid")
    input("Click enter to close: ")
    exit()
elif test.status_code == 200:
    print("\n The webhook is valid")
    delete()