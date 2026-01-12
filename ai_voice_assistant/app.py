from flask import Flask, render_template
import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from openai import OpenAI

# Try to load the .env file explicitly
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Check if the key was actually found
if not api_key:
    print("CRITICAL ERROR: API Key not found in .env file!")
else:
    print(f"API Key loaded successfully (Starts with: {api_key[:5]}...)")

client = OpenAI(api_key=api_key)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask_ai():
    try:
        data = request.get_json()
        user_message = data.get('message')
        print(f"User sent: {user_message}")

        # Calling OpenAI
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}]
        )
        
        # Extracting the text
        ai_reply = response.choices[0].message.content
        print(f"AI Response: {ai_reply}") # Check your terminal for this!
        
        return jsonify({'reply': ai_reply})
    
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'reply': "Error connecting to AI"}), 500
if __name__ == "__main__":
    app.run(debug=True)