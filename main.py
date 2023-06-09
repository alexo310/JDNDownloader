import os, json
import requests

def main_menu():
    os.system('cls')
    print('\n- Just Dance Now Downloader\n---------------------------')
    print('[1] Download Everything')
    print('[2] Download Audio Preview')
    print('[3] Download Bundle')
    print('[4] Download Json')
    print('[5] Download Pictos')
    print('[6] Download Textures')
    print('[7] Exit this script\n---------------------------')

    try:
        choice = int(input('Choose one of the above: '))
    except ValueError:
        main_menu()
    
    if choice == 7:
        exit()

    if choice < 1 or choice > 7:
        main_menu()

    server = input('Enter the server path (prod/uat): ')
    if server not in ["uat", "prod"]:
        main_menu()

    map_name = input("What's the codename?: ")
    os.makedirs(f'output/{map_name}/', exist_ok=True)

    if server == "uat":
        dl_uat(choice, map_name)
    elif server == "prod":
        dl_prod(choice, map_name)

    main_menu()


def dl_uat(choice, map_name):
        download_files(choice, map_name, '', server="uat")
        input('\nThe files were downloaded! Press enter to continue')


def dl_prod(choice, map_name):
        print('Downloading Latest Songdbs')
        with requests.get('https://sin-prod-api.justdancenow.com/v1/songs/published') as a:
            songdb = a.content.decode('utf-8')
            songdb = json.loads(songdb)
            selected_song = next((song for song in songdb if song.get('id') == map_name), None)
            print(f"Download {selected_song['base']}/{selected_song['id']}")
            if selected_song:
                download_files(choice, selected_song['id'], selected_song['base'], server="prod")
                input('\nThe files were downloaded! Press enter to continue')
            else:
                print('can\'t find codename')


def download_files(choice, song_name, song_url, server):
    if choice == 1:
        download_file(song_name, song_url, server, 'audio')
        download_file(song_name, song_url, server, 'bundle')
        download_file(song_name, song_url, server, 'json')
        download_file(song_name, song_url, server, 'pictos')
        download_file(song_name, song_url, server, 'pictos.css')
        print(f'\nAll {song_name} files were downloaded!')
    elif choice == 2:
        download_file(song_name, song_url, server, 'audio')
        print(f'\nAudio preview for {song_name} was downloaded!')
    elif choice == 3:
        download_file(song_name, song_url, server, 'bundle')
        print(f'\nBundle for {song_name} was downloaded!')
    elif choice == 4:
        download_file(song_name, song_url, server, 'json')
        print(f'\nJson for {song_name} was downloaded!')
    elif choice == 5:
        download_file(song_name, song_url, server, 'pictos')
        download_file(song_name, song_url, server, 'pictos.css')
        print(f'\nPictos for {song_name} were downloaded!')
    elif choice == 6:
        download_file(song_name, song_url, server, 'textures')
        print(f'\nTextures for {song_name} were downloaded!')


def download_file(song_name, song_url, server, file_type):
    url = ""
    save_dir = ""

    if file_type == 'audio':
        ## Set Audio Url
        save_dir = "assets/web"
        if server == 'prod':
            url = f'{song_url}/assets/web/{song_name}.mp3'
        elif server == 'uat':
            url = f'https://jdnowweb-s.cdn.ubi.com/uat/release_tu2/20150928_1740/songs/{song_name}/assets/web/{song_name}.ogg'
    elif file_type == 'bundle':
        ## Set Bundle Url
        if server == 'prod':
            url = f'{song_url}/bundle.zip'
        elif server == 'uat':
            url = f'https://jdnowweb-s.cdn.ubi.com/uat/release_tu2/20150928_1740/dist/bundle/{song_name}.zip'
    elif file_type == 'json':
        ## Set Json Url
        if server == 'prod':
            url = f'{song_url}/{song_name}.json'
        elif server == 'uat':
            url = f'https://jdnowweb-s.cdn.ubi.com/uat/release_tu2/20150928_1740/songs/{song_name}/{song_name}.json'
    elif file_type == 'pictos':
        save_dir = "assets/web"
        ## Set Pictos.css Url
        if server == 'prod':
            url = f'{song_url}/assets/web/pictos-atlas.png'
        elif server == 'uat':
            url = f'https://jdnowweb-s.cdn.ubi.com/uat/release_tu2/20150928_1740/songs/{song_name}/assets/web/pictos-sprite.png'
    elif file_type == 'pictos.css':
        save_dir = "assets/web"
        ## Set Pictos.css Url
        if server == 'prod':
            url = f'{song_url}/assets/web/pictos-atlas.json'
        elif server == 'uat':
            url = f'https://jdnowweb-s.cdn.ubi.com/uat/release_tu2/20150928_1740/songs/{song_name}/assets/web/pictos-sprite.css'
    elif file_type == 'textures':
        print('Not Working')
        return

    headers = {
    'Accept': 'text/plain, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Host': 'jdnow-api-contentapistoragest.justdancenow.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': 'Windows',
    'Origin': 'https://justdancenow.com',
    'Referer': 'https://justdancenow.com/'
    #Hide Headers To Avoid JDN Dev Patched It
    }
    os.makedirs(f'output/{song_name}/{save_dir}', exist_ok=True)
    response = requests.get(url, headers=headers, allow_redirects=False, stream=True)
    if response.status_code == 200 or response.status_code == 206:
        total_size = int(response.headers.get('content-length', 0))
        if total_size == 0: total_size = 1
        progress = 0
        chunk_size = 1024
        with open(f'output/{song_name}/{save_dir}/{os.path.basename(url)}', 'wb') as file:
            for chunk in response.iter_content(chunk_size=chunk_size):
                if chunk:
                    file.write(chunk)
                    progress += len(chunk)
                    percent = (progress / total_size) * 100
                    print(f'Downloading {os.path.basename(url)}: {progress}/{total_size} bytes ({percent:.2f}%)',
                          end='\r')
    elif response.status_code == 403:
        print('access forbidden')

main_menu()
