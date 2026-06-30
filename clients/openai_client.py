import json
import os
import aiohttp
import requests
import httpx

try:
  data = json.loads('s')
except json.JSONDecodeError as e:
  print("Invalid JSON from the model:", e)

async def ask_model(session: aiohttp.ClientSession, prompt: str) -> str:
  openai = os.getenv("OPENAI_API_KEY")
  payload = {"prompt": prompt}

  async with session.post(openai, json=payload) as response:
    response.raise_for_status()
    data = await response.json()
    return data["text"]
  
response = requests.post(
  "https://api.openai.com/v1/chat", 
  json={...}
)

def handler(request: httpx.Request) -> httpx.Response:
  return httpx.Response(
    200,
    json={
      "answer": "Mock response",
      "openai_model": "gpt-3.5"
    }
  )

# Mock Response
client = httpx.Client

response = client.post(
  "https://api.openai.com/v1/generate",
  json={"prompt": "What is RAG?"}
)

print(response.json())