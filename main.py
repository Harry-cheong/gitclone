import subprocess
from art import text2art
from dotenv import load_dotenv
import os

load_dotenv()

Art = text2art(f"{os.getenv('user')}")
print(Art)

token = os.getenv('GITHUB_TOKEN')
repo_owner = input('Repo Owner: ')
repo_name = input('Repo Name: ')

if not input(f"Verify 'git clone https://[TOKEN]@github.com/{repo_owner}/{repo_name}' (Y/N): ") == "Y":
    raise SystemExit

print("\n")

subprocess.Popen(f'cd .. && git clone https://{token}@github.com/{repo_owner}/{repo_name}', shell=True)