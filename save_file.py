import requests


url_ = r'http://smtm.com.ua/_prices/import-retail-horoshop.xls'
r = requests.get(url_, allow_redirects=True)

open('1.xls', 'wb').write(r.content)