import requests
import random
check='5'
if check=='5':
    a=''
    a=a+requests.get(url='https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=200&country=all&ssl=all&anonymity=all').text.strip()+'\n'

    file=open('proxy.txt','w')
    file.write(a)
    file.close()
    file=open('proxy.txt')
    a=file.readlines()
    a=list(set(a))
    random.shuffle(a)
    file.close()
    file=open('proxy.txt','w')
    for i in a:
      if i.strip()!='':
        file.write(i)
    file.close()

