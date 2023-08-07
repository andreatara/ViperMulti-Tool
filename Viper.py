import subprocess
from pystyle import *
import time
import os

def load_proxies():
    print("❗Loading proxies❗")
    for i in range(20):
        time.sleep(0.1)
        print("=", end='', flush=True)
    time.sleep(1)
    print("\n❗Proxies loaded successfully❗")
    print("\n=====================")
    time.sleep(0.5)
    print("❗Activating proxies❗")
    for i in range(20):
        time.sleep(0.1)
        print("=", end='', flush=True)
    time.sleep(1)
    print("\n🟢Proxies activated🟢")
    time.sleep(0.5)


load_proxies()

os.system("color 2")
os.system("title Viper MultiTool / Made by Tara")


asciibyme = (Colorate.Vertical(Colors.red_to_purple,
                                '''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣄⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡖⣻⠉⢿⣿⠆⠈⠙⢶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⡚⠒⠊⠙⠂⠀⠀⢆⣱⡘⡷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡟⠛⠳⣖⠒⠒⢙⡤⣿⣷⠃⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⢻⠆⠤⠤⡗⣿⢻⣼⢀⢷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠇⠀⠸⣼⣏⡒⢲⠟⡟⣾⡾⣎⢾⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⠀⢸⡴⢻⠃⠀⡜⢸⣻⠴⠛⠁⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⣰⣰⣷⠏⠀⢰⠃⣿⣷⢳⣰⣤⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠹⣯⣿⣟⠢⢤⣇⣸⣿⡽⣧⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣶⣭⠓⠌⠉⡛⠉⣿⣼⣾⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⠀⠀⣰⠁⣼⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠃⠀⠀⠐⠁⣴⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     V1
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠇⠀⠀⠀⠀⣼⠏⢰⢦⡀⠀⠀⠀⠀⠀⣀⡠⠤⠤⠤⠤⣀⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⠀⡀⠀⠀⣸⡟⠀⠈⢯⡓⠦⢤⡤⠴⠚⠁⠀⠀⠀⠀⠀⢘⠍⠳⡄⠀⠀⠀⠀
⠀⠀⢀⣠⠤⠖⠒⡒⠒⠢⢤⡗⢤⡉⢺⠒⣿⡃⣀⣀⣠⠽⠷⠒⠛⠉⠉⣉⣉⣛⣛⣛⣛⡉⠀⠀⣸⠀⠀⠀⠀
⢀⡴⠋⠀⠀⢠⠊⠀⠀⠀⢸⡇⢄⡈⠛⣏⣿⠉⠁⠀⢀⣠⠤⠖⠚⠉⠉⠀⠀⠀⠓⠦⣄⠉⠙⠚⠯⣄⡀⠀⠀
⡜⠀⠀⠀⠀⢸⣤⡶⠦⢤⣼⣇⠀⠈⢉⣧⢿⣧⠴⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⠀⠀⠀⠀⠉⢦⠀
⣇⠀⠀⠀⠀⠈⠳⣄⣀⣀⣈⣿⠑⠢⠤⠼⡞⣿⡄⠀⠀⠀⠀⠀⢀⣀⣠⡤⠴⠶⠶⠒⠒⢿⡇⠀⠀⠀⠀⠸⡆
⠘⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢇⠈⠐⠂⠙⣖⠻⣤⣠⣤⡶⠞⠋⠉⠀⠀⠀⠀⠀⠀⢀⡼⠃⠀⠀⠀⠀⢸⠇
⠀⠈⠓⢦⣀⠀⠀⠀⠀⠀⠀⠀⠘⢧⡀⠀⠀⠈⠢⠀⠉⠓⠦⠤⢤⣀⣠⠤⠤⠤⠒⠚⠉⠀⠀⠀⠀⠀⣠⡟⠁
⠀⠀⠀⠀⠈⠙⠓⠲⠶⠶⠶⠶⠞⠛⠓⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⠟⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠤⢄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣤⠴⠞⠋⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
'''))


def execute_script(script_name):
    try:
        subprocess.call(["python", f"data/{script_name}.py"])
    except Exception as e:
        print(f"Error executing the script: {e}")

    input("\nPress any key to return to the menu...")
    display_menu()

def display_menu():
    options = [
        "Token Bruteforce",
        "FN IP Sniffer",
        "Username Scrape",
        "Webhook Destroyer",
        "Login Bruteforce",
        "DDoS Attack",
        "Gmail BruteForce",
        "Gc Spammer",
        "Mass Report",
        "Token Decrypt",
        "Image Logger",
        "Port Scanner",
        "Pinger",
        "Quit",
    ]
    border =  "=" * 90

    print(f"{asciibyme}\n{border}")
    print("💫  Choose your poison  💫".center(65))
    for idx, option in enumerate(options, 1):
        print(f"[{idx}] {option}".ljust(23), end="")
        if  idx %  4  == 0:  # After every 3 options, start a new line
            print()
    
    print("\n")


    prompt = Colorate.Vertical(Colors.red, "[input] > ")
    choice = input(prompt)

    try:
        script_name = options[int(choice) - 1]
        if script_name == "Token Bruteforce":
            execute_script("ViperToken-BRT")
        elif script_name == "FN IP Sniffer":
            execute_script("ViperFN-Sniffer")
        elif script_name == "Username Scrape":
            execute_script("UsernameScrape")
        elif script_name == "DDoS Attack":
            execute_script("ViperDDoS")
        elif script_name == "Gmail BruteForce":
            execute_script("ViperGmail-BRT")
        elif script_name == "Token Decrypt":
            execute_script("Viper T-Decrypt")
        elif script_name == "Gc Spammer":
            execute_script("ViperGC-Spammer")
        elif script_name == "Mass Report":
            execute_script("ViperMass-RPT")
        elif script_name == "Login Bruteforce":
            execute_script("ViperLogin-BRT")
        elif script_name == "Image Logger":
            execute_script("ImageLogger")
        elif script_name == "Webhook Destroyer":
            execute_script("ViperWebhookremover")
        elif script_name == "Port Scanner":
            execute_script("ViperPORTscanner")
        elif script_name == "Pinger":
            execute_script("ViperPinger")
        # Add the rest of the scripts here with their respective filenames
        elif script_name == "Quit":
            print("Exiting the menu...")
        else:
            print("Invalid choice. Please select a valid option.")
            display_menu()
    except Exception as e:
        print("Invalid choice. Please select a valid option.")
        display_menu()

if __name__ == "__main__":
    display_menu()
