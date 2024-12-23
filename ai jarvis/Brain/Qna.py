
API = "OpenAI API Key"


import openai
from dotenv import load_dotenv

openai.api_key = API
load_dotenv()
completion = openai.Completion()

def QuestionsAnswer(question):
    FileLog = open("DataBase\\qna_log.txt", "r")
    Qna_log_template = FileLog.read()
    FileLog.close()

    prompt = f'{Qna_log_template}Question : {question}\nAnswer : '
    response = completion.create(model="text-davinci-002",
        prompt=prompt,
        temperature=0,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)
    answer = response.choices[0].text.strip()
    Qna_log_template_update = Qna_log_template + f"\nQuestion : {question} \nAnswer : {answer}"
    FileLog = open("DataBase\\qna_log.txt", "w")
    FileLog.write(Qna_log_template_update)
    FileLog.close()
    return answer