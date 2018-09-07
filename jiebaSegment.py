import jieba_fast as jieba

#delete the stop words
stop = [line.strip().decode('utf-8') for line in open('//home//liyicong//Desktop//lyrics//stop_words_zh.txt','r').readlines()]

with open("//home//ubuntu//Desktop//lyrics//lyrics.txt","r") as lyricFile:
    segmentLyrics = open('//home//ubuntu//Desktop//lyrics//SegmentLyrics.txt', 'a+')
    for line in lyricFile:
        seg_list = jieba.cut(line, cut_all=False)  ##type:generator
        for seg in seg_list:
            if seg not in stop:
                segmentLyrics.write(seg.encode('utf-8'))
                if seg != '\n':
                    segmentLyrics.write(' ')
    segmentLyrics.close()


