import kivy
kivy.require('2.0.0')  # Make sure you have Kivy 2.0.0 or higher installed
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Color, Rectangle
import requests

class MessageApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.message_screen = Screen(name='message')  # Define message_screen here

    def build(self):
        self.screen_manager = ScreenManager()

        # Create a screen for the main UI
        main_screen = Screen(name='main')
        layout = BoxLayout(orientation='vertical', spacing=10)

        self.text_input = TextInput(
            hint_text=("U.S.P.S - The package has arrived at the warehouse and "
                    "cannot be delivered due to incomplete address information. "
                    "Confirm your address at the link. "
                    "https://lihi3.cc/wvfsR (Copy the link to your Safari browser "
                    "and open it)"),
            padding_y=(200, 200),  # Add padding to the top and bottom
            readonly=True  # Make the TextInput read-only
        )
        layout.add_widget(self.text_input)
        self.text_input.bind(on_touch_down=self.open_link_options)  # Bind touch event

        # Middle part: Text input for typing messages
        self.text_input_message = TextInput(hint_text="Type your message here")
        layout.add_widget(self.text_input_message)

        # Bottom part: Send button
        send_button = Button(text="Send")
        send_button.bind(on_press=self.send_message)
        layout.add_widget(send_button)

        main_screen.add_widget(layout)
        self.screen_manager.add_widget(main_screen)

        return self.screen_manager

    def open_link_options(self, instance, touch):
        if self.text_input.collide_point(*touch.pos):  # Check if touch is inside the label
            # Create a Popup with options for opening the link
            self.popup = Popup(title="Open Link Options", size_hint=(None, None), size=(700, 700))

            # Create a BoxLayout for the buttons
            button_layout = BoxLayout(orientation='vertical', spacing=10)

            # Button to open in Safari
            open_safari_button = Button(text="Open with Safari")
            open_safari_button.bind(on_press=lambda x: self.open_link("Safari"))
            button_layout.add_widget(open_safari_button)

            # Button to open in Chrome
            open_chrome_button = Button(text="Open with Chrome")
            open_chrome_button.bind(on_press=lambda x: self.open_link("Chrome"))
            button_layout.add_widget(open_chrome_button)

            # Button to open with MSM and fetch the message from the backend
            open_msm_button = Button(text="Open with MSM")
            open_msm_button.bind(on_press=self.fetch_message_from_backend)
            button_layout.add_widget(open_msm_button)

            # Add the button layout to the popup
            self.popup.content = button_layout

            # Open the popup
            self.popup.open()

    def open_link(self, option):
        # Replace this with your code to open the link based on the selected option
        link = self.text_input.text
        print(f"Opening link in {option}: {link}")

    def fetch_message_from_backend(self, instance):
        api_url = "http://localhost:5001/parseMessage"  # Update to your Flask API URL
        text_to_parse = self.text_input.text

        data = {"text": text_to_parse}
        response = requests.post(api_url, json=data)
        

        if response.status_code == 200:
            # parsed_message = response.json().get("result")
            parsed_message = "Successfull"
            self.display_message(parsed_message)  # Call a method to display the message on a new screen
            if self.popup:
                self.popup.dismiss()  # Close the popup
        else:
            print("Error fetching message from the backend")

    def display_message(self, message):
        #Create a new screen to display the fetched message
        message_screen = Screen(name='message')
        layout = BoxLayout(orientation='vertical', spacing=10)
        message_label = Label(text=message)
        layout.add_widget(message_label)
        message_screen.add_widget(layout)
        self.screen_manager.switch_to(message_screen)
        
    def send_message(self, instance):
        message_text = self.text_input_message.text
        if message_text:
            received_message = Label(text=f"You: {message_text}")
            self.messages_label.text += f"\n{received_message.text}"
            self.text_input_message.text = ""

if __name__ == '__main__':
    MessageApp().run()





