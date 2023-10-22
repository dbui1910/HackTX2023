from kivy.app import App
from kivy.uix.label import Label
from flask import Flask, request
import parse
import test_call_DB

global stringSQLCall 

class MyApp(App):
    def build(self):
        return Label(text="Hello, Kivy!")

app = Flask(__name__)

@app.route('/parseMessage', methods=['GET','POST'])
def parseText():
    text = 'U.S.P.S - The package has arrived at the warehouse and cannot be delivered due to incomplete address information. Confirm your address at the link. https://lihi3.cc/wvfsR '
    stringSQLCall = parse.parseMessage(text)
    return stringSQLCall 

input_query = parseText()
print("before calling the DB")
print(input_query)
placeholder = "SELECT * FROM scams WHERE url_hyperlink_data = 'https://lihi3.cc/wvfsR' OR message_from_sender = 'The package has arrived at the warehouse and cannot be delivered due to incomplete address information. Confirm your address at the link.' OR number_of_sender = 'amy@hotmail.com';"
placeholder = "SELECT * FROM scams WHERE url_hyperlink_data = 'https://lihi3.cc/wvfssssssR' OR message_from_sender = 'aaaaaThe package has arrived at the warehouse and cannot be delivered due to incomplete address information. Confirm your address at the link.' OR number_of_sender = 'amy@hotmail.com';"

test_call_DB.call_the_db(placeholder)

print("After calling call the DB")

#TotalVirusAPI.call_the_VT()


#if __name__ == '__main__':
#   MyApp().run()
#   app.run()

