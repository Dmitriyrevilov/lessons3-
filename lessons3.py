import smtplib 
import os 
from dotenv import load_dotenv, find_dotenv 
import logging

load_dotenv(find_dotenv()) 


letter="""From: {send_adress} 
To: {recip_adress} 
Subject: {heading} 
Content-Type: text/plain; charset="UTF-8";  


Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%! 
%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл. 
""". format(send_adress = "dimrevilov@mail.ru", recip_adress = "dmitryrevilov@yandex.ru", heading = "Приглашение")

letter = letter.replace  ("%website%" , "https://dvmn.org/profession-ref-program/dimrevilov/74reg/ ")
letter = letter.replace ("%friend_name%" , "Артём")
letter = letter.replace ("%my_name%" , "Дмитрий")


send_adress = "Адрес отправителя"
recip_adress = "Адрес получателя" 
heading = "Заголовок письма"
site_name = "https://dvmn.org/profession-ref-program/dimrevilov/74reg/"
friends_name = "Артём"
send_name = "Дмитрий"

send_adress = os.environ['SEND_ADRESS']
password_name = os.environ['PASSWORD_NAME']
recip_adress = "dmitryrevilov@yandex.ru"


letter = letter.encode("UTF-8")
server = smtplib.SMTP_SSL('smtp.mail.ru:465')
server.login(send_adress, password_name)
server.sendmail(send_adress,recip_adress, letter)

server.quit()