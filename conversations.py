import requests
import json

# Replace with your API key
api_key = 'YOUR API KEY HERE'
endpoint = 'https://api.openai.com/v1/engines/text-davinci-003/completions'

headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

# Define a function to send a message to ChatGPT
def send_message(prompt):
    data = {
        'prompt': prompt,
        'max_tokens': 50,
        'n': 1,
        'stop': None,
        'temperature': 0.5,
    }
    response = requests.post(endpoint, headers=headers, json=data)
    if response.status_code == 200:
        response_text = response.json()['choices'][0]['text'].strip()
        return response_text
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None

# Collect and store conversation data
conversations = []
user_input = ""

while user_input.lower() != "exit":
    user_input = input("You: ")
    if user_input.lower() != "exit":
        chatgpt_response = send_message(user_input)
        if chatgpt_response:
            print(f"ChatGPT: {chatgpt_response}")
            conversations.append({
                'user': user_input,
                'chatgpt': chatgpt_response
            })

# Save the conversation data to a .txt file
with open('conversations.txt', 'w') as outfile:
    for conversation in conversations:
        outfile.write(f"You: {conversation['user']}\n")
        outfile.write(f"ChatGPT: {conversation['chatgpt']}\n")
        outfile.write("\n")
