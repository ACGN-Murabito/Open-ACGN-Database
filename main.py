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


def markdown_generator(obj: Animation):
    date = obj.start.split('.')
    season = season_acquire(date[1])
    dir = './database/' + date[0] + '/' + season + '/'
    filename = dir + obj.name + '.md'
    print(filename)
    if not os.path.exists(dir):
        os.makedirs(dir)
    file = open(filename, 'w', encoding='utf-8')
    file.write("# " + obj.name + '\n\n')
    file.write("|------|スタッフ|\n")
    file.write("|:------:|:------:|\n")
    file.write("|原作|" + obj.author + '|\n')
    file.write("|原作イラスト|" + obj.illustrator + '|\n')
    file.write("|監督|" + obj.director + '|\n')
    file.write("|アニメーション制作|" + obj.studio + '|\n')
    file.write("|製作委員会|" + obj.committee + '|\n')
    file.write("|放送開始期間|" + obj.start + '|\n')
    file.write("|放送終了期間|" + obj.end + '|\n')
    file.write("|話数|" + str(obj.episode) + '|\n')
    file.write("|OVA話数|" + str(obj.ova) + '|\n')
    file.close()


def process():
    files = os.listdir(path='./_temp')
    for file in files:
        if file.endswith('.json'):
            filename = './_temp/' + file
            markdown_generator(json_phase(filename))


if __name__ == '__main__':
    process()
