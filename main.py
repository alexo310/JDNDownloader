#Script by alexo
import os, requests

def mainMenu():
    os.system('cls')
    print('\n- Just Dance Now Downloader Legacy\n---------------------------\n[1] Download Everything\n[2] Download Audio Preview\n[3] Download Bundle\n[4] Download Json\n[5] Download Pictos\n[6] Download Textures\n[7] Exit this script\n---------------------------')
    try: choice = int(input('Choose one of the above: '))
    except: mainMenu()
    if choice < 1 or choice > 7: mainMenu()
    elif choice == 7: exit()
    mapName = input("What's the codename?: ")
    os.makedirs(f'output/{mapName}/', exist_ok=True)
    if choice == 1: dlEverything(mapName)
    elif choice == 2: dlAudio(mapName)
    elif choice == 3: dlBundle(mapName)
    elif choice == 4: dlJson(mapName)
    elif choice == 5: dlPictos(mapName)
    elif choice == 6: dlTexture(mapName)
    if choice < 7 and choice > 1: input('\nThe file was downloaded! Press enter to continue')
    mainMenu()

def dlEverything(SongName):
    dlAudio(SongName)
    dlBundle(SongName)
    dlPictos(SongName)
    input(f'\nAll {SongName} files were downloaded! Press enter to continue')

def dlAudio(SongName):
    with requests.get(f'https://jdnowweb-s.cdn.ubi.com/uat/release_tu2/20150928_1740/songs/{SongName}/assets/web/{SongName}.ogg', allow_redirects=True) as audio: open(f'output/{SongName}/{SongName}.ogg', 'wb').write(audio.content)

def dlBundle(SongName):
    bundleLink = f'https://jdnowweb-s.cdn.ubi.com/uat/release_tu2/20150928_1740/dist/bundle/{SongName}.zip'
    with requests.get(bundleLink, allow_redirects=True) as bundle: open(f'output/{SongName}/{SongName}.zip', 'wb').write(bundle.content)

def dlJson(SongName):
    with requests.get(f'https://jdnowweb-s.cdn.ubi.com/uat/release_tu2/20150928_1740/songs/{SongName}/{SongName}.json', allow_redirects=True) as json: open(f'output/{SongName}/{SongName}.json', 'wb').write(json.content)
    
def dlPictos(SongName):
    with requests.get(f'https://jdnowweb-s.cdn.ubi.com/uat/release_tu2/20150928_1740/songs/{SongName}/assets/web/pictos-sprite.png', allow_redirects=True) as picto: open(f'output/{SongName}/pictos-sprite.png', 'wb').write(picto.content)
    with requests.get(f'https://jdnowweb-s.cdn.ubi.com/uat/release_tu2/20150928_1740/songs/{SongName}/assets/web/pictos-sprite.css', allow_redirects=True) as css: open(f'output/{SongName}/pictos-sprite.css', 'wb').write(css.content)

def dlTexture(SongName):
    print('Not Working')

mainMenu()