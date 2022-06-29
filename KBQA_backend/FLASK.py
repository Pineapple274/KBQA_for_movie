from itertools import chain
from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot_graph import ChatBotGraph

app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route("/")
def root():
    return "Yo bro"


@app.route("/query", methods=["POST"])
def query():
    handler = ChatBotGraph()
    question = request.json.get("question")
    answer = handler.chat_main(question)[0].strip()
    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)