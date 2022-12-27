import requests
import random

class Cat():
    embedColor = 0x3498DB
    breedList = ['abys', 'aege', 'abob', 'acur', 'asho', 'awir', 'amau', 'amis', 'bali', 'bamb', 'beng', 'birm', 'bomb', 'bslo', 'bsho', 'bure', 'buri', 'cspa', 'ctif', 'char', 'chau', 'chee', 'csho', 'crex', 'cymr', 'cypr', 'drex', 'dons', 'lihu', 'emau', 'ebur', 'esho', 'hbro', 'hima', 'jbob', 'java', 'khao', 'kora', 'kuri', 'lape', 'mcoo', 'mala', 'manx', 'munc', 'nebe', 'norw', 'ocic', 'orie', 'pers', 'pixi', 'raga', 'ragd', 'rblu', 'sava', 'sfol', 'srex', 'siam', 'sibe', 'sing', 'snow', 'soma', 'sphy', 'tonk', 'toyg', 'tang', 'tvan', 'ycho']
    subList = ['IllegallySmolCats', 'cats', 'Catloaf', 'Catswithjobs', 'WhatsWrongWithYourCat', 'blackcats', 'CatSlaps', 'SupermodelCats', 'CatsStandingUp', 'bigcatgifs', 'catbellies', 'catpictures', 'catpranks', 'catsareliquid', 'catsinsinks', 'catsinbusinessattire', 'catswhoyell', 'catswithjobs', 'cattaps', 'catsisuottafo', 'blep', 'fromkittentocat', 'holdmycatnip', 'jellybeantoes', 'kittens', 'kitting', 'kneadycats', 'mainecoons', 'murdermittens', 'nebelung', 'petthedamncat', 'pocketpussy', 'ragdolls', 'startledcats', 'stuffoncats', 'teefies', 'thecattrapisworking', 'tightpussy', 'toebeans', 'tuckedinkitties']
    keyList = []
    token = 'enter-token-here'

    def getKey(self):
        return random.choice(Cat.keyList)
    
    def image(self, *breed):
        try:
            breed = str(breed[0])
        except:
            breed = None

        if breed:
            r = requests.get(f'https://api.thecatapi.com/v1/images/search?mime_types=jpg,png&breed_ids={breed}', headers={'x-api-key': Cat.getKey(self)})
            return r.json()[0]['url']
        else:
            r = requests.get('https://api.thecatapi.com/v1/images/search?mime_types=jpg,png', headers={'x-api-key': Cat.getKey(self)})
            return r.json()[0]['url']
    
    def gif(self):
        r = requests.get('https://api.thecatapi.com/v1/images/search?mime_types=gif', headers={'x-api-key': Cat.getKey(self)})
        return r.json()[0]['url']
    
    def get_breeds(self):
        r = requests.get('https://api.thecatapi.com/v1/breeds', headers={'x-api-key': Cat.getKey(self)})
        return r.json()
    
    def get_breed_info(self, breedid):
        r = requests.get(f'https://api.thecatapi.com/v1/breeds/{breedid}', headers={'x-api-key': Cat.getKey(self)})
        return r.json()

    def upvote(self, imageid, subid):
        data = {
            'image_id': imageid,
            'sub_id': subid,
            'value': 1
        }
        r = requests.post('https://api.thecatapi.com/v1/votes', json=data, headers={'x-api-key': Cat.getKey(self)})
        return r.json()

    def downvote(self, imageid, subid):
        data = {
            'image_id': imageid,
            'sub_id': subid,
            'value': -1
        }
        r = requests.post('https://api.thecatapi.com/v1/votes', json=data, headers={'x-api-key': Cat.getKey(self)})
        return r.json()

    def get_votes(self, subid):
        r = requests.get(f'https://api.thecatapi.com/v1/votes?sub_id={subid}', headers={'x-api-key': Cat.getKey(self)})
        return r.json()

    def favourite(self, imageid, subid):
        data = {
            'image_id': imageid, 
            'sub_id': subid
        }
        r = requests.post('https://api.thecatapi.com/v1/favourites', json=data, headers={'x-api-key': Cat.getKey(self)})
        return r.json()

    def unfavourite(self, favouriteid):
        r = requests.delete(f'https://api.thecatapi.com/v1/favourites/{favouriteid}', headers={'x-api-key': Cat.getKey(self)})
        return r.json()

    def get_favourites(self, subid):
        r = requests.get(f'https://api.thecatapi.com/v1/favourites?sub_id={subid}', headers={'x-api-key': Cat.getKey(self)})
        return r.json()