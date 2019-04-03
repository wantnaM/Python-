import re
import os
import urllib.request
import threading
import time

T = True
class DownloadThread(threading.Thread):  # 继承父类threading.Thread
    def __init__(self, threadID, name, wpcollection):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.wpcollection = wpcollection

    def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        downloadwp(self.wpcollection)

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
        print(i[1] + " 已经开始下载...")
        wp_url = getwp(i[0])  # 获取壁纸的网页
        for each in wp_url:  # 保存壁纸
            if(T):
                print("下载中止")
                return
            save_img(each)
        print(i[1] + " 下载完成。")
        os.chdir(root)

def getwp(url):
    # 每张壁纸的网页集合
    wp_url = []
    # 获取壁纸页数
    html = url_open(url).decode('utf-8')
    url_1 = url.replace(".shtml", "")
    page_goal = r"<a href='" + url_1 + r"_(\d+).shtml'>"
    page = re.compile(page_goal).findall(html)
    #获取壁纸网页地址
    wp_goal = r'<a target="_blank" href="(.+\.jpg)"><img'
    wp_url.append(re.compile(wp_goal).findall(html))
    url_2 = url
    for i in page:
        url_2 = url.replace('.shtml', '_' + i + '.shtml')
        #获取当前网页的所有壁纸地址
        html = url_open(url_2).decode('utf-8')
        wp_url.append(re.compile(wp_goal).findall(html))

    wp_result = []
    for i in wp_url:
        for each in i:
            wp_result.append(each.split('?')[-1])  # 问号后面的是图片的网址

    # 返回每张壁纸的网址
    return wp_result

def save_img(url):
    filename = url.split('/')[-1]
    urllib.request.urlretrieve(url, filename)

def download(wpcollection):
    DownloadThread(0, "download", wpcollection).start()

if __name__ == '__main__':
    url = 'http://www.gamersky.com/ent/wp'
    wpcollection = get_wpcollection(url, 3)
    download(wpcollection)
    time.sleep(30)
    T = False


