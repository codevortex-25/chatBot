from google import genai

client = genai.Client(api_key="AIzaSyB6v9jwYXdL7asoOgbh3HiI0oX2GT2ZFGg")

chat = client.chats.create(model="gemini-2.5-flash")

print("Simple Gemini Chatbot! Type 'exit' to quit.\n")

while True:
    user_msg = input("You: ")
    if user_msg.lower() == "exit":
        break
    response = chat.send_message(user_msg)
    print("Bot:", response.text)
