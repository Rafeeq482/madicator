import openai
import os
import time
import sys

# Set your Azure OpenAI credentials
api_key = "2558fb7b74aa49f58474e5a160a99fd3"
endpoint = "https://openai0878675.openai.azure.com/"
deployment_name = "gpt-35-turbo-16k"

# Initialize the OpenAI API client
openai.api_type = "azure"
openai.api_key = api_key
openai.api_base = endpoint
openai.api_version = "2023-05-15"

def say(str):
    for letter in str + '\n':
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.03)


print("***********************************************************************************************************************")
print('''


 ▄▄       ▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░▌     ▐░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░▌░▌   ▐░▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌
▐░▌▐░▌ ▐░▌▐░▌▐░▌          ▐░▌       ▐░▌    ▐░▌     ▐░▌          ▐░▌       ▐░▌     ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌
▐░▌ ▐░▐░▌ ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌       ▐░▌    ▐░▌     ▐░▌          ▐░█▄▄▄▄▄▄▄█░▌     ▐░▌     ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌
▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌    ▐░▌     ▐░▌          ▐░░░░░░░░░░░▌     ▐░▌     ▐░▌       ▐░▌▐░░░░░░░░░░░▌
▐░▌   ▀   ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░▌       ▐░▌    ▐░▌     ▐░▌          ▐░█▀▀▀▀▀▀▀█░▌     ▐░▌     ▐░▌       ▐░▌▐░█▀▀▀▀█░█▀▀ 
▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌    ▐░▌     ▐░▌          ▐░▌       ▐░▌     ▐░▌     ▐░▌       ▐░▌▐░▌     ▐░▌  
▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▄▄▄▄█░█▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌       ▐░▌     ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░▌      ▐░▌ 
▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌     ▐░▌     ▐░░░░░░░░░░░▌▐░▌       ▐░▌
 ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀       ▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀ 
                                                                                                                    
                                                                                            
''')
say("Welcome")
time.sleep(0.5)
say("I am Medicator, an artificial intelligence powered assistant that helps you find the right medicines for your symptoms.")
time.sleep(0.5)
say("I can provide you with information on the best medicines to take for a variety of ailments.")
time.sleep(0.8)
say("Go on!")
print("***********************************************************************************************************************")


def get_advice(illness):
    prompt = f"You are a medical assistant. Provide advice for the following symptoms: {illness}. Include common over-the-counter medications if applicable."
    response = openai.ChatCompletion.create(
        engine=deployment_name,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content'].strip()

def main():
    print("Welcome to the Medical Assistant Chatbot!")
    while True:
        user_input = input("Please describe your symptoms (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        advice = get_advice(user_input)
        print(f"Advice: {advice}\n")

if __name__ == "__main__":
    main()
