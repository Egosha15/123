import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType 

# токен группы, которая будет добавлять обратно другого бота в беседу
adding_group_token = 'vk1.a.YMdhZCVUTJ1T64WO_G_7DcrLr-yBewCP9gTqeU9AeV9sbo8NxMYuDwOjlJxowQWDgv6SJofkddB1rJkD5mh8umKvBiRoeulLGbeShQNmM2fO2fNgWJluSx5pmYMd14ETsqexIPvna6zwiTpbJ4iE9LV2LEbEQOBLettI22vGac-LfQM8RYhz60rIujDi6Ymm7P2xeZCGwKsVpWAuZlx2sA'

# токен группы, которую нужно будет добавить обратно в беседу
kicked_group_token = 'vk1.a.aeW4MvVFlS_MBTmK2f04rAiLHLFBztYToQoroh2fetG-ZZ3brLXSLUl4Y4NIpkz0wohZfjeBhHZCD34TO33qOx4yUAfTcJ3BB7tH9Syre35d7amXs0TxkmdO2-5_PplUNSjxRJuGgJ1nMe3zpQJ-B88ofDkWb8qIsg9BwGH1QlV7DsOYEGtrJntElJCxdbuO0UWNMdM1xyX6-YTwZrLdDA'

# инициализация сессии и API
vk_session = vk_api.VkApi(token=adding_group_token)
vk = vk_session.get_api()

# инициализация LongPoll
longpoll = VkLongPoll(vk_session)


# функция добавления группы в беседу
def add_group_to_chat(chat_id, group_id):
    vk.messages.addChatUser(chat_id=chat_id, user_id=group_id)


# основной цикл обработки событий
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.from_user:
        # если пришло новое сообщение от пользователя, просто игнорируем его
        pass
    elif event.type == VkEventType.CHAT_KICKED and event.info['user_id'] == -vk_session.group_id:
        # если наш бот был удален из беседы, то добавляем его обратно
        add_group_to_chat(event.chat_id, -vk_session.group_id)
    elif event.type == VkEventType.MESSAGE_NEW and event.text.startswith('!add_bot'):
        # если пришло сообщение "!add_bot", добавляем удаленную группу обратно в беседу
        vk_session_kicked = vk_api.VkApi(token=kicked_group_token)
        vk_kicked = vk_session_kicked.get_api()
        add_group_to_chat(event.chat_id, -vk_kicked.groups.getById()[0]['id'])

