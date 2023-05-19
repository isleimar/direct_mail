
import pyexcel
from time import sleep
from jinja2 import Template
from send_email import Email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import dotenv_values

class DirectMail:

    def __init__(self, email: Email):
        self.__email = email        
        env_vars = dotenv_values()
        self.__ods_file_name = env_vars['ODS_FILE']
        self.__message_file_name = env_vars['MSG_FILE']
        self.__from_name = env_vars['FROM_NAME']
        self.__subject = env_vars['SUBJECT']
        self.__reconnect_on = int(env_vars['RECONNECT_ON'])

        pass

    @property
    def email(self):
        return self.__email
    
    @property
    def from_name(self):
        return self.__from_name
    
    @property
    def subject(self):
        return self.__subject
    
    @property
    def reconnect_on(self):
        return self.__reconnect_on

    @property
    def ods_file_name(self):
        return self.__ods_file_name
    
    @property
    def message_file_name(self):
        return self.__message_file_name    

    def send(self):
        data = pyexcel.get_records(file_name=self.ods_file_name)
        with open(self.message_file_name) as file:
            template_content = file.read()
        template = Template(template_content)
        self.email.connect()
        reconnect = self.reconnect_on
        count = 0
        for row in data:
            email_body = template.render(row)
            emails = row['e-mails'].replace(",",";").split(';')
            for email in emails:
                msg = MIMEMultipart()
                if reconnect == 0:
                    reconnect = self.reconnect_on
                    self.email.quit()
                    print("Aguardando...")
                    sleep(5)
                    self.email.connect()
                msg['From'] = self.from_name
                msg['To'] = email
                msg['Subject'] = self.subject
                msg.attach(MIMEText(email_body, 'html'))
                self.email.send(message=msg)
                reconnect -= 1
                count += 1
                print("Enviando email {} - {}".format(email, count))
        self.email.quit()
        pass
    pass