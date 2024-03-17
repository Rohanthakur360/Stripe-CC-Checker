import requests

def hit_sender(card,message,chat_id):
    bot_token = 'Your bot token'
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    data = {'chat_id': chat_id, 'text': message}
    requests.post(url, data=data)
