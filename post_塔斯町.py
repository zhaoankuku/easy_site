import urllib.request
import urllib.parse
import json
base_data={
'pageNo':1,
'pageSize':10,
'shopName':"青岛"
}

def create_request(page):
    base_url = 'https://tastien.tastientech.com/api/principalShop/platform/getOfficialPageListV2'
    base_data = {
        'pageNo': page,
        'pageSize': 10,
        'shopName': "青岛"
    }
    data=urllib.parse.urlencode(base_data).encode('utf8')
    headers={
    "Host": "tastien.tastientech.com",
    "Connection": "keep-alive",
    "Content-Length": "46",
    "sec-ch-ua-platform": "Windows",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "sec-ch-ua": "Chromium;v=146, Not-A.Brand;v=24, Microsoft Edge;v=146",
    "Content-Type": "application/json;",
    "sec-ch-ua-mobile": "?0",
    "Origin": "https://www.tasiting.com",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://www.tasiting.com/",

    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6"
}


    request=urllib.request.Request(url=base_url,headers=headers,data=data)
    return request

def get_content(request):
    responses=urllib.request.urlopen(request)
    content=responses.read().decode('utf8')
    return content

def download(page,content):
    with open(f'tata_{str(page)}.json','w+',encoding='utf8')as f:
        f.write(content)


if __name__=='__main__':
    start=int(input('star'))
    end=int(input('end'))
    for page in range(start,end+1):
        request=create_request(page)
        content=get_content(request)
        download(page,content)

