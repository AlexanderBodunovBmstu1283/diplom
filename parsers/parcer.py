#!/usr/bin/python
# -*- coding: cp1251 -*-
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import os

url1='http://www.stihi.ru/2018/02/09/8797'
url2='http://www.stihi.ru/avtor/mborovkova'

#&s=50
#'http://www.stihi.ru/avtor/gomer3'
#html_doc = urlopen(url2).read()
#2018/02/11/10904
#http://www.stihi.ru/avtor/poeziya1
#http://www.stihi.ru/avtor/agata8

author="none"

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

def bar():
    print (1)

def read_poem_links(link):

    global author
    a_all=[]
    number=1
    i=0
    while number>0 and i<=100:
        html_doc_parent=urlopen(link+'&s='+str(i))
        #html_doc_parent=open('ilia.html')
        soup = BeautifulSoup(html_doc_parent,"html5lib")

        div=soup.find('div',class_='text')
        #a1=soup.find_all('a',href=re.compile('/avtor/'))#,class_='link')
        a2=soup.find_all('a',class_='poemlink')
        if i==0:
            author=soup.find('h1')
        #number_poems=soup.find('p',text=re.compile("Произведений"))
        #print(number_poems)
        number=len(a2)
        #print(div)
        a_all.append(a2)
        i+=50
        print(i)
        print(a_all)
    i=0
    print(author.next)
    return a_all

def create_poem_files(a_all,author_meta):
    os.makedirs("author/"+author_meta+"/"+author_meta+"/texts")
    os.makedirs("author/"+author_meta+"/"+author_meta+"/meta")
    i=0
    for a2 in a_all:
        for a in a2:
            html_doc_poem=urlopen('http://www.stihi.ru'+str(a.get('href')))
            #print(str(a.get('href')))
            #print(html_doc_child)
            soup_poem = BeautifulSoup(html_doc_poem, "html5lib")
            div1 = soup_poem.find('div', class_='text')
            #print(a.get('href'))
            #print(str(div1))
            div1=str(div1).replace("</div>","").replace('<div class="text">',"").replace("<br/>","")

            with open('author/'+author_meta+"/"+author_meta+'/texts/' + str(i) + '.txt', 'w',encoding='cp1252') as file:
                        file.write(div1)
            with open('author/'+author_meta+"/"+author_meta+'/meta/' + str(i) + '.txt', 'w',encoding='cp1252') as file:
                        file.write("title:\n"+str(a.next)+"\nauthor:\n"+str(author.next))
            i += 1

    return [div1, str(a.next), str(author.next),i]


def check_poem(a_all):
    html_doc_poem = urlopen('http://www.stihi.ru' + str(a_all[0][0].get('href')))
    soup_poem = BeautifulSoup(html_doc_poem, "html5lib")
    div1 = soup_poem.find('div', class_='text')
    div1 = str(div1).replace("</div>", "").replace('<div class="text">', "").replace("<br/>", "")
    return [div1, str(a_all[0][0].next), str(author.next)]

#print(soup)

#for i in read_author_links():
#    create_poem_files(read_poem_links(),i)
