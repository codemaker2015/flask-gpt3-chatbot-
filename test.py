import json
import openai
import os

# openai.api_key = "API_KEY" #os.getenv("API_KEY")
openai.api_key = "" # provide your openai key here

def bot(question):
    prompt = """This is chat between Sushant and Siri. Siri is an AI assistant
    and knows almost everything. It is designed to assist and help humans with
    all kinds of questions and provide them detailed answers to any questions
    that they ask.
    Sushant: {}
    Siri:""".format(question)

    response = openai.Completion.create(
        engine="ada",
        prompt=prompt,
        stop="Sushant:",
        temperature=0,
        max_tokens=200
    )

    json_response = json.dumps(response)
    rep = json.loads(json_response)
    bot_reply = rep['choices'][0]['text']
    return str(bot_reply)
