import urllib.request as dw

imgUrl = "http://post.phinf.naver.net/20160621_169/1466482468068lmSHj_JPEG/If7GeIbOPZuYwI-GI3xU7ENRrlfI.jpg"
htmlUrl = "https://www.google.com/"

savePath1 = "../save/download2-2-1.jpg"
savePath2 = "../save/download2-2-1.html"

dw.urlretrieve(imgUrl, savePath1)
dw.urlretrieve(htmlUrl, savePath2)

print("다운로드 완료")
