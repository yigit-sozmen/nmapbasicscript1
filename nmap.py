import subprocess
import re

def clean_url(url):
    cleaned_url = re.sub(r'^(https?://|www\.)', '', url)
    return cleaned_url

def run_nmap_scan(target):
    cleaned_target = clean_url(target)
    
    nmap_command = f"nmap -v -sS -T4 {cleaned_target}"

    try:
        print(f"Running Nmap scan on {cleaned_target}...")
        result = subprocess.run(nmap_command, shell=True, capture_output=True, text=True)

        if result.returncode == 0:
            print("Scan completed successfully!\n")
            print(result.stdout)
        else:
            print("Error in running nmap scan.\n")
            print(result.stderr)
    except Exception as e:
        print(f"An error occurred: {e}")

target = input("Enter the target URL or IP address: ")

run_nmap_scan(target)

