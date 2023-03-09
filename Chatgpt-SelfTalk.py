import pprint
import openai
import time

openai.api_key = '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'


# Fügt den aktuellen Chat an die Liste an
def update_chat(messages, role, content):
    messages.append({"role": role, "content": content})
    return messages

# Generiert eine Antwort


def get_chatgpt_response(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response['choices'][0]['message']['content']


# Vorgeschriebens Gespräch
messages = [{'content': 'This is a conversation between 2 good friends talking about '
             'their feelings',
             'role': 'system'},
            {'content': 'Anna: Hey Max! How  are you', 'role': 'assistant'},
            {'content': 'Max: Hey Anna. Not really good at the moment',
             'role': 'assistant'}]
# Counter um Loop zu brechen
c = 0

# Chat Loop
while True:
    # Error handler
    try:
        pprint.pprint(messages)
        model_response = get_chatgpt_response(messages)
        messages = update_chat(messages, "assistant", model_response)

        model_response = get_chatgpt_response(messages)
        messages = update_chat(messages, "assistant", model_response)
    # Lässt das Programm schlafen sollte die Tokens/min überschritten werden
    except (openai.error.RateLimitError):
        time.sleep(60)
    c += 1
    if c >= 15:
        break
