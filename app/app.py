import openai
from flask import Flask, jsonify, request
import test_call_DB
import TotalVirusAPI
import domain

app = Flask(__name__)

OPENAI_API_KEY = "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"
openai.api_key = OPENAI_API_KEY

global stringSQLCall 

def parse_message(text):
    # Define how OpenAI will interpret the text
    conversation =  [
    {"role": "system", "content": "You are a helpful assistant that reads in message and extract information"},
    {"role": "user", "content": "This is the message that I recieved: " +text },
    {"role": "user", "content": "Extract the sender of the message, the URL link and the message content."},
    {"role": "user", "content": "create a varaible named party_claimed_by_sender and save where the message came from/the author of the message"},
    {"role": "user", "content": "Return a string in this exact format:SELECT * FROM scams WHERE url_hyperlink_data = 'extracted URL link' OR message_from_sender = 'the message content'"}
    ]
    
    # Make the request to the API to create a response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation,
        temperature=0,
    )

    # Extract the response
    stringSQLCall = response['choices'][0]['message']['content']

    # return stringSQLCall
    message_sender = " OR number_of_sender = 'amy@hotmail.com';"
    comboString = stringSQLCall + message_sender
    print(comboString)
    print("inside parse")
    print(comboString + "This is an app")
    return comboString
 


@app.route('/', methods=['GET'])
def get_data():
    data = {"message": "Hello from Flask API!"}
    return jsonify(data)

@app.route('/parseMessage', methods=['GET','POST'])
def parseText():
    text = "U.S.P.S - The package has arrived at the warehouse and cannot be delivered due to incomplete address information.Confirm your address at the link. https://lihi3.cc/wvfsR "
    # stringSQLCall = parse_message(text)
    # # Call the functions to get the lists of strings
    # list1 = "There has been a match in our database. DO NOT CLICK ON THE LINK!"
    # list2 = "WEBSITE NOT FOUND! Moving on to layer 3..."
    # # list3 = domain.compareDomain('/Users/diembui/hacktx/HackTX2023/app/badDomain.json', '/Users/diembui/hacktx/HackTX2023/app/goodDomain.json')
    # list3= "This link is not safe"

    # # Combine the lists into one
    # combined_list = list1 + list2 + list3
    
    # return jsonify(combined_list)
    stringSQLCall = parse_message(text)

    return stringSQLCall


input_query = parseText()
print("before calling the DB")
print(input_query)
placeholder = "SELECT * FROM scams WHERE url_hyperlink_data = 'https://lihi3.cc/wvfsR' OR message_from_sender = 'The package has arrived at the warehouse and cannot be delivered due to incomplete address information. Confirm your address at the link.' OR number_of_sender = 'amy@hotmail.com';"
placeholder = "SELECT * FROM scams WHERE url_hyperlink_data = 'https://lihi3.cc/wvfssssssR' OR message_from_sender = 'aaaaaThe package has arrived at the warehouse and cannot be delivered due to incomplete address information. Confirm your address at the link.' OR number_of_sender = 'amy@hotmail.com';"

#test_call_DB.call_the_db(placeholder)

print("After calling call the DB")
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
