def send_email(message, recipient, sender='university.help@gmail.com'):
    at = '@'
    domens = ['com', 'ru', 'net']
    recipient = recipient.lower()
    sender = sender.lower()
    if sender == recipient:
        print('Нельзя писать самому себе')
    elif sender == 'university.help@gmail.com':
        print(f'письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! письмо отправлено с адреса {sender} на адрес {recipient}')

    for i in range(len(recipient)):
        have_at = False
        if recipient[i] == at:

            username, after_at = recipient.split("@")
            after_at, domen = after_at.split('.')
            if domen in domens:
                have_at = True
                return have_at
    if not have_at:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')

    for i in range(len(sender)):
        have_at_send = False
        if sender[i] == at:
            username1, after_at1 = sender.split("@")
            after_at1, domen1 = after_at.split('.')
            if domen1 in domens:
                have_at_send = True
                return have_at_send
    if not have_at_send:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')




send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
