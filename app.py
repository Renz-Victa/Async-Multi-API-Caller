from dotenv import load_dotenv
import os
from openai import OpenAI
import time
import requests
import asyncio
import time
import random

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.responses.create(
  model=os.getenv("MODEL_NAME", "gpt-3.5"),
  input="Write a short product description for an AI note-taking app."
)

print(response.output_text)

response requests.post("https://api.example.com/v1/chat", json={...})

if response.status_code == 429:
  wait_time = int(response.headers.get("Retry-After", 5))
  print(f"Rate limited. Waiting {wait_time} seconds...")
  time.sleep(wait_time)

async def call_llm(prompt_id):
  print(f"Starting prompt {prompt_id}")

  await asyncio.sleep(2)

  print(f"Finished prompt {prompt_id}")

async def main():
  await asyncio.gather(
    call_llm(1),
    call_llm(2)
  )

asyncio.run(main())

def call_llm():
  if random.random() < 0.7:
    raise Exception("API failed")
  return "Response from model"

def get_response():
  retries = 5

  for i in range(retries):
    try:
      return call_llm()
    except Exception as e:
      print(f"Attempt {i+1} failed, retrying again...")
      time.sleep(2)

  return "Failed after retries"
