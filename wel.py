import tkinter
import pickle
import random
root=tkinter.Tk()
root.title("HANGMAN")
root.configure(bg="black")
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
lb1=tkinter.Label(root, text='Developed By Aryan Khewal and Akshay Agarwal', font=('times', 34), bg='black', fg='crimson')
lb1.pack(pady=250)
count=0

def all_children (window) :
    _list = window.winfo_children()

    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())

    return _list

def welc():
    global root
    global score
    global uname
    score=0
    uname=None



    def play():
        global root
        global but5
        global bu
        global ent
        global lb3
        global lb4
        global lb5
        global word
        global inp
        global life
        global lf
        global disp
        global hngm
        global hng
        global scr
        global scr
        global ernd
        global uname
        global nent
        global name

        if uname==None:
            name=tkinter.Tk()
            name.title('Enter Name')
            name.configure(bg='grey')
            name.geometry("{0}x{1}+0+0".format(name.winfo_screenwidth()//3, name.winfo_screenheight()//3))
            name.overrideredirect(True)
            nlbl=tkinter.Label(name, text='Enter Player Name', font=('times', 30), fg='navyblue')
            nlbl.pack(pady=10)
            nent=tkinter.Entry(name, font=('times', 30), fg='maroon', width=20, state=tkinter.NORMAL)
            nent.pack(pady=10)
            def sub(event=None):
                global uname
                global name
                global nent
                global name
                global ent
                uname=(nent.get()).upper()
                ent.configure(state=tkinter.NORMAL)
                name.destroy()
            nbut=tkinter.Button(name, text='Submit', bg='black', fg='crimson', command=sub, font=('times', 30))
            nbut.pack(pady=10)
            name.bind('<Return>', sub)
            

        widget_list = all_children(root)
        for item in widget_list:
            item.pack_forget()
        widget_list = all_children(root)
        for item in widget_list:
            item.grid_forget()
        
        root.rowconfigure(5)
        root.columnconfigure(4)
        life=7
        f=open('Data\wrd100.eli', 'rb')
        d=pickle.load(f)
        f.close()
        wrd=len(d.keys())
        lst=list(d.keys())
        if score==0:
            rnd=random.randrange(0,wrd-1)
            ernd=rnd
            word=lst[rnd]
            cat=d[word]
        else:
            ilst=[]
            for i in range(0, ernd-ernd%10):
                ilst.append(i)
            for i in range((ernd//10+1)*10, wrd-1):
                ilst.append(i)
            rnd=random.choice(ilst)
            ernd=rnd
            word=lst[rnd]
            cat=d[word]
        inp=''
        disp='-'*len(word)
        hngm='Media\i{}.png'.format(life)
        lf=tkinter.Label(root, text="Life: {}".format(life), font=('times', 24), fg='darkblue', bg='darkorange')
        lf.grid(row=0, column=1, rowspan=1, columnspan=1, pady=25)
        scr=tkinter.Label(root, text="Score: {}".format(score), font=('times', 24), fg='darkblue', bg='darkorange')
        scr.grid(row=0, column=0, rowspan=1, columnspan=1, pady=25)
        hng=tkinter.PhotoImage(file=hngm)
        lb3=tkinter.Label(root, image=hng, relief='sunken', border=10)
        lb3.grid(row=1, column=0, rowspan=4, columnspan=2, padx=150)
        lbcat=tkinter.Label(root, text='Category: {}'.format(cat), fg='darkblue', bg='darkorange', font=('lucida console', 30))
        lbcat.grid(row=0, column=2, rowspan=1, columnspan=2)
        lb4=tkinter.Label(root, text=disp, fg='darkblue', bg='darkorange', font=('lucida console', 60))
        lb4.grid(row=1, column=2, rowspan=1, columnspan=2)
        ent=tkinter.Entry(root, fg='crimson', font=('times',90), width=2)
        ent.grid(row=2, column=2, columnspan=2, rowspan=1)
        if uname==None:
            ent.configure(state=tkinter.DISABLED)

        def check(event=None):
            global word
            global inp
            global ent
            global life
            global lb4
            global lf
            global disp
            global hngm
            global hng
            global lb3
            global bu
            global but5
            global lb5
            global score
            inp=ent.get()
            ent.delete('0')
            out=''
            mid=inp[0].upper()
            if (mid not in word) or ((mid in word) and (mid in disp)) :
                life-=1
            for i in range(0, len(disp)):
                if word[i]==mid:
                    out+=mid
                else:
                    out+=disp[i]
            lb4.configure(text=out)
            disp=out
            lf.configure(text="Life: {}".format(life))
            if life==0:
                lb4.configure(text=word)
                ent.destroy()
                bu.destroy()
                but5.destroy()
                lb5=tkinter.Label(root, bg='maroon', fg='white', text="YOU LOSE", font=('times', 50))
                lb5.grid(column=2, row=4, columnspan=2, rowspan=1)
                hsc={uname:score}
                f = open('Data/hs.eli', 'rb+')
                d=pickle.load(f)
                f.truncate(0)
                f.seek(0)
                if uname in list(d.keys()):
                    if d[uname]<score:
                        d.update(hsc)
                else:
                    d.update(hsc)
                pickle.dump(d,f)
                f.close()
                root.after(1500, welc)
            if disp==word:
                score+=len(word)*life
                root.after(1500, play)
                ent.destroy()
                bu.destroy()
                but5.destroy()
                lb5=tkinter.Label(root, bg='darkgreen', fg='white', text="YOU WIN", font=('times', 50))
                lb5.grid(column=2, row=4, columnspan=2, rowspan=1)
            hngm='Media\i{}.png'.format(life)
            hng=tkinter.PhotoImage(file=hngm)
            lb3.configure(image=hng)
        
        bu=tkinter.Button(root, command=check, text='Check', width=10, font=('times', 20), fg='navyblue')
        bu.grid(column=2, row=3, columnspan=2, rowspan=1)
        root.bind('<Return>', check)
        def backHigh():
            global uname
            global score
            global root
            global name
            try:
                name.destroy()
            except:
                hsc={uname:score}
                f = open('Data/hs.eli', 'rb+')
                d=pickle.load(f)
                f.truncate(0)
                f.seek(0)
                if uname in list(d.keys()):
                    if d[uname]<score:
                        d.update(hsc)
                else:
                    d.update(hsc)
                pickle.dump(d,f)
                f.close()
            root.after(10, welc)
        
        but5=tkinter.Button(root, text='Back', command=backHigh, width=15, font=('times', 24), bg='black', fg='firebrick', relief='sunken', border=10)
        but5.grid(column=2, row=4, columnspan=2, rowspan=1)


    
    def howto():
        global root
        widget_list = all_children(root)
        for item in widget_list:
            item.pack_forget()
        lbh=tkinter.Label(root, text='''Guess the word using the category and word length, with 6 wrong guesses allowed. Game continues to a new word till you lose a round.
                          \nFor each username, only their best ever score is stored in the highscore tab.
                          \nScore for one round=Lives left X length of the word guessed. Total score is the sum of all round scores''', fg='darkblue', bg='darkorange',
                          font=('lucida calligraphy', 30), justify=tkinter.LEFT, wraplength=1200)
        lbh.pack(pady=20)
        hbut=tkinter.Button(root, text='Back', command=welc, width=15, font=('times', 20), bg='white', fg='firebrick', relief='sunken', border=5)
        hbut.pack()



    def highScore():
        global root
        widget_list = all_children(root)
        for item in widget_list:
            item.pack_forget()
        root.rowconfigure(7)
        root.columnconfigure(2)
        f=open('Data/hs.eli', 'rb')
        d=pickle.load(f)
        f.close()
        g=[('Name', 'Score')]
        g+=(sorted(list(d.items()), key=lambda item: item[1], reverse=True))
        for i in range(0,6):
            for j in range(0,2):
                if j==0:
                    if i==0:
                        tbl=tkinter.Label(root, text=str(g[i][j]), font=('times', 24), fg='white', bg='firebrick', border=5, relief='sunken', width=35)
                        tbl.grid(row=i, column=j, rowspan=1, columnspan=1, pady=30, sticky=tkinter.E)
                    else:
                        tbl=tkinter.Label(root, text=str(g[i][j]), font=('times', 24), fg='darkblue', bg='darkorange', border=5, relief='sunken', width=35)
                        tbl.grid(row=i, column=j, rowspan=1, columnspan=1, pady=30, sticky=tkinter.E)
                else:
                    if i==0:
                        tbl=tkinter.Label(root, text=str(g[i][j]), font=('times', 24), fg='white', bg='firebrick', border=5, relief='sunken', width=35)
                        tbl.grid(row=i, column=j, rowspan=1, columnspan=1, pady=30, sticky=tkinter.W)
                    else:
                        tbl=tkinter.Label(root, text=str(g[i][j]), font=('times', 24), fg='darkblue', bg='darkorange', border=5, relief='sunken', width=35)
                        tbl.grid(row=i, column=j, rowspan=1, columnspan=1, pady=30, sticky=tkinter.W)
            bbut=tkinter.Button(root, text='Back', font=('times', 30), width=40, fg='crimson', bg='darkgrey', command=welc)

        bbut=tkinter.Button(root, text='Back', font=('times', 30), width=50, fg='crimson', bg='darkgrey', command=welc)
        bbut.grid(row=6, column=0, columnspan=2)
        
        
    
    widget_list = all_children(root)
    for item in widget_list:
        item.pack_forget()
    widget_list = all_children(root)
    for item in widget_list:
        item.grid_forget()
            
    root.configure(bg='darkorange')
    count=1
    hang=tkinter.PhotoImage(file='Media\hngc.png')
    lbe2=tkinter.Label(root, image=hang, height=400)
    lbe2.photo=hang
    lbe2.pack(pady=10)
    but1=tkinter.Button(root, text='Play', command=play, width=15, font=('times', 24), bg='steelblue', fg='firebrick', relief='raised', border=10, activebackground='yellow', activeforeground='maroon')
    but1.pack()
    but2=tkinter.Button(root, text='About the Game', command=howto, width=15, font=('times', 24), bg='steelblue', fg='firebrick', relief='raised', border=10, activebackground='yellow', activeforeground='maroon')
    but2.pack(pady=10)
    but3=tkinter.Button(root, text='Highscore', command=highScore, width=15, font=('times', 24), bg='steelblue', fg='firebrick', relief='raised', border=10, activebackground='yellow', activeforeground='maroon')
    but3.pack(pady=10)
    but4=tkinter.Button(root, text='Exit', command=root.destroy, width=15, font=('times', 24), bg='black', fg='firebrick', relief='sunken', border=10)
    but4.pack(pady=10)

if count==0:
    root.after(2000, welc)


root.mainloop()
