#!/usr/bin/python
# -*- coding: cp1251 -*-
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import os
name_dir="revolution"
name_category="fet"

url1='http://www.stihi.ru/2018/02/09/8797'
url2='http://www.stihi.ru/avtor/mborovkova'

#&s=50
#'http://www.stihi.ru/avtor/gomer3'
#html_doc = urlopen(url2).read()
#2018/02/11/10904
#http://www.stihi.ru/avtor/poeziya1
#http://www.stihi.ru/avtor/agata8

#author="none"

def read_author_links():
    result=[]
    html_doc_parent = urlopen('http://www.stihi.ru/authors')
    soup = BeautifulSoup(html_doc_parent, "html5lib")
    authors=soup.find_all('a',class_='recomlink')
    for i in authors:
        result.append(str(i.get('href')).replace('/avtor/',""))
    return result

#print(read_author_links())
print(os.getcwd())

def read_poem_links(link):
    global author
    a_all = []

    html_doc_parent = urlopen(link)  # =open("rev.html","r")
    # html_doc_parent=urlopen('http://stih.su/revolyuciya/')
    soup = BeautifulSoup(html_doc_parent, "html5lib")

    a2 = soup.find_all('h2', class_='entry-title')
    a_page = []

    for a in a2:
        a_all.append(a.next.get('href'))
    return a_all

def create_poem_files(a_all,author_meta):
    try:
        os.makedirs("author/"+author_meta+"/"+name_category+"/texts")
        os.makedirs("author/" + author_meta + "/" + name_category + "/meta")
        os.makedirs("author/" + author_meta + "/shadow/texts")
    except:
        pass
    try:
        os.makedirs("author/" + author_meta + "/test/" + name_category + "/texts")
        os.makedirs("author/" + author_meta + "/result/" + name_category)
        os.makedirs("author/" + author_meta + "/result/shadow")
        os.makedirs("author/" + author_meta + "/test_result/" + name_category)
        os.makedirs("author/" + author_meta + "/test_result/shadow")
    except:
        pass
    i=0
    count_all=len(a_all)*len(a_all[0])
    count_page=len(a_all[0])
    count_page_old=count_page
    for a in a_all:
        print(str(count_page / count_all * 100) + '%')
        count_page += count_page_old
        html = urlopen(str(a))
        soup = BeautifulSoup(html, "html5lib")

        title = soup.find('h1', class_='entry-title')
        try:
            text = soup.find('div', class_='entry-content').get_text()#.encode('cp1252').decode('cp1251')
        except:
            pass
        try:
                    with open('author/'+author_meta+'/'+name_category+'/texts/' + str(i) + '.txt', 'w',encoding='cp1251') as file:
                                file.write(text)
                        #print(str(title.next),str(author.next))
                    with open('author/'+author_meta+'/'+name_category+'/meta/' + str(i) + '.txt', 'w',encoding='cp1251') as file:
                                file.write("title:\n"+str(title.next)+"\nauthor:\n"+str("Маяковский В.В."))
                    i += 1
        except:
                    pass
            #except:
                #print("Russ              link!!!!!!")



#print(soup)
#for i in read_author_links():
#    create_poem_files(read_poem_links(),i)

list_links=["http://stih.su/esenin/","http://stih.su/lermontov/","http://stih.su/fet-aa/"]

#create_poem_files(read_poem_links(list_links[0]),"esenin")
#create_poem_files(read_poem_links(list_links[1]),"lermontov")
#create_poem_files(read_poem_links(list_links[0]),"fet")

def check_poem(a_all):
    html = urlopen(str(a_all[0]))
    soup = BeautifulSoup(html, "html5lib")

    title = soup.find('h1', class_='entry-title').next
    try:
        text = soup.find('div', class_='entry-content').get_text()  # .encode('cp1252').decode('cp1251')
        text=text.split("var adsxpls=")[0]
        return [text, title]
    except:
        pass
