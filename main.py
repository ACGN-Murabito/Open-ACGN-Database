import json


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


def json_phase(dir: str = './_temp/fffff0.json') -> Animation:
    file = open(dir, 'r', encoding='utf-8')
    anime = json.loads(file.read())
    object = Animation()
    for key in anime.keys():
        object.__setattr__(key, anime[key])
    return object


def season_acquire(date: str):
    date = date.split('.')
    if date[1] in ('1', '2', '3'):
        season = 'winter'
    if date[1] in ('4', '5', '6'):
        season = 'sprint'
    if date[1] in ('7', '8', '9'):
        season = 'summer'
    if date[1] in ('10', '11', '12'):
        season = 'autumn'
    return season


def markdown_generator():
    obj = json_phase()
    season = season_acquire(obj.start)
    


if __name__ == '__main__':
    markdown_generator()
