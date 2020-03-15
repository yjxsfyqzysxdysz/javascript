#-*- coding:UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import requests
import json
import time
import xlwt

def fetchURL(url):
    '''
    功能：访问 url 的网页，获取网页内容并返回
    参数：
        url ：目标网页的 url
    返回：目标网页的 html 内容
    '''
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }
    
    try:
        r = requests.get(url,headers=headers)
        r.raise_for_status()
        # print(r.url)
        return r.text
    except requests.HTTPError as e:
        print(e)
        print("HTTPError")
    except requests.RequestException as e:
        print(e)
    except:
        print("Unknown Error !")

def parserHtml(html):
    '''
    功能：根据参数 html 给定的内存型 HTML 文件，尝试解析其结构，获取所需内容
    参数：
            html：类似文件的内存 HTML 文本对象
    '''
    try:
        s = json.loads(html)
    except:
        print('error')
        
    commentlist = []
    page = s['data']['page']['num']
    num = (page - 1) * s['data']['page']['size'] + 1
    if (page == 1):
      hlist = []

      hlist.append("序号")
      hlist.append("名字")
      hlist.append("性别")
      hlist.append("时间")
      hlist.append("评论")
      hlist.append("点赞数")
      hlist.append("回复数")

      commentlist.append(hlist)
    # 楼层，用户名，性别，时间，评价，点赞数，回复数
    for i in range(20):
        comment = s['data']['replies'][i]
        blist = []
        floor = num + i
        username = comment['member']['uname']
        sex = comment['member']['sex']
        ctime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(comment['ctime']))
        content = comment['content']['message']
        likes = comment['like']
        rcounts = comment['rcount']

        blist.append(floor)
        blist.append(username)
        blist.append(sex)
        blist.append(ctime)
        blist.append(content)
        blist.append(likes)
        blist.append(rcounts)

        commentlist.append(blist)

    writePage(commentlist)
    # print('---' * 20)
    print(page)
    exportExcel(page)

def writePage(urating):
    '''
        Function : To write the content of html into a local file
        html : The response content
        filename : the local filename to be used stored the response
    '''
    import pandas as pd
    dataframe = pd.DataFrame(urating)
    dataframe.to_csv('Bilibili_comment5-1000.csv', mode='a', index=False, sep=',', header=False)

def exportExcel(page):
    import pandas as pd
    if page == totalPage:
      pd.read_csv("./Bilibili_comment5-1000.csv", sep=",").to_excel('Bilibili.xlsx', index=False)
      print('--end--')

if __name__ == '__main__':
  # totalPage 总页数
  totalPage = 100
  for page in range(0, totalPage):
    url = 'https://api.bilibili.com/x/v2/reply?type=1&oid=11357166&pn=' + str(page + 1)
    html = fetchURL(url)
    parserHtml(html)

    # 为了降低被封ip的风险，每爬20页便歇5秒。
    if page%20 == 0:
      time.sleep(5)