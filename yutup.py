
from pytube import YouTube

url = input("Video URL'sini giriniz: ")
path = ""  # Videoyu indireceğiniz dizin (isteğe bağlı, boş bırakabilirsiniz)

# YouTube nesnesini oluşturun
yt = YouTube(url)

# Mevcut stream'leri listeleyin
print("Mevcut Video Formatları:")
for stream in yt.streams:
    print(f"{stream.resolution} - {stream.mime_type}")

# Kullanıcıdan istenen çözünürlüğü seçmesini isteyin
resolution = input("İndirmek istediğiniz çözünürlüğü seçin (örneğin 720p): ")

# Seçilen çözünürlükteki stream'i alın ve indirin
selected_stream = yt.streams.filter(res=resolution, file_extension="mp4").first()
if selected_stream:
    print(f"{resolution} çözünürlüğündeki video indiriliyor...")
    selected_stream.download(output_path=path)
    print("Video başarıyla indirildi.")
else:
    print(f"{resolution} çözünürlüğünde bir video bulunamadı.")
