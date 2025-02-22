from flask import Flask, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Initialize Gemini API
genai.configure(api_key="YOUR_GEMINI_API_KEY")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"error": "Message is required"}), 400

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(user_input)

    return jsonify({"response": response.text})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
