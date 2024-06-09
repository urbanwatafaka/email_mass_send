import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# Необходимо дать доступ к Яндексу в настройках.
# Все настройки -> Почтовые программы -> Поставить галочку к 'С сервера imap.yandex.ru по протоколу IMAP' и все галочки внутри.
def send_ya_mail(recipients_emails: list, msg_text: str):
    login = 'ur_email@yandex.ru' #login = os.getenv('YA_LOGIN', 'kell.me.plz@yandex.ru')
    password = 'ur_password'#password = os.getenv('YA_PASSWORD')
# Логин и пароль можно поместить в переменную среду. Сделать это можно через командную строку(если виндовс)
# setx YA_PASSWORD ваш_пароль

    msg = MIMEText(f'{msg_text}', 'plain', 'utf-8')
    msg['Subject'] = Header('Важно!!!', 'utf-8')
    msg['From'] = login
    msg['To'] = ', '.join(recipients_emails)

    try:
        with smtplib.SMTP('smtp.yandex.ru', 587, timeout=10) as s:
            s.starttls()
            s.login(login, password)
            s.sendmail(msg['From'], recipients_emails, msg.as_string())
    except Exception as ex:
        print(f"Ошибка при отправке почты: {ex}")


def main():
    send_ya_mail(recipients_emails=['mail@mail.ru', 'mail2@mail.ru' ], msg_text='Привет, займи тыщу плиз')


if __name__ == '__main__':
    main()
