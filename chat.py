import google.generativeai as genai

# Directly set the API key
api_key = "AIzaSyC1GPKSHn6zLvGBZReodBAZwufQ2aGGlXs"

# Configure Gemini API
genai.configure(api_key=api_key)

# Initialize chat model
model = genai.GenerativeModel("gemini-pro")

# Start conversation
print("Bot: Hello, how can I help you?")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Bot: Goodbye!")
        break
    response = model.generate_content(user_input)
    print("Bot:", response.text)
