def find_webms(URL):
    import requests
    from bs4 import BeautifulSoup
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    thread=soup.find("div",{"class":"thread"})
    threads=thread.findAll("div",{"class":["postContainer opContainer","postContainer replyContainer"]})
    combined=[]
    for i in threads:
        if i.find("a",{"class":"fileThumb"}):
            try:
                webm="https:" + i.findAll("a",{"class":"fileThumb"})[0]['href']
                filename=i.findAll("div",{"class":"fileText"})[0].getText()
            except:
                pass
            finally:
                if not(filename==""):
                    joined=[filename,webm]
                    combined.append(joined)
        else:
            pass
    return combined

##finds threads using 4chan archive
def find_thread(URL):
    import requests
    import json
    import re
    from bs4 import BeautifulSoup

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    threadList=soup.findAll("a",{"class":"quotelink"})
    threads=["https://boards.4channel.org" + i['href'] for i in threadList]
    return threads



def produce_random_file(board, requiredString="ENTER"):
    import random
    
    
    try:
        boards=find_thread("https://boards.4channel.org/{}/archive".format(board))
        if requiredString != "ENTER":
            boards=[i for i in boards if i.upper().find(requiredString)>-1]
        if len(boards)==0:
            return 0
        boardLength=random.randrange(0,len(boards))
        selectedThread=boards[boardLength]

        threadList=find_webms(selectedThread)
        imageCount=len(threadList)
        randLink=threadList[random.randrange(0,imageCount-1)]
        return randLink[1],selectedThread
    except:
        print("ERROR")
    


def open_file(url,name):
    import urllib.request
    from PIL import Image
      
    urllib.request.urlretrieve(
      url,name)
      
    img = Image.open(name)
    img.show()



def Post_Meme(postText):
    from discord import SyncWebhook

    webhook = SyncWebhook.from_url()
    webhook.send(postText)


produce_random_file("wsg","HUMOR") 
 