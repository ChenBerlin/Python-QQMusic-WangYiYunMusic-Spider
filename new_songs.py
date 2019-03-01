import requests
import bs4
import json
import time
import datetime

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36",
    "Referer": "https://music.163.com/"
    }
#start_num = 3779628
#获取日期
def get_date():
    return time.strftime("%Y-%m-%d", time.localtime()) 

#获取网易云音乐新歌榜
def wangyiyunmusic():
    #origin_date = datetime.datetime(2019, 2, 26)
    #test_date = datetime.datetime.now()
    #end_num = start_num +(test_date-origin_date).days
    response = requests.get("https://music.163.com/discover/toplist?id="+"3779629",headers = headers)
    result = response.text
    soup = bs4.BeautifulSoup(result,"html.parser")
    wangyiyunmusic_list = soup.select("#song-list-pre-data")
    wangyiyunmusic_json = json.loads(wangyiyunmusic_list[0].text)
    num = 0
    f.write("网易云音乐新歌榜\n")
    for n in wangyiyunmusic_json:
        num += 1
        f.write("\n")
        f.write("排名：" + str(num) + "\n")
        f.write("歌名："+wangyiyunmusic_json[num-1]['name'] + "\n")
        f.write("歌手：")
        sum = len(wangyiyunmusic_json[num-1]['artists'])
        temp = 0
        while (temp != (sum-1)):
            f.write(wangyiyunmusic_json[num-1]['artists'][temp]['name']+'/')
            temp +=1
        f.write(wangyiyunmusic_json[num-1]['artists'][temp]['name'])
        f.write("\n")

#获取QQ音乐巅峰榜·新歌榜
def qqmusic():
    response = requests.get("https://c.y.qq.com/v8/fcg-bin/fcg_v8_toplist_cp.fcg?tpl=3&page=detail&date="+date+"&topid=27&type=top&song_begin=0&song_num=100&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0",headers = headers)
    qqmusic_json = json.loads(response.text)
    qqmusic_songlist_dic = qqmusic_json['songlist']
    num = 0
    f.write("QQ音乐巅峰榜·新歌榜\n")
    for each in qqmusic_songlist_dic:
        num += 1
        f.write("\n")
        f.write("排名：" + str(num) + "\n")
        f.write("歌名："+ each['data']['songname'] + "\n")
        f.write("歌手：")
        sum = len(each['data']['singer'])
        temp = 0
        while (temp != (sum-1)):
            f.write(each['data']['singer'][temp]['name']+'/')
            temp +=1
        f.write(each['data']['singer'][temp]['name'])
        f.write("\n")

if __name__ == "__main__":
    date = get_date()
    with open(date+'新歌榜.txt','w',encoding="utf-8")as f:
        f.write(date+"\n")
        f.write("------------------------------------------------------------------"+"\n")
        qqmusic()
        f.write("------------------------------------------------------------------"+"\n")
        wangyiyunmusic()
        f.close()
    a = input("今日新歌榜排行爬取完成！")
