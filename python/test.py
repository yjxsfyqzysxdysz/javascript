import json
import requests


def getHTML(html):
    count = 1
    fi = open('bilibili.txt', 'w', encoding='utf-8')
    while(True):
        url = html+str(count)
        url = requests.get(url)
        if url.status_code == 200:
            cont = json.loads(url.text)
        else:
            break
        lengthRpy = len(cont['data']['replies'])
        if count == 1:
            try:
                lengthHot = len(cont['data']['hots'])
                for i in range(lengthHot):
                    # 热门评论内容
                    hotMsg = cont['data']['hots'][i]['content']['message']
                    fi.write(hotMsg + '\n')
                    leng = len(cont['data']['hots'][i]['replies'])
                    for j in range(leng):
                        # 热门评论回复内容
                        hotMsgRp = cont['data']['hots'][i]['replies'][j]['content']['message']
                        fi.write(hotMsgRp+'\n')
            except:
                pass
        if lengthRpy != 0:
            for i in range(lengthRpy):
                comMsg = cont['data']['replies'][i]['content']['message']
                fi.write(comMsg + '\n')
                # print('评论:',cont['data']['replies'][i]['content']['message'])
                leng = len(cont['data']['replies'][i]['replies'])
                for j in range(leng):
                    comMsgRp = cont['data']['replies'][i]['replies'][j]['content']['message']
                    fi.write(comMsgRp + '\n')
        else:
            break
        print("第%d页写入成功！" % count)
        count += 1
    fi.close()
    print(count-1, '页评论写入成功！')


url = "https://api.bilibili.com/x/v2/reply?type=1&oid="
av = input("input your url:")
html = url+av+'&pn='
getHTML(html)
