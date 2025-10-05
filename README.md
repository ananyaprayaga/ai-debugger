# ai-debugger
## ai-debugger

A small AI-powered Python code debugger web app using Groq's chat completions.

### Features

- Web UI to paste Python code and receive an explanation plus corrected code from the model.

### Requirements

- Python 3.8+
- A Groq API key (set in the environment variable GROQ_API_KEY). For local testing the repo includes a demo fallback key but you should set your own.

### Quick start

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export GROQ_API_KEY=your_real_api_key_here
python app.py
```

Open http://127.0.0.1:5000 in your browser.

### Notes

- This is a minimal demo. The Groq API usage is synchronous and simple; for production consider async/queued requests, error handling, rate-limiting, and not embedding fallback API keys in code.
- The UI is intentionally minimal to focus on functionality. Contributions welcome.
