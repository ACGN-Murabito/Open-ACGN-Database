from components.classes import *


def anime_markdown(filename: str, obj: Animation) -> None:
    """
    Create a Markdown File for specific animation

    :param filename: The filename of Animation Markdown File
    :param obj: Target Animation Object
    :return: None
    """
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
