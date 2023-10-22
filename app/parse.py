import openai

OPENAI_API_KEY = "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"
openai.api_key = OPENAI_API_KEY

text = ""
# This method takes in a text (String) and parse out the sender, the URL and the content of the message in the format of a sql call as a String type
def parseMessage(text):
    
    # Define how openAI will interprete the text
    conversation =  [
    {"role": "system", "content": "You are a helpful assistant that reads in message and extract information"},
    {"role": "user", "content": "This is the message that I recieved: " +text },
    {"role": "user", "content": "Extract the sender of the message, the URL link and the message content."},
    {"role": "user", "content": "create a varaible named party_claimed_by_sender and save where the message came from/the author of the message"},
    {"role": "user", "content": 'Return a string in this exact format:WHERE url_hyperlink_data = "extracted URL link" OR message_from_sender = "the message content"'}
    ]
    
    # Make the request to the API to create response
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages= conversation,
    temperature=0,
    )

    # Extract the response
    stringSQLCall = response['choices'][0]['message']['content']
    return stringSQLCall

