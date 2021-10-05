import bs4
import tkinter as tk
window = tk.Tk()

paths = {'Activities Board': "Simple/Activity.html",
         'Drink Menu': "Simple/Drink.html",
         'Food Menu': "Simple/Eat.html",
         'Music Board': "Simple/Music.html",
         'Food and Drink Board': "Simple/Food.html",
         'Home': "Simple/Home.html"}
k = list(paths.keys())
variable = tk.StringVar(window)
variable.set(k[0]) # default value

titleLabel = tk.Label(text = "Title")
messageLabel = tk.Label(text = "Message")
imgLabel = tk.Label(text = "Image Name")

entryTitle=tk.Entry()
entryMessage=tk.Entry()
entryImg=tk.Entry()
menu = tk.OptionMenu(window,variable, *k)

def changeFile(title, message, image, pathway):
    with open(pathway) as inf:
        txt = inf.read()
    soup = bs4.BeautifulSoup(txt, features="html.parser")
    string = "<button class=\"button1\" onclick=\"send('"+message+"')\"><img src=\"imgs/Custom/"+image+"\"/>"+title+"</button>"
    
    str1 = soup.contents
    str2 = str1[0].__str__().split(string, 1)
    
    
    
    
    data = str2[0] + str2[1]
    print(data)
    soup2 = bs4.BeautifulSoup(data, features="html.parser")

    with open(pathway, "w") as outf:
        outf.write(str(soup2))

def handle_click(event):
    message = entryMessage.get()
    title = entryTitle.get()
    image = entryImg.get()
    pathway = paths[variable.get()]
    print(title, message, image, pathway)
    changeFile(title, message, image, pathway)
   

button = tk.Button(text="Remove Button")

button.bind("<Button-1>", handle_click)

menu.pack()
titleLabel.pack()
entryTitle.pack()
messageLabel.pack()
entryMessage.pack()
imgLabel.pack()
entryImg.pack()
button.pack()


window.mainloop()