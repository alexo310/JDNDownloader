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
| Old Servers (2015-2017) | uat |
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

**Note:** You'll need to know how json files work to understand this.

### Credits
- Kubabisi - Implement linux & mac cmd into the script
- ibratabian17 - Implement new server into the script