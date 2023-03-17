import os
from dotenv import load_dotenv

# Find the .env file based on the project's root directory
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
# Load environment variables from the .env file
load_dotenv(dotenv_path)
