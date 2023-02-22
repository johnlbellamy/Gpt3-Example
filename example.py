import os
from dotenv import load_dotenv
import openai

load_dotenv()

openai.api_key = os.environ.get('OPENAI_KEY')
completion = openai.Completion()

import argparse

def ask(question):
    """Answers a user question passed as required arg1 and logs prompt to file"""

    with open("logs", "r") as file:
        logs = file.read()
    
    prompt = f'{logs}Human: {question}\nAI:'
    response = completion.create(
        prompt=prompt, engine="davinci", stop=['\nHuman'], temperature=0.9,
        top_p=1, frequency_penalty=0, presence_penalty=0.6, best_of=1,
        max_tokens=150)
    answer = response.choices[0].text.strip()
    
    with open("logs", "a") as file:
        file.write(f"{prompt} {answer}\n")
    return answer

if __name__=="__main__":
    parser = argparse.ArgumentParser("simple_example")
    parser.add_argument("question", 
                        help="Passes a prompt to OpenAI GPT3.", 
                        type=str)
    args = parser.parse_args()
    answer = ask(args.question)
    print(answer)
    

    
