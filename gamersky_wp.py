import re
import os
import urllib.request


def url_open(url):  # 打开网页
    req = urllib.request.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.3228.1 Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read()

    return html


# 获取该网页所有壁纸集合的网页和名称
def get_wpcollection(url, count=0):
    html = url_open(url).decode('utf-8')
    count = count if (0 < count <= 14) else 0

    goal = r'<a href="(.+)" target="_blank" title="(每周壁纸精选.+)">'
    a = re.compile(goal).findall(html)
    wpcollection = []
    for i in a:
        if i[0][:4] != 'http':
            temp = ['https://www.gamersky.com' + i[0], i[1]]
            if temp not in wpcollection:
                wpcollection.append(temp)
        else:
            wpcollection.append([i[0], i[1]])
    # 返回一个周壁纸列表wpcollection【0】为网页，wpcollection【1】为名称
    if(count != 0):
        wpcollection = wpcollection[0:count]
    return wpcollection


def downloadwp(wpcollection):
    # 创建根目录
    root = os.getcwd()
    root += r'\游民星空壁纸'
    try:
        os.mkdir(root)
    except:
        pass
    finally:
        os.chdir(root)

    for i in wpcollection:
        # 创建每周壁纸文件夹
        try:
            os.mkdir(i[1])
        except:
            pass
        os.chdir(i[1])
        wp_url = getwp(i[0])  # 获取壁纸的网页(36)
        for each in wp_url:  # 保存壁纸
            save_img(each)

        os.chdir(root)


def getwp(url):
    # 获取每张壁纸的网页
    wp_url = []
    wp_url_2 = []
    url_2 = url
    for i in range(1, 7):  # 每周壁纸一般有6页,一页6张
        if i != 1:
            url_2 = url.replace('.shtml', '_' + str(i) + '.shtml')
        html = url_open(url_2).decode('utf-8')
        goal = r'<a target="_blank" href="(.+\.jpg)"><img'
        wp_url.append(re.compile(goal).findall(html))

    for i in wp_url:
        for each in i:
            wp_url_2.append(each.split('?')[-1])  # 问号后面的是图片的网址

    # 返回每张壁纸的网址
    return wp_url_2


def save_img(url):
    filename = url.split('/')[-1]
    with open(filename, 'wb') as f:
        img = url_open(url)
        f.write(img)


if __name__ == '__main__':
    url = 'http://www.gamersky.com/ent/wp'
    wpcollection = get_wpcollection(url,3)
    print(wpcollection)
    print(len(wpcollection))
##    downloadwp(wpcollection)
