import openai
import json

OPENAI_API_KEY = "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"
openai.api_key = OPENAI_API_KEY

# This method compares safe domain JSON file to a bad domain JSON file and determine whether it is a safe domain or not
def compareDomain(file1, file2):
    
    with open(file1,'r') as badDomain, open(file2,'r') as goodDomain:
        badDomain = json.load(badDomain)
        goodDomain = json.load(goodDomain)

    # Define how openAI will check to see wheather the domain is safe or not
    conversation =  [
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": f'Read in the two Json files {badDomain} and {goodDomain} determine if there is a strong enough correlation to assume both files are talking about the same thing. If yes then return this exact string and nothing else "The link is safe to click", else return this exact string and nothing else "This link is not safe to click on" '},
    ]
    
    # Make the request to the API to create response
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages= conversation,
    temperature=0,
    )

    # Extract the response
    safeOrNot = response['choices'][0]['message']['content']
    return safeOrNot

compareDomain('./app/badDomain.json', './app/goodDomain.json')
