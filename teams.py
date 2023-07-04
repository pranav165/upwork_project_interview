import time
import unittest
import socket
import subprocess
import settings
from appium import webdriver
from datetime import datetime

def get_teams_app_id():
    cmd = 'powershell "Get-StartApps | Where-Object {$_.Name -eq \'Skype\'} | Select-Object AppId"'
    result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
    app_id = result.stdout.strip().split('\n')[-1]
    return app_id

def get_device_name():
    return socket.gethostname()

def log_to_console(msg):
    time_now = datetime.now().isoformat().replace("T", " ")
    return f"{time_now}: {msg}"

class SimpleTeamsTests(unittest.TestCase):

    def setUp(self) -> None:
        desired_caps = {
            "platformName": "Windows",
            "app": get_teams_app_id(),
            "deviceName": get_device_name(),
        }

        self.driver = webdriver.Remote(command_executor="http://127.0.0.1:4723",desired_capabilities=desired_caps)
        print("CONNECTED")
        self.username = settings.MICROSOFT_TEAMS_USERNAME
        self.password = settings.MICROSOFT_TEAMS_PASSWORD
        self.is_initiator = settings.IS_CHAT_INITIATOR
        print(self.username, self.password)

    def tearDown(self):
        self.driver.quit()

    def login(self):
        sign_in_button = self.driver.find_element_by_xpath("//button[contains(text(), 'Sign In')]")
        sign_in_button.click()

        email_field = self.driver.find_element_by_xpath("//input[@name='loginfmt']")
        email_field.send_keys(self.username)

        next_button = self.driver.find_element_by_xpath("//input[@value='Next']")
        next_button.click()
        password_field = self.driver.find_element_by_xpath("//input[@name='passwd']")
        password_field.send_keys(self.password)

        final_sign_in_button = self.driver.find_element_by_xpath("//input[@value='Sign in']")
        final_sign_in_button.click()

    def send_message(self, message):
        channel = self.driver.find_element_by_xpath("//*[@Name='Skype']/Group/Group/Group/Group[starts-with(@Name,'Suhail')]")
        channel.click()

        # Locate the message input field and enter the message
        message_input = self.driver.find_element_by_xpath("//div[@role='textbox']")
        message_input.send_keys(message)

        # Send the message
        send_button = self.driver.find_element_by_xpath("//button[@title='Send']")
        send_button.click()

    def test_login_and_chat(self):
        # self.login()
        log_to_console("Logged In.")
        time.sleep(5)  # Add a delay to allow for successful login

        # Check if the test case is the chat initiator
        if self.is_initiator:
            # Send a message to the specified Microsoft Teams contact
            self.send_message(settings.TEAMS_CONTACT_USERNAME, "Hello, how are you?")
            time.sleep(2)  # Add a delay to allow for the message to be sent

        else:
            # Listen for incoming messages and reply when a message is received
            while True:
                # Implement logic to listen for incoming messages
                # Once a message is received, extract the sender and message content
                sender = "Sender's Name"  # Replace with the actual sender's name
                message_content = "Received message content"  # Replace with the actual received message content

                # Reply to the received message
                reply_message = f"Hi {sender}, thank you for your message!"
                self.send_message(sender, reply_message)
                time.sleep(2)  # Add a delay to allow for the reply message to be sent

                # Add logic to break out of the while loop based on a condition (e.g., specific number of messages received or specific content)


if __name__ == '__main__':

    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleTeamsTests)
    unittest.TextTestRunner(verbosity=2).run(suite)