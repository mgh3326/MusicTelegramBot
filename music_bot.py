import json
from time import sleep
import telepot
from alsong_parse import alsong
from m_net_parse.m_net import Mnet


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    global ohoh_val
    if content_type == 'text':
        if msg['text'] == '/start':  # 시작
            bot.sendMessage(
                chat_id, text='음악에 대해 자유롭게 검색을 해주세요')
        elif msg['text']:
            var = Mnet(msg['text'])

            if var.mComment == "":
                alsong_lyric = alsong.parse(var.mTitle, var.mArtist)
                bot.sendPhoto(chat_id, var.mImagePath)

                bot.sendMessage(
                    chat_id,
                    text="제목 : " + var.mTitle + "\n가수 : " + var.mArtist + "\n앨범 : " + var.mAlbum + "\n가사\n" + alsong_lyric)
            else:
                if var.mTitle == "":
                    bot.sendMessage(
                        chat_id,
                        text="검색 결과가 없습니다.")
                else:
                    bot.sendMessage(
                        chat_id,
                        text="제목 : " + var.mTitle + "\n가수 : " + var.mArtist + "\n앨범 : " + var.mAlbum + "\n가사\n" + var.mLyric)

    else:
        bot.sendMessage(
            chat_id, text='음악에 대해 자유롭게 검색을 해주세요')

    # else:
    #     bot.sendMessage(chat_id, text='Test 중입니다.')
    # bot.sendMessage(chat_id, "당신이 보낸 메시지 : "+msg['text'])


class Student:
    def __init__(self):
        self.id = ""
        self.password = ""
        self.value = 0
        self.key = 0


if __name__ == "__main__":
    with open("./config/secret.json") as f:
        data = json.load(f)
    bot = telepot.Bot(data["telepot_key"])
    bot.message_loop(handle)
    print('Listening ...')

    while 1:
        # sleep(randint(10, 20))
        sleep(10)
