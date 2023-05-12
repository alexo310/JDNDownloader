#Script by alexo
import os, requests

def mainMenu():
    os.system('cls')
    print('\n- Just Dance Now Downloader Legacy\n---------------------------\n[1] Download Everything\n[2] Download Audio Preview\n[3] Download Bundle\n[4] Download Json\n[5] Download Pictos\n[6] Download Textures\n[7] Exit this script\n---------------------------')
    choice = input('Choose one of the above: ')
    checkInt(choice,mainMenu)
    if int(choice) < 1 or int(choice) > 7: mainMenu()
    elif int(choice) == 7: exit()
    mapName = input("What's the codename?: ")
    os.makedirs(f'output/{mapName}/', exist_ok=True)
    if int(choice) == 1: dlEverything(mapName)
    elif int(choice) == 2: dlAudio(mapName)
    elif int(choice) == 3: dlBundle(mapName)
    elif int(choice) == 4: dlJson(mapName)
    elif int(choice) == 5: dlPictos(mapName)
    elif int(choice) == 6: dlTexture(mapName)
    if int(choice) < 7 and int(choice) > 1: input('\nThe file was downloaded! Press enter to continue')
    mainMenu()

def dlEverything(SongName):
    dlAudio(SongName)
    dlBundle(SongName)
    dlPictos(SongName)
    input(f'\nAll {SongName} files were downloaded! Press enter to continue')

def dlAudio(SongName):
    audioLink = f'https://jdnowweb-s.cdn.ubi.com/uat/release_tu2/20150928_1740/songs/{SongName}/assets/web/{SongName}.ogg'
    audio = requests.get(audioLink, allow_redirects=True)
    open(f'output/{SongName}/{SongName}.ogg', 'wb').write(audio.content)

def dlBundle(SongName):
    bundleLink = f'https://jdnowweb-s.cdn.ubi.com/uat/release_tu2/20150928_1740/dist/bundle/{SongName}.zip'
    bundle = requests.get(bundleLink, allow_redirects=True)
    open(f'output/{SongName}/{SongName}.zip', 'wb').write(bundle.content)

def dlJson(SongName):
    jsonLink = f'https://jdnowweb-s.cdn.ubi.com/uat/release_tu2/20150928_1740/songs/{SongName}/{SongName}.json'
    json = requests.get(jsonLink, allow_redirects=True)
    open(f'output/{SongName}/{SongName}.json', 'wb').write(json.content)
    
def dlPictos(SongName):
    pictoLink = f'https://jdnowweb-s.cdn.ubi.com/uat/release_tu2/20150928_1740/songs/{SongName}/assets/web/pictos-sprite.png'
    picto = requests.get(pictoLink, allow_redirects=True)
    open(f'output/{SongName}/pictos-sprite.png', 'wb').write(picto.content)
    cssLink = f'https://jdnowweb-s.cdn.ubi.com/uat/release_tu2/20150928_1740/songs/{SongName}/assets/web/pictos-sprite.css'
    css = requests.get(cssLink, allow_redirects=True)
    open(f'output/{SongName}/pictos-sprite.css', 'wb').write(css.content)

def dlTexture(SongName):
    squareLink = f'https://jdnowweb-s.cdn.ubi.com/uat/release_tu2/20150928_1740/songs/{SongName}/assets/web/{SongName.lower()}.jpg'
    square = requests.get(squareLink, allow_redirects=True)
    open(f'output/{SongName}/{SongName.lower()}_cover_generic.png', 'wb').write(square.content)
    coachNum = ['1', '2', '3', '4']
    for coachPng in coachNum:
        coachLink = f'https://jdnowweb-s.cdn.ubi.com/uat/release_tu2/20150928_1740/songs/{SongName}/assets/common/coaches/{SongName.lower()}_coach_{coachPng}_big.png'
        coach = requests.get(coachLink, allow_redirects=True)
        open(f'output/{SongName}/{SongName.lower()}_coach_{coachPng}.png', 'wb').write(coach.content)

def checkInt(varName,menuName):
    try: intValue = int(varName)
    except: menuName()
    else: pass

mainMenu()