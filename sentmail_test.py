import smtplib



print('write the massage  ')
content = str(input())
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login("mandalsuman760@gmail.com", 'mabirisussum')
server.sendmail('mandalsuman760@gmail.com', "28sudeshnadey@gmail.com", content)
server.close()
print('Email sent!')
