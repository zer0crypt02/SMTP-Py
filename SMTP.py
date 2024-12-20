import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Gönderen:
gonderen = 'gonderenmail@gmail.com'
gonderen_passwd = 'gonderenşifre'

# Alıcı:
alici = 'alicimail@gmail.com'

# E posta Içeriği:
konu = 'Python'
mesaj = 'Mail Gönderme'

# MIME Formatına Dönüştürme:
email = MIMEMultipart()
email['From'] = gonderen
email['To'] = alici
email['Subject'] = konu
email.attach(MIMEText(mesaj, 'plain'))

try: 
    # SMTP Sunucusuna Bağlan:
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(gonderen, gonderen_passwd)
        
        # Eposta Gönder:
        server.sendmail(gonderen, alici, email.as_string())
        print('Eposta gönderildi')
        
except Exception as e:
    print('Eposta Gönderilemedi: ', e)