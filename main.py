# script by alexo
import json, os, requests

def cls():
    if os.name == 'posix': os.system('clear')
    else: os.system('cls')

def download(mapname, savedir, server, url):
    headers = {
    'Accept': 'text/plain, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Host': 'jdnow-api-contentapistoragest.justdancenow.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': 'Windows',
    'Origin': 'https://justdancenow.com',
    'Referer': 'https://justdancenow.com/'
    }
    os.makedirs(f'output/{mapname}/{savedir}', exist_ok=True)
    if server == 'prod': response = requests.get(url, headers=headers, allow_redirects=False, stream=True)
    else: response = requests.get(url, allow_redirects=False, stream=True)
    if response.status_code == 200 or response.status_code == 206:
        total_size = int(response.headers.get('content-length', 0))
        if total_size == 0: total_size = 1
        progress = 0
        chunk_size = 1024
        with open(f'output/{mapname}/{savedir}/{os.path.basename(url)}', 'wb') as file:
            for chunk in response.iter_content(chunk_size=chunk_size):
                if chunk:
                    file.write(chunk)
                    progress += len(chunk)
                    percent = (progress / total_size) * 100
                    print(f'Downloading {os.path.basename(url)}', end='\r')
    elif response.status_code == 403: print('access forbidden')
    return

def url_files(mapname, mapurl, server, file):
    if file == 'textures':
        print('Textures are not available yet.')
        return
    
    uat_url = {
        'audio': f'https://jdnowweb-s.cdn.ubi.com/uat/release_tu2/20150928_1740/songs/{mapname}/assets/web/{mapname}.ogg',
        'bundle': f'https://jdnowweb-s.cdn.ubi.com/uat/release_tu2/20150928_1740/dist/bundle/{mapname}.zip',
        'json': f'https://jdnowweb-s.cdn.ubi.com/uat/release_tu2/20150928_1740/songs/{mapname}/{mapname}.json',
        'pictos': f'https://jdnowweb-s.cdn.ubi.com/uat/release_tu2/20150928_1740/songs/{mapname}/assets/web/pictos-sprite.png',
        'pictos.css': f'https://jdnowweb-s.cdn.ubi.com/uat/release_tu2/20150928_1740/songs/{mapname}/assets/web/pictos-sprite.css'
    }
    prod_url = {
        'audio': f'{mapurl}/assets/web/{mapname}.mp3',
        'bundle': f'{mapurl}/bundle.zip',
        'json': f'{mapurl}/{mapname}.json',
        'pictos': f'{mapurl}/assets/web/pictos-atlas.png',
        'pictos.css': f'{mapurl}/assets/web/pictos-atlas.json'
    }
    if file != 'audio' and file.split('.')[0] != 'pictos': savedir = ''
    else: savedir = 'assets/web'
    if server == 'uat': url = uat_url[file]
    elif server == 'prod': url = prod_url[file]
    download(mapname, savedir, server, url)

def get_files(choice, mapname, mapurl, server):
    if choice == 1: url_files(mapname, mapurl, server, 'audio')
    elif choice == 2: url_files(mapname, mapurl, server, 'bundle')
    elif choice == 3: url_files(mapname, mapurl, server, 'json')
    elif choice == 4:
        url_files(mapname, mapurl, server, 'pictos')
        url_files(mapname, mapurl, server, 'pictos.css')
    elif choice == 5: url_files(mapname, mapurl, server, 'textures')
    elif choice == 6:
        for i in ['audio', 'bundle', 'json', 'pictos', 'pictos.css']:
            url_files(mapname, mapurl, server, i)
    input('\nThe files were downloaded! Press enter to continue')



def main_menu():
    cls()
    try: choice = int(input('''
- Just Dance Now Downloader
------------------------------
[1] Download Audio Preview
[2] Download Bundle
[3] Download Json
[4] Download Pictos
[5] Download Textures (Not Working)!
[6] Download All of the Above
------------------------------
Choose one of the above: '''))
    except: main_menu()
    if choice < 1 or choice > 6: main_menu()
    mapname = str(input('Codename: '))
    server = input('Server (Check README.md): ').lower()
    if server not in ['uat', 'prod']: main_menu()
    os.makedirs(f'output/{mapname}/', exist_ok=True)
    if server == 'uat':
        get_files(choice, mapname,'', 'uat')
    elif server == 'prod':
        with requests.get('https://sin-prod-api.justdancenow.com/v1/songs/published') as a:
            songdb = json.loads(a.content.decode('utf-8'))
            selected_song = next((song for song in songdb if song.get('id') == mapname), None)
            print(f"Download {selected_song['base']}/{selected_song['id']}")
            if selected_song: get_files(choice, selected_song['id'], selected_song['base'], 'prod')
            else: input('Can\'t find codename')
    main_menu()

main_menu()