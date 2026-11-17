import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app_name = os.getenv("APP_NAME")
app_key = os.getenv("APP_KEY")

print("APP_NAME:", app_name)
print("APP_KEY loaded:", app_key is not None)
