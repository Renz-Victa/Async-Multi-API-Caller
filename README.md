## Async Multi-API Caller

An Async Multi-API Caller built with Python 

---

## Repository Structure

```
Async Multi-API Caller
├── main.py
├── README.md
├── .env.example
├── results.json          # Log comparisons over time
├── .env
├── .gitignore
├── compare.py            # Hardcoded test prompt
├── display.py
├── requirements.txt
├── .venv/
├── clients/
|   ├── gemini_client.py
|   ├── openai_client.py
└── core/
    └── retry.py
```

---

## Prerequisites

| Tool     | Version  |
|----------|----------|
| Python   | ≥ 3.10    |
| pip      | Latest   |

---

## Quick Start

```bash
# 1. Clone the Repository
git clone https://github.com/Renz-Victa/Async-Multi-API-Caller
cd Async Multi-API-Caller

# 2. Install the Dependencies
pip install -r requirements.txt

# 3. Run the Caller
python main.py
``` 

---

## Configuration

Create an API key in the .env file

```
API_KEY=your_api_key_here
```

After that, load it in main.py file before you run the CLI.

---

## License

This project is licensed under the MIT License