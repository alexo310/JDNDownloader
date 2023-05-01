#Script by alexo
import os, requests

def mainMenu():
    os.system('cls')
    print('\n- Just Dance Now Downloader Legacy')
    print('---------------------------')
    print('[1] Download Everything\n[2] Download Audio Preview\n[3] Download Bundle\n[4] Download Json\n[5] Download Pictos\n[6] Download Textures\n[7] Exit this script')
    print('---------------------------')
    choice = input('Choose one of the above: ')
    mapName = input("What's the codename?")
    os.makedirs('output/'+mapName+'/', exist_ok=True)
    checkInt(choice,mainMenu)
    if int(choice) < 1 or int(choice) > 6: mainMenu()
    #elif int(choice) == 1: dlEverything(mapName)
    #elif int(choice) == 2: dlAudio(mapName)
    #elif int(choice) == 3: dlBundle(mapName)
    elif int(choice) == 4: dlJson(mapName)
    #elif int(choice) == 5: dlPictos(mapName)
    #elif int(choice) == 6: dlTextures(mapName)
    elif int(choice) == 7: exit()

def dlJson(SongName):
    jsonLink = 'https://jdnowweb-s.cdn.ubi.com/uat/release_tu2/20150928_1740/songs/'+SongName+'/'+SongName+'.json'
    json = requests.get(jsonLink, allow_redirects=True)
    open('output/'+SongName+'/'+SongName+'.json', 'wb').write(json.content)
    input('\n'+SongName+'.json was downloaded! Press enter to continue')
    mainMenu()


def checkInt(varName,menuName):
    try: intValue = int(varName)
    except: menuName()
    else: pass

mainMenu()