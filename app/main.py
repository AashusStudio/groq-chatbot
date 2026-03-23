from app.chatbot import get_response

def run_chat():
    print("🤖 Groq Chatbot (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        reply = get_response(user_input)
        print(f"Bot: {reply}\n")

if __name__ == "__main__":
    run_chat()