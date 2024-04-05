import requests
from fake_useragent import UserAgent
from wbsell import OPENAI_KEY


openai_url = 'https://api.openai.com/v1/chat/completions'
question_reply_url = 'https://feedbacks-api.wildberries.ru/api/v1/questions'
feedback_reply_url = 'https://feedbacks-api.wildberries.ru/api/v1/feedbacks'

def get_ai_response(msg):
    headers = {
                'User-Agent':str(UserAgent().random),
                'Content-Type': 'application/json; charset=utf-8',
                'Authorization':'Bearer '+OPENAI_KEY
            }
    payload = {
                'model': 'gpt-3.5-turbo',
                'messages': [
                    {'role': 'system', 'content': 'Ты помощник, который генерирует ответы на полученные отзывы и вопросы.'},
                    {'role': 'user', 'content': 'Сгенерируй ответ до 20 слов на данное сообщение: '+msg}
                ],
                'temperature': 1.0
            }
    response = requests.post(openai_url, json=payload, headers=headers, stream=False)
    return response.json()['choices'][0]['message']['content']
