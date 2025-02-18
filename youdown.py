from pytubefix import YouTube
from pytubefix.cli import on_progress

def yt_download(link):
    try:
        yt = YouTube(link, on_progress_callback= on_progress)

        print(yt.title)

        ys = yt.streams.get_highest_resolution()

        destino = input(r"Cole o endereço da pasta para salvar o vídeo: ")
        ys.download(output_path=destino)
        print("Download Completo... ✅")
    except:
        print("Erro com o download, tente novamente ❌")

link = input("Cole aqui a URL do youtube: ")
yt_download(link=link)