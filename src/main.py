import json, os, requests

def clear() -> None:
    os.system('clear' if os.name == 'posix' else 'cls')

class Download:
    cdnLink: str
    codename: str
    serverName: str

    def getSongdb(self, codename: str, url: str) -> str:
        if not os.path.exists(f'{self.serverName}Codes.json'):
            with requests.get(url) as songdb:
                codes = {}
                for song in json.loads(songdb.content):
                    codes[song['id']] = song['base'].split('_')[-1]
                json.dump(codes, open(f'{self.serverName}Codes.json', 'w'))
        songdb = json.load(open(f'{self.serverName}Codes.json', encoding='utf8'))
        try: return f'{codename}_{songdb[codename]}'
        except:
            input('song not found. returning to main menu.')
            main()

    @staticmethod
    def download(url: str, output: str) -> None:
        response = requests.get(url, allow_redirects=False, stream=True)
        statusCode = response.status_code
        if statusCode == 403: print('access forbidden')
        elif statusCode in [200, 206]:
            os.makedirs(output, exist_ok=True)
            with open(f'{output}/{os.path.basename(url)}', 'wb') as file:
                print(f'Downloading {os.path.basename(url)}')
                file.write(response.content)
        else: print(f'{os.path.basename(url)} is not available.')

    def main(self, server: dict[str|bool]) -> None:
        clear()
        self.cdnLink: str = server['cdnLink']
        self.download(f'{self.cdnLink}/songs/{self.codename}/assets/web/{self.codename.split("_")[0]}.ogg', f'output/{self.codename.split("_")[0]}/assets')
        self.download(f'{self.cdnLink}/songs/{self.codename}/assets/web/{self.codename.split("_")[0]}.mp3', f'output/{self.codename.split("_")[0]}/assets')
        self.download(f'{self.cdnLink}/songs/{self.codename}/assets/web/{self.codename.split("_")[0].lower()}.jpg', f'output/{self.codename.split("_")[0]}/assets')
        self.download(f'{self.cdnLink}/songs/{self.codename}/assets/web/{self.codename.split("_")[0].lower()}_small.jpg', f'output/{self.codename.split("_")[0]}/assets')
        self.download(f'{self.cdnLink}/songs/{self.codename}/assets/web/pictos-sprite.png', f'output/{self.codename.split("_")[0]}/assets')
        self.download(f'{self.cdnLink}/songs/{self.codename}/assets/web/pictos-sprite.css', f'output/{self.codename.split("_")[0]}/assets')
        self.download(f'{self.cdnLink}/songs/{self.codename}/assets/web/pictos-atlas.png', f'output/{self.codename.split("_")[0]}/assets')
        self.download(f'{self.cdnLink}/songs/{self.codename}/assets/web/pictos-atlas.json', f'output/{self.codename.split("_")[0]}/assets')
        self.download(f'{self.cdnLink}/songs/{self.codename}/assets/app/{self.codename.split("_")[0].lower()}_cover.jpg', f'output/{self.codename.split("_")[0]}/assets')
        self.download(f'{self.cdnLink}/songs/{self.codename}/assets/app/{self.codename.split("_")[0].lower()}_cover%402x.jpg', f'output/{self.codename.split("_")[0]}/assets')
        self.download(f'{self.cdnLink}/songs/{self.codename}/assets/app/{self.codename.split("_")[0].lower()}_cover@2x.jpg', f'output/{self.codename.split("_")[0]}/assets')
        self.download(f'{self.cdnLink}/songs/{self.codename}/{self.codename.split("_")[0]}.json', f'output/{self.codename.split("_")[0]}/data')
        for i in range(4):
            self.download(f'{self.cdnLink}/songs/{self.codename}/assets/common/coaches/{self.codename.split("_")[0].lower()}_coach_{i + 1}_big.png', f'output/{self.codename.split("_")[0]}/assets')
            self.download(f'{self.cdnLink}/songs/{self.codename}/assets/common/coaches/{self.codename.split("_")[0].lower()}_coach_{i + 1}.png', f'output/{self.codename.split("_")[0]}/assets')
            self.download(f'{self.cdnLink}/songs/{self.codename}/data/moves/{self.codename.split("_")[0]}_moves{i}.json', f'output/{self.codename.split("_")[0]}/data/moves')
    
    def prod(self, server: dict[str|bool], serverName: str):
        self.serverName: str = serverName
        self.codename = self.getSongdb(input('\ncodename:\n>>> '), server['songdbLink'])
        self.main(server)
        self.download(f'{self.cdnLink}/map_bkg/{self.codename.split("_")[0]}_map_bkg.jpg', f'output/{self.codename.split("_")[0]}/assets')
        self.download(f'{self.cdnLink}/songs/{self.codename}/bundle.zip', f'output/{self.codename.split("_")[0]}/bundle')
        try:
            with requests.get(f'{server["jdnsLink"]}/getPreviewVideo?song={self.codename.split("_")[0]}', headers={'x-platform': 'web'}) as cookies:
                self.download(json.loads(cookies.content)['url'], f'output/{self.codename.split("_")[0]}/video')
        except:
            print(f'jdns server or video is not available.')

    def uat(self, server: dict[str|bool], serverName: str):
        self.codename: str = input('\ncodename:\n>>> ')
        self.main(server)
        self.download(f'{self.cdnLink}/dist/bundle/{self.codename}.zip', f'output/{self.codename}/bundle')
        for i in range(8):
            self.download(f'{self.cdnLink}/dist/bundle/{self.codename}_{i+2}.zip', f'output/{self.codename}/bundle')

with open('settings.json') as file:
    settings: dict = json.load(file)

def main() -> None:
    clear()
    print('\n- just dance now downloader by alexo\n-------------------------------------')
    serverList: dict[function] = {}
    for index, server in enumerate(settings['servers']):
        serverList[str(index+1)] = Download().prod if settings['servers'][server].get('isProdBased', False) else Download().uat
        print(f'[{index+1}] {server} - {settings["servers"][server]["description"]}')
    print('[0] exit this script\n-------------------------------------')
    choice: str = input('choose a number associated with the number\n>>> ')
    serverName = list(settings['servers'].keys())[int(choice)-1]
    if choice == '0': exit()
    elif choice in serverList: serverList[choice](settings['servers'][serverName], serverName)
    else: input('\nchoice is not available. press enter to return')
    main()

if __name__ == '__main__':
    main()