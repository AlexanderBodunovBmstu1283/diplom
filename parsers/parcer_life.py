#!/usr/bin/python
# -*- coding: cp1251 -*-
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import os
name_dir="revolution"
name_category="about_life"

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

def read_poem_links():

    global author
    a_all = []
    for i in range(1, 7):
        html_doc_parent = urlopen(
            'https://rustih.ru/stihi-o-zhizni/page/'+str(i)+'/')  # =open("rev.html","r")
        # html_doc_parent=urlopen('http://stih.su/revolyuciya/')
        soup = BeautifulSoup(html_doc_parent, "html5lib")
        a2 = soup.find_all('li', class_='title')
        a_page = []

        for a in a2:
            a_page.append(a.get('href'))
        a_all.append(a_page)
        print(a_page[0])
    return a_all

def create_poem_files(a_all,author_meta):
    try:
        os.makedirs("author/"+author_meta+"/"+name_category+"/texts")
        os.makedirs("author/" + author_meta + "/" + name_category + "/meta")
    except:
        pass
    try:
        os.makedirs("author/" + author_meta + "/test/" + name_category + "/texts")
        os.makedirs("author/" + author_meta + "/result/" + name_category)
        os.makedirs("author/" + author_meta + "/test_result/" + name_category)
    except:
        pass
    i=0
    count_all = len(a_all) * len(a_all[0])
    count_page = len(a_all[0])
    count_page_old = count_page
    for a2 in a_all:
        print(str(count_page / count_all * 100) + '%')
        count_page += count_page_old
        for a in a2:
                print(a)

                html_doc_poem=urlopen(str(a))

                soup = BeautifulSoup(html_doc_poem, "html5lib")
                title = str(soup.find('span', property='name').next).split(' - ')
                author = title[0]
                title=title[0]
                text = (soup.find('div',
                                  class_='poem-text').get_text())
                text = str(text).replace('<div class="field-items">', '').replace('<div>', '').replace('<p>',
                                                                                                       '').replace(
                    '</p>', '').replace('<br/>', '').replace('</div>', '')
                #print(text)
                try:
                    with open('author/'+author_meta+'/'+name_category+'/texts/' + str(i) + '.txt', 'w',encoding='cp1251') as file:
                                file.write(text)
                        #print(str(title.next),str(author.next))
                    with open('author/'+author_meta+'/'+name_category+'/meta/' + str(i) + '.txt', 'w',encoding='cp1251') as file:
                                file.write("title:\n"+str(title)+"\nauthor:\n"+str(author))
                    i += 1
                except:
                    pass
            #except:
                #print("Russ              link!!!!!!")



#print(soup)
#for i in read_author_links():
#    create_poem_files(read_poem_links(),i)

#create_poem_files(read_poem_links(),"about_life")