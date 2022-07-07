import urllib.error
from urllib import request

try:
    request.urlopen('http://pudim.com.br/')
except urllib.error.URLError:
    print('\033[1:31mSite indísponivel.')
else:
    print('\033[1:32mSite disponível. ')
