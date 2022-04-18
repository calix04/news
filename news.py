import tkinter.messagebox as msgbox
from tkinter import*
from pip import main
import requests
from bs4 import BeautifulSoup
import tkinter

header  = {'user-agent':'mozila/2.0'}
news = Tk()
news.title("뉴스 헤드라인")
news.geometry("300x250+200+100")

def info_1() :
    if info_1:
        response_politics= requests.get('https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=100', headers= header)
        html = response_politics.text
        soup = BeautifulSoup(html, 'html.parser')
        titles = soup.select('.cluster_text_headline')
        window = tkinter.Tk()
        window.title('정치 뉴스 헤드라인')
        window.geometry("1000x600+150+100")
        frame = Frame(window)
        frame.grid(column=0, row=0)
        
        scrollbar = Scrollbar(frame)
        scrollbar.pack(side='right', fill='both')
        
        list = Listbox(frame, yscrollcommand= scrollbar.set, font= 30, width= 122,height= 34)

        for title in titles:
            head = title.text.strip()
  
            list.insert(END, head)

        list.pack(side='left',fill='both')
            
        scrollbar.config(command=list.yview)
        mainloop()

    
def info_2() :
    if info_2:
        response_politics= requests.get('https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=101', headers= header)

        html = response_politics.text
        soup = BeautifulSoup(html, 'html.parser')

        titles = soup.select('.cluster_text_headline')
        window = tkinter.Tk()
        window.title('경제 뉴스 헤드라인')
        window.geometry("1000x600+150+100")
        frame = Frame(window)
        frame.grid(column=0, row=0)
        
        scrollbar = Scrollbar(frame)
        scrollbar.pack(side='right', fill='both')
        
        list = Listbox(frame, yscrollcommand= scrollbar.set, font= 30, width= 122,height= 34)
        
        for title in titles:
            head = title.text.strip()

            list.insert(END, head)

        list.pack(side='left',fill='both')
            
        scrollbar.config(command=list.yview)
        mainloop()

def info_3() :
    if info_3:
        response_politics= requests.get('https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=102', headers= header)

        html = response_politics.text
        soup = BeautifulSoup(html, 'html.parser')

        titles = soup.select('.cluster_text_headline')
        window = tkinter.Tk()
        window.title('사회 뉴스 헤드라인')
        window.geometry("1000x600+150+100")
        frame = Frame(window)
        frame.grid(column=0, row=0)
        
        scrollbar = Scrollbar(frame)
        scrollbar.pack(side='right', fill='both')
        
        list = Listbox(frame, yscrollcommand= scrollbar.set, font= 30, width= 122,height= 34)

        for title in titles:
            head = title.text.strip()

            list.insert(END, head)

        list.pack(side='left',fill='both')
            
        scrollbar.config(command=list.yview)
        mainloop()

def info_4() :
    if info_4:
        response_politics= requests.get('https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=103', headers= header)

        html = response_politics.text
        soup = BeautifulSoup(html, 'html.parser')

        titles = soup.select('.cluster_text_headline')
        window = tkinter.Tk()
        window.title('생활/문화 뉴스 헤드라인')
        window.geometry("1000x600+150+100")
        frame = Frame(window)
        frame.grid(column=0, row=0)
        
        scrollbar = Scrollbar(frame)
        scrollbar.pack(side='right', fill='both')
        
        list = Listbox(frame, yscrollcommand= scrollbar.set, font= 30, width= 122,height= 34)

        for title in titles:
            head = title.text.strip()

            list.insert(END, head)

        list.pack(side='left',fill='both')
            
        scrollbar.config(command=list.yview)
        mainloop()


def info_5() :
    if info_5:
        response_politics= requests.get('https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105', headers= header)

        html = response_politics.text
        soup = BeautifulSoup(html, 'html.parser')
   
        titles = soup.select('.cluster_text_headline')
        window = tkinter.Tk()
        window.title('IT/과학 뉴스 헤드라인')
        window.geometry("1000x600+150+100")
        frame = Frame(window)
        frame.grid(column=0, row=0)
        
        scrollbar = Scrollbar(frame)
        scrollbar.pack(side='right', fill='both')
        
        list = Listbox(frame, yscrollcommand= scrollbar.set, font= 30, width= 122,height= 34)

        for title in titles:
            head = title.text.strip()

            list.insert(END, head)

        list.pack(side='left',fill='both')
            
        scrollbar.config(command=list.yview)
        mainloop()
def info_6() :
    if info_6:
        response_politics= requests.get('https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=104', headers= header)

        html = response_politics.text
        soup = BeautifulSoup(html, 'html.parser')
        
        titles = soup.select('.cluster_text_headline')
        window = tkinter.Tk()
        window.title('세계 뉴스 헤드라인')
        window.geometry("1000x600+150+100")
        frame = Frame(window)
        frame.grid(column=0, row=0)
        
        scrollbar = Scrollbar(frame)
        scrollbar.pack(side='right', fill='both')
        
        list = Listbox(frame, yscrollcommand= scrollbar.set, font= 30, width= 122,height= 34)

        for title in titles:
            head = title.text.strip()

            list.insert(END, head)#label1)

        list.pack(side='left',fill='both')
            
        scrollbar.config(command=list.yview)
        mainloop()

Button(news, command=info_1,text='정치',width=40,height= 2).pack()
Button(news, command=info_2,text='경제',width=40,height= 2).pack()
Button(news, command=info_3,text='사회',width=40,height= 2).pack()
Button(news, command=info_4,text='생활/문화',width=40,height= 2).pack()
Button(news, command=info_5,text='IT/과학',width=40,height= 2).pack()
Button(news, command=info_6,text='세계',width=40,height= 2).pack()


news.mainloop()