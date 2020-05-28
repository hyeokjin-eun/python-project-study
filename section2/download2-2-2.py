import urllib.request as dw

imgUrl = "http://post.phinf.naver.net/20160621_169/1466482468068lmSHj_JPEG/If7GeIbOPZuYwI-GI3xU7ENRrlfI.jpg"
htmlUrl = "https://www.google.com/"

savePath1 = "../save/download2-2-2.jpg"
savePath2 = "../save/downlaod2-2-2.html"

file1 = dw.urlopen(imgUrl).read()
file2 = dw.urlopen(htmlUrl).read()

saveFile1 = open(savePath1, 'wb')
saveFile1.write(file1)
saveFile1.close()

with open(savePath2, 'wb') as saveFile2:
    saveFile2.write(file2)

print("다운로드 완료")
