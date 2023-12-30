from dotenv import load_dotenv
import os
import openai

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Ajouter votre clé API OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

def check_text(input):
    messages = [
        {"role": "user",
         "content": ""},
    ]

    messages.append({"role": "user", "content": f"{input}"})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    reply = completion.choices[0].message.content
    return reply


