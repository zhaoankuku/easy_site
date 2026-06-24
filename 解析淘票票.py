import urllib.request
import json
import jsonpath


url='https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1773889779408_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'
headers = {
    "Accept": "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",
    # "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "bx-v": "2.5.36",
    "Cookie": "t=cc968fc22c42954a8cff4b325caa4daa; cna=kkxBIsvXCgsCARvfas5EGjOG; xlly_s=1; cookie2=15df9a91e9090bf33baafe5a97977e49; v=0; _tb_token_=589809f81fe73; mtop_partitioned_detect=1; _m_h5_tk=db60a8e98275fa2c60791579d55ab2bc_1773899387667; _m_h5_tk_enc=49708c1e29e9f91a875749c0f5298d93; tb_city=370200; tb_cityName=\"x+C1ug==\"; isg=BNvb7Q-UNtmxB0qs49raaq73aj9FsO-ywluN7s0Yj1rxrPuOVYDNArwiRgwiikeq",
    "Priority": "u=1, i",
    "Referer": "https://dianying.taobao.com/?spm=a1z21.3046609.city.227.7559112aFNBt7O&city=370200",
    "sec-ch-ua": "'Chromium';v=146, 'Not-A.Brand';v=24, Google Chrome;v=146",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}

def get_content(url,headers):
    request=urllib.request.Request(url,headers=headers)
    response=urllib.request.urlopen(request)
    content=response.read().decode('utf-8')
    content=content.split('(')[1].split(')')[0]
    return content

def download(content):
    with open('QDao_TPP.json','w',encoding='utf-8') as f:
        f.write(content)
path='QDao_TPP.json'

def analysis(path):
    obj=json.loads(open(path,'r',encoding='utf-8').read())
    list1=jsonpath.jsonpath(obj,'$..regionName')
    print(list1)



if __name__=='__main__':
    content=get_content(url,headers)
    download(content)
    analysis(path)
