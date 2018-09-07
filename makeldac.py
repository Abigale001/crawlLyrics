from collections import Counter

# read dic from txt
lyricDict = {}
dicFile = open("//home//ubuntu//Desktop//lyrics//lyrics.dict","r")
for eachterm in dicFile:
    (key,value) = eachterm.split(' ')
    lyricDict[key] = int(value)
print lyricDict

segmentLyrics = open('//home//ubuntu//Desktop//lyrics//SegmentLyrics.txt', 'r')
ldaclyrics = open('//home//ubuntu//Desktop//lyrics//lyrics.ldac', 'a+')
for line in segmentLyrics:
    wordListInline = line.split(' ')[:-1]  #delete char \n
    wordSetInline = set(wordListInline)
    uniqueWordNum = len(wordSetInline)
    if uniqueWordNum == 0:
        continue
    result = dict(Counter(wordListInline))

    ldaclyrics.write(str(uniqueWordNum))
    ldaclyrics.write(' ')
    for term in result:
        # print type(term)  --> string
        ldaclyrics.write(str(lyricDict[term]))
        ldaclyrics.write(':')
        ldaclyrics.write(str(result[term]))
        ldaclyrics.write(' ')

    ldaclyrics.write('\n')
segmentLyrics.close()
ldaclyrics.close()
