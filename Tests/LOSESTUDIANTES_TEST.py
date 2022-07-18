import requests as rq

r = rq.get('https://losestudiantes.com/universidad-nacional/professors/jose-ricardo-martinez-vargas')

htmlparser = r.text

try:
    html = open('page.html', 'w')
    html.write(htmlparser)
    html.close()
except:
    html.close()


