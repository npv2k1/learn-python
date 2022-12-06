import requests
file_url = "https://cdimage.kali.org/kali-2020.1/kali-linux-2020.1a-installer-amd64.iso"
r = requests.get(file_url, stream = True)
with open("/content/gdrive/My Drive/kali-linux-2020.1a-installer-amd64.iso","wb") as file:
  for block in r.iter_content(chunk_size = 1024):
    if block:
      file.write(block)