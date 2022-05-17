import configparser
from getpass import getpass
from peewee import *
import sys
from time import sleep
from api.models import (Credentials,Posts)

config=configparser.ConfigParser()
config['DEFAULT']={ 
    'HOST':'localhost',
    'DATABASE':'mydb',
    'PASSWORD':'hhimanshu',
    'USER':'hhimanshu'
}

def verify_credentials_and_create_tables():
    '''
    Attempts connecting to database based on suplied credentials.
    Create required tables if it can, else return an error.
    '''

    db=PostgresqlDatabase('mydb',user='hhimanshu',_Password='hhimanshu',host='localhost')

    try:
        db.connect()
        db.create_tables([Credentials,Posts,])
    
    except OperationalError:
        return True
    return None

# def set_interactive_credentials():
#     '''
#     Obtain database variables from user to connect to database, and store in configuration file.
#     '''

#     config['DEFAULT']['HOST']=input('Server name/IP (leave blank if on local serve): ') or config['DEFAULT']['HOST']

#     config['DEFAULT']['DATABASE']=input('The name of database you created (leave blank if using the ' 'name "blogstate"): ') or config['DEFAULT']['DATABASE']

#     config['DEFAULT']['HOST']=input('User name for the database : ') or config['DEFAULT']['USER']

#     config['DEFAULT']['PASSWORD']=getpass('Password for database: ') or config['DEFAULT']['PASSWORD']


def generate_config_files():
    '''
    Gnerate as ini file of the configuration which works so far.
    Running this function overwrites any previous setup values
    '''
    config['TOKENS']={}
    config['TOKENS']['API']='secret'

    with open('config.ini','w') as cfg:
        config.write(cfg)

if __name__=='__main__':
    print('\n============================\n'
    '+++ Development server setup ++++'
    '\n============================\n')
    sleep(1)

    # set_interactive_credentials()

    print('\nAttempt connection to database and create tables ...')
    sleep(0.5)

    err=verify_credentials_and_create_tables()

    if err is not None:
        print('Error occured in database')
        exit(1)

    generate_config_files()

    sleep(0.5)

    print('Database has been setup')


