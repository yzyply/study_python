import requests
import re
from bs4 import BeautifulSoup
import bs4
def gethtml(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
def getunverlist(demo,ulist):
    soup = BeautifulSoup(demo,"html.parser")
    for tr in soup.find("tbody").children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr("td")
            ulist.append([tds[0].get_text("", strip=True), tds[1].get_text("", strip=True), tds[2].get_text("", strip=True), tds[3].get_text("", strip=True), tds[4].get_text("", strip=True), tds[5].get_text("", strip=True)])
def printunverlist(ulist,num):
    print("{:<5}\t{:5}\t{:5}\t{:5}\t{:>5}".format("大学排名","大学名称","所在地","类型","总分",))
    for i in range(num):
        u = ulist[i]
        print("{:<5}\t{:5}\t{:5}\t{:5}\t{:>5}".format(u[0],u[1],u[2],u[3],u[4]))
def main():
    ulist = []
    url = "https://www.shanghairanking.cn/rankings/bcur/2020"
    demo = gethtml(url)
    getunverlist(demo,ulist)
    printunverlist(ulist,20)
main()