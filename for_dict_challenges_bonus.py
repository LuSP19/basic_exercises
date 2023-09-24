"""
Пожалуйста, приступайте к этой задаче после того, как вы сделали и получили ревью ко всем остальным задачам
в этом репозитории. Она значительно сложнее.


Есть набор сообщений из чата в следующем формате:

```
messages = [
    {
        "id": "efadb781-9b04-4aad-9afe-e79faef8cffb",
        "sent_at": datetime.datetime(2022, 10, 11, 23, 11, 11, 721),
        "sent_by": 46,  # id пользователя-отправителя
        "reply_for": "7b22ae19-6c58-443e-b138-e22784878581",  # id сообщение, на которое это сообщение является ответом (может быть None)
        "seen_by": [26, 91, 71], # идентификаторы пользователей, которые видели это сообщение
        "text": "А когда ревью будет?",
    }
]
```

Так же есть функция `generate_chat_history`, которая вернёт список из большого количества таких сообщений.
Установите библиотеку lorem, чтобы она работала.

Нужно:
1. Вывести айди пользователя, который написал больше всех сообщений.
2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).

Весь код стоит разбить на логические части с помощью функций.
"""

from collections import defaultdict
import random
import uuid
import datetime

import lorem


def count_user_messages(chat_history):
    user_messages_count = defaultdict(int)
    for message in chat_history:
        user_id = message['sent_by']
        user_messages_count[user_id] += 1

    return user_messages_count


def get_user_messages(chat_history):
    user_messages = {}
    for message in chat_history:
        user_id = message['sent_by']
        if user_id in user_messages:
            user_messages[user_id].append(message['id'])
        else:
            user_messages[user_id] = [message['id']]

    return user_messages


def get_message_viewers(chat_history):
    message_viewers = {}
    for message in chat_history:
        message_viewers[message['id']] = message['seen_by']

    return message_viewers


def count_unique_viewers(chat_history):
    user_messages = get_user_messages(chat_history)
    message_viewers = get_message_viewers(chat_history)
    unique_viewers_count = {}
    for user in user_messages:
        unique_viewers = set()
        for message_id in user_messages[user]:
            unique_viewers.update(message_viewers[message_id])
        unique_viewers_count[user] = len(unique_viewers)

    return unique_viewers_count


def count_replies_to_messages(chat_history):
    replies_to_messages_count = defaultdict(int)
    for message in chat_history:
        message_id = message['reply_for']
        if message_id is None:
            continue
        replies_to_messages_count[message_id] += 1

    return replies_to_messages_count


def count_replies_to_users(chat_history):
    replies_to_messages_count = count_replies_to_messages(chat_history)
    replies_to_users_count = {}
    for message in chat_history:
        user_id = message['sent_by']
        message_id = message['id']
        replies_count = replies_to_messages_count.get(message_id, 0)
        if user_id in replies_to_users_count:
            replies_to_users_count[user_id] += replies_count
        else:
            replies_to_users_count[user_id] = replies_count

    return replies_to_users_count


def get_daily_activity(chat_history):
    daily_activity = defaultdict(int)
    for message in chat_history:
        sent_at_hour = message['sent_at'].hour
        if sent_at_hour < 12:
            daily_activity['morning'] += 1
        elif sent_at_hour < 18:
            daily_activity['afternoons'] += 1
        else:
            daily_activity['evening'] += 1

    return daily_activity


def get_largest_value_key(dictionary):
    return max(dictionary, key=dictionary.get)


def get_largest_value_keys(dictionary, count):
    value_key_pairs = sorted(
        ((value, key) for key, value in dictionary.items()), reverse=True
    )[:count]

    return [pair[1] for pair in value_key_pairs]


def generate_chat_history():
    messages_amount = random.randint(200, 1000)
    users_ids = list(
        {random.randint(1, 10000) for _ in range(random.randint(5, 20))}
    )
    sent_at = datetime.datetime.now() - datetime.timedelta(days=100)
    messages = []
    for _ in range(messages_amount):
        sent_at += datetime.timedelta(minutes=random.randint(0, 240))
        messages.append({
            "id": uuid.uuid4(),
            "sent_at": sent_at,
            "sent_by": random.choice(users_ids),
            "reply_for": random.choice(
                [
                    None,
                    (
                        random.choice([m["id"] for m in messages])
                        if messages else None
                    ),
                ],
            ),
            "seen_by": random.sample(users_ids,
                                     random.randint(1, len(users_ids))),
            "text": lorem.sentence(),
        })
    return messages


def main():
    chat_history = generate_chat_history()
    user_messages_count = count_user_messages(chat_history)
    replies_to_messages_count = count_replies_to_messages(chat_history)
    replies_to_users_count = count_replies_to_users(chat_history)
    unique_viewers_count = count_unique_viewers(chat_history)
    daily_activity = get_daily_activity(chat_history)

    print(
        f'User with the most messages: '
        f'{get_largest_value_key(user_messages_count)}'
    )
    print(
        f'User with the most replies: '
        f'{get_largest_value_key(replies_to_users_count)}'
    )
    print('Users with the most seen replies: ', end='')
    print(*get_largest_value_keys(unique_viewers_count, 3), sep=', ')
    print(
        f'Maximum activity period: '
        f'{get_largest_value_key(daily_activity)}'
    )
    print('Messages with the most replies: ', end='')
    print(*get_largest_value_keys(replies_to_messages_count, 3), sep=', ')


if __name__ == "__main__":
    main()
