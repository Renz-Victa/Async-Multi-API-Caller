import argparse
import sys
from dataclasses import dataclass
from typing import List
import json
from typing import Optional
import asyncio
import aiohttp
import httpx
from google import genai

class Dataset:
  def __init__(self, data):
    self.data = data

  def predict(self, x):
    return self.data
  
model = Dataset(data=2)
result = model.predict(5)

def greet(name: Optional[str]) -> str:
  if name is None:
    print("Hello, Guest!")
  print(f"Hello, {name}")

class NeuralNetworks():
  def __init__(self):
    user = input("Check for Initialised Neural Network? y/n: ")
    if input == "y":
      print("Neural Networks are Initialised")
    else:
      print("Neural Networks are not initialised")

model = NeuralNetworks()

@dataclass
class ModelConfig:
  model_name: str
  max_tokens: int = 1000
  temperature: float = 0.9
  hidden_size: int = 768
  vocab_size: int = 20000
  hidden_size: int = 768
  num_layers: int = 12
  dropout: float = 0.1

config = ModelConfig(
  hidden_size=128,
  num_layers=12,
  dropout=0.1,
  vocab_size=20000,
  model_name="gpt-model",
  max_tokens=1000,
  temperature=0.9
)

@dataclass 
class Message:
  role: str
  timestamp: str
  content: str=""

model1 = "gpt-3.5"
model2 = "gemini-flash"

status = f"model {model1} & {model2} has used {tokens_used} so far"
user1 = input("Do you want the status tokens for these models? y/n: ")
if int == "y":
  print("status")

user_prompt: str = input("Enter your question: ")
response = f"AI response to: {user_prompt}"
print(response)

message = input("Do you want to exit: ")
if message == "exit":
  print("Goodbye, Have a great day!")

asyncio = call_openai(prompt: str)
asyncio = call_gemini(prompt: str)

results = await asyncio.gather(
  call_openai(prompt),
  call_gemini(prompt),
  return_exemptions=True
)
print(results)

try:
  response = response.create(
    model="gpt-3.5"
  )

except Exception as e:
  print(f"LLM API failed: {e}")

try:
  data = json.loads()
except json.JSONDecodeError:
  print("Invalid JSON from the model")

async def fetch_one(client: httpx.AsyncClient, api: int) -> int:
  response = await client.get(api)
  response.raise_for_status()
  return response.text

async def main():
  apis = [
    openai_api_key,
    gemini_api_key
  ]

  async with httpx.AsyncClient(timeout=10.0) as client:
    results = await asyncio.gather(*(fetch_one(client)))

  for i, text in enumerate(results, start=1):
    print(f"Result {i}: {text[:80]}")

asyncio.run(main())

client = genai.Client()

def call_genai(prompt: str) -> str:
  response = client.models.generate_content(
    model="gemini-3.5-flash",
    content="Summarize this support ticket in 3 bullets: The user cannot log in after resetting their password."
  )
  return response.output_text

async def ask_model(session: aiohttp.ClientSession, prompt: str) -> str:
  api = "your_api_key"
  payload = {"prompt": prompt}

  async with session.post(api, json=payload) as response:
    response.raise_for_status()
    data = await response.json()
    return data["text"]
  
async def main():
  prompts = [
    "Summarise this ticket in one sentence",
    "Rewrite this paragraph more clearly"
  ]

  async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=10)) as session:
    results = await asyncio.gather(*(ask_model(session, p) for p in prompts))

  for i, text in enumerate(results, start=1):
    print(i, text)

asyncio.run(main())