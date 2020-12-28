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
    while number>0 and i<=21:
        html_doc_parent=urlopen('http://www.verses.ru/category/stihi-o-politike/page-'+str(i))
        #html_doc_parent=open('ilia.html')
        soup = BeautifulSoup(html_doc_parent,"html5lib")

        div=soup.find('div',class_='text')
        #a1=soup.find_all('a',href=re.compile('/avtor/'))#,class_='link')
        a2=soup.find_all('div',class_='more')#,text=re.compile("<span class='hl' data-link="))
        print(a2[0].next.get('data-link'))
        a_page=[]
        for a in a2:
            a_page.append(a.next.get('data-link'))
        if i==0:
            author=soup.find('h1')
        #number_poems=soup.find('p',text=re.compile("Произведений"))
        #print(number_poems)
        number=len(a2)
        #print(div)
        a_all.append(a_page)
        i+=1
        #print(i)
        #print(a_all)
    i=0
    #print(author.next)
    return a_all

def create_poem_files(a_all,author_meta):
    os.makedirs("author/"+author_meta+"/texts")
    os.makedirs("author/"+author_meta+"/meta")
    i=0
    for a2 in a_all:
        for a in a2:
            try:
                html_doc_poem=urlopen('http://www.verses.ru'+str(a))
                #print(str(a.get('href')))
                #print(html_doc_child)
                soup_poem = BeautifulSoup(html_doc_poem, "html5lib")
                div1 = soup_poem.find('div', class_='verses-content')
                author = soup_poem.find('div', class_='verses-info').find('a')
                title = soup_poem.find('h1')
                # print(a.get('href'))
                # print(str(div1))
                div1=str(div1).replace("</div>","").replace('<div class="verses-content">',"").replace("<br/>","").replace("<pre>","").replace("</pre>","")
                print(div1)
                try:
                    with open('author/'+author_meta+'/texts/' + str(i) + '.txt', 'w',encoding='cp1251') as file:
                            file.write(div1)
                    #print(str(title.next),str(author.next))
                    with open('author/'+author_meta+'/meta/' + str(i) + '.txt', 'w',encoding='cp1251') as file:
                            file.write("title:\n"+str(title.next)+"\nauthor:\n"+str(author.next))
                    i += 1
                except:
                    pass
            except:
                print("Russ              link!!!!!!")

def check_poem(a_all):
    html_doc_poem = urlopen('http://www.verses.ru' + str(a_all))
    soup_poem = BeautifulSoup(html_doc_poem, "html5lib")
    div1 = soup_poem.find('div', class_='verses-content')
    author = soup_poem.find('div', class_='verses-info').find('a')
    title = soup_poem.find('h1')
    return [div1, author, title]


#print(soup)

#for i in read_author_links():
#    create_poem_files(read_poem_links(),i)

#create_poem_files(read_poem_links(),"politics")