# Chatgpt_Automation_tool
OSS Development

ChatGPT Automation is a Python project that tries to make it easier to talk to OpenAI's ChatGPT using Selenium WebDriver. Right now, a person has to log in and confirm their identity. It manages starting Chrome, connecting to ChatGPT, sending messages, and getting replies. This tool can help you try out ChatGPT or make other automated web tools.

Prerequisites
1. Install all required libraries.
2. Download the appropriate version of chromedriver.exe and save it to a known location on your system.

   
create a python file and insert the following code and make the necessary changes.

from handler.chatgpt_selenium_automation import ChatGPTAutomation
# Define the path where the chrome driver is installed on your computer
chrome_driver_path = r"C:\Users\user\Desktop\chromedriver.exe"
# the sintax r'"..."' is required because the space in "Program Files" in the chrome path
chrome_path = r'"C:\Program Files\Google\Chrome\Application\chrome.exe"'
# Create an instance
chatgpt = ChatGPTAutomation(chrome_path, chrome_driver_path)
# Define a prompt and send it to chatgpt
prompt = "Write an example of a database schema for an online store"
chatgpt.send_prompt_to_chatgpt(prompt)
# Retrieve the last response from ChatGPT
response = chatgpt.return_last_response()
print(response)
# Save the conversation to a text file
file_name = "conversation.txt"
chatgpt.save_conversation(file_name)
# Close the browser and terminate the WebDriver session
chatgpt.quit()

Note
After instantiating the ChatGPTAutomation class, chrome will open up to chatgpt page, it will require you to manually complete the register/ log-in / Human-verification. After that, you must tell the program to continue, in the console type 'y'. After Those steps, the program will be able to continue autonomously.


Since all the steps have been followed for the application to work you will need to launch it from the command line on your computer as an administrator. because this way you will bypass Google Chrome permissions.
