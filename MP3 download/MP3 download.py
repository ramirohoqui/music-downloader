#import os

#urls = ['https://www.youtube.com/watch?v=FRgQQZwippg', 'https://www.youtube.com/watch?v=1A5mYOj9oMs', 'https://www.youtube.com/watch?v=clORj86oJYw', 'https://www.youtube.com/watch?v=3elwRq1utjY', 'https://www.youtube.com/watch?v=qd_8mm906GA', 'https://www.youtube.com/watch?v=it2taxkagOs', 'https://www.youtube.com/watch?v=5Ba9qpD3Z1c', 'https://www.youtube.com/watch?v=IDWf8D6nfR0', 'https://www.youtube.com/watch?v=Kt9aW6uxYwk', 'https://www.youtube.com/watch?v=_KhR1Fx5RNA', 'https://www.youtube.com/watch?v=ldogwnnirx8', 'https://www.youtube.com/watch?v=lNoHnRSCYGw', 'https://www.youtube.com/watch?v=VZvARSvqjtI', 'https://www.youtube.com/watch?v=Kl6cvOfAYwM', 'https://www.youtube.com/watch?v=DIon0Hb73Yk', 'https://www.youtube.com/watch?v=Y0EerGClZP4', 'https://www.youtube.com/watch?v=iOqRGErpkSE', 'https://www.youtube.com/watch?v=hfTH3ZJvy8Q', 'https://www.youtube.com/watch?v=LPoDkFABf5c', 'https://www.youtube.com/watch?v=cBaEOrOLKCQ', 'https://www.youtube.com/watch?v=rTVcPBI2JQs', 'https://www.youtube.com/watch?v=dFafDMmKAeQ', 'https://www.youtube.com/watch?v=4m_g0srhE8U', 'https://www.youtube.com/watch?v=jBjLJ0moWBI', 'https://www.youtube.com/watch?v=fV4ZzE6uy4k', 'https://www.youtube.com/watch?v=HGqEc3IOiWA', 'https://www.youtube.com/watch?v=XeQvpnLs3ss', 'https://www.youtube.com/watch?v=_l17YvlVNKU', 'https://www.youtube.com/watch?v=y7e5rwIh4g8', 'https://www.youtube.com/watch?v=Gbs8ogjBoRY', 'https://www.youtube.com/watch?v=yIX1C-Yj1yk', 'https://www.youtube.com/watch?v=s5mtrDnzvjA', 'https://www.youtube.com/watch?v=uwYw07dmZ2I', 'https://www.youtube.com/watch?v=g1HhIBUvB00', 'https://www.youtube.com/watch?v=NqLzQHp_OaA', 'https://www.youtube.com/watch?v=v5_SYkFpFiY', 'https://www.youtube.com/watch?v=jM-gBnYcbzg', 'https://www.youtube.com/watch?v=PTOpEQmxlpA', 'https://www.youtube.com/watch?v=IDWf8D6nfR0', 'https://www.youtube.com/watch?v=ECSqOEBVnzo', 'https://www.youtube.com/watch?v=60m4gd0b2rc', 'https://www.youtube.com/watch?v=crczoPVgJfw', 'https://www.youtube.com/watch?v=IWCFMMNm1GU', 'https://www.youtube.com/watch?v=DiZvE5HiSJg', 'https://www.youtube.com/watch?v=BtT50xsXvws', 'https://www.youtube.com/watch?v=ljz_nW7nTJQ', 'https://www.youtube.com/watch?v=JpWHmFQvNR8', 'https://www.youtube.com/watch?v=S9qklIkAXQE', 'https://www.youtube.com/watch?v=4DDvedYrlFw', 'https://www.youtube.com/watch?v=cCFqE2MGNKs', 'https://www.youtube.com/watch?v=igxOPZ4cU7c', 'https://www.youtube.com/watch?v=hvEH6ASSXWI', 'https://www.youtube.com/watch?v=IUxt5xRzL1w', 'https://www.youtube.com/watch?v=NHooYCybEn8', 'https://www.youtube.com/watch?v=0K_a7AYNDYU', 'https://www.youtube.com/watch?v=HvZZw7Zf0w0', 'https://www.youtube.com/watch?v=uErs3YbV6xI', 'https://www.youtube.com/watch?v=OlUtUBKs0So', 'https://www.youtube.com/watch?v=Oc_ddHcZk4Y', 'https://www.youtube.com/watch?v=i9s2Ytbm9Zk', 'https://www.youtube.com/watch?v=JjSVh9sjBKI', 'https://www.youtube.com/watch?v=CJWFP7V616Q', 'https://www.youtube.com/watch?v=yrSs3V_DMOw', 'https://www.youtube.com/watch?v=zDz881oebP4', 'https://www.youtube.com/watch?v=dRJYzsLJmBc', 'https://www.youtube.com/watch?v=FEoBjH6_ScU', 'https://www.youtube.com/watch?v=GgzJD0AoxZA', 'https://www.youtube.com/watch?v=Esn6U6w1zV4', 'https://www.youtube.com/watch?v=dF8VzMi2hLo', 'https://www.youtube.com/watch?v=GlhOvrYLsO8', 'https://www.youtube.com/watch?v=k-tTxtLTpfk', 'https://www.youtube.com/watch?v=DTGiiA2IBiA', 'https://www.youtube.com/watch?v=MzsyqCXlP-0', 'https://www.youtube.com/watch?v=bO_AGgiELx8', 'https://www.youtube.com/watch?v=2H1Qvwx6UnM', 'https://www.youtube.com/watch?v=ntZKeM9OdlQ', 'https://www.youtube.com/watch?v=IRt_BmczlNM', 'https://www.youtube.com/watch?v=yPhmeeunqII', 'https://www.youtube.com/watch?v=kUXhMaWzGKM', 'https://www.youtube.com/watch?v=EML039lPNfo', 'https://www.youtube.com/watch?v=FEoBjH6_ScU', 'https://www.youtube.com/watch?v=NfPwdBFeDCQ', 'https://www.youtube.com/watch?v=A6f96pD-PH8', 'https://www.youtube.com/watch?v=n67nHlAs4Ag', 'https://www.youtube.com/watch?v=epQ3rHx0VbE', 'https://www.youtube.com/watch?v=Rx06YR77wag', 'https://www.youtube.com/watch?v=Rjdn5D3V_GM', 'https://www.youtube.com/watch?v=q8sBEjOe1ZI', 'https://www.youtube.com/watch?v=fa9laqXv4L4', 'https://www.youtube.com/watch?v=8JOcLKuJupY', 'https://www.youtube.com/watch?v=410LS6VH6nI', 'https://www.youtube.com/watch?v=SJRgQ2qxeWQ', 'https://www.youtube.com/watch?v=VICzzFUo9FM', 'https://www.youtube.com/watch?v=O2acDT0R4LY', 'https://www.youtube.com/watch?v=jUfTJyU7oQU', 'https://www.youtube.com/watch?v=9ubm5DLiV-k', 'https://www.youtube.com/watch?v=RxGAUkXNGog', 'https://www.youtube.com/watch?v=-DbmNaSrvY4', 'https://www.youtube.com/watch?v=mU0RqEcclug'


#for url in urls:
    #os.system(f"youtube-dl --extract-audio --audio-format mp3 {url}")


# youtube-dl --extract-audio --audio-format Mp3 -batch-file lista canciones.txt


# import subprocess
#
# command = [
#     'youtube-dl',
#     '--extract-audio',
#     '--audio-format',
#     'mp3',
#     '--batch-file',
#     'lista canciones.txt'
# ]
#
# subprocess.run(command)

# import youtube_dl
#
# def download_video(url):
#     ydl_opts = {
#         'format': 'bestaudio/best',
#         'postprocessors': [{
#             'key': 'FFmpegExtractAudio',
#             'preferredcodec': 'mp3',
#             'preferredquality': '192',
#         }],
#     }
#     with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#         ydl.download([url])
#
# # For a list of URLs
# with open("lista canciones.txt", "r") as file:
#     urls = [url.strip("'") for url in file.readline().split(", ")]
#
# for url in urls:
#     try:
#         download_video(url.strip())  # strip to remove any newline characters
#     except:
#         print(f"No pudo descargar {url}")

#SECOND TRY

import yt_dlp as youtube_dl

def download_video(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# For a list of URLs
with open("lista canciones.txt", "r") as file:
    urls = [url.strip("'") for url in file.readline().split(", ")]

for url in urls:
    try:
        download_video(url.strip())  # strip to remove any newline characters
    except:
        print(f"No pudo descargar {url}")

