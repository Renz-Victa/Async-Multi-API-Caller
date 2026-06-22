from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.responses.create(
  model=os.getenv("MODEL_NAME", "gpt-3.5"),
  input="Write a short product description for an AI note-taking app."
)

print(response.output_text)