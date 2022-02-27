#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
import json
import os


class Animation:
    def __init__(self):
        # 作品
        self.name = ''
        # 原作
        self.author = ''
        # 原作イラスト
        self.illustrator = ''
        # 監督
        self.director = ''
        # アニメーション制作
        self.studio = ''
        # 製作委員会
        self.committee = ''
        # 放送開始期間
        self.start = ''
        # 放送終了期間
        self.end = ''
        # 話数
        self.episode = ''
        # OVA話数
        self.ova = ''


def json_phase(dir: str) -> Animation:
    file = open(dir, 'r', encoding='utf-8')
    anime = json.loads(file.read())
    object = Animation()
    for key in anime.keys():
        object.__setattr__(key, anime[key])
    return object


def season_acquire(month: str):
    if month in ('1', '2', '3'):
        season = '01-Winter'
    if month in ('4', '5', '6'):
        season = '02-Sprint'
    if month in ('7', '8', '9'):
        season = '03-Summer'
    if month in ('10', '11', '12'):
        season = '04-Autumn'
    return season


def markdown_generator(jsonfile: str):
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
    return json.dumps(json.loads(open(jsonfile, 'r', encoding='utf-8').read()))


def gethash(jsonfile: str) -> str:
    return hashlib.sha256(json_to_str(jsonfile).encode()).hexdigest()


if __name__ == '__main__':
    process()
