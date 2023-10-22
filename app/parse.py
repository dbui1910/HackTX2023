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
    {"role": "user", "content": 'Return a string in this format:"WHERE url_hyperlink_data = extracted URL link AND message_from_sender = the message content AND party_claimed_by_sender: where the message came from/the author of the message'}
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

