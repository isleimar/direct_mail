import logging
from dotenv import dotenv_values
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Email():

    def __init__(self):        
        self.__read_env()
        pass
    
    def __read_env(self):
        logging.info('Iniciando classe.')
        logging.info('Lendo variáveis.')
        self.__server = None
        try:
            env_vars = dotenv_values()
            self.__smtp_server = env_vars['SMTP_SERVER']
            self.__smtp_port = env_vars['SMTP_PORT']
            self.__user_name = env_vars['USER_NAME']
            self.__user_password = env_vars['USER_PASSWORD']
            logging.info('Iniciando classe.')
        except Exception as error:
            logging.error("Falha ao ler variáveis  \n '{}'".format(error))
        pass

    @property
    def server(self):
        return self.__server
    @server.setter
    def server(self, server):
        self.__server = server

    @property
    def smtp_server(self):
        return self.__smtp_server
    
    @property
    def smtp_port(self):
        return self.__smtp_port
    
    @property
    def user_name(self):
        return self.__user_name
    
    @property
    def user_password(self):
        return self.__user_password
    
    def connect(self):
        logging.info('Iniciando conexão com o servidor.')
        try:
            self.server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            self.server.starttls()
            logging.info('Efetuando login.')
            self.server.login(self.user_name, self.user_password)
        except Exception as error:
            logging.error("Falha ao conectar com o servidor. \n '{}'".format(error))
        logging.info('Conexão estabelecida com o servidor.')
    
    def quit(self):
        logging.info('Fechando conexão com o servidor.')
        try:            
            self.server.quit()
        except Exception as error:
            logging.error("Falha ao fechar conexão com o servidor. \n '{}'".format(error))
        logging.info('Conexão fechada.')
    
    def send(self, message):
        try:
            logging.info('Iniciando envio de e-mail.')            
            self.server.send_message(message)
            logging.info('Mensagem enviada.')            
        except Exception as error:
            logging.error("Falha ao enviar email  \n '{}'".format(error))
            pass
    pass