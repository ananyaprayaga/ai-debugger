from groq import Groq
import os
import logging
from flask import Flask, request, render_template, jsonify
from flask_cors import CORS


def make_client():
    api_key = os.getenv("GROQ_API_KEY", None)
    if not api_key:
        # Keep behavior similar to the original: if env var missing, don't crash but warn.
        # Users should set GROQ_API_KEY for production use.
        api_key = "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"
    return Groq(api_key=api_key)


client = make_client()


def debug_code(user_code: str) -> str:
    """Send the user's code to the Groq chat model and return the assistant reply.

    Inputs:
      - user_code: Python source code as a string
    Outputs:
      - assistant reply as string on success
      - error message string on failure
    """
    prompt = f"Debug the following Python code. Explain the errors simply and give corrected code:\n{user_code}"

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
        )
        # Response shape: choices[0].message.content
        return response.choices[0].message.content
    except Exception as e:
        logging.exception("debug_code failed")
        return f"Error: {e}"


app = Flask(__name__)
# Limit incoming request size (bytes)
app.config['MAX_CONTENT_LENGTH'] = 64 * 1024  # 64 KB
CORS(app)

logging.basicConfig(level=logging.INFO)


@app.route('/health', methods=['GET'])
def health():
    return jsonify({'ok': True, 'status': 'ready'})


@app.route("/", methods=["GET"])
def index():
    # Render a simple form to paste code and submit
    return render_template("index.html")


@app.route("/api/debug", methods=["POST"])
def api_debug():
    data = request.form or request.json or {}
    code = data.get("code")
    if not code:
        return jsonify({"error": "No code provided"}), 400

    result = debug_code(code)
    return jsonify({"result": result})


if __name__ == "__main__":
    # Simple dev server
    port = int(os.getenv("PORT", "5002"))
    # Run without the reloader/debugger for a stable single process during manual testing
    app.run(host="127.0.0.1", port=port, debug=False)
