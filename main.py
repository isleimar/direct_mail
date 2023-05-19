import logging
from direct_mail import DirectMail
from send_email import Email
def main():
    logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    email = Email()    
    dm = DirectMail(email=email)
    dm.send()
    pass

if __name__ == "__main__":
    main()