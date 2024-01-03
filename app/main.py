print("Hello")
from dotenv import load_dotenv
# Load the .env file
load_dotenv()

# Now you can access the variables
import os
db_uri = os.getenv('DATABASE_URI')
api_key = os.getenv('API_KEY')

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"status":"todo api is running"}
