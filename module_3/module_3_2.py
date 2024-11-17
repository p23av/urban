def send_email(message, recipient, *, sender='university.help@gmail.com'):
    has_at = '@' in recipient and '@' in sender
    # is_valid_domain = (recipient.endswith('.com') or recipient.endswith('.ru') or recipient.endswith('.net')) and (sender.endswith('.com') or sender.endswith('.ru') or sender.endswith('.net'))
    is_valid_domain = (recipient.endswith(tuple(['.com', '.ru', '.net']))) and (sender.endswith(tuple(['.com', '.ru', '.net'])))
    if  has_at == False or is_valid_domain == False:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif recipient == sender:
        print(f'Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')