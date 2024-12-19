import gspread
import base64
import csv
import json
import pandas as pd
import requests
from bs4 import BeautifulSoup
from oauth2client.service_account import ServiceAccountCredentials

results = {'scrape': []}

with open('blog_data.json', 'w') as fp:
    json.dump(results, fp)

# with open('inputlinks.csv') as f:
#     p = f.read()

scope = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/drive.file'
]
file_name = 'credentials.json'

creds = ServiceAccountCredentials.from_json_keyfile_name(file_name, scope)
client = gspread.authorize(creds)
sheet = client.open("NEXTBUTTON SAME STRUCTURE").worksheet('Feuille 1')
# links = list()
# for col in range(1,17):
#     links.append(sheet.cell(1,col).value)

def write_json(new_data, filename='blog_data.json'):
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        file_data["scrape"].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent=4)


headers = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
    'sec-ch-ua-mobile': '?0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Accept-Language': 'en-US,en;q=0.9',
}


def traduce(text):
    url = "https://google-translate20.p.rapidapi.com/translate"

    payload = f"text={text}&tl=fr&sl=en".encode('utf-8')
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'x-rapidapi-host': "google-translate20.p.rapidapi.com",
        'x-rapidapi-key': "b97e8d69d8msh3248db25784f7b2p1aaf81jsnf78c53e40dbc"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    result = response.json()['data']['translation']
    return result


def wordpress_upload(h1, content):
    url = 'https://julesgalian.fr/wp-json/wp/v2'
    user = 'testseo'
    password = 'rggZ wuTJ N3Jg HlSs QdUT DsBR'
    creds = user + ':' + password
    token = base64.b64encode(creds.encode())
    header = {'Authorization': 'Basic ' + token.decode('utf-8')}
    post = {
        # 'date':'2021-10-02T09:00:00',
        'title': h1,
        'content': content,
        'status': 'publish',
    }
    requests.post(url + '/posts', headers=header, json=post)
    print('Article posted.')



results = []

def scrapedata(row):
# for row in df.iterrows():
    NUMBERXD = 1
    while True:
        link = sheet.cell(1,NUMBERXD).value
        NUMBERXD = NUMBERXD + 1
        res = requests.get(link, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        heading = soup.find('h1')
        content = soup.find('div', {'class': f"{'entry-content'}"})
        print(content)
        for tag in ['img', 'style', 'svg', 'iframe', 'h1']:
            try:
                content.find(f'{tag}').decompose()
            except:
                pass

        content.append(BeautifulSoup(
                    f'<br> generated content with <a href="https://infinityreborn.com">infinityreborn.com</a> from {link}',
                    'html.parser'))
        results = [[str(heading), str(content), res.url]]
        write_json(results)
        heading_text = heading.text.strip()
        content_ttt = traduce(heading_text)
        heading.string.replace_with(content_ttt)

        for child in content.findChildren(True, recursive=True):
            child_text = child.string
            if child_text:
                if len(child_text) > 1:
                    content_ttt = traduce(child_text)
                    child_text.replace_with(content_ttt)
        
        wordpress_upload(heading.text, str(content))
        print(f'Scraping and update completed for {link}')
        nextpage = soup.find('div', {'class': f"{'nav-next'}"}).find('a')
        # print(nextpage)
        if nextpage is not None:
            link = nextpage.get('href')
            print('.', end='')
        else:
            sheet.update_cell(1,10,link)
            break
       
        
data = sheet.get_all_records()
for row in data:
    scrapedata(row)