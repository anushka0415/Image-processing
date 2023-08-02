import openai
from config import CONFIG
import random
import time
import requests
import json

def generate_openai_answer(
    prompt,
    api_key=CONFIG["open_ai"]["api-key"],


    model=CONFIG["open_ai"]["openai_model_name"],
):
    try_no=0
   
    openai.api_key = api_key
    while try_no <=5:
        try_no +=1
        try:
            response = openai.ChatCompletion.create(
            model=model, messages=[{"role": "user", "content": prompt}]
            )

            message = response["choices"][0]["message"]["content"].strip()
            return message
        except openai.error.AuthenticationError as e:
            print("Authentication error: Please check your API key.")
        except openai.error.InvalidRequestError as e:
            print(f"Invalid request error: {e}")
        except openai.error.RateLimitError as e:
            print("Rate limit error: We have exceeded the number of requests allowed by the API.")
            print(f"retrying in 20 seconds # RETRY NO {try_no}/ 5 retries")
            time.sleep(20)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")





# URL = "https://8b2a-172-190-140-49.ngrok-free.app/generate"

#URL = "https://1054-40-114-69-45.ngrok-free.app/generate"


'''def generate_falcon(inp):

    data = {"text": inp}

    headers = {'Content-type': 'application/json'}

    response = requests.post(URL, data=json.dumps(data), headers=headers)

    return response.json()['sequences'][0]['generated_text'][len(inp):].strip().replace("\n", "")'''





