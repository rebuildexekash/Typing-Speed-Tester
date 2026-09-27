from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import time 
import threading 
from test_data import l, L
import random
window=Tk()
x=IntVar()
currenttext=""
starttime = None

n = random.randint(0,4)

label1 = Label(
    window,
    text="HOP IN! 🎯",
    font=("Britannic Bold", 30, "bold"),
    bg="#DBABF1"
)
label1.pack(pady=(20, 5))
label_heading = Label(
    window,
    text="Let's see how fast you can type!",
    font=("Comic Sans MS", 16),
    bg="#DBABF1"
)
label_heading.pack(pady=(0, 15))
def script():
    global currenttext
    global starttime
    starttime=None
    if(x.get()==0):
        y=l[n]
        currenttext=l[n]
    if(x.get()==1):
        y=L[n]
        currenttext=L[n]
    label2.config(state=NORMAL)
    label2.delete("1.0", END)
    label2.insert("1.0", currenttext)
    label2.tag_remove("correct", "1.0", END)
    label2.tag_remove("wrong", "1.0", END)
    label2.config(state=DISABLED) #make sure when the sentence pai overwrite nah hogaye
frame1=Frame(window,bg="#E8B9FD")
frame1.pack()

ch=["SENTENCE","PARAGRAPH"]
for i in range(len(ch)):
    choice1=Radiobutton(frame1,
                        text=ch[i],
                        variable=x,
                        value=i)
    choice1.config (padx=10,pady=10,
                   font=("Times New Roman",10),
                   indicatoron=0,
                   width=15,
                   command=script)
    choice1.pack(side=LEFT)
label2 = Text(
    window,
    font=("Britannic Bold", 12),
    bg="#E2AEF3",
    wrap="word",
    height=4,
    width=75,
    padx=15,
    pady=15
)

label2.pack(pady=20)
label2.tag_config("correct", foreground="#037E09")
label2.tag_config("wrong", foreground="#7E0303")

#textbox actual shit 
def check_typing(event):
    global starttime
    if starttime == None :
        starttime = time.time()
    thought = text.get("1.0", "end-1c")

    for i in range(len(thought)):

        if i >= len(currenttext):
            break

        if thought[i] == currenttext[i]:
            label2.tag_remove("wrong", f"1.{i}", f"1.{i+1}")
            label2.tag_add("correct", f"1.{i}", f"1.{i+1}")

        else:
            label2.tag_remove("correct", f"1.{i}", f"1.{i+1}")
            label2.tag_add("wrong", f"1.{i}", f"1.{i+1}")
def submit():
    global currenttext
    global starttime
    thought = text.get("1.0", "end-1c")
    if (len(thought)==0):
        messagebox.showwarning(title='WARNING',message='Please type something before submitting.')
        return

    endtime = time.time()
    elapsed = endtime - starttime
    minutes = elapsed / 60
    characters = len(currenttext.replace(" ", ""))
    wpm = characters / 5 / minutes
    cpm = characters / minutes
    resultwpm.config(text=f"WPM - {round(wpm, 2)}")
    resultcpm.config(text=f"CPM - {round(cpm, 2)}")
    resulttime.config(text=f"TIME - {round(elapsed, 2)}s")
    
    print("Time taken:", round(elapsed, 2), "seconds")
    thought=text.get("1.0","end-1c")
    worderror=0
    lettererror=0
    actualtext=currenttext.split()
    thoughttext=thought.split()

    max_words = max(len(actualtext), len(thoughttext))
    for i in range(max_words):
        if i >= len(actualtext):
            worderror += 1
            lettererror += len(thoughttext[i])
            continue
        if i >= len(thoughttext):
            worderror += 1
            lettererror += len(actualtext[i])
            continue
        if actualtext[i] != thoughttext[i]:
            worderror+=1
        for j in range(min(len(actualtext[i]), len(thoughttext[i]))):
            if actualtext[i][j] != thoughttext[i][j]:
                lettererror += 1
        lettererror += abs(len(actualtext[i]) - len(thoughttext[i]))


    
    characters = len(currenttext.replace(" ", ""))
    wordaccuracy=(len(actualtext)-worderror)/len(actualtext)*100
    characteraccuracy=(characters-lettererror)/characters*100
    resultcharacteraccuracy.config(text=f"CHARACTER ACCURACY- {round(characteraccuracy,2)}")
    resultwordaccuracy.config(text=f"WORD  ACCURACY- {round(wordaccuracy,2)}")
    
    

    

text=Text(window,
          bg="#EED0F1",
          font=('Britannic Bold',15),
          height=5,
          width=60,
          padx=15,
          pady=15,
          fg="#070707")
text.pack()
text.bind("<KeyRelease>", check_typing)
button=Button(window,text="Submit your text",command=submit)
button.pack()
result_frame = Frame(window, bg="#E8B9FD",relief=RAISED)
Label(result_frame,text="RESULT",font=("Bahnschrift",20,'bold',)).pack(side=TOP)

result_frame = Frame(window, bg="#E8B9FD", relief=RAISED)
result_frame.pack(pady=15)

result_heading = Label(
    result_frame,
    text="RESULT",
    font=("Bahnschrift", 20, "bold"),
    bg="#E8B9FD"
)
result_heading.grid(row=0, column=0, columnspan=3, pady=(5, 10))

resultwpm = Label(
    result_frame,
    text="WPM: --",
    font=("Bahnschrift", 15),
    bg="#E8B9FD"
)
resultwpm.grid(row=1, column=0, padx=15)

resultcpm = Label(
    result_frame,
    text="CPM: --",
    font=("Bahnschrift", 15),
    bg="#E8B9FD"
)
resultcpm.grid(row=1, column=1, padx=15)

resulttime = Label(
    result_frame,
    text="TIME: --",
    font=("Bahnschrift", 15),
    bg="#E8B9FD"
)
resulttime.grid(row=1, column=2, padx=15)
result_frame2 = Frame(window, bg="#E8B9FD", relief=RAISED)
result_frame2.pack(pady=15)
resultwordaccuracy = Label(
    result_frame2,
    text="WORD ACCURACY - --",
    font=("Bahnschrift", 15),
    bg="#E8B9FD"
)
resultwordaccuracy.pack(side=LEFT, padx=15)

resultcharacteraccuracy = Label(
    result_frame2,
    text="CHARACTER ACCURACY - --",
    font=("Bahnschrift", 15),
    bg="#E8B9FD"
)
resultcharacteraccuracy.pack(side=LEFT, padx=15)


window.title("TYPING SPEED TEST")
window.geometry("850x800")
window.config(background="#DBABF1")
window.resizable(False, False)

window.mainloop()
