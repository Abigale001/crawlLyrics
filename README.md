# crawlLyrics

This is a project to crawl lyrics from the website and make it to lda-c format.

>>What's lda-c format?
>>
>>Each lyric of a song makes a line: uniqueWordNumber term1:count1 term2:count2 term3:count3 ....
>>
>>The uniqueWordNumber is vacabulary of a lyric. Term means a word and the count means the number of the term in the lyric.

Steps from lyrics to lda-c format dataset:
1. crawl lyrics from netease-music --> pa.py
2. segment the lyrics and delete the stop words --> jiebaSegment.py
3. make dictionary for the Chinese words --> makeDic.py
4. turn the words to id AT. dict --> makeldac.py


**1 pa.py**

This is a simple python crawler to get lyrics from netease-music. 
ONLY for CHINESE songs.

It's my first time to code a crawler. So if you have any questions, please contact me to learn together.


Steps:
1. get names of songs from playlists (playlists_id is from user)
2. delete the duplicated songs
3. get all lyrics and save in txt file

How to use:
1. change the file path to save in LINE 30
2. change the playlist ids in LINE 63,64 and 65
3. run it

What the txt file looks like:

 one line one song

**2 jiebaSegment.py**

This is a simple python script to segment lyrics and delete the stop word （stop word file URL: https://pan.baidu.com/s/1QDcbkV6z6WNHq1_l53lvMw）.

**3 makeDict.py**

This is a simple python scirpt to make dictionary AT. words in the jiebaSegment file.

**4 makeldac.py**

This is a simple python script to make ldac format dataset.


If you have any questions, welcome to contact me.
