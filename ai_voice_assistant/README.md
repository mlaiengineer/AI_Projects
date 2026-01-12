# AI Voice Assistant (Bilingual)

A real-time, web-based voice assistant that supports **English** and **Arabic**. This project uses a Flask backend to connect the browser's Speech Recognition API with OpenAI's GPT-3.5 model for intelligent, spoken responses.

## 🚀 Live Demo
**[Test the Live Project Here](https://ai-projects-6e99.onrender.com/)**

---

## 📸 Project Preview

### English Interaction
![English Demo](https://raw.githubusercontent.com/mlaiengineer/AI_Projects/main/ai_voice_assistant/image_af0983.png)

### Arabic Interaction
![Arabic Demo](https://raw.githubusercontent.com/mlaiengineer/AI_Projects/main/ai_voice_assistant/image_af09ff.png)

---

## 🛠️ Tech Stack
* **Frontend:** HTML5, CSS3, JavaScript (Web Speech API)
* **Backend:** Python, Flask
* **AI Engine:** OpenAI GPT-3.5 API
* **Deployment:** Render & Gunicorn

## 🌟 Key Features
* **Speech-to-Text:** Real-time voice capture via the browser.
* **Bilingual Intelligence:** Fully understands and responds in English and Arabic.
* **Voice Synthesis:** AI responses are read aloud using the browser's text-to-speech engine.
* **Cloud Hosted:** Fully deployed and accessible via a web URL.

## ⚙️ Setup (Local)
1. Clone the repository.
2. Create a `.env` file with your `OPENAI_API_KEY`.
3. Install dependencies: `pip install -r requirements.txt`.
4. Run the app: `python app.py`.