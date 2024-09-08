def send_email(message, recipient, sender='university.help@gmail.com'):
    at = '@'
    domens = ['com', 'ru', 'net']


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
        pass
    recipient = recipient.lower()
    sender = sender.lower()
    if sender == recipient:
        print('Нельзя писать самому себе')


send_email("sos", 'university.help@gmail.com')




