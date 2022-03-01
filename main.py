#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
import os
from components.classes import *
import json


def json_phase(dir: str) -> Animation:
    """Transfer the json content to Animation object

    :param dir: The directory of json file
    :return: Transferred Animation object
    """
    file = open(dir, 'r', encoding='utf-8')
    anime = json.loads(file.read())
    object = Animation()
    for key in anime.keys():
        object.__setattr__(key, anime[key])
    return object


def season_acquire(month: str) -> str:
    """ Chose the season that correspond with the month

    :param month: The month when the animation starts to broadcast
    :return: Corresponding season
    """
    if month in ('1', '2', '3', '01', '02', '03'):
        season = '01-Winter'
    if month in ('4', '5', '6', '04', '05', '06'):
        season = '02-Sprint'
    if month in ('7', '8', '9', '07', '08', '09'):
        season = '03-Summer'
    if month in ('10', '11', '12'):
        season = '04-Autumn'
    return season


def markdown_generator(jsonfile: str) -> None:
    """Generate corresponding markdown file by allocated json file

    :param jsonfile: The directory of the allocated json file
    :return: None
    """
    obj = json_phase(jsonfile)
    hashcode = gethash(jsonfile)
    date = obj.start.split('.')
    season = season_acquire(date[1])
    dir = './database/' + date[0] + '/' + season + '/' + obj.name + '/'
    filename = dir + obj.name + '.md'
    hashfile = dir + hashcode + '.json'
    if not os.path.exists(dir):
        os.makedirs(dir)
    if os.path.exists(hashfile):
        print(obj.name + " is not Changed, skip...")
        return None
    print('Generate copy and markdown for ' + obj.name + '...')
    hashfile = open(hashfile, 'w', encoding='utf-8')
    hashfile.write(json_to_str(jsonfile).encode('utf8').decode('unicode_escape'))
    hashfile.close()
    mdfile = open(filename, 'w', encoding='utf-8')
    mdfile.write("# " + obj.name + '\n\n')
    mdfile.write("|------|スタッフ|\n")
    mdfile.write("|:------:|:------:|\n")
    mdfile.write("|原作|" + obj.author + '|\n')
    mdfile.write("|原作イラスト|" + obj.illustrator + '|\n')
    mdfile.write("|監督|" + obj.director + '|\n')
    mdfile.write("|アニメーション制作|" + obj.studio + '|\n')
    mdfile.write("|製作委員会|" + obj.committee + '|\n')
    mdfile.write("|放送開始期間|" + obj.start + '|\n')
    mdfile.write("|放送終了期間|" + obj.end + '|\n')
    mdfile.write("|話数|" + str(obj.episode) + '|\n')
    mdfile.write("|OVA話数|" + str(obj.ova) + '|\n')
    mdfile.close()


def process() -> None:
    files = os.listdir(path='./_temp')
    for file in files:
        if file.endswith('.json'):
            filename = './_temp/' + file
            markdown_generator(filename)


def json_to_str(jsonfile: str) -> str:
    """Transfer content of json file to string

    :param jsonfile: The directory of json file
    :return: Corresponding string
    """
    return json.dumps(json.loads(open(jsonfile, 'r', encoding='utf-8').read()))


def gethash(jsonfile: str) -> str:
    """Calculate the hash code of the content of json file

    :param jsonfile: the content of json file
    :return: Calculated hash code
    """
    return hashlib.sha256(json_to_str(jsonfile).encode()).hexdigest()


if __name__ == '__main__':
    process()
