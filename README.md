# chatBot
2. Install dependencies
pip install -U google-genai

🔑 Setup API Key

Get your API key from Google AI Studio and set it as an environment variable.

Windows (PowerShell)
$env:GEMINI_API_KEY="YOUR_API_KEY"

macOS / Linux
export GEMINI_API_KEY="YOUR_API_KEY"


Or you can pass the key directly in the code:

client = genai.Client(api_key="YOUR_API_KEY")

🧩 Usage

Run the chatbot:

python simple_chatbot.py


You will see:

Simple Gemini Chatbot! Type 'exit' to quit.

You:


Start chatting!

🧪 Example Code
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

chat = client.chats.create(model="gemini-2.5-flash")

print("Simple Gemini Chatbot! Type 'exit' to quit.\n")

while True:
    user_msg = input("You: ")

    if user_msg.lower() == "exit":
        print("Goodbye!")
        break

    response = chat.send_message(user_msg)
    print("Bot:", response.text)

📁 Project Structure
simple-gemini-chatbot/
│── simple_chatbot.py
│── README.md
│── requirements.txt (optional)

🛠 Requirements

Python 3.9+

google-genai library

Gemini API key

📌 Future Improvements

Add GUI with Tkinter

Add voice input/output

Create a web version using FastAPI or Flask

Save chat history
