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
from dotenv import load_dotenv
import os
from openai import OpenAI
import time
import requests
import asyncio
import time
import random
from tenacity import retry, wait_exponential, stop_after_attempt
from rich.console import Console
from rich.table import Table
from rich.live import Live
from rich.table import Table
import panel as Panel
import httpx
from pydantic import BaseModel, Field
from typing import Optional
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

try:
  data = json.loads()
except json.JSONDecodeError:
  print("Invalid JSON from the model")

async def fetch_one(client: httpx.AsyncClient, api: int) -> int:
  response = await client.get(api)
  response.raise_for_status()
  return response.text

async def main():
  API = {
    "openai": os.getenv("OPENAI_API_KEY"),
    "gemini": os.getenv("GEMINI_API_KEY")
  }

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

load_dotenv()

response = client.responses.create(
  model=os.getenv("MODEL_NAME", "gpt-3.5"),
  input="Write a short product description for an AI note-taking app."
)

print(response.output_text)

response = requests.post("https://api.example.com/v1/chat", json={...})

if response.status_code == 429:
  wait_time = int(response.headers.get("Retry-After", 4))
  print(f"Rate limited. Waiting {wait_time} seconds...")
  time.sleep(wait_time)

async def call_llm(prompt_id):
  print(f"Starting prompt {prompt_id}")

  await asyncio.sleep(2)

  print(f"Finished prompt {prompt_id}")

async def main(prompt: str):
  results = await asyncio.gather(
    call_openai(prompt),
    call_gemini(prompt),
    return_exceptions=True
  )
  print(results)

asyncio.run(main())

def call_llm():
  if random.random() < 0.7:
    raise Exception("API failed")
  return "Response from model"

def get_response():
  retries = 3

  for i in range(retries):
    try:
      return call_llm()
    except Exception as e:
      print(f"Attempt {i+1} failed, retrying again...")
      time.sleep(2)

  return "Failed after retries"

@retry(wait=wait_exponential(multiplier=1, min=1, max=10),
       stop=stop_after_attempt(4))
def call_llm(prompt):
  response = client.responses.create(
    model="gpt-3.5",
    input=prompt
  )
  return response

console = Console()

cards = [
  Panel("GPT-3.5"),
  Panel("Gemini-Flash")
]

table = Table(title="LLM Benchmark")

table.add_column("Model")
table.add_column("Latency")
table.add_column("Accuracy")

table.add_row("GPT-3.5", "1.3", "86%")
table.add_row("Gemini-Flash", "1.4", "88%")

def make_table(step, status):
  table = Table(title="AI Pipeline Status")
  table.add_column("Step")
  table.add_column("Status")
  table.add_row("Load data", "Done" if step > 0 else "Pending")
  table.add_row("Embed chunks", "Done" if step > 1 else "Pending")
  table.add_row("Call LLM", status)
  return table

with Live(make_table(0, "Pending"), console=console, refresh_per_second=4) as live:
          time.sleep(1)
          live.update(make_table(1, "Pending"))
          time.sleep(1)
          live.update(make_table(2, "Running"))
          time.sleep(1)
          live.update(make_table(3, "Done"))

parser = argparse.ArgumentParser()
parser.add_argument("--model", type=str, default="gpt")
args = parser.parse_args()

client = genai.Client(api_key="GEMINI_API_KEY")

def call_gemini(prompt: str) -> str:
   response = client.responses.create(
      model = "gemini-flash",
      input = prompt
   )
   return response.output_text

client = OpenAI()

def call_openai(prompt: str, model: str = "gpt-3.5") -> str:
   response = client.responses.create(
      model = model,
      input = prompt
   )
   return response.output_text

def handler(request: httpx.Request) -> httpx.Response:
   return httpx.Response(
      200,
      json={
         "answer": "Mocked response",
         "model": "test-model"
      }
   )

client = httpx.Client(transport=httpx.MockTransport(handler))

response = client.post(
   "https://api.example.com/v1/generate",
   json={"prompt": "What is RAG?"}
)

print(response.json())

class SupportTicket(BaseModel):
   issue: str
   category: str
   priority: int = Field(ge=1, le=5)

data = {
   "issue": "Login page not working",
   "priority": 3,
   "category": "auth"
}

ticket = SupportTicket(**data)

async def fetch_model_status():
   async with httpx.AsyncClient(timeout=10.0) as client:
      response = await client.get("https://api.example.com/status")
      response.raise_for_students()
      return response.json()
   
async def main():
   data = await fetch_model_status()
   return data

asyncio.run(main())

async def call_service(client: httpx.AsyncClient, url: str):
   response = await client.get(url)
   response.raise_for_status()
   return response.json()

async def main():
   urls = [
      "https://api.example.com/embeddings/1",
      "https://api.example.com/embeddings/2"
   ]

   async with httpx.AsyncClient(timeout=10.0) as client:
      results = await asyncio.gather(*(call_service(client, url) for url in urls))

   return results

asyncio.run(main())

class LLMResponse(BaseModel):
   provider: str
   text: str
   error: Optional[str] = None
   latency_ms: int
   tokens: int

start = time.perf_counter()

response = LLMResponse(
   provider="openi",
   text="Approved claim under policty terms",
   error=None,
   latency_ms=842,
   tokens=156
)

latency_ms = int((time.perf_counter() - start) * 1000)

result = LLMResponse(
   provider="OpenAI",
   text=response.output_text,
   latency_ms=latency_ms
)

end = time.perf_counter()

print(start - end)

try: 
   response = client.responses.create(
      model="gpt-3.5",
      input = "Summarise thsi claim."
   )

   result = LLMResponse(
      provider="OpenAI",
      text=response.output_text,
      error=None
   )

except Exception as e:
   result = LLMResponse(
      provider="OpenAI",
      text="",
      error=str(e)
   )

def call_openai(prompt):
   for attempt in range(4):
      try:
         response = client.responses.create(
            model = "gpt-3.5",
            input = prompt
         )
         return response.output_text
      except Exception:
         if attempt == 3:
            raise

def call_llm_api(payload, max_retries=5, base_delay=1.0, max_delay=20.0): 
   url = [
      "https://api.example.com/v1/chat/completions",
      "https://api.example.com/v1/chat/completions"
   ]
   
   headers = {"Authorization": "Bearer YOUR_API_KEY"}

   for attempt in range(max_retries):
      try:
         response = requests.post(url, json=payload, headers=headers, timeout=30)

         if response.status_code == 200:
            return response.json()
         
         if response.status_code in (429, 500, 502, 503, 504):
            delay = min(max_delay, base_delay * (2 ** attempt))
            jitter = random.uniform(0, 0.25 * delay)
            sleep_time = delay + jitter
            print(f"Attempt {attempt + 1} failed with {response.status_code}. Retrying in {sleep_time:.2f}s...")
            time.sleep(sleep_time)
            continue

         response.raise_for_status()

      except requests.RequestException as e:
         delay = min(max_delay, base_delay * (2 ** attempt))
         jitter = random.uniform(0, 0.25 * delay)
         sleep_time = delay + jitter
         print(f"Attempt {attempt + 1} error: {e}. Retrying in {sleep_time:.2f}s...")
         time.sleep(sleep_time)

   raise RuntimeError("LLM API call failed after retries")