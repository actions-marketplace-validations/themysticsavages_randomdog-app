import base64
import requests
import datetime
import json
import os

os.chdir(os.getcwd())
print(os.listdir())

base = json.loads(open('config.json', 'r').read())
url = 'https://raw.github.com/{}/{}/{}'.format(base['slugpath'], base['branch'], base['file'])
dog = json.loads(requests.get('https://dog.ceo/api/breeds/image/random').text)['message']

with open(base['file'], 'w', encoding='utf-8') as fh:
    fh.write(requests.get(url).text.replace('/dog/', '[🐕 Random dog!]({})'.format(dog)))
fh.close()
sha = json.loads(requests.get('https://api.github.com/repos/{}/contents/README.md'.format(base['slugpath'])).text)['sha']
r = requests.put('https://api.github.com/repos/{}/contents/{}'.format(base['slugpath'], base['file']),
  headers = {'Authorization': 'Token {}'.format(base['token'])},
  json = {
    'message': 'push {}, {}'.format(base['file'], datetime.date.today().strftime("%d/%m/%Y")),
    'content': base64.b64encode(open(base['file'], 'r', encoding='utf-8').read().encode()).decode(),
    'branch': base['branch'],
    'sha': sha
   })
print('executed sucessfully :)')
