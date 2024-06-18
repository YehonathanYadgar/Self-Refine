import os
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
from colorama import Fore, Back, Style, init

class SelfRefiner:
    # loading the openai api key,and asingning is to a attribute in the object
    def __init__(self):
        load_dotenv(find_dotenv())
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def refine_answer(self, initial_prompt, feedback_prompt, refine_prompt, initial_model, feedback_model,refine_model,num_iterations):
        # generating inital answer
        answer_text = self.client.chat.completions.create(
            model = initial_model,
            messages = [
            {"role": "system", "content": 'you are an helpfull asistant'},
            {"role": "user", "content": initial_prompt}

            ]
        )
        answer_text = answer_text.choices[0].message.content
        print(answer_text)

        # looping in order to do the feedback,response cycle
        for i in range(num_iterations):
            # giving feedback to the initial,and refined answer
            feedback = self.client.chat.completions.create(
                model=feedback_model,
                messages=[
                    {"role": "user", "content": initial_prompt},
                    {"role": "assistant", "content": answer_text},
                    {"role": "user", "content": feedback_prompt}
                ]
            )
            feedback_text = feedback.choices[0].message.content
            print("="*118)
            print(f'Iteration:{i}')
            print(Fore.RED + feedback_text)

            # making a refined answer using the feedback
            refined_response = self.client.chat.completions.create(
                model=refine_model,
                messages=[
                    {"role": "user", "content": answer_text},
                    {"role": "assistant", "content": feedback_text},
                    {"role": "user", "content": refine_prompt}
                ]
            )
            answer_text = refined_response.choices[0].message.content
            print("?"*118)
            print(f'Iteration:{i}')
            print(Fore.BLUE + answer_text)

        return answer_text

# Usage
refiner = SelfRefiner()
initial_prompt = "make a song about birds"
feedback_prompt = "check the song and give critical feedback about it"
refine_prompt = "Make a new song using the feedback you have got."
num_iterations = 2
refined_answer = refiner.refine_answer(initial_prompt, feedback_prompt, refine_prompt, initial_model="gpt-3.5-turbo", feedback_model="gpt-3.5-turbo", refine_model="gpt-3.5-turbo",num_iterations=num_iterations)
