import requests
import json
import re
from bs4 import BeautifulSoup


### get lyric from one song
def getLyricFromASong(songId):
    lrc_url = 'http://music.163.com/api/song/lyric?' + 'id=' + str(songId) + '&lv=1&kv=1&tv=-1'
    lyricHTML = requests.get(lrc_url)
    json_obj = lyricHTML.text
    lyricjson = json.loads(json_obj)
    try:
        lrcPlusTime = lyricjson['lrc']['lyric']
    except KeyError:
        return

    # delete the time in the lyric
    timePattern = re.compile(r'\[.*\]')
    lrc = re.sub(timePattern, "", lrcPlusTime)
    # delete the redundant space
    lrc = lrc.strip()
    # delete ":"
    prePattern = re.compile(r'.*:.*')
    lrc = re.sub(prePattern,"",lrc)
    # only save Chinese
    ChinesePattern = re.compile(ur"[^\u4e00-\u9fa5]")
    lrc = ChinesePattern.sub('',lrc)
    # save to txt file
    lyricFile = open('//home//ubuntu//Desktop//lyrics//lyrics.txt','a+')
    lyricFile.write(lrc.encode('utf-8'))
    lyricFile.write('\n')
    lyricFile.close()


musicIdList = []
# delete the same music id
musicIdListNonDup = []

### get music from a playList
def getMusicFromPlaylist(playlistId):
    headers = {
        'Referer': 'http://music.163.com',
        'Host': 'music.163.com',
        'User-Agent': 'Mozilla/5.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    }
    playList_url = "http://music.163.com/playlist?id="+ str(playlistId)

    s = requests.session()
    s = BeautifulSoup(s.get(playList_url,headers=headers).content, 'lxml')
    htmlList = s.find('ul', {'class':'f-hide'})

    for musichtml in htmlList.find_all('a'):
        musicIdList.append(musichtml.attrs['href'][9:])




if __name__ == '__main__':
    ######need to update to get the playlists automatically
    print "get music from playlists..."
    getMusicFromPlaylist(2243090268)
    getMusicFromPlaylist(2236351380)
    getMusicFromPlaylist(2337333174)

    # print "delete the duplicated songs..."
    # delete the duplicated songs
    musicIdListNonDup = list(set(musicIdList))
    print "There are " + str(len(musicIdListNonDup)) + " songs."

    print "get lyrics and save in txt file..."
    # for each music in the musicList, get the lyrics
    musicNum = 0
    for musicEle in musicIdListNonDup:
        getLyricFromASong(str(musicEle))
        musicNum += 1
        if musicNum % 300 == 0:
            print "get and saved %d lyrics..." % musicNum

    print "All saved."


