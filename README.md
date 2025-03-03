# JDNDownloader by alexo
**JDNDownloader** downloads files from every (and any) Just Dance Now server.
## Instructions
To make this script work, install Python. After installing, open the folder on terminal and paste this:
```bash
  python -m pip install -r requirements.txt
```
## Servers
| Server | Codename |
| ------------- | ------------- |
| Demo Servers (2014-2015) | demo  |
| ~~Old Servers (2015-2017)~~ | ~~uat~~ |
| New Servers (2018-Present) | prod |

## How to add a new server
Add a new item to the servers list in settings.json
| Key | Type | Meaning |
| ------------- | ------------- | ------------- |
| cdnLink* | str | Link to the server |
| description* | str | Self-explanatory |
| isProdBased | bool | Tells the script if it needs an id |
| jdnsLink | str | Link to the server that will give us the cookies if it's prod based |
| songdbLink | str | Link to the server that will give us the songdb if it's prod based |
TODO: Make the script be able to get the songdb link through the query
**Note:** You'll need to know how json files work to understand this.

## UAT Sever
In early 2025, Ubisoft started wiping the 2015-2017 servers and, unfortunately, most songs were not properly archived. In the bundles folder, there'll be zipped bundles of the songs that could be saved.

## Credits
- Kubabisi - Implement linux & mac terminal command into the script
- ibratabian17 - Implement songdb functionality into the script