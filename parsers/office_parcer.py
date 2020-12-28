#!/usr/bin/python
# -*- coding: cp1251 -*-
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import os
name_dir="revolution"
name_category="office"

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
    a_all=[]
    number=1
    i=1
    while number>0 and i<=4:
        if i!=0:
            html_doc_parent=urlopen('http://jollyjob.ru/category/stixi-o-rabote/page/'+str(i)+'/index.html')
        else:
            html_doc_parent=urlopen('http://jollyjob.ru/category/stixi-o-rabote/index.html/')
        #html_doc_parent=open('ilia.html')
        soup = BeautifulSoup(html_doc_parent,"html5lib")

        a2 = soup.find_all('h2', class_='title')
        a_page=[]
        for a in a2:
            a_page.append(a.next.get('href'))
        a_all.append(a_page)
        i+=1
        #print(i)
        #print(a_all)
    i=0
    #print(author.next)
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
    for a2 in a_all:
        for a in a2:
            try:
                html_doc_poem=urlopen(str(a))
                #print(str(a.get('href')))
                #print(html_doc_child)
                soup_poem = BeautifulSoup(html_doc_poem, "html5lib")
                title = soup_poem.find('h2', class_='title').next
                text = soup_poem.find('div', class_='entry').find_all('p')[1].get_text()
                try:
                    with open('author/'+author_meta+'/texts/' + str(i) + '.txt', 'w',encoding='cp1251') as file:
                            file.write(text)
                    #print(str(title.next),str(author.next))
                    with open('author/'+author_meta+'/meta/' + str(i) + '.txt', 'w',encoding='cp1251') as file:
                            file.write("title:\n"+str(title.next))#+"\nauthor:\n"+str(author.next))
                    i += 1
                except:
                    pass
            except:
                print("Russ              link!!!!!!")


#print(soup)

#for i in read_author_links():
#    create_poem_files(read_poem_links(),i)

#create_poem_files(read_poem_links(),"office_home")