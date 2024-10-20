from flask import Flask, render_template, request, jsonify
from huggingface_hub import InferenceClient
import pdb

app = Flask(__name__)


# Route for the home page
@app.route("/")
def home():
    return render_template("index.html")


# Route to handle chat messages (AJAX request)
@app.route("/send_message", methods=["POST"])
def send_message():
    user_message = request.json["message"]  # Get the message from the user
    # Simulate a bot response
    bot_response = ask_question_with_phi(user_message)
    return jsonify({"response": bot_response})


client = InferenceClient(api_key="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")


def ask_question_with_phi(question):
    """
    Asks a question using the 'microsoft/Phi-3.5-mini-instruct' model with optional context.

    Parameters:
    question (str): The question to ask.
    context (str, optional): Additional context from the document.

    Returns:
    str: The model's response.
    """
    try:
        print(question)
        messages = [{"role": "user", "content": f"Question: {question}"}]

        output = client.chat.completions.create(
            model="microsoft/Phi-3.5-mini-instruct",
            messages=messages,
            stream=True,
            temperature=0.5,
            max_tokens=1024,
            top_p=0.7,
        )

        # Collect all chunks in a list and join them after the loop
        full_response = []
        for chunk in output:
            full_response.append(chunk.choices[0].delta.content)

        return "".join(full_response)

    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    app.run(debug=True)
