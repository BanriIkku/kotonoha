import requests
import yaml

configFilePath = '../config.yml'

with open('../../../testdata/config.yml', 'r') as yml:
    config = yaml.load(yml)


print('===============================================')
print('  LOCAL:')
print('    wavefile   : ', config['settings']['wavefile'])
print(' ')
print('  SERVER:')
print('    URL        : ', config['settings']['url'])
print('===============================================')

files = {
    'myFile': open(config['settings']['wavefile'], 'rb')
}

session = requests.Session()
req = session.post(config['settings']['url'], files=files)
print(req.text)

