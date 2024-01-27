from dotenv import load_dotenv,find_dotenv
import os
load_dotenv(find_dotenv(raise_error_if_not_found=True))

print("Settings Loaded...")
OPEN_API_KEY = os.environ.get("OPEN_API_KEY")
ORG_ID = os.environ.get("ORG_ID")

