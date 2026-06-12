import json, os, requests

def clearConsole() -> None:
    os.system('clear' if os.name == 'posix' else 'cls')

class Downloader:
    def __init__(self, codename: str, **kwargs) -> None:
        clearConsole()
        self.codename, self.name = codename, kwargs['name']
        print(f'\n- downloading {codename}\n' + '-' * 50)
        try: self._main(codename, **kwargs)
        except: input('\nthere was an error. press enter to go back.\n')
        
    def _main(self, codename: str, name: str, link: str, isProdBased: bool = False, **kwargs):
        if isProdBased:
            print('getting server links')
            with requests.get(f'{link}/query') as query:
                self.jdns = json.loads(query.content)['jdns']
            print('updating song codes')
            try:
                with requests.get(f'{self.jdns.replace('jdns', 'api')}/v1/songs/published', stream=True) as songdb:
                    db = self._saveDb(json.loads(songdb.content))
            except:
                    db = self._saveDb([])
            song = [db[song] for song in db if song == codename]
            if not len(song):
                input(f'{codename} was not found. press enter to go back.\n')
                return
            self.base = song[0]
        else: self.base = f'{link}/songs/{codename}'
        self.output = f'output/{codename}/{name}'
        self._dlFile(f'{self.base}/assets/web/{codename}.ogg', f'{self.output}/assets')
        self._dlFile(f'{self.base}/assets/web/{codename}.mp3', f'{self.output}/assets')
        self._dlFile(f'{self.base}/assets/web/{codename.lower()}.jpg', f'{self.output}/assets')
        self._dlFile(f'{self.base}/assets/web/{codename.lower()}_small.jpg', f'{self.output}/assets')
        self._dlFile(f'{self.base}/assets/web/pictos-sprite.png', f'{self.output}/assets')
        self._dlFile(f'{self.base}/assets/web/pictos-sprite.css', f'{self.output}/assets')
        self._dlFile(f'{self.base}/assets/app/{codename.lower()}_cover.jpg', f'{self.output}/assets')
        try: self._dlFile(f'{self.base}/assets/app/{codename.lower()}_cover%402x.jpg', f'{self.output}/assets', True)
        except: self._dlFile(f'{self.base}/assets/app/{codename.lower()}_cover@2x.jpg', f'{self.output}/assets')
        self._dlFile(f'{self.base}/{codename}.json', f'{self.output}/data')
        for i in range(4):
            try:
                self._dlFile(f'{self.base}/assets/common/coaches/{codename.lower()}_coach_{i+1}.png', f'{self.output}/assets', True)
                self._dlFile(f'{self.base}/assets/common/coaches/{codename.lower()}_coach_{i+1}_big.png', f'{self.output}/assets', True)
                self._dlFile(f'{self.base}/data/moves/{codename}_moves{i}.json', f'{self.output}/data', True)
            except: break
            if name != 'rio':
                moves = json.loads(open(f'{self.output}/data/{codename}_moves{i}.json').read().split('(', 1)[1].rsplit(')', 1)[0])
                for move in moves:
                    url = f'{self.base}/data/classifiers{'_WIIU' if isProdBased else ''}/{move['name']}.msm'
                    self._dlFile(url, f'{self.output}/data/classifiers', log=False)
        self.cdn = os.path.dirname(self.base).rsplit('/', 1)[0]
        if isProdBased: self._prodDl()
        elif name == 'uat': self._uatDl()
        #input(f'\n{codename} was successfully downloaded! press enter to go back.\n')

    @staticmethod
    def _dlFile(url: str, output: str, handleExceptions: bool = False, log=True) -> None:
        filename = os.path.basename(url)
        if not os.path.exists(f'{output}/{filename}'):
            with requests.get(url, allow_redirects=False, stream=True) as response:
                if response.status_code >= 400:
                    # really useful way i found to make for loops stop
                    if handleExceptions: raise Exception
                    else: print(f'{filename} is not available')
                elif response.status_code in [200, 206]:
                    print(f'downloading {filename}')
                    os.makedirs(output, exist_ok=True)
                    open(f'{output}/{filename}', 'wb').write(response.content)
        elif log: print(f'{filename} was already downloaded.')
    
    def _saveDb(self, songdb: dict) -> dict:
        try: newDb = json.load(open(f'{self.name}Versions.json'))
        except: newDb = {}
        for song in songdb:
            if song['id'] in newDb and song['base'] == newDb[song['id']]: continue
            newDb[song['id']] = song['base']
        json.dump(newDb, open(f'{self.name}Versions.json', 'w'))
        return newDb

    def _prodDl(self):
        self._dlFile(f'{self.base}/songMetadata.zip', f'{self.output}')
        self._dlFile(f'{self.base}/assets/web/pictos-atlas.png', f'{self.output}/assets')
        self._dlFile(f'{self.base}/assets/web/pictos-atlas.json', f'{self.output}/assets')
        self._dlFile(f'{self.cdn}/map_bkg/{self.codename}_map_bkg.jpg', f'{self.output}/assets')
        self._dlFile(f'{self.base}/bundle.zip', f'{self.output}/bundle')
        try:
            with requests.get(f'{self.jdns}/getPreviewVideo?song={self.codename}', headers={'x-platform': 'web'}) as cookies:
                self._dlFile(json.loads(cookies.content)['url'], f'{self.output}/video')
        except:
            print(f'{self.codename}\'{'s' if self.codename[-1]!='s' else ''} videos are not available.')

    def _uatDl(self):
        self._dlFile(f'{self.cdn}/dist/bundle/{self.codename}.zip', f'{self.output}/bundle')
        for i in range(8):
            try: self._dlFile(f'{self.cdn}/dist/bundle/{self.codename}_{i+2}.zip', f'{self.output}/bundle', True)
            except: break


def main():
    clearConsole()
    print(f'\n- j___ d____ now downloader by a_______\n' + '-' * 50)
    for ind, server in enumerate(settings['servers']):
        print(f'[{ind+1}] {server["name"]} - {server['description']}')
    print('[0] exit this script\n' + '-' * 50)
    try:
        choice = int(input('choose a number associated with an option\n>>> '))
        if choice > 0 and choice <= len(settings['servers']):
            MapName = input('\ninsert the codename here:\n>>> ')
            Downloader(MapName, **settings['servers'][choice-1])
        elif choice == 0: exit()
    except: input('that choice isn\'t available')
    main()

if __name__ == '__main__':
    settings = json.load(open('settings.json'))
    main()
