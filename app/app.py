from kivy.app import App
from kivy.uix.label import Label
from flask import Flask, request
import parse

class MyApp(App):
    def build(self):
        return Label(text="Hello, Kivy!")

app = Flask(__name__)

@app.route('/parseMessage', methods=['GET','POST'])
def parseText():
    text = "U.S.P.S - The package has arruved at the warehouse and cannot be delivered due to incomplete address information.Confirm your address at the link. https://lihi3.cc/wvfsR "
    stringSQLCall = parse.parseMessage(text)
    return stringSQLCall 

if __name__ == '__main__':
#   MyApp().run()
   app.run()