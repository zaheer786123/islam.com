from flask import Flask, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Configure Gemini API
genai.configure(api_key="YOUR_GEMINI_API_KEY")
model = genai.GenerativeModel('gemini-pro')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    response = model.generate_content(user_message)
    return jsonify({'response': response.text})

if __name__ == '__main__':
    app.run(debug=True)