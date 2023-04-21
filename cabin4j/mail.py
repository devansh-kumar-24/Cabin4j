import smtplib


server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()

  
server.login('devk.241202@gmail.com', "qjtsexakxfilzyoa")

subject = "CHALLENGES COMPLETED"
body = " NAME: Devansh Kumar \n Email: devansh.2125it1176@kiet.edu \n Ph.No:7310640877 \nB.Tech IT \n 2nd year \n2100290130063 \n photo: https://drive.google.com/file/d/183x9gvbwF27rtAUJzh6Z8DpprnpPiyMa/view?usp=share_link"
msg = f"subject: {subject} \n\n\n {body}"

server.sendmail(
        'devk.241202@gmail.com',
        'sales@cabin4j.com',
    msg
    )
print('Message is sent succesfully!')

