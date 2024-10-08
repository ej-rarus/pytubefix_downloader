from pytubefix import YouTube


def let_the_download_begin():

    url = input("다운로드할 유튜브 영상의 주소를 입력해주세요: ")
    yt=YouTube(url)

    want_to_download = yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()

    want_to_download.download(filename=yt.author+'-'+want_to_download.title+'.mp4')

    print(yt.author+want_to_download.title+" 다운로드 완료!")


while(True):
    let_the_download_begin()



#$ pip install pytubefix

#$ pip install pyinstaller
#$ pyinstaller --onefile main.py


#https://www.youtube.com/watch?v=F1xw0IaBpOU
# url = "https://www.youtube.com/watch?v=-NqaupGcCpw"
# yt=YouTube(url)


# # stream = yt.streams.filter(progressive=True)
# # print(stream)   

# want_to_download = yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
# want_to_download.download()