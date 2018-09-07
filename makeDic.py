
wordList = []
worddic = {}
with open("//home//ubuntu//Desktop//lyrics//SegmentLyrics.txt","r") as SegmentLyrics:
    for line in SegmentLyrics:
        listLyric = line.split(' ')
        print listLyric
        for word in listLyric:
            wordList.append(word)

wordSet = set(wordList)
wordSet.remove('\n')
print len(wordSet)

dicFile = open("//home//liyicong//Desktop//lyrics//lyrics.dict","a+")

eleId = 0
for ele in wordSet:
    worddic[ele] = eleId

    dicFile.write(ele)
    dicFile.write(' ')
    dicFile.write(str(eleId))
    dicFile.write('\n')
    eleId += 1

print worddic
print len(worddic)



