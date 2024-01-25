# script by alexo
import json, os, requests

# function by kubabisi
def cls() -> None:
    if os.name == 'posix': os.system('clear')
    else: os.system('cls')

# code by ibratabian17
# i do not know what this does, but it works!
def getSongdb(MapName: str) -> dict:
    with requests.get('https://sin-prod-api.justdancenow.com/v1/songs/published') as a:
            songdb = a.content.decode('utf-8')
            songdb = json.loads(songdb)
            selectedSong = next((song for song in songdb if song.get('id') == MapName), None)
    return selectedSong

# code by ibratabian17
# same as the other one.
def dlFile(url: str, output: str, isRequest: bool = False) -> None:
    headers = { 'Accept': 'text/plain, */*; q=0.01', 'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive', 'Host': 'jdnow-api-contentapistoragest.justdancenow.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': 'Windows', 'Origin': 'https://justdancenow.com',
    'Referer': 'https://justdancenow.com/' }
    response = requests.get(url, headers=headers, allow_redirects=False, stream=True)
    if response.status_code == 403: print('Access Forbidden')    
    elif response.status_code == 200 or response.status_code == 206:
        os.makedirs(output, exist_ok=True)
        chunkSize = 1024
        with open(f'{output}\\{os.path.basename(url)}', 'wb') as file:
            print(f'Downloading {os.path.basename(url)}')
            for chunk in response.iter_content(chunk_size=chunkSize):
                if chunk: file.write(chunk)
    else: print(f'{os.path.basename(url)} is not available.')

def demoDl(MapName: str) -> None:
    cls()
    print(f'\n- downloading {MapName}\n---------------------------')
    webPath = f'https://static2.cdn.ubi.com/rio/prod/20140826_1330/songs/{MapName}'
    dlFile(f'{webPath}/assets/web/{MapName}.ogg', f'output/{MapName}/demo/assets')
    dlFile(f'{webPath}/assets/web/{MapName.lower()}.jpg', f'output/{MapName}/demo/assets')
    dlFile(f'{webPath}/assets/web/{MapName.lower()}_small.jpg', f'output/{MapName}/demo/assets')
    dlFile(f'{webPath}/assets/web/pictos-sprite.png', f'output/{MapName}/demo/assets')
    dlFile(f'{webPath}/assets/web/pictos-sprite.css', f'output/{MapName}/demo/assets')
    dlFile(f'{webPath}/{MapName}.json', f'output/{MapName}/demo/data')
    dlFile(f'https://static2.cdn.ubi.com/rio/prod/20140826_1330/dist/bundle/{MapName}.zip', f'output/{MapName}/demo/bundle')
    for i in range(4):
        dlFile(f'{webPath}/assets/common/coaches/{MapName.lower()}_coach_{i + 1}_big.png', f'output/{MapName}/demo/assets')
        dlFile(f'{webPath}/assets/common/coaches/{MapName.lower()}_coach_{i + 1}.png', f'output/{MapName}/demo/assets')
        dlFile(f'{webPath}/data/moves/{MapName}_moves{i}.json', f'output/{MapName}/demo/data/moves')

def uatDl(MapName: str) -> None:
    cls()
    print(f'\n- downloading {MapName}\n---------------------------')
    webPath = f'https://jdnowweb-s.cdn.ubi.com/uat/release_tu2/20150928_1740/songs/{MapName}'
    dlFile(f'{webPath}/assets/web/{MapName}.ogg', f'output/{MapName}/uat/assets')
    dlFile(f'{webPath}/assets/web/{MapName.lower()}.jpg', f'output/{MapName}/uat/assets')
    dlFile(f'{webPath}/assets/web/{MapName.lower()}_small.jpg', f'output/{MapName}/uat/assets')
    dlFile(f'{webPath}/assets/web/pictos-sprite.png', f'output/{MapName}/uat/assets')
    dlFile(f'{webPath}/assets/web/pictos-sprite.css', f'output/{MapName}/uat/assets')
    dlFile(f'{webPath}/{MapName}.json', f'output/{MapName}/uat/data')
    dlFile(f'https://jdnowweb-s.cdn.ubi.com/uat/release_tu2/20150928_1740/dist/bundle/{MapName}.zip', f'output/{MapName}/uat/bundle')
    for i in range(8):
        dlFile(f'https://jdnowweb-s.cdn.ubi.com/uat/release_tu2/20150928_1740/dist/bundle/{MapName}_{i + 2}.zip', f'output/{MapName}/uat/bundle')
    for i in range(4):
        dlFile(f'{webPath}/assets/common/coaches/{MapName.lower()}_coach_{i + 1}_big.png', f'output/{MapName}/uat/assets')
        dlFile(f'{webPath}/assets/common/coaches/{MapName.lower()}_coach_{i + 1}.png', f'output/{MapName}/uat/assets')
        dlFile(f'{webPath}/data/moves/{MapName}_moves{i}.json', f'output/{MapName}/uat/data/moves')

def prodDl(MapName: str) -> None:
    cls()
    print(f'\n- downloading {MapName}\n---------------------------')
    songInfo = getSongdb(MapName)
    webPath = songInfo['base']
    dlFile(songInfo['bkg_image'], f'output/{MapName}/prod/assets')
    dlFile(f'{webPath}/assets/web/{MapName}.ogg', f'output/{MapName}/prod/assets')
    dlFile(f'{webPath}/assets/web/{MapName.lower()}.jpg', f'output/{MapName}/prod/assets')
    dlFile(f'{webPath}/assets/web/{MapName.lower()}_small.jpg', f'output/{MapName}/prod/assets')
    dlFile(f'{webPath}/assets/web/pictos-sprite.png', f'output/{MapName}/prod/assets')
    dlFile(f'{webPath}/assets/web/pictos-sprite.css', f'output/{MapName}/prod/assets')
    dlFile(f'{webPath}/assets/web/pictos-atlas.png', f'output/{MapName}/prod/assets')
    dlFile(f'{webPath}/assets/web/pictos-atlas.json', f'output/{MapName}/prod/assets')
    dlFile(f'{webPath}/{MapName}.json', f'output/{MapName}/prod/data')
    dlFile(f'{webPath}/bundle.zip', f'output/{MapName}/prod/bundle')
    for i in range(4):
        dlFile(f'{webPath}/assets/common/coaches/{MapName.lower()}_coach_{i + 1}_big.png', f'output/{MapName}/prod/assets')
        dlFile(f'{webPath}/assets/common/coaches/{MapName.lower()}_coach_{i + 1}.png', f'output/{MapName}/prod/assets')
        dlFile(f'{webPath}/data/moves/{MapName}_moves{i}.json', f'output/{MapName}/prod/data/moves')

def main() -> None:
    cls()
    try: choice = int(input('''
- just dance now downloader by alexo
--------------------------------------
[1] download files from the demo servers
[2] download files from the uat servers (2014-2015)
[3] download files from the prod servers (2015-present)
--------------------------------------
>>> '''))
    except ValueError: main()
    if choice < 1 or choice > 3: main()
    functions = { 1: demoDl, 2: uatDl, 3: prodDl }
    codename = input('codename (ex: Umbrella)\n>>> ')
    functions[choice](codename)
    main()

if __name__ == '__main__':
    main()