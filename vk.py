import time
import vk_api

vk = vk_api.VkApi(token = 'Your api token')

param = {
    'count': 1,
    'time_offset': 5,
    'filter': 'unread'
}

def write_msg(user_id, msg, random):
    vk.method('messages.send', {
        'user_id': user_id,
        'message': msg,
        'random_id': random
    })

try:
    while True:
        response = vk.method('messages.getConversations', param)
        print('JSON response: {0}'.format(response))
        if response['items']:
            item = response['items'][0]
            last_mess = item['last_message']
            random = last_mess['random_id']
            my_id = last_mess['peer_id']
            text = last_mess['text'] + '. By the way! I am bot!'
            write_msg(my_id, text, random)
        time.sleep(1)
except KeyboardInterrupt:
    print('Keyboard interrupt detected.')
finally:
    print('The program was stopped.')