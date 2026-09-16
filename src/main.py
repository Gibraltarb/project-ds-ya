from dotenv import load_dotenv
import os
load_dotenv(dotenv_path="prct.env")

author = os.getenv("AUTHOR")

print(f"Hello from repository by {author}!")

