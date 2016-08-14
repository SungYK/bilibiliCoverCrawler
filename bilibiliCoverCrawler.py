#bilibili.py
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import re

#得到视频所在链接
def inputAVnum(url):
    avmun_pattern = re.compile(r'(av)?\d+')
    while True:
        avnum = input();
        avnum = avmun_pattern.search(avnum)
        if avnum:
            avnum = avnum.group()
            if avnum[0] != 'a':
                avnum = 'av' + avnum
            break
        else:
            print('请输入正确AV号或视频链接，如:av5685228或5685228')
    url = url + avnum
    return url

#得到封面缩略图链接
def findImg(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    try:
        imgs = soup.select('div.so-wrap > ul > li > a > div > img')
        img = imgs[0].get('src')
    except:
        print('该视频不存在')
    return img

#处理缩略图链接，得到原图链接
def getOriginImg(img):
    imgurl_pattern_new = re.compile(r'(.+)(.jpg_\d{3}x\d{3})(.jpg)')
    imgurl_pattern_old = re.compile(r'(.+)(/\d{3}_\d{3})(.+)')
    if re.match(imgurl_pattern_new, img):
        imgurl = re.match(imgurl_pattern_new, img)   
    elif re.match(imgurl_pattern_old, img):
        imgurl = re.match(imgurl_pattern_old, img) 
    else:
        print('error')
    return (imgurl.group(1)+imgurl.group(3))

if __name__ == '__main__':
    searchURL = 'http://search.bilibili.com/all?keyword='
    viodeURL = inputAVnum(searchURL)
    
    img = findImg(viodeURL)
    imgurl = getOriginImg(img)
    print(imgurl)
    
#两种封面链接形式,2016年2月后的视频为 new ,之前为 old
''' 
new = http://i0.hdslb.com/bfs/archive/eaa41481620de4f4126cb502cd9ef16a51fa6ecf.jpg_320x200.jpg
old = http://i0.hdslb.com/320_200/video/cb/cb20a0994d0d3a6cf721e6871cd04eb2.jpg
'''
