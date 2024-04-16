from flask import Flask, render_template, request
import jsonify

app = Flask(__name__)

# Placeholder for your AI model's response generation
def generate_response(user_input):
    # Replace this with your AI model's logic
    return "AI Response"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_text = request.args.get('msg')
    return generate_response(user_text)

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.get_json()
    user_message = data['message']
    # Process user message and get bot response
    bot_response = get_bot_response(user_message)
    return jsonify({'response': bot_response})

#if __name__ == "__main__":
app.run()