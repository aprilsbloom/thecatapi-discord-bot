import requests
import json
import random
from datetime import datetime

class cat():
    def __init__(self):
        self.embedColor = 0x3498DB
        self.subList = ['IllegallySmolCats', 'cats', 'Catloaf', 'Catswithjobs', 'WhatsWrongWithYourCat', 'blackcats', 'CatSlaps', 'SupermodelCats', 'CatsStandingUp', 'bigcatgifs', 'catbellies', 'catpictures', 'catpranks', 'catsareliquid', 'catsinsinks', 'catsinbusinessattire', 'catswhoyell', 'catswithjobs', 'cattaps', 'catsisuottafo', 'blep', 'fromkittentocat', 'holdmycatnip', 'jellybeantoes', 'kittens', 'kitting', 'kneadycats', 'mainecoons', 'murdermittens', 'nebelung', 'petthedamncat', 'pocketpussy', 'ragdolls', 'startledcats', 'stuffoncats', 'teefies', 'thecattrapisworking', 'tightpussy', 'toebeans', 'tuckedinkitties']
        self.keyList = ['']

    def image(self, *breed):
        try:
            breed = str(breed[0])
        except IndexError:
            breed = None

        if breed:
            r = requests.get(f'https://api.thecatapi.com/v1/images/search?mime_types=jpg,png&breed_ids={breed}', headers={'x-api-key': random.choice(self.keyList)})
            return r.json()[0]['url']
        else:
            try:
                r = requests.get('https://api.thecatapi.com/v1/images/search?mime_types=jpg,png', headers={'x-api-key': random.choice(self.keyList)})
                return r.json()[0]['url']
            except json.decoder.JSONDecodeError:
                return 'https://cdn.discordapp.com/attachments/967001823351304232/1080754805632409670/BOJ9__HCMAE7PhB.jpg'

    def gif(self):
        randomNum = random.randint(1, 2)

        try:
            if randomNum == 1:
                r = requests.get('https://api.thecatapi.com/v1/images/search?mime_types=gif', headers={'x-api-key': random.choice(self.keyList)})
                return r.json()[0]['url']
            else:
                r = requests.get('https://edgecats.net/all')
                gifLinks = [i.split('href="')[1].split('"')[0] for i in r.text.splitlines() if 'href="' in i]
                return random.choice(gifLinks)
        except json.decoder.JSONDecodeError:
            return 'https://cdn.discordapp.com/attachments/889397754458169385/985133240098627644/ezgif-3-df748915d9.gif'

    def get_breeds(self):
        r = requests.get('https://api.thecatapi.com/v1/breeds', headers={'x-api-key': random.choice(self.keyList)})
        return r.json()

    def get_breed_info(self, breedid):
        r = requests.get(f'https://api.thecatapi.com/v1/breeds/{breedid}', headers={'x-api-key': random.choice(self.keyList)})
        return r.json()

class logger:
    def __init__(self):
        self.red = '\033[91m'
        self.yellow = '\033[93m'
        self.green = '\033[92m'
        self.reset = '\033[0m'

    def info(self, text):
        time = datetime.now().strftime('%H:%M:%S')
        print(f'[-] {time} - {text}')

    def error(self, text):
        time = datetime.now().strftime('%H:%M:%S')
        print(f'{self.red}[-]{self.reset} {time} - {text}')

    def warning(self, text):
        time = datetime.now().strftime('%H:%M:%S')
        print(f'{self.yellow}[!]{self.reset} {time} - {text}')

    def success(self, text):
        time = datetime.now().strftime('%H:%M:%S')
        print(f'{self.green}[+]{self.reset} {time} - {text}')