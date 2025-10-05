from groq import Groq
import os


client = Groq(api_key=os.getenv("GROQ_API_KEY", "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"))

def debug_code(user_code):
    prompt = f"Debug the following Python code. Explain the errors simply and give corrected code:\n{user_code}"
    
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",  
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    print("Paste your Python code below.")
    print("When finished, type END on a new line and press Enter.\n")

    user_code = ""
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        user_code += line + "\n"

    print("\n--- AI Debugger Output ---\n")
    print(debug_code(user_code))
