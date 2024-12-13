import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(subject, body, to_email):
    from_email = "yaroslavmurz@gmail.com"
    password = "2010ro2524"

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(from_email, password)

        msg = MIMEMultipart()
        msg["From"] = from_email
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "html"))

        server.send_message(msg)
        print("Письмо успешно отправлено!")
        server.quit()
    except Exception as e:
        print(f"Ошибка при отправке письма: {e}")


url = 'https://script.google.com/macros/s/AKfycbzYUVcK6sGXpK1EQdrWSiiN9tNs6QB0R1khVPdwOkAofT4Onb-2juV2udRdM8uiSvnV/exec'
response = requests.get(url)
Animals: list[dict] = response.json()["Animals"]
cost_of_care = 0
number_of_African_animals = 0
most_expensive_animal = None


for animal in Animals:
    if animal["Отруйна"]:
        cost_of_care += animal["Вартість догляду"]
    if animal["Континент"] == "Африка":
        number_of_African_animals += animal["Кількість"]
    if most_expensive_animal is None or animal["Вартість догляду"] > most_expensive_animal["Вартість догляду"]:
        most_expensive_animal = animal

print(f"Общая стоимость ухода за ядовитыми животными: {cost_of_care}")
print(f"Количество африканских животных: {number_of_African_animals}")

if most_expensive_animal:
    subject = "Информация о самой дорогой твари"
    if most_expensive_animal["Отруйна"]:
        body = f"<h3>Самая дорогая в обслуговуванні тварина</h3>"
    else:
        body = f"<h4>Самая дорогая в обслуговуванні тварина</h4>"
    body += f"""
    <p>Название: {most_expensive_animal['Назва тварини']}</p>
    <p>Континент: {most_expensive_animal['Континент']}</p>
    <p>Стоимость ухода: {most_expensive_animal['Вартість догляду']}</p>
    """

    send_email(subject, body, "yaroslavmurz@gmail.com")
