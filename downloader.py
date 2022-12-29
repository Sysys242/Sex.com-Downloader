import requests, os, threading
from eazy_ui import *

print(Colors.pink + Ascii.get("SEX.COM-DL", AsciiType.ALLIGATOR2))
Console.printError("Please enter the name of the pp u want to download: ", PrintType.CLEAN)
name = input("\r")
print("\n\n")

try:
    os.mkdir(name)
except:
    pass


ses = requests.session()
ses.headers = {
    'x-sx-client-uid': '25ba89ae-b4a0-40f1-ab5a-0332b3f7e1e2',
    'x-sx-ray-id': '335ca955-cc1c-4326-a617-193a562d9934',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36',
    'x-sx-t': '1672257052496',
    'Accept': 'application/json, text/plain, */*',
    'Referer': 'https://www.sex.com/' + name,
    'x-sx-h': '8277939235251024',
    'x-sx-interested-in': 'woman',
}
ses.get("https://www.sex.com/" + name)


file = 1
def downloadFile(videoId, videoLink):
    global file
    response = ses.get(videoLink,)
    open("./"+ name + "/" + videoId + '.mp4', 'wb').write(response.content)
    Console.printSuccess("Downloaded [" + str(file) + "]", PrintType.CLEAN)
    file += 1

i=1

while True:
    try:
        params = {
            'pageNumber': i,
            'pageSize': '12',
            'sortBy': 'position',
            'username': name,
            'mediaType': 'video',
            'visibility': [
                'public'
            ],
        }
        i+=1
        response = ses.get('https://www.sex.com/api/feed/listUserItems', params=params)

        for media in response.json()['page']['items']:
            threading.Thread(target=downloadFile(media['media']['videoUid'],media['media']['sources'][0]['fullPath'])).start()
    except Exception as e:
        print("Finished Downloading :)")
        break
    