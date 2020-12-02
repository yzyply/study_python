import re
import requests
header = {
    'authority': 'uland.taobao.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-dest': 'document',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'referer': 'https://uland.taobao.com/sem/tbsearch?refpid=mm_26632258_3504122_32538762&keyword=&clk1=78764ce5ac39b4a302916c19cb056375&upsId=78764ce5ac39b4a302916c19cb056375',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': '__wpkreporterwid_=a88709b6-0ac8-49d4-0388-6575b7344bfb; miid=1647487704679443705; t=339475975d58c410dfd9680b9d7d2380; cna=BZGYFqH3Jj4CAXUr+Kva9C8t; sgcookie=E100n5U%2Fhph34s0V5Kwal8mWvDGW3MsevV9K5BENecUGXhKXi9guVCJ6Ii14gCVj%2BSs66g6pug27IgKOW6Ad2IwwQg%3D%3D; uc3=id2=UNDSzNUGu7ZB3g%3D%3D&vt3=F8dCufwtFxhMFa3Tems%3D&nk2=oeCcS6w4QT0%3D&lg2=UtASsssmOIJ0bQ%3D%3D; lgc=%5Cu7F57%5Cu5927%5Cu5237%5Cu9505; uc4=id4=0%40UgcieflsjSmUojxzZltHqAJGsRwP&nk4=0%40o6gltBtWWkVfXz48af%2FjUfrygA%3D%3D; tracknick=%5Cu7F57%5Cu5927%5Cu5237%5Cu9505; _cc_=W5iHLLyFfA%3D%3D; enc=UmdByNvZ%2BYjoNE%2Fo9E4rsVOTibepI1qQYnVVlJlyvWQFiy0MQf6qa925yveW9cHBPj%2F7tQIWM779lSz2PG8QPg%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; lLtC1_=1; cookie2=12c1e1fe39c1d663fa93edd3d642ef3e; v=0; _tb_token_=714ebe4e96333; tk_trace=oTRxOWSBNwn9dPyorMJE%2FoPdY8zfvmw%2Fq5v3hTXy7Cdrl8BeE4rGJN8iXlj%2BYL%2Bu3%2FP6pfBjDlGGaaKlUmsUzxND5DcSuiJyXDneMcaM2YPs%2F3GkQ9gxjbuk%2Fq9DoRCKPOeE0Z84kUMjisjnI%2BEAZNPdDRr7RJ%2FM8luV%2FRWkWP9Axa9Z6osytL4%2BmI3pqNvBMllwSYBjXqNt5t5CSgKnuR1ys812t8HwNjMj5O%2B22Zgu6yAKF183q0p%2BWXE75BajF48iSscOV260JjT%2BNho9ITdf%2Fbs1; ctoken=Qb54lSNwsnZUniCKhVO1OVyN; lego2_cna=CCH2KMTED2W1D1X5H85K5XC2; mt=ci=-1_0; _m_h5_tk=d2a93672b0752557e651e37ffa10ed1d_1606719263674; _m_h5_tk_enc=1cefbfd93cd7d427728952ca481a5d95; xlly_s=1; uc1=cookie14=Uoe0azFggueySw%3D%3D; l=eBSVTQScOGeNnvyCKOfanurza77OSLAYouPzaNbMiOCPO65p57A5WZRRlK89C3GVhsLwR3lYhYuWBeYBqSvjPGKnNSVsr4Dmn; tfstk=cX2RBdi1RZbl2OmYb7CDOU48DhSGZxt--3gppGPuTPtD4qJdihygQc1PNDkNfiC..; isg=BBgYtSZr8z_7Ct_MtfmqtnMb_EaqAXyLozRVLVIJZNMG7bjX-hFMGy5PISVdezRj',
}

# param = (
#     ('refpid', 'mm_26632258_3504122_32538762'),
#     ('keyword', '\u624B\u529E'),
#     ('clk1', '78764ce5ac39b4a302916c19cb056375'),
#     ('upsId', '78764ce5ac39b4a302916c19cb056375'),
#     ('spm', 'a2e0b.20350158.search.1'),
#     ('pid', 'mm_26632258_3504122_32538762'),
#     ('union_lens', 'recoveryid:201_11.27.75.37_15422726_1606710623249;prepvid:201_11.27.75.37_15422726_1606710623249'),
# )

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://uland.taobao.com/sem/tbsearch?refpid=mm_26632258_3504122_32538762&keyword=%E6%89%8B%E5%8A%9E&clk1=78764ce5ac39b4a302916c19cb056375&upsId=78764ce5ac39b4a302916c19cb056375&spm=a2e0b.20350158.search.1&pid=mm_26632258_3504122_32538762&union_lens=recoveryid%3A201_11.27.75.37_15422726_1606710623249%3Bprepvid%3A201_11.27.75.37_15422726_1606710623249', headers=headers)

def gethtml(url):                                      #获取页面信息
    try:
        r = requests.get(url,headers = header)
        print(r.status_code)
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("网址出错")
        return ""

def passbag(lis,html):                                 #处理页面信息
    try:
        pil = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        til = re.findall(r'\"raw_title\"\:\".*?\"',html)
        for i in len(pil):
            price = eval(pil[i].split(':')[1])
            name = eval(til[i].split(':')[1])
            lis.append([price,name])
    except:
        print("出错了")

def printend(lis):                                     #输出结果
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号","商品名称","商品价格"))
    count=0
    for g in lis:
        count += 1
        print(tplt.format(count,g[0],g[1]))

def main():
    obj = "手办"
    depth = 2    #爬取深度
    starturl = 'http:/s.taobao.com/search?q=' + obj
    inforlist = []
    for i in range(depth):
        try:
            url = starturl + '&s=' + str(44*i)
            print(url)
            html = gethtml(url)
            passbag(inforlist,html)
        except:
            continue
    printend(inforlist)
main()
