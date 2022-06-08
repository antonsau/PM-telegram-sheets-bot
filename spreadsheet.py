from datetime import date
import re
import json

import pygsheets


# Load config parameters
with open('config.json') as config:
    CONFIG = json.load(config)

# Set client
client = pygsheets.authorize(service_account_file='service_account.json')
spreadsheet_url = CONFIG['SPREADSHEET_URL']


def add_new_message(message):

    spreadsheet = client.open_by_url(spreadsheet_url)
    sheet = spreadsheet.worksheet('title', '01 - Журнал')

    links_list = []
    links_regx = re.compile(r"<a[^>]+href=\"(.*?)\"[^>]*>")

    if message.html_caption is not None:
        links_list.extend(re.findall(links_regx, message.html_caption))

    if message.html_text is not None:
        links_list.extend(re.findall(links_regx, message.html_text))

    # Convert list of links to the string value
    links_value = '\n'.join([str(elem) for elem in links_list])

    text = message.caption if (message.text is None) else message.text

    # Post in a channel
    values = ['', str(date.today()), message.author_signature, '', '', '', text, links_value]

    sheet.append_table(values=values, start='A1', dimension='ROWS')
