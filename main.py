import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header


def send_ya_mail(recipients_emails: list, msg_text: str):
    login = 'kell.me.plz@yandex.ru'
    password = 'your_password'

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
    send_ya_mail(recipients_emails=['hlopchegg@gmail.com', 'kell.me.plz@yandex.ru'], msg_text='Привет, возьми Светку на шашлыки')


if __name__ == '__main__':
    main()
