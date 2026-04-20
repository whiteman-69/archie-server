from flask import Flask, request, jsonify
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_text = data.get("text", "")

    if not user_text:
        return jsonify({"error": "No text provided"}), 400

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are ARCHIE, a friendly AI teddy bear."},
            {"role": "user", "content": user_text}
        ]
    )

    reply = response.choices[0].message.content

    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
