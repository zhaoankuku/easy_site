import urllib.request
import urllib.parse

def create_req(page):
    base_url='https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action='
    b_data={
        'start':(page-1)*20,
        'limit':20
    }
    data=urllib.parse.urlencode(b_data)
    url=base_url+data

    headers={
    'user-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0',
    }
    request = urllib.request.Request(url=url, headers=headers)
    return request

def get_content(request):
    response=urllib.request.urlopen(request)
    content=response.read().decode('utf8')
    return content

def download(page,content):
    with open('douban_'+str(page)+'.json','w+',encoding='utf8')as f:
        f.write(content)

if __name__=='__main__':
    start_page=int(input('起始页码'))
    end_page=int(input('结束页码'))
    for page in range(start_page,end_page+1):
        request=create_req(page)
        content=get_content(request)
        download(page,content)




