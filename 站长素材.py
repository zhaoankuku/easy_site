import time
import urllib.request
from lxml import etree

base_url='https://sc.chinaz.com/tupian/ribenmeinv'

def built_url(page):

    if page == 1:
        url='https://sc.chinaz.com/tupian/ribenmeinv.html'

    else:
        data=f'_{page}.html'
        url=base_url+data
    return url

def create_request(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0",
        'referer':'https://sc.chinaz.com/tupian/ribenmeinv.html'}
    request=urllib.request.Request(url,headers=headers)
    return request

def get_content(request):
    responses=urllib.request.urlopen(request)
    content=responses.read().decode('utf8')
    return content

def download(content):
    # urllib.request.urlretrieve('http','')
    tree=etree.HTML(content)
    name_list=tree.xpath("//div[@class='item']//a[@class='name']/text()")
    src_list=tree.xpath("//div[@class='item']//img/@data-original")

    for i in range(len(name_list)):
        name=name_list[i]
        src=src_list[i]
        urllib.request.urlretrieve(url=src,filename='./rbmv_jpg/'+name+'.jpg')
        time.sleep(1)

if __name__=="__main__":
    start_page=input('start')
    end_page=input('end')

    for page in range(int(start_page),int(end_page)+1):
        url=built_url(page)
        request=create_request(url)
        content=get_content(request)
        download(content)













