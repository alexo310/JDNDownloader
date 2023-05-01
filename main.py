#Script by alexo
import os, requests

def mainMenu():
    os.system('cls')
    print('\n- Just Dance Now Downloader Legacy')
    print('---------------------------')
    print('[1] Download Everything\n[2] Download Audio Preview\n[3] Download Bundle\n[4] Download Json\n[5] Download Pictos\n[6] Download Textures\n[7] Exit this script')
    print('---------------------------')
    choice = input('Choose one of the above: ')
    checkInt(choice,mainMenu)
    if int(choice) < 1 or int(choice) > 7: mainMenu()
    elif int(choice) == 7: exit()
    mapName = input("What's the codename?: ")
    os.makedirs('output/'+mapName+'/', exist_ok=True)
    #if int(choice) == 1: dlEverything(mapName)
    #elif int(choice) == 2: dlAudio(mapName)
    if int(choice) == 3: dlBundle(mapName)
    elif int(choice) == 4: dlJson(mapName)
    elif int(choice) == 5: dlPictos(mapName)
    #elif int(choice) == 6: dlTextures(mapName)
    if int(choice) < 7 and int(choice) > 1: input('\nThe file was downloaded! Press enter to continue')
    mainMenu()

def dlBundle(SongName):
    bundleLink = 'https://jdnowweb-s.cdn.ubi.com/uat/release_tu2/20150928_1740/dist/bundle/'+SongName+'.zip'
    bundle = requests.get(bundleLink, allow_redirects=True)
    open('output/'+SongName+'/'+SongName+'.zip', 'wb').write(bundle.content)

def dlJson(SongName):
    jsonLink = 'https://jdnowweb-s.cdn.ubi.com/uat/release_tu2/20150928_1740/songs/'+SongName+'/'+SongName+'.json'
    json = requests.get(jsonLink, allow_redirects=True)
    open('output/'+SongName+'/'+SongName+'.json', 'wb').write(json.content)
    
def dlPictos(SongName):
    pictoLink = 'https://jdnowweb-s.cdn.ubi.com/uat/release_tu2/20150928_1740/songs/'+SongName+'/assets/web/pictos-sprite.png'
    picto = requests.get(pictoLink, allow_redirects=True)
    open('output/'+SongName+'/pictos-sprite.png', 'wb').write(picto.content)
    cssLink = 'https://jdnowweb-s.cdn.ubi.com/uat/release_tu2/20150928_1740/songs/'+SongName+'/assets/web/pictos-sprite.css'
    css = requests.get(cssLink, allow_redirects=True)
    open('output/'+SongName+'/pictos-sprite.css', 'wb').write(css.content)

def checkInt(varName,menuName):
    try: intValue = int(varName)
    except: menuName()
    else: pass

mainMenu()