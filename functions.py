from configparser import ConfigParser
from exchangelib import DELEGATE, Configuration, Credentials, Account


def read_emails(email, password, server='outlook.office365.com'):
    credentials = Credentials(email, password=password)
    config = Configuration(server=server, credentials=credentials)
    account = Account(email, autodiscover=False, config=config, access_type=DELEGATE)

    for item in account.inbox.filter(is_read=False).order_by('-datetime_received')[:100]:
        print(item.subject, item.sender, item.datetime_received)


def read_ini_config(filename='settings.ini', section='DEFAULT'):
    parser = ConfigParser()
    parser.read(filename)
    data = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            data[item[0]] = item[1]
    else:
        raise Exception('{0} not found in the {1} file'.format(section, filename))
    return data
