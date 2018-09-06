from json import loads
from urllib.request import urlopen
html = urlopen("http://www.google.com/")
print(html)
import datetime
data = loads(urlopen("http://httpbin.org/ip").read())
print("The public IP is : %s" % data["origin"])
now = datetime.datetime.now()
teks = str(data) + str(now) + "\n"
with open("test.txt", "a") as myfile:
    myfile.write(teks)