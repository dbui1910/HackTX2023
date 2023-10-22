import openai
from flask import Flask, jsonify, request

app = Flask(__name__)

OPENAI_API_KEY = "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"
openai.api_key = OPENAI_API_KEY

def parse_message(text):
    # Define how OpenAI will interpret the text
    conversation = [
        {"role": "system", "content": "You are a helpful assistant that reads in messages and extracts information"},
        {"role": "user", "content": "This is the message that I received: " + text},
        {"role": "user", "content": "Extract the sender of the message, the URL link, and the message content."},
        {"role": "user", "content": 'Return a string in this format:"WHERE url_hyperlink_data = extracted URL link AND message_from_sender = the message content AND party_claimed_by_sender: where the message came from/the author of the message'}
    ]
    
    # Make the request to the API to create a response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation,
        temperature=0,
    )

    # Extract the response
    stringSQLCall = response['choices'][0]['message']['content']

    return stringSQLCall

@app.route('/', methods=['GET'])
def get_data():
    data = {"message": "Hello from Flask API!"}
    return jsonify(data)

@app.route('/parseMessage', methods=['GET','POST'])
def parseText():
    text = "U.S.P.S - The package has arrived at the warehouse and cannot be delivered due to incomplete address information.Confirm your address at the link. https://lihi3.cc/wvfsR "
    stringSQLCall = parse_message(text)
    return stringSQLCall 


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
