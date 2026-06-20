import argparse
import sys
from dataclasses import dataclass
from typing import List
import json
from typing import Optional

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