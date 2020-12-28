#!/usr/bin/python
# -*- coding: cp1251 -*-
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import os

url1='http://www.stihi.ru/2018/02/09/8797'
url2='http://www.stihi.ru/avtor/mborovkova'

name_dir="revolution"
name_category="revolution"


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
        html_doc_parent=urlopen('http://stih.su/stikhi-russkikh-poyetov-o-revolyucii/')
        #html_doc_parent=open('ilia.html')
        soup = BeautifulSoup(html_doc_parent,"html5lib")
        author=soup.find_all('a',target_='otst_5')
        a2=[]
        for i in author:
            a2.append(i.find('a').get('href'))
            #print((a2[0]))
        return a2

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
    for a in a_all:
            try:
                html_doc_poem=urlopen(str(a))
                #print(str(a.get('href')))
                #print(html_doc_child)
                soup_poem = BeautifulSoup(html_doc_poem, "html5lib")
                title=soup_poem.find('h1',class_='entry-title')
                author=soup_poem.find('div',class_="breadcrumbs").next.next
                text = ""
                for j in soup_poem.find('div', class_="entry-content").find_all('p'):
                    text += str(j.next).replace("<br/>", "") + "\n"

                #try:
                try:
                    with open('author/'+author_meta+"/"+name_category+'/texts/' + str(i) + '.txt', 'w',encoding='cp1251') as file:
                            file.write(text)
                        #print(str(title.next),str(author.next))

                    with open('author/'+author_meta+"/"+name_category+'/meta/' + str(i) + '.txt', 'w',encoding='cp1251') as file:
                            file.write("title:\n"+str(title.next)+"\nauthor:\n"+str(author.next))

                    i+=1
                except:
                    pass
            except:
                print("Russ              link!!!!!!")


#print(soup)

#for i in read_author_links():
#    create_poem_files(read_poem_links(),i)

#create_poem_files(read_poem_links(),name_dir)