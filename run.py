from exchangelib import DELEGATE, Configuration, Credentials, Account

from functions import read_emails
import config as cfg


if __name__ == '__main__':
    email = cfg.get('CREDENTIALS', 'EMAIL')
    password = cfg.get('CREDENTIALS', 'PASSWORD', encrypted=True)
    read_emails(email, password)
