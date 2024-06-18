import os 
from openai import OpenAI
from dotenv import load_dotenv , find_dotenv
import prompts


_  = load_dotenv(find_dotenv())
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
    )


fake_answer = "The rapid advancement of technology has led to the emergence of groundbreaking concepts such as  AI, and nanotechnology. These innovations have paved the way for revolutionary developments in fields like genetic engineering and augmented reality. With the integration of blockchain and robotics, we are witnessing a transformative era in biotechnology and IoT. 3D printing and virtual reality are reshaping industries, while renewable energy and cybersecurity are becoming paramount in our digital world. The convergence of neurotechnology and space exploration is pushing boundaries, while autonomous vehicles and bioinformatics are shaping the future of transportation and healthcare. Quantum cryptography and wearable technology are ensuring secure communication and personal data protection."


def self_refine(prompt):
    messages= [
        {"role": "system", "content": "your are an asistant"},
        {"role": "user", "content": prompt}
            ]
    
    
    answer = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    answer_text = answer.choices[0].message.content
    print(answer_text)


    for i in range(2):
        feedback = client.chat.completions.create(
            model="gpt-4",
            messages=[
            {"role": "user", "content": prompt},
            {"role": "assistant", "content": answer_text},
            {"role": "user", "content": prompts.feedback_prompt}
            ]
        )
        print("======================================================================================================================")
        print(i)
        feedback_text = feedback.choices[0].message.content
        print(feedback_text)


        refined_answer = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
            {"role": "user", "content": answer_text},
            {"role": "assistant", "content": feedback_text},
            {"role": "user", "content": "make a new poem using the feedback you have got" }
            ]
        )
        print("????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????")
        print(i)
        refined_answer_text = refined_answer.choices[0].messae.content
        answer_text= refined_answer_textg
        print(answer_text)


self_refine(prompts.start_prompt)   
   







