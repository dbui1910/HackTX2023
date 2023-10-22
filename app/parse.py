import openai

# OPENAI_API_KEY = "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"
# openai.api_key = OPENAI_API_KEY

# text = ""
# # This method takes in a text (String) and parse out the sender, the URL and the content of the message in the format of a sql call as a String type
# def parseMessage(text):
    
#     # Define how openAI will interprete the text
#     conversation =  [
#     {"role": "system", "content": "You are a helpful assistant that reads in message and extract information"},
#     {"role": "user", "content": "This is the message that I recieved: " +text },
#     {"role": "user", "content": "Extract the sender of the message, the URL link and the message content."},
#     {"role": "user", "content": "create a varaible named party_claimed_by_sender and save where the message came from/the author of the message"},
#     {"role": "user", "content": "Return a string in this exact format:SELECT * FROM scams WHERE url_hyperlink_data = 'extracted URL link' OR message_from_sender = 'the message content'"}
#     ]
    
#     # Make the request to the API to create response
#     response = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages= conversation,
#     temperature=0,
#     )

#     # Extract the response
#     stringSQLCall = response['choices'][0]['message']['content']
#     #print(stringSQLCall)
#     message_sender = " OR number_of_sender = 'amy@hotmail.com';"
#     comboString = stringSQLCall + message_sender
#     print(comboString)
#     print("inside parse")
#     return comboString

# text = "U.S.P.S - The package has arrived at the warehouse and cannot be delivered due to incomplete address information.Confirm your address at the link. https://lihi3.cc/wvfsR "
# parseMessage(text)