import tkinter as tk
import tkinter.messagebox
import random
import operator
import time

# 十點半遊戲
class poker():

    global count 
    count = 0
    global POKER
    POKER = list(range(1,53))
    random.shuffle(POKER)

    # 抽牌
    def getCard():
        global POKER
        global count
        card = POKER.pop(count) # pop() 取後不放回
        count += 1
        return card
    
    # 得到撲克牌花色
    def color(n):
        if ((n-1) // 13) == 0 : 
            color = '  ♠  '
        elif ((n-1) // 13) == 1 :
            color = '  ♥  '
        elif ((n-1) // 13) == 2 :
            color = '  ♦  '
        elif ((n-1) // 13) == 3 :
            color = '  ♣  '
        return color

    # 取得撲克牌點數 A~K
    def strPoint(n):
        point = n % 13

        if point == 0:
            point = 'K'
        elif point == 12:
            point = 'Q'
        elif point == 11:
            point = 'J'
        elif point == 1:
            point = 'A'

        strPoint = str(point)
        return strPoint

    # 計算撲克牌點數 0.5~10
    def point(n):
        point = n % 13

        if point == 0:
            point = 0.5
        elif point == 12:
            point = 0.5
        elif point == 11:
            point = 0.5

        return point

    # 確認點數是否超過十點半
    def check(n):
        if n <= 10.5:
            flag = True
        else:
            flag = False
        return  flag

# 基準介面，共有的設定在這裡調整
class basedesk():  
    def __init__(self,master):
        self.root = master
        self.root.config()
        self.root.title('Poker Game')
        w, h = root.maxsize()
        self.root.geometry("{}x{}".format(w, h))
        self.root.resizable(True, True) # 可調整大小
        startScene(self.root)        

# 小遊戲選擇畫面
class startScene():
    def __init__(self,master):

        def confirm_to_quit():          
            if tk.messagebox.askokcancel('溫馨提示', '確定退出嗎🥺🥺🥺'):
                self.startScene.quit() 
        
        self.master = master
        self.master.config(bg='#EFEFEF')
        self.startScene = tk.Frame(self.master,)
        self.startScene.pack()

        label = tk.Label(self.startScene, text = '\n\n\n⚝ 小遊戲 ⚝\n', font = 'Arial -32', fg = 'brown')
        label.config(bg='#EFEFEF')
        label.pack(expand=1)

        btn = tk.Button(self.startScene, text='十點半',font = 'Arial -24',command=self.changeToInitface)
        btn.config(bg='white')
        btn.pack(padx=10, pady=20,anchor='center')

        btn2 = tk.Button(self.startScene, text='德州撲克牌',font = 'Arial -24',command=self.changeToTexas)
        btn2.config(bg='white')
        btn2.pack(padx=10, pady=20,anchor='center')

        button = tk.Button(self.startScene, text = '退出',font = 'Arial -24', command=confirm_to_quit)
        button.config(bg='white')
        button.pack(padx=10, pady=20,anchor='center')  

    # 從遊戲開始畫面切換到十點半 
    def changeToInitface(self,):       
        self.startScene.destroy()
        initface(self.master) 
    
    # 從遊戲開始畫面切換到德州撲克牌
    def changeToTexas(self,):
        self.startScene.destroy()
        texas(self.master) 

# 遊戲初始畫面                
class initface():
    def __init__(self,master):

        def confirm_to_quit():          
            if tk.messagebox.askokcancel('溫馨提示', '確定退出嗎🥺🥺🥺'):
                self.initface.quit()
        
        self.master = master
        self.master.config(bg='#EFEFEF')
        self.initface = tk.Frame(self.master,)
        self.initface.pack()

        label = tk.Label(self.initface, text = '\n\n\n\n撲克牌遊戲\n十點半', font = 'Arial -32', fg = 'brown')
        label.config(bg='#EFEFEF')
        label.pack(expand=1) 

        btn = tk.Button(self.initface,text='遊戲規則',font = 'Arial -24',command=self.changeToFace1)
        btn.config(bg='white')
        btn.pack(padx=10, pady=20,anchor='center')

        btn2 = tk.Button(self.initface,text='遊戲開始',font = 'Arial -24',command=self.changeToFace2)
        btn2.config(bg='white')
        btn2.pack(padx=10, pady=20,anchor='center')

        button = tk.Button(self.initface, text = '退出',font = 'Arial -24', command=confirm_to_quit)
        button.config(bg='white')
        button.pack(padx=10, pady=20,anchor='center')    
        
    # 從遊戲開始畫面切換到遊戲規則  
    def changeToFace1(self,):       
        self.initface.destroy()
        face1(self.master) 

    # 從遊戲開始畫面切換到遊戲進行畫面\
    def changeToFace2(self,):
        self.initface.destroy()
        face2(self.master)     

# 遊戲規則介面
class face1():
    def __init__(self,master):
        self.master = master
        self.master.config(bg='#EFEFEF')
        self.face1 = tk.Frame(self.master,)
        self.face1.pack()  

        label1 = tk.Label(self.face1, text = '\n\n\n遊戲規則\n', font = 'Arial -28', fg = 'black')
        label1.config(bg='#EFEFEF')
        label1.pack()

        label1 = tk.Label(self.face1, text = '1. 拿到比莊家更接近十點半的牌\n\n2. 不能超過十點半，會爆掉\n\n3. A-10 分別代表1-10\n\n4. J、Q、K為半點\n\n5. 一開始每人1張底牌\n\n6. 最多可加到手上有5張牌\n', font = 'Arial -20', fg = 'black')
        label1.config(bg='#EFEFEF')
        label1.pack()

        btn = tk.Button(self.face1,text='遊戲開始',font = 'Arial -24',command=self.changeToFace2)
        btn.config(bg='white')
        btn.pack(padx=240 ,anchor='se')

    # 遊戲規則畫面切換到遊戲進行畫面
    def changeToFace2(self,):       
        self.face1.destroy()
        face2(self.master) 

# 遊戲中的介面    
class face2():
    def __init__(self,master):
        self.master = master
        self.master.config(bg='#EFEFEF')
        self.face2 = tk.Frame(self.master,)
        self.face2.pack()

        label1 = tk.Label(self.face2, text = '\n\n\n莊家', font = 'Arial -28', fg = 'brown')
        label1.config(bg='#EFEFEF')
        label1.grid(row = 0, column = 0, columnspan = 5, pady = 20)

        # b1 ~ b5 : 遊戲介面中顯示莊家牌的 label
        global b1, b2, b3, b4, b5
        b1 = tk.Label(self.face2)
        b1.config(bg='#EFEFEF',text = '    \n    ', font = 'Arial -26', fg='black')
        b1.grid(row = 1, column = 0, padx = 10)

        b2 = tk.Label(self.face2)
        b2.config(bg='#EFEFEF',text = '    \n    ', font = 'Arial -26', fg='#EFEFEF')
        b2.grid(row = 1, column = 1, padx = 10)

        b3 = tk.Label(self.face2)
        b3.config(bg='#EFEFEF',text = '    \n    ', font = 'Arial -26', fg='#EFEFEF')
        b3.grid(row = 1, column = 2, padx = 10)

        b4 = tk.Label(self.face2)
        b4.config(bg='#EFEFEF',text = '    \n    ', font = 'Arial -26', fg='#EFEFEF')
        b4.grid(row = 1, column = 3, padx = 10)

        b5 = tk.Label(self.face2)
        b5.config(bg='#EFEFEF',text = '    \n    ', font = 'Arial -26', fg='#EFEFEF')
        b5.grid(row = 1, column = 4, padx = 10)

        label2 = tk.Label(self.face2, text = '玩家', font = 'Arial -28', fg = 'brown')
        label2.config(bg='#EFEFEF')
        label2.grid(row = 3, column=0, columnspan=5, pady = 20)

        # p1 ~ p5 : 遊戲介面中顯示玩家牌的 label
        global p1, p2, p3, p4, p5
        p1 = tk.Label(self.face2)
        p2 = tk.Label(self.face2)
        p3 = tk.Label(self.face2)
        p4 = tk.Label(self.face2)
        p5 = tk.Label(self.face2)
        
        global state
        state = tk.Label(self.face2, text = '遊戲狀態:遊戲中', font = 'Arial -24', fg='#EFEFEF')
        state.config(bg = '#EFEFEF')
        state.grid(row=5,  column=0, columnspan=8, pady = 20)

        ask_add = tk.Label(self.face2,text='  加牌?',font = 'Arial -28')
        ask_add.config(bg='#EFEFEF')
        ask_add.grid(row = 2, column = 6, columnspan = 2)

        global btn1
        btn1 = tk.Button(self.face2)
        btn1.config(bg = 'white',text = '是', font = 'Arial -26', command = self.addCard)
        btn1.grid(row = 3, column = 6, padx=15)

        global btn2   
        btn2 = tk.Button(self.face2)
        btn2.config(bg = 'white',text = '否', font = 'Arial -26', command = self.addBanker)
        btn2.grid(row = 3, column = 7)

        stop = tk.Button(self.face2)
        stop.config(bg = 'white',text = '結束遊戲', font = 'Arial -22', command=self.stopPlaying)
        
        again = tk.Button(self.face2)
        again.config(bg = 'white',text = '再玩一次', font = 'Arial -22', command=self.playAgain)

        global pointP, sumP
        sumP = 0
        global pointB, sumB
        sumB = 0

        # 玩家第一張牌
        card1 = poker.getCard()
        pointP = poker.point(card1)
        sumP = sumP + pointP
        c1 = poker.color(card1) + '\n' + poker.strPoint(card1)
        p1.config(bg='white',text = c1 , font = 'Arial -30')
        p1.grid(row = 4, column = 0, padx = 10)

        # 莊家第一張牌
        card2 = poker.getCard()
        pointB = poker.point(card2)
        sumB = sumB + pointB
        c2 = poker.color(card2) + '\n' + poker.strPoint(card2)
        b1.config(bg='white',text = c2 , font = 'Arial -30')
        b1.grid(row = 1, column = 0, padx = 10)
  
    global countPlayerAdd
    countPlayerAdd = 0
    # 玩家加牌 / 按鈕'是'的指令
    def addCard(self,):
        
        global countPlayerAdd, pointP, sumP

        # 將玩家牌加到指定位置
        if countPlayerAdd == 0 : 
            card = poker.getCard()
            pointP = poker.point(card)
            sumP = sumP + pointP
            c = poker.color(card) + '\n' + poker.strPoint(card)
            p2.config(bg='white',text = c , font = 'Arial -30')
            p2.grid(row = 4, column = 1, padx = 10)
            countPlayerAdd += 1

        elif countPlayerAdd == 1 : 
            card = poker.getCard()
            pointP = poker.point(card)
            sumP = sumP + pointP
            c = poker.color(card) + '\n' + poker.strPoint(card)
            p3.config(bg='white',text = c , font = 'Arial -30')
            p3.grid(row = 4, column = 2, padx = 10)
            countPlayerAdd += 1   

        elif countPlayerAdd == 2 : 
            card = poker.getCard()
            pointP = poker.point(card)
            sumP = sumP + pointP
            c = poker.color(card) + '\n' + poker.strPoint(card)
            p4.config(bg='white',text = c , font = 'Arial -30')
            p4.grid(row = 4, column = 3, padx = 10)
            countPlayerAdd += 1       

        elif countPlayerAdd == 3 : 
            card = poker.getCard()
            pointP = poker.point(card)
            sumP = sumP + pointP
            c = poker.color(card) + '\n' + poker.strPoint(card)
            p5.config(bg='white',text = c , font = 'Arial -30')
            p5.grid(row = 4, column = 4, padx = 10)
            countPlayerAdd += 1

        # 確認點數大小是否超過十點半 並 判斷玩家是否有一條龍
        if poker.check(sumP) == False:
            btn1 = tk.Button(self.face2, state = tk.DISABLED)
            btn1.config(bg = 'white',text = '是', font = 'Arial -26', command = self.addCard)
            btn1.grid(row = 3, column = 6, padx=15)

            btn2 = tk.Button(self.face2, state = tk.DISABLED)
            btn2.config(bg = 'white',text = '否', font = 'Arial -26', command = self.addCard)
            btn2.grid(row = 3, column = 7, padx=15)

            state = tk.Label(self.face2, text = '玩家點數超過十點半，莊家獲勝😣', font = 'Arial -24')
            state.config(bg = '#EFEFEF')
            state.grid(row=5,  column=0, columnspan=8, pady = 20)

            stop = tk.Button(self.face2)
            stop.config(bg = 'white',text = '結束遊戲', font = 'Arial -22', command=self.stopPlaying)
            stop.grid(row = 6, column = 4, columnspan=2, pady=10)

            again = tk.Button(self.face2)
            again.config(bg = 'white',text = '再玩一次', font = 'Arial -22', command=self.playAgain)
            again.grid(row = 6, column = 2, columnspan=2, pady=10)

        elif countPlayerAdd == 4:
            state = tk.Label(self.face2, text = '恭喜! 一條龍! 玩家獲勝😀', font = 'Arial -24')
            state.config(bg = '#EFEFEF')
            state.grid(row=5,  column=0, columnspan=8, pady = 20)

            stop = tk.Button(self.face2)
            stop.config(bg = 'white',text = '結束遊戲', font = 'Arial -22', command=self.stopPlaying)
            stop.grid(row = 6, column = 4, columnspan=2, pady=10)

            again = tk.Button(self.face2)
            again.config(bg = 'white',text = '再玩一次', font = 'Arial -22', command=self.playAgain)
            again.grid(row = 6, column = 2, columnspan=2, pady=10)

            btn1 = tk.Button(self.face2, state = tk.DISABLED)
            btn1.config(bg = 'white',text = '是', font = 'Arial -26', command = self.addCard)
            btn1.grid(row = 3, column = 6, padx=15)

            btn2 = tk.Button(self.face2, state = tk.DISABLED)
            btn2.config(bg = 'white',text = '否', font = 'Arial -26', command = self.addCard)
            btn2.grid(row = 3, column = 7, padx=15)

        return sumP

    global countBankerAdd
    countBankerAdd = 0
    # 莊家自動加牌 / 按鈕'否'的指令
    def addBanker(self,):

        global countBankerAdd
        global pointB
        global sumB
        global sumP

        # 按鈕'是'失效
        btn1 = tk.Button(self.face2, state = tk.DISABLED)
        btn1.config(bg = 'white',text = '是', font = 'Arial -26', command = self.addCard)
        btn1.grid(row = 3, column = 6, padx=15)

        # 莊家點數小於7.5時，會自動抽牌
        while sumB < 7.5:

            # 莊家牌顯示到指定位置
            if countBankerAdd == 0: 
                card = poker.getCard()
                pointB = poker.point(card)
                sumB = sumB + pointB
                c = poker.color(card) + '\n' + poker.strPoint(card)
                b2.config(bg='white',text = c , font = 'Arial -30', fg='black')
                b2.grid(row = 1, column = 1, padx = 10)
                countBankerAdd += 1
            elif countBankerAdd == 1:
                card = poker.getCard()
                pointB = poker.point(card)
                sumB = sumB + pointB
                c = poker.color(card) + '\n' + poker.strPoint(card)
                b3.config(bg='white',text = c , font = 'Arial -30', fg='black')
                b3.grid(row = 1, column = 2, padx = 10)
                countBankerAdd += 1
            elif countBankerAdd == 2:
                card = poker.getCard()
                pointB = poker.point(card)
                sumB = sumB + pointB
                c = poker.color(card) + '\n' + poker.strPoint(card)
                b4.config(bg='white',text = c , font = 'Arial -30', fg='black')
                b4.grid(row = 1, column = 3, padx = 10)
                countBankerAdd += 1
            elif countBankerAdd == 3:
                card = poker.getCard()
                pointB = poker.point(card)
                sumB = sumB + pointB
                c = poker.color(card) + '\n' + poker.strPoint(card)
                b5.config(bg='white',text = c , font = 'Arial -30', fg='black')
                b5.grid(row = 1, column = 4, padx = 10)
                countBankerAdd += 1
        # 按鈕'否'失效       
        btn2 = tk.Button(self.face2, state = tk.DISABLED)
        btn2.config(bg = 'white',text = '否', font = 'Arial -26', command = self.addCard)
        btn2.grid(row = 3, column = 7, padx=15)

        # 判斷莊家點數是否超過十點半 / 遊戲結束，獲勝者判斷
        if poker.check(sumB) == False:
            state = tk.Label(self.face2, text = '莊家點數超過十點半，玩家獲勝😀', font = 'Arial -24')
            state.config(bg = '#EFEFEF')
            state.grid(row=5,  column=0, columnspan=8, pady = 20)

            stop = tk.Button(self.face2)
            stop.config(bg = 'white',text = '結束遊戲', font = 'Arial -22', command=self.stopPlaying)
            stop.grid(row = 6, column = 4, columnspan=2, pady=10)

            again = tk.Button(self.face2)
            again.config(bg = 'white',text = '再玩一次', font = 'Arial -22', command=self.playAgain)
            again.grid(row = 6, column = 2, columnspan=2, pady=10)

        elif countBankerAdd == 4:
            state = tk.Label(self.face2, text = '莊家一條龍! 莊家獲勝😣😣😣', font = 'Arial -24')
            state.config(bg = '#EFEFEF')
            state.grid(row=5,  column=0, columnspan=8, pady = 20)

            stop = tk.Button(self.face2)
            stop.config(bg = 'white',text = '結束遊戲', font = 'Arial -22', command=self.stopPlaying)
            stop.grid(row = 6, column = 4, columnspan=2, pady=10)

            again = tk.Button(self.face2)
            again.config(bg = 'white',text = '再玩一次', font = 'Arial -22', command=self.playAgain)
            again.grid(row = 6, column = 2, columnspan=2, pady=10)

            btn1 = tk.Button(self.face2, state = tk.DISABLED)
            btn1.config(bg = 'white',text = '是', font = 'Arial -26', command = self.addCard)
            btn1.grid(row = 3, column = 6, padx=15)

            btn2 = tk.Button(self.face2, state = tk.DISABLED)
            btn2.config(bg = 'white',text = '否', font = 'Arial -26', command = self.addCard)
            btn2.grid(row = 3, column = 7, padx=15)

        elif sumP > sumB :
            state = tk.Label(self.face2, text = '玩家點數大於莊家，玩家獲勝😀', font = 'Arial -24')
            state.config(bg = '#EFEFEF')
            state.grid(row=5,  column=0, columnspan=8, pady = 20)

            stop = tk.Button(self.face2)
            stop.config(bg = 'white',text = '結束遊戲', font = 'Arial -22', command=self.stopPlaying)
            stop.grid(row = 6, column = 4, columnspan=2, pady=10)

            again = tk.Button(self.face2)
            again.config(bg = 'white',text = '再玩一次', font = 'Arial -22', command=self.playAgain)
            again.grid(row = 6, column = 2, columnspan=2, pady=10)

        elif sumB > sumP :
            state = tk.Label(self.face2, text = '莊家點數大於玩家，莊家獲勝😣', font = 'Arial -24')
            state.config(bg = '#EFEFEF')
            state.grid(row=5,  column=0, columnspan=8, pady = 20)

            stop = tk.Button(self.face2)
            stop.config(bg = 'white',text = '結束遊戲', font = 'Arial -22', command=self.stopPlaying)
            stop.grid(row = 6, column = 4, columnspan=2, pady=10)

            again = tk.Button(self.face2)
            again.config(bg = 'white',text = '再玩一次', font = 'Arial -22', command=self.playAgain)
            again.grid(row = 6, column = 2, columnspan=2, pady=10)

        elif sumP == sumB and countPlayerAdd > countBankerAdd:
            state = tk.Label(self.face2, text = '點數相等，玩家牌數大於莊家，玩家獲勝😀', font = 'Arial -24')
            state.config(bg = '#EFEFEF')
            state.grid(row=5,  column=0, columnspan=8, pady = 20)

            stop = tk.Button(self.face2)
            stop.config(bg = 'white',text = '結束遊戲', font = 'Arial -22', command=self.stopPlaying)
            stop.grid(row = 6, column = 4, columnspan=2, pady=10)

            again = tk.Button(self.face2)
            again.config(bg = 'white',text = '再玩一次', font = 'Arial -22', command=self.playAgain)
            again.grid(row = 6, column = 2, columnspan=2, pady=10)

        elif sumP == sumB and countPlayerAdd < countBankerAdd:
            state = tk.Label(self.face2, text = '點數相等，莊家牌數大於玩家，莊家獲勝😣', font = 'Arial -24')
            state.config(bg = '#EFEFEF')
            state.grid(row=5,  column=0, columnspan=8, pady = 20)

            stop = tk.Button(self.face2)
            stop.config(bg = 'white',text = '結束遊戲', font = 'Arial -22', command=self.stopPlaying)
            stop.grid(row = 6, column = 4, columnspan=2, pady=10)

            again = tk.Button(self.face2)
            again.config(bg = 'white',text = '再玩一次', font = 'Arial -22', command=self.playAgain)
            again.grid(row = 6, column = 2, columnspan=2, pady=10)

        elif sumP == sumB and countPlayerAdd == countBankerAdd:
            state = tk.Label(self.face2, text = '點數相等，牌數相等，和局', font = 'Arial -24')
            state.config(bg = '#EFEFEF')
            state.grid(row=5,  column=0, columnspan=8, pady = 20)

            stop = tk.Button(self.face2)
            stop.config(bg = 'white',text = '結束遊戲', font = 'Arial -22', command=self.stopPlaying)
            stop.grid(row = 6, column = 4, columnspan=2, pady=10)

            again = tk.Button(self.face2)
            again.config(bg = 'white',text = '再玩一次', font = 'Arial -22', command=self.playAgain)
            again.grid(row = 6, column = 2, columnspan=2, pady=10)
        
        return sumB

    # 遊戲結束
    def stopPlaying(self,):
        self.face2.quit()

    # 再玩一次
    def playAgain(self,):
        global countBankerAdd
        global countPlayerAdd
        global count
        global POKER
        countPlayerAdd = 0
        countBankerAdd = 0
        count = 0
        POKER = list()
        POKER = list(range(1,53))
        random.shuffle(POKER)
        self.face2.destroy()
        initface(self.master) 

# 德州撲克牌初始介面
class texas():  
    def __init__(self,master):
   
        self.master = master
        self.master.config(bg='#EFEFEF')
        self.texas = tk.Frame(self.master,)
        self.texas.pack()

        label = tk.Label(self.texas, text = '\n\n\n德州撲克牌\n', font = 'Arial -32', fg = 'brown')
        label.config(bg='#EFEFEF')
        label.pack(expand=1) 

        btn = tk.Button(self.texas, text='遊戲規則',font = 'Arial -24',command=self.changeToTexasRule)
        btn.config(bg='white')
        btn.pack(padx=10, pady=20,anchor='center')

        btn2 = tk.Button(self.texas, text='遊戲開始',font = 'Arial -24',command=self.changeToTexasGame)
        btn2.config(bg='white')
        btn2.pack(padx=10, pady=20,anchor='center')

        button = tk.Button(self.texas, text ='退出',font = 'Arial -24', command=self.confirm_to_quit)
        button.config(bg='white')
        button.pack(padx=10, pady=20,anchor='center')  

    def confirm_to_quit(self,):          
        if tk.messagebox.askokcancel('溫馨提示', '確定退出嗎🥺🥺🥺'):
            self.texas.quit()  
        
    
    # 從遊戲開始畫面切換到遊戲規則  
    def changeToTexasRule(self,):       
        self.texas.destroy()
        texasRule(self.master) 

    # 從遊戲開始畫面切換到遊戲進行畫面\
    def changeToTexasGame(self,):
        self.texas.destroy()
        texasGame(self.master)     

# 德州撲克牌遊戲規則介面
class texasRule():
    def __init__(self,master):
        self.master = master
        self.master.config(bg='#EFEFEF')
        self.texasRule = tk.Frame(self.master,)
        self.texasRule.pack()  

        label1 = tk.Label(self.texasRule, text = '\n\n\n\n遊戲規則\n', font = 'Arial -28', fg = 'black')
        label1.config(bg='#EFEFEF')
        label1.pack()

        label1 = tk.Label(self.texasRule, text = '1. 玩家會拿到2張底牌,只有玩家自己看得到牌面\n\n2. 莊家會發下5張公用牌,玩家須利用公用牌組成最佳的5張牌組。\n\n3. 最後由握有最佳撲克牌組的玩家贏得勝利\n\n4. 同花順>鐵支>葫蘆>同花>順子>三條>兩對>一對>高牌(單張)\n\n5. 點數相同比花色(黑桃>紅心>稜形>梅花)\n\n', font = 'Arial -20', fg = 'black')
        label1.config(bg='#EFEFEF')
        label1.pack()

        btn = tk.Button(self.texasRule,text='遊戲開始',font = 'Arial -24',command=self.changeToTexasGame)
        btn.config(bg='white')
        btn.pack(padx=240 ,anchor='se')

    # 遊戲規則畫面切換到遊戲進行畫面
    def changeToTexasGame(self,):       
        self.texasRule.destroy()
        texasGame(self.master) 

# 德州撲克牌遊戲  
class texasPoker():
    def POINT(card):  #點數
        card_point = list(range(len(card)))
        for i in range(len(card)):
            card_point[i] = card[i][0]
        return card_point

    # 取得撲克牌點數(type:String)
    def strPoint(card):
        strP= str(card[0])
        if strP == '13':
            strP = 'K'
        elif strP == '12':
            strP = 'Q'
        elif strP == '11':
            strP = 'J'
        elif strP == '1':
            strP = 'A'
        return strP

    # 撲克牌花色從數字轉變成符號
    def strColor(card):
        strC = str(card[1])
        if strC == '1':
            strC = '  ♠  '
        elif strC == '2':
            strC = '  ♥  '
        elif strC == '3':
            strC = '  ♦  '
        elif strC == '4':
            strC = '  ♣  '
        return strC

    global moneyA, moneyB
    moneyA = 200 
    moneyB = 200

    def PC(point,bp,p,b):   #牌型判斷
        total_point = point+bp  #將玩家的牌和公牌結合
        total_point.sort()
        
        point_counter = {}
        for i in total_point:
            point_counter[i] = point_counter.get(i,0)+1

        pc = list(point_counter.values())
        num_pair = pc.count(2)
        num_triple = pc.count(3)

        handtype = []
        pointtype = []

        #check Full House
        if (2 in point_counter.values()) and (3 in point_counter.values()):
            handtype = ["葫蘆"]
            ht = 7
            pointtype = [max(total_point,key = total_point.count)] * 3
            if num_pair == 2:
                total_point2 = total_point.copy()
                total_point2.remove(max(total_point,key = total_point.count))
                total_point2.remove(max(total_point,key = total_point.count))
                total_point2.remove(max(total_point,key = total_point.count))
                if max(total_point2,key = total_point.count) != 1:
                    total_point2.remove(max(total_point2,key = total_point.count))
                    total_point2.remove(max(total_point2,key = total_point.count))
                    pointtype.append(max(total_point2,key = total_point2.count))
                    pointtype.append(max(total_point2,key = total_point2.count))
                else:
                    pointtype.append(max(total_point2,key = total_point.count))
                    pointtype.append(max(total_point2,key = total_point.count))
            elif num_pair == 1:
                total_point2 = total_point.copy()
                total_point2.remove(max(total_point,key = total_point.count))
                total_point2.remove(max(total_point,key = total_point.count))
                total_point2.remove(max(total_point,key = total_point.count))
                pointtype.append(max(total_point2,key = total_point.count))
                pointtype.append(max(total_point2,key = total_point.count))
        elif num_triple == 2:  #葫蘆
            handtype = ["葫蘆"]
            ht = 7
            if max(total_point,key = total_point.count) != 1:
                total_point2 = total_point.copy()
                total_point2.remove(max(total_point,key = total_point.count))
                total_point2.remove(max(total_point,key = total_point.count))
                total_point2.remove(max(total_point,key = total_point.count))
                pointtype = [max(total_point2,key = total_point2.count)] * 3
                pointtype.append(max(total_point,key = total_point.count))
                pointtype.append(max(total_point,key = total_point.count))
            else:
                pointtype = [max(total_point,key = total_point.count)] * 3
                total_point2 = total_point.copy()
                total_point2.remove(max(total_point,key = total_point.count))
                total_point2.remove(max(total_point,key = total_point.count))
                total_point2.remove(max(total_point,key = total_point.count))
                pointtype.append(max(total_point2,key = total_point.count))
                pointtype.append(max(total_point2,key = total_point.count))
                
        elif num_triple == 1:
            handtype = ["三條"]
            ht = 4
            pointtype = [max(total_point,key = total_point.count)] * 3

        elif num_pair == 3:  #兩對
            handtype = ["兩對"]
            ht = 3
            total_point2 = total_point.copy()
            total_point2.remove(max(total_point,key = total_point.count))
            total_point2.remove(max(total_point,key = total_point.count))
            pointtype = [max(total_point2,key = total_point.count)] * 2
            total_point2.remove(max(total_point2,key = total_point.count))
            total_point2.remove(max(total_point2,key = total_point.count))
            pointtype.append(max(total_point2,key = total_point2.count))
            pointtype.append(max(total_point2,key = total_point2.count))
            if max(total_point,key = total_point.count) == 1:
                pointtype = pointtype[2:] + [1,1]
        elif num_pair == 2:
            handtype = ["兩對"]
            ht = 3
            total_point2 = total_point.copy()
            pointtype = [max(total_point,key = total_point.count)] * 2
            total_point2.remove(max(total_point,key = total_point.count))
            total_point2.remove(max(total_point,key = total_point.count))
            pointtype.append(max(total_point2,key = total_point2.count))
            pointtype.append(max(total_point2,key = total_point2.count)) 
            
        elif num_pair == 1:
            handtype = ["一對"]
            ht = 2
            pointtype = [max(total_point,key = total_point.count)] * 2
            
        #check Four-of-a-Kind
        if 4 in point_counter.values():
            handtype = ["鐵支"]
            ht = 8
            pointtype = [max(total_point,key = total_point.count)] * 4
            total_point2 = total_point.copy()
            total_point2.remove(max(total_point,key = total_point.count))
            total_point2.remove(max(total_point,key = total_point.count))
            total_point2.remove(max(total_point,key = total_point.count))
            total_point2.remove(max(total_point,key = total_point.count))
            pointtype.append(max(total_point2,key = total_point2.count))
            
        #check Straight
        pt = set(total_point)
        point_straight = []
        straight = {1,10,11,12,13}
        x = 0
        for i in range(6):
            if (total_point[i+1]-total_point[i]) == 1 and x < 4:
                x += 1
                point_straight.append(total_point[i])
            elif (total_point[i+1]-total_point[i]) < 1 and x < 4:
                x = x
            elif x == 4:
                handtype = ["順子"]
                ht = 5
                point_straight.append(total_point[i])
                pointtype = point_straight
                break
            elif (total_point[i+1]-total_point[i]) > 1:
                x = 0
                point_straight = []
        
        if (len(point_straight) == 4) and (x == 4):
            handtype = ["順子"]
            ht = 5
            point_straight.append(total_point[-1])
            pointtype = point_straight
        if straight.issubset(pt):
            handtype = ["順子"]
            ht = 5
            point_straight = [10,11,12,13,1]
            pointtype = point_straight

        #check Flush
        if (handtype != ["鐵支"]) or (handtype != ["葫蘆"]):
            total_p = p + b

            total_flush = list(range(len(total_p)))
            for i in range(len(total_p)):
                total_flush[i] = total_p[i][1]

            flush_counter = {}
            for i in total_flush:
                flush_counter[i] = flush_counter.get(i,0)+1

            if (5 in flush_counter.values()) or (6 in flush_counter.values()) or (7 in flush_counter.values()):
                handtype = ["同花"]
                ht = 6
                max_flush = max(flush_counter, key = flush_counter.get)

                pointtype = []
                for i in range(len(total_p)):
                    if total_p[i][1] == max_flush:
                        pointtype.append(total_p[i][0])
                pointtype.sort()
                
                #check Flush Straight
                point_straight = []
                
                x = 0
                for i in range(5):
                    if x == 4:
                        handtype = ["同花順"]
                        ht = 9
                    elif (pointtype[i+1]-pointtype[i]) == 1 and x < 4:      
                        x += 1
                    else:
                        break
                if pointtype == [1,10,11,12,13]:
                    handtype = ["同花順"]
                    ht = 9
                    pointtype = [10,11,12,13,1]

        if handtype == []:  #高牌(單張)
            pointtype = [max(point)]
            if 1 in point:
                pointtype = [1]
            handtype = ["高牌"]
            ht = 1

        return pointtype,ht

    poker = list(range(52))
    for i in range(52):
        color = i//13+1
        point = i%13+1
        poker[i] = (point,color)

    random.shuffle(poker)

    global playerA, playerA1, playerA2
    playerA = poker[:2]
    playerA.sort()
    playerA1 = poker[0]
    playerA2 = poker[1]

    global playerB, playerB1, playerB2
    playerB = poker[2:4]
    playerB.sort()
    playerB1 = poker[2]
    playerB2 = poker[3]

    global board, board1, board2, board3, board4, board5
    board = poker[4:9]
    board1 = poker[4]
    board2 = poker[5]
    board3 = poker[6]
    board4 = poker[7]
    board5 = poker[8]

    playerA_point = POINT(playerA)
    playerB_point = POINT(playerB)
    board_point = POINT(board)

    #牌型判斷
    global A_point, A_ht
    A_point,A_ht = PC(playerA_point,board_point,playerA,board)

    global B_point, B_ht
    B_point,B_ht = PC(playerB_point,board_point,playerB,board)

    # 比較大小，判斷輸贏
    def whoWin(A_ht,B_ht,A_point,B_point):

        flag = 0

        if A_ht > B_ht:
            flag = 0  # 0代表A獲勝
        elif A_ht < B_ht:
            flag = 1  # 1代表B獲勝
        else:
            if A_ht == 1:   #高牌
                if ((A_point[0] > B_point[0]) and (B_point[0] != 1)) or ((A_point[0] == 1) and (B_point[0] != 1)):
                    flag = 0
                elif ((A_point[0] < B_point[0]) and (A_point[0] != 1)) or ((B_point[0] == 1) and (A_point[0] != 1)):
                    flag = 1
                else:
                    if playerA[0][1] < playerB[0][1]:
                        flag = 0
                    else:
                        flag = 1

            elif A_ht == 2:  #一對
                if ((A_point[0] > B_point[0]) and (B_point[0] != 1)) or ((A_point[0] == 1) and (B_point[0] != 1)):
                    flag = 0
                elif ((A_point[0] < B_point[0]) and (A_point[0] != 1)) or ((B_point[0] == 1) and (A_point[0] != 1)):
                    flag = 1
                else:
                    if ((playerA[1][0] > playerB[1][0]) and (playerB[1][0] != 1)) or ((playerA[1][0] == 1) and (playerB[1][0] != 1)):
                        flag = 0
                    elif ((playerA[1][0] < playerB[1][0]) and (playerA[1][0] != 1)) or ((playerB[1][0] == 1) and (playerA[1][0] != 1)):
                        flag = 1
                    else:
                        if playerA[1][1] < playerB[1][1]:
                            flag = 0
                        else:
                            flag = 1

            elif A_ht == 3:  #兩對
                if ((A_point[-1] > B_point[-1]) and (B_point[-1] != 1)) or ((A_point[-1] == 1) and (B_point[-1] != 1)):
                    flag = 0
                elif ((A_point[-1] < B_point[-1]) and (A_point[-1] != 1)) or ((B_point[-1] == 1) and (A_point[-1] != 1)):
                    flag = 1
                else:
                    if ((A_point[0] > B_point[0]) and (B_point[0] != 1)) or ((A_point[0] == 1) and (B_point[0] != 1)):
                        flag = 0
                    elif ((A_point[0] < B_point[0]) and (A_point[0] != 1)) or ((B_point[0] == 1) and (A_point[0] != 1)):
                        flag = 1
                    else:
                        if ((playerA[1][0] > playerB[1][0]) and (playerB[1][0] != 1)) or ((playerA[1][0] == 1) and (playerB[1][0] != 1)):
                            flag = 0
                        elif ((playerA[1][0] < playerB[1][0]) and (playerA[1][0] != 1)) or ((playerB[1][0] == 1) and (playerA[1][0] != 1)):
                            flag = 1
                        else:
                            if playerA[1][1] < playerB[1][1]:
                                flag = 0
                            else:
                                flag = 1

            elif 3 < A_ht < 6:  #三條、順子
                if ((A_point[-1] > B_point[-1]) and (B_point[-1] != 1)) or ((A_point[-1] == 1) and (B_point[-1] != 1)):
                    flag = 0
                elif ((A_point[-1] < B_point[-1]) and (A_point[-1] != 1)) or ((B_point[-1] == 1) and (A_point[-1] != 1)):
                    flag = 1
                else:
                    if A_point == B_point:
                        if ((playerA[1][0] > playerB[1][0]) and (playerB[1][0] != 1)) or ((playerA[1][0] == 1) and (playerB[1][0] != 1)):
                            flag = 0
                        elif ((playerA[1][0] < playerB[1][0]) and (playerA[1][0] != 1)) or ((playerB[1][0] == 1) and (playerA[1][0] != 1)):
                            flag = 1
                        else:
                            if playerA[1][1] < playerB[1][1]:
                                flag = 0
                            else:
                                flag = 1

            elif 6 < A_ht < 9:  #葫蘆、鐵支
                if ((A_point[0] > B_point[0]) and (B_point[0] != 1)) or ((A_point[0] == 1) and (B_point[0] != 1)):
                    flag = 0
                elif ((A_point[0] < B_point[0]) and (A_point[0] != 1)) or ((B_point[0] == 1) and (A_point[0] != 1)):
                    flag = 1
                else:
                    if ((A_point[-1] > B_point[-1]) and (B_point[-1] != 1)) or ((A_point[-1] == 1) and (B_point[-1] != 1)):
                        flag = 0
                    elif ((A_point[-1] < B_point[-1]) and (A_point[-1] != 1)) or ((B_point[-1] == 1) and (A_point[-1] != 1)):
                        flag = 1
                    else:
                        if ((playerA[1][0] > playerB[1][0]) and (playerB[1][0] != 1)) or ((playerA[1][0] == 1) and (playerB[1][0] != 1)):
                            flag = 0
                        elif ((playerA[1][0] < playerB[1][0]) and (playerA[1][0] != 1)) or ((playerB[1][0] == 1) and (playerA[1][0] != 1)):
                            flag = 1
                        else:
                            if playerA[1][1] < playerB[1][1]:
                                flag = 0
                            else:
                                flag = 1

            elif A_ht == 6:  #同花
                if ((playerA[1][0] > playerB[1][0]) and (playerB[1][0] != 1)) or ((playerA[1][0] == 1) and (playerB[1][0] != 1)):
                    flag = 0
                elif ((playerA[1][0] < playerB[1][0]) and (playerA[1][0] != 1)) or ((playerB[1][0] == 1) and (playerA[1][0] != 1)):
                    flag = 1
                else:
                    if playerA[1][1] < playerB[1][1]:
                        flag = 0
                    else:
                        flag = 1

            elif A_ht == 9:  #同花順
                if ((A_point[-1] > B_point[-1]) and (B_point[-1] != 1)) or ((A_point[-1] == 1) and (B_point[-1] != 1)):
                    flag = 0
                elif ((A_point[-1] < B_point[-1]) and (A_point[-1] != 1)) or ((B_point[-1] == 1) and (A_point[-1] != 1)):
                    flag = 1
        return flag

# 德州撲克牌遊戲畫面
class texasGame():
    def __init__(self,master):
        self.master = master
        self.master.config(bg='#EFEFEF')
        self.texasGame = tk.Frame(self.master,)
        self.texasGame.pack()

        global moneyA, moneyB, chipA, chipB
        chipA = 0
        chipB = 0

        pubLabel = tk.Label(self.texasGame, text = '\n公牌', font = 'Arial -30', fg = 'black')
        pubLabel.config(bg='#EFEFEF')
        pubLabel.grid(row = 0, column = 5, pady = 10)

        gameState = tk.Label(self.texasGame, text = '\n玩家👻請下注', font = 'Arial -28', fg = '#52387B')
        gameState.config(bg='#EFEFEF')
        gameState.grid(row = 6, column = 0, columnspan = 11)

        #global public1, public2, public3, b4public4, public5
        public1 = tk.Button(self.texasGame)
        public1.config(bg='white',text = '      \n      ', font = 'Arial -26', fg='black')
        public1.grid(row = 1, column = 3, padx = 10, pady=40)

        public2 = tk.Button(self.texasGame)
        public2.config(bg='white',text = '      \n      ', font = 'Arial -26', fg='#EFEFEF')
        public2.grid(row = 1, column = 4, padx = 10, pady=40)

        public3 = tk.Button(self.texasGame)
        public3.config(bg='white',text = '      \n      ', font = 'Arial -26', fg='#EFEFEF')
        public3.grid(row = 1, column = 5, padx = 10, pady=40)

        public4 = tk.Button(self.texasGame)
        public4.config(bg='white',text = '      \n      ', font = 'Arial -26', fg='#EFEFEF')
        public4.grid(row = 1, column = 6, padx = 10, pady=40)

        public5 = tk.Button(self.texasGame)
        public5.config(bg='white',text = '      \n      ', font = 'Arial -26', fg='#EFEFEF')
        public5.grid(row = 1, column = 7, padx = 10, pady=40)

        nameA = tk.Label(self.texasGame, text = '玩家👻', font = 'Arial -28', fg = '#000276')
        nameA.config(bg='#EFEFEF')
        nameA.grid(row = 2, column = 0, columnspan = 2, pady = 10)

        global moneyA_name
        moneyA_name = tk.Label(self.texasGame, text = ' $' + str(moneyA) + ' ', font = 'Arial -24', fg = 'black')
        moneyA_name.config(bg='#FFFF83')
        moneyA_name.grid(row = 2, column = 2, pady = 10)        

        betA = tk.Button(self.texasGame)
        betA.config(bg='#FCFFDF',text = '下注', font = 'Arial -22', fg='black', command = self.clickBetA)
        betA.grid(row = 3, column = 4, padx = 10)

        ac10 = tk.Button(self.texasGame, text = ' $10 ', font = 'Arial -18', fg = 'black', command = self.clickAC10)
        ac10.config(bg='#B7F2FF')
        ac10.grid(row = 3, column = 0, padx=5, pady=10)

        ac25 = tk.Button(self.texasGame, text = ' $25 ', font = 'Arial -18', fg = 'black', command = self.clickAC25)
        ac25.config(bg='#FFBAD7')
        ac25.grid(row = 3, column = 1, padx=5, pady=10)

        ac50 = tk.Button(self.texasGame, text = ' $50 ', font = 'Arial -18', fg = 'white', command = self.clickAC50)
        ac50.config(bg='#003C76')
        ac50.grid(row = 3, column = 2, padx=5, pady=10)

        ac100 = tk.Button(self.texasGame, text = ' $100 ', font = 'Arial -18', fg = 'white', command = self.clickAC100)
        ac100.config(bg='black')
        ac100.grid(row = 3, column = 3, padx=5, pady=10)

        finishA = tk.Button(self.texasGame, state = tk.DISABLED)
        finishA.config(bg='white', text = '完成', font = 'Arial -20', fg = 'black', command = self.clickFinishA)
        finishA.grid(row = 2, column = 4, padx=5, pady=10)

        global A1, A2, A3, A4, A5
        A1 = tk.Label(self.texasGame)
        A1.config(bg='white',text = '       \n       ', font = 'Arial -26', fg='black')
        A1.grid(row = 4, column = 0, padx = 10)

        A2 = tk.Label(self.texasGame)
        A2.config(bg='white',text = '       \n       ', font = 'Arial -26', fg='black')
        A2.grid(row = 4, column = 1, padx = 10)

        A3 = tk.Label(self.texasGame)
        A3.config(bg='white',text = '       \n       ', font = 'Arial -26', fg='black')
        A3.grid(row = 4, column = 2, padx = 10)

        A4 = tk.Label(self.texasGame)
        A4.config(bg='white',text = '       \n       ', font = 'Arial -26', fg='black')
        A4.grid(row = 4, column = 3, padx = 10)

        A5 = tk.Label(self.texasGame)
        A5.config(bg='white',text = '       \n       ', font = 'Arial -26', fg='black')
        A5.grid(row = 4, column = 4, padx = 10)

        cardNameA = tk.Label(self.texasGame)
        cardNameA.config(bg='#EFEFEF',text = ' 手 \n 牌 ', font = 'Arial -26', fg='black')
        cardNameA.grid(row = 5, column = 0, padx = 10)

        global aCard1, aCard2
        aCard1 = tk.Button(self.texasGame)
        aCard1.config(bg='white',text = '    \n    ', font = 'Arial -26', fg='#EFEFEF')
        aCard1.grid(row = 5, column = 1, padx = 10, pady=10)

        aCard2 = tk.Button(self.texasGame)
        aCard2.config(bg='white',text = '    \n    ', font = 'Arial -26', fg='#EFEFEF')
        aCard2.grid(row = 5, column = 2, padx = 10, pady=10) 

        nameB = tk.Label(self.texasGame, text = '玩家🎃', font = 'Arial -28', fg = '#000276')
        nameB.config(bg='#EFEFEF')
        nameB.grid(row = 2, column = 6, columnspan = 2, pady = 10)

        moneyB_name = tk.Label(self.texasGame, text = ' $' + str(moneyB) + ' ', font = 'Arial -24', fg = 'black')
        moneyB_name.config(bg='#FFFF83')
        moneyB_name.grid(row = 2, column = 8, pady = 10)

        betB = tk.Button(self.texasGame, state = tk.DISABLED)
        betB.config(bg='#FCFFDF',text = '下注', font = 'Arial -22', fg='black')
        betB.grid(row = 3, column = 10, padx = 10)

        bc10 = tk.Button(self.texasGame, state = tk.DISABLED)
        bc10.config(bg='#B7F2FF', text = ' $10 ', font = 'Arial -18', fg = 'black', command = self.clickBC10)
        bc10.grid(row = 3, column = 6, padx=5, pady=10)

        bc25 = tk.Button(self.texasGame, state = tk.DISABLED)
        bc25.config(bg='#FFBAD7', text = ' $25 ', font = 'Arial -18', fg = 'black', command = self.clickBC25)
        bc25.grid(row = 3, column = 7, padx=5, pady=10)

        bc50 = tk.Button(self.texasGame, state = tk.DISABLED)
        bc50.config(bg='#003C76', text = ' $50 ', font = 'Arial -18', fg = 'white', command = self.clickBC50)
        bc50.grid(row = 3, column = 8, padx=5, pady=10)

        bc100 = tk.Button(self.texasGame, state = tk.DISABLED)
        bc100.config(bg='black', text = ' $100 ', font = 'Arial -18', fg = 'white', command = self.clickBC100)
        bc100.grid(row = 3, column = 9, padx=5, pady=10)

        global a1,a2,a3,a4,a5
        finishB = tk.Button(self.texasGame, state = tk.DISABLED)
        finishB.config(bg='white', text = '完成', font = 'Arial -20', fg = 'black')
        finishB.grid(row = 2, column = 10, padx=5, pady=10)

        global B1, B2, B3, B4, B5
        B1 = tk.Label(self.texasGame)
        B1.config(bg='white',text = '       \n       ', font = 'Arial -26', fg='black')
        B1.grid(row = 4, column = 6, padx = 10)

        B2 = tk.Label(self.texasGame)
        B2.config(bg='white',text = '       \n       ', font = 'Arial -26', fg='black')
        B2.grid(row = 4, column = 7, padx = 10)

        B3 = tk.Label(self.texasGame)
        B3.config(bg='white',text = '       \n       ', font = 'Arial -26', fg='black')
        B3.grid(row = 4, column = 8, padx = 10)

        B4 = tk.Label(self.texasGame)
        B4.config(bg='white',text = '       \n       ', font = 'Arial -26', fg='black')
        B4.grid(row = 4, column = 9, padx = 10)

        B5 = tk.Label(self.texasGame)
        B5.config(bg='white',text = '       \n       ', font = 'Arial -26', fg='black')
        B5.grid(row = 4, column = 10, padx = 10)

        cardNameB = tk.Label(self.texasGame)
        cardNameB.config(bg='#EFEFEF',text = ' 手 \n 牌 ', font = 'Arial -26', fg='black')
        cardNameB.grid(row = 5, column = 6, padx = 10)

        bCard1 = tk.Button(self.texasGame, state = tk.DISABLED)
        bCard1.config(bg='white',text = '      \n      ', font = 'Arial -26', fg='#EFEFEF')
        bCard1.grid(row = 5, column = 7, padx = 10, pady=10)

        bCard2 = tk.Button(self.texasGame, state = tk.DISABLED)
        bCard2.config(bg='white',text = '      \n      ', font = 'Arial -26', fg='#EFEFEF')
        bCard2.grid(row = 5, column = 8, padx = 10, pady=10)

        global totalChipA, totalChipB
        totalChipA = tk.Label(self.texasGame)
        totalChipA.config(bg='#EAFFB6', text = ' 下注金額  \n  $???  ', font = 'Arial -24', fg='black')
        totalChipA.grid(row = 5, column = 3, columnspan = 2, padx = 10)

        totalChipB = tk.Label(self.texasGame)
        totalChipB.config(bg='#EAFFB6', text = ' 下注金額  \n  $???  ', font = 'Arial -24', fg='black')
        totalChipB.grid(row = 5, column = 9, columnspan = 2, padx = 10)

        global textA1, textA2, textB1, textB2, textP1, textP2, textP3, textP4, textP5

        textA1 =  texasPoker.strColor(playerA1) + '\n' + texasPoker.strPoint(playerA1)
        aCard1 = tk.Button(self.texasGame, state = tk.DISABLED)
        aCard1.config(bg='white',text = textA1, font = 'Arial -26', fg='black', command = self.clickAcard1)
        aCard1.grid(row = 5, column = 1, padx = 10, pady=10)

        textA2 = texasPoker.strColor(playerA2) + '\n' + texasPoker.strPoint(playerA2)
        aCard2 = tk.Button(self.texasGame, state = tk.DISABLED)
        aCard2.config(bg='white',text = textA2, font = 'Arial -26', fg='black', command = self.clickAcard2)
        aCard2.grid(row = 5, column = 2, padx = 10, pady=10)

        textB1 = texasPoker.strColor(playerB1) + '\n' + texasPoker.strPoint(playerB1)
        bCard1 = tk.Button(self.texasGame, state = tk.DISABLED)
        bCard1.config(bg='white',text = textB1, font = 'Arial -26', fg='white', command = self.clickBcard1)
        #bCard1.grid(row = 5, column = 7, padx = 10, pady=40)

        textB2 = texasPoker.strColor(playerB2) + '\n' + texasPoker.strPoint(playerB2)
        bCard2 = tk.Button(self.texasGame, state = tk.DISABLED)
        bCard2.config(bg='white',text = textB2, font = 'Arial -26', fg='white', command = self.clickBcard2)
        #bCard2.grid(row = 5, column = 8, padx = 10, pady=40)

        textP1 =  texasPoker.strColor(board1) + '\n' + texasPoker.strPoint(board1)
        public1 = tk.Button(self.texasGame, state = tk.DISABLED)
        public1.config(bg='white',text = textP1, font = 'Arial -26', fg='black', command = self.clickPublic1)
        public1.grid(row = 1, column = 3, padx = 10, pady=40)

    global count 
    count = 0
    global a1,a2,a3,a4,a5
    a1 = a2 = a3 = a4 = a5 = 0
    def clickPublic1(self,):
        global a1,a2,a3,a4,a5
        global A1, A2, A3, A4, A5
        public1 = tk.Button(self.texasGame, state = tk.DISABLED)
        public1.config(bg='white',text = textP1, font = 'Arial -26', fg='black', command = self.clickPublic1)
        public1.grid(row = 1, column = 3, padx = 10, pady=40)
       
        global count
        if count == 0:
            A1.config(bg='white',text = textP1, font = 'Arial -26', fg='black')
            A1.grid(row = 4, column = 0, padx = 10)
            a1 = 1
        elif count == 1:
            A2.config(bg='white',text = textP1, font = 'Arial -26', fg='black')
            A2.grid(row = 4, column = 1, padx = 10)
            a2 = 1
        elif count == 2:
            A3.config(bg='white',text = textP1, font = 'Arial -26', fg='black')
            A3.grid(row = 4, column = 2, padx = 10)
            a3 = 1
        elif count == 3:
            A4.config(bg='white',text = textP1, font = 'Arial -26', fg='black')
            A4.grid(row = 4, column = 3, padx = 10)
            a4 = 1
        elif count == 4:
            A5.config(bg='white',text = textP1, font = 'Arial -26', fg='black')
            A5.grid(row = 4, column = 4, padx = 10)
            a5 = 1
        
        elif count == 10:
            B1.config(bg='white',text = textP1, font = 'Arial -26', fg='black')
            B1.grid(row = 4, column = 6, padx = 10)
        elif count == 11:
            B2.config(bg='white',text = textP1, font = 'Arial -26', fg='black')
            B2.grid(row = 4, column = 7, padx = 10)
        elif count == 12:
            B3.config(bg='white',text = textP1, font = 'Arial -26', fg='black')
            B3.grid(row = 4, column = 8, padx = 10)
        elif count == 13:
            B4.config(bg='white',text = textP1, font = 'Arial -26', fg='black')
            B4.grid(row = 4, column = 9, padx = 10)
        elif count == 14:
            B5.config(bg='white',text = textP1, font = 'Arial -26', fg='black')
            B5.grid(row = 4, column = 10, padx = 10)

        count = count + 1
    
    def clickPublic2(self,):
        global a1,a2,a3,a4,a5
        global A1, A2, A3, A4, A5
        public2 = tk.Button(self.texasGame, state = tk.DISABLED)
        public2.config(bg='white',text = textP2, font = 'Arial -26', fg='black', command = self.clickPublic1)
        public2.grid(row = 1, column = 4, padx = 10, pady=40)

        global count
        if count == 0:
            A1.config(bg='white',text = textP2, font = 'Arial -26', fg='black')
            A1.grid(row = 4, column = 0, padx = 10)
            a1 = 2
        elif count == 1:
            A2.config(bg='white',text = textP2, font = 'Arial -26', fg='black')
            A2.grid(row = 4, column = 1, padx = 10)
            a2 = 2
        elif count == 2:
            A3.config(bg='white',text = textP2, font = 'Arial -26', fg='black')
            A3.grid(row = 4, column = 2, padx = 10)
            a3 = 2
        elif count == 3:
            A4.config(bg='white',text = textP2, font = 'Arial -26', fg='black')
            A4.grid(row = 4, column = 3, padx = 10)
            a4 = 2
        elif count == 4:
            A5.config(bg='white',text = textP2, font = 'Arial -26', fg='black')
            A5.grid(row = 4, column = 4, padx = 10)
            a5 = 2

        elif count == 10:
            B1.config(bg='white',text = textP2, font = 'Arial -26', fg='black')
            B1.grid(row = 4, column = 6, padx = 10)
        elif count == 11:
            B2.config(bg='white',text = textP2, font = 'Arial -26', fg='black')
            B2.grid(row = 4, column = 7, padx = 10)
        elif count == 12:
            B3.config(bg='white',text = textP2, font = 'Arial -26', fg='black')
            B3.grid(row = 4, column = 8, padx = 10)
        elif count == 13:
            B4.config(bg='white',text = textP2, font = 'Arial -26', fg='black')
            B4.grid(row = 4, column = 9, padx = 10)
        elif count == 14:
            B5.config(bg='white',text = textP2, font = 'Arial -26', fg='black')
            B5.grid(row = 4, column = 10, padx = 10)
        count = count + 1

    def clickPublic3(self,):
        global a1,a2,a3,a4,a5
        global A1, A2, A3, A4, A5
        public3 = tk.Button(self.texasGame, state = tk.DISABLED)
        public3.config(bg='white',text = textP3, font = 'Arial -26', fg='black', command = self.clickPublic3)
        public3.grid(row = 1, column = 5, padx = 10, pady=40)

        global count
        if count == 0:
            A1.config(bg='white',text = textP3, font = 'Arial -26', fg='black')
            A1.grid(row = 4, column = 0, padx = 10)
            a1 = 3
        elif count == 1:
            A2.config(bg='white',text = textP3, font = 'Arial -26', fg='black')
            A2.grid(row = 4, column = 1, padx = 10)
            a2 = 3
        elif count == 2:
            A3.config(bg='white',text = textP3, font = 'Arial -26', fg='black')
            A3.grid(row = 4, column = 2, padx = 10)
            a3 = 3
        elif count == 3:
            A4.config(bg='white',text = textP3, font = 'Arial -26', fg='black')
            A4.grid(row = 4, column = 3, padx = 10)
            a4 = 3
        elif count == 4:
            A5.config(bg='white',text = textP3, font = 'Arial -26', fg='black')
            A5.grid(row = 4, column = 4, padx = 10)
            a5 = 3

        elif count == 10:
            B1.config(bg='white',text = textP3, font = 'Arial -26', fg='black')
            B1.grid(row = 4, column = 6, padx = 10)
        elif count == 11:
            B2.config(bg='white',text = textP3, font = 'Arial -26', fg='black')
            B2.grid(row = 4, column = 7, padx = 10)
        elif count == 12:
            B3.config(bg='white',text = textP3, font = 'Arial -26', fg='black')
            B3.grid(row = 4, column = 8, padx = 10)
        elif count == 13:
            B4.config(bg='white',text = textP3, font = 'Arial -26', fg='black')
            B4.grid(row = 4, column = 9, padx = 10)
        elif count == 14:
            B5.config(bg='white',text = textP3, font = 'Arial -26', fg='black')
            B5.grid(row = 4, column = 10, padx = 10)

        count = count + 1

    def clickPublic4(self,):
        global a1,a2,a3,a4,a5
        global A1, A2, A3, A4, A5
        public4 = tk.Button(self.texasGame, state = tk.DISABLED)
        public4.config(bg='white',text = textP4, font = 'Arial -26', fg='black', command = self.clickPublic4)
        public4.grid(row = 1, column = 6, padx = 10, pady=40)

        global count
        if count == 0:
            A1.config(bg='white',text = textP4, font = 'Arial -26', fg='black')
            A1.grid(row = 4, column = 0, padx = 10)
            a1 = 4
        elif count == 1:
            A2.config(bg='white',text = textP4, font = 'Arial -26', fg='black')
            A2.grid(row = 4, column = 1, padx = 10)
            a2 = 4
        elif count == 2:
            A3.config(bg='white',text = textP4, font = 'Arial -26', fg='black')
            A3.grid(row = 4, column = 2, padx = 10)
            a3 = 4
        elif count == 3:
            A4.config(bg='white',text = textP4, font = 'Arial -26', fg='black')
            A4.grid(row = 4, column = 3, padx = 10)
            a4 = 4
        elif count == 4:
            A5.config(bg='white',text = textP4, font = 'Arial -26', fg='black')
            A5.grid(row = 4, column = 4, padx = 10)
            a5 = 4

        elif count == 10:
            B1.config(bg='white',text = textP4, font = 'Arial -26', fg='black')
            B1.grid(row = 4, column = 6, padx = 10)
        elif count == 11:
            B2.config(bg='white',text = textP4, font = 'Arial -26', fg='black')
            B2.grid(row = 4, column = 7, padx = 10)
        elif count == 12:
            B3.config(bg='white',text = textP4, font = 'Arial -26', fg='black')
            B3.grid(row = 4, column = 8, padx = 10)
        elif count == 13:
            B4.config(bg='white',text = textP4, font = 'Arial -26', fg='black')
            B4.grid(row = 4, column = 9, padx = 10)
        elif count == 14:
            B5.config(bg='white',text = textP4, font = 'Arial -26', fg='black')
            B5.grid(row = 4, column = 10, padx = 10)

        count = count + 1

    def clickPublic5(self,):
        global a1,a2,a3,a4,a5
        global A1, A2, A3, A4, A5
        public5 = tk.Button(self.texasGame, state = tk.DISABLED)
        public5.config(bg='white',text = textP5, font = 'Arial -26', fg='black', command = self.clickPublic5)
        public5.grid(row = 1, column = 7, padx = 10, pady=40)

        global count
        if count == 0:
            A1.config(bg='white',text = textP5, font = 'Arial -26', fg='black')
            A1.grid(row = 4, column = 0, padx = 10)
            a1 = 5
        elif count == 1:
            A2.config(bg='white',text = textP5, font = 'Arial -26', fg='black')
            A2.grid(row = 4, column = 1, padx = 10)
            a2 = 5
        elif count == 2:
            A3.config(bg='white',text = textP5, font = 'Arial -26', fg='black')
            A3.grid(row = 4, column = 2, padx = 10)
            a3 = 5
        elif count == 3:
            A4.config(bg='white',text = textP5, font = 'Arial -26', fg='black')
            A4.grid(row = 4, column = 3, padx = 10)
            a4 = 5
        elif count == 4:
            A5.config(bg='white',text = textP5, font = 'Arial -26', fg='black')
            A5.grid(row = 4, column = 4, padx = 10)
            a5 = 5

        elif count == 10:
            B1.config(bg='white',text = textP5, font = 'Arial -26', fg='black')
            B1.grid(row = 4, column = 6, padx = 10)
        elif count == 11:
            B2.config(bg='white',text = textP5, font = 'Arial -26', fg='black')
            B2.grid(row = 4, column = 7, padx = 10)
        elif count == 12:
            B3.config(bg='white',text = textP5, font = 'Arial -26', fg='black')
            B3.grid(row = 4, column = 8, padx = 10)
        elif count == 13:
            B4.config(bg='white',text = textP5, font = 'Arial -26', fg='black')
            B4.grid(row = 4, column = 9, padx = 10)
        elif count == 14:
            B5.config(bg='white',text = textP5, font = 'Arial -26', fg='black')
            B5.grid(row = 4, column = 10, padx = 10)

        count = count + 1          

    def clickAcard1(self,):
        global A1, A2, A3, A4, A5
        global a1,a2,a3,a4,a5

        aCard1 = tk.Button(self.texasGame, state = tk.DISABLED)
        aCard1.config(bg='white',text = textA1, font = 'Arial -26', fg='#EFEFEF')
        aCard1.grid(row = 5, column = 1, padx = 10, pady=10)

        global count
        if count == 0:
            A1.config(bg='white',text = textA1, font = 'Arial -26', fg='black')
            A1.grid(row = 4, column = 0, padx = 10)
            a1 = 6
        elif count == 1:
            A2.config(bg='white',text = textA1, font = 'Arial -26', fg='black')
            A2.grid(row = 4, column = 1, padx = 10)
            a2 = 6
        elif count == 2:
            A3.config(bg='white',text = textA1, font = 'Arial -26', fg='black')
            A3.grid(row = 4, column = 2, padx = 10)
            a3 = 6
        elif count == 3:
            A4.config(bg='white',text = textA1, font = 'Arial -26', fg='black')
            A4.grid(row = 4, column = 3, padx = 10)
            a4 = 6
        elif count == 4:
            A5.config(bg='white',text = textA1, font = 'Arial -26', fg='black')
            A5.grid(row = 4, column = 4, padx = 10)
            a5 = 6

        count = count + 1

    def clickAcard2(self,):
        global A1, A2, A3, A4, A5
        global a1,a2,a3,a4,a5

        aCard2 = tk.Button(self.texasGame, state = tk.DISABLED)
        aCard2.config(bg='white',text = textA2, font = 'Arial -26', fg='#EFEFEF')
        aCard2.grid(row = 5, column = 2, padx = 10, pady=10)
        
        global count
        if count == 0:
            A1.config(bg='white',text = textA2, font = 'Arial -26', fg='black')
            A1.grid(row = 4, column = 0, padx = 10)
            a1 = 7
        elif count == 1:
            A2.config(bg='white',text = textA2, font = 'Arial -26', fg='black')
            A2.grid(row = 4, column = 1, padx = 10)
            a2 = 7
        elif count == 2:
            A3.config(bg='white',text = textA2, font = 'Arial -26', fg='black')
            A3.grid(row = 4, column = 2, padx = 10)
            a3 = 7
        elif count == 3:
            A4.config(bg='white',text = textA2, font = 'Arial -26', fg='black')
            A4.grid(row = 4, column = 3, padx = 10)
            a4 = 7
        elif count == 4:
            A5.config(bg='white',text = textA2, font = 'Arial -26', fg='black')
            A5.grid(row = 4, column = 4, padx = 10)
            a5 = 7
        count = count + 1
        
    def clickBcard1(self,):
        bCard1 = tk.Button(self.texasGame, state = tk.DISABLED)
        bCard1.config(bg='white',text = textB1, font = 'Arial -26', fg='#EFEFEF')
        bCard1.grid(row = 5, column = 7, padx = 10, pady=10)

        global count
        if count == 10:
            B1.config(bg='white',text = textB1, font = 'Arial -26', fg='black')
            B1.grid(row = 4, column = 6, padx = 10)
        elif count == 11:
            B2.config(bg='white',text = textB1, font = 'Arial -26', fg='black')
            B2.grid(row = 4, column = 7, padx = 10)
        elif count == 12:
            B3.config(bg='white',text = textB1, font = 'Arial -26', fg='black')
            B3.grid(row = 4, column = 8, padx = 10)
        elif count == 13:
            B4.config(bg='white',text = textB1, font = 'Arial -26', fg='black')
            B4.grid(row = 4, column = 9, padx = 10)
        elif count == 14:
            B5.config(bg='white',text = textB1, font = 'Arial -26', fg='black')
            B5.grid(row = 4, column = 10, padx = 10)
        count = count + 1

    def clickBcard2(self,):
        bCard2 = tk.Button(self.texasGame, state = tk.DISABLED)
        bCard2.config(bg='white',text = textB2, font = 'Arial -26', fg='#EFEFEF')
        bCard2.grid(row = 5, column = 8, padx = 10, pady=10)

        global count
        if count == 10:
            B1.config(bg='white',text = textB2, font = 'Arial -26', fg='black')
            B1.grid(row = 4, column = 6, padx = 10)
        elif count == 11:
            B2.config(bg='white',text = textB2, font = 'Arial -26', fg='black')
            B2.grid(row = 4, column = 7, padx = 10)
        elif count == 12:
            B3.config(bg='white',text = textB2, font = 'Arial -26', fg='black')
            B3.grid(row = 4, column = 8, padx = 10)
        elif count == 13:
            B4.config(bg='white',text = textB2, font = 'Arial -26', fg='black')
            B4.grid(row = 4, column = 9, padx = 10)
        elif count == 14:
            B5.config(bg='white',text = textB2, font = 'Arial -26', fg='black')
            B5.grid(row = 4, column = 10, padx = 10)
        count = count + 1

    def clickAC10(self,):
        global moneyA, chipA
        moneyA = moneyA - 10
        chipA = chipA + 10

        global moneyA_name
        moneyA_name = tk.Label(self.texasGame, text = ' $' + str(moneyA) + ' ', font = 'Arial -24', fg = 'black')
        moneyA_name.config(bg='#FFFF83')
        moneyA_name.grid(row = 2, column = 2, pady = 10)

        totalChipA.config(bg='#EAFFB6', text = ' 下注金額  \n  $' + str(chipA) + ' ', font = 'Arial -24', fg='black')
        totalChipA.grid(row = 5, column = 3, columnspan = 2, padx = 10)
    
    def clickAC25(self,):
        global moneyA, chipA
        moneyA = moneyA - 25
        chipA = chipA + 25

        global moneyA_name
        moneyA_name = tk.Label(self.texasGame, text = ' $' + str(moneyA) + ' ', font = 'Arial -24', fg = 'black')
        moneyA_name.config(bg='#FFFF83')
        moneyA_name.grid(row = 2, column = 2, pady = 10)

        totalChipA.config(bg='#EAFFB6', text = ' 下注金額  \n  $' + str(chipA) + ' ', font = 'Arial -24', fg='black')
        totalChipA.grid(row = 5, column = 3, columnspan = 2, padx = 10)

    def clickAC50(self,):
        global moneyA, chipA
        moneyA = moneyA - 50
        chipA = chipA + 50

        global moneyA_name
        moneyA_name = tk.Label(self.texasGame, text = ' $' + str(moneyA) + ' ', font = 'Arial -24', fg = 'black')
        moneyA_name.config(bg='#FFFF83')
        moneyA_name.grid(row = 2, column = 2, pady = 10)

        totalChipA.config(bg='#EAFFB6', text = ' 下注金額  \n  $' + str(chipA) + ' ', font = 'Arial -24', fg='black')
        totalChipA.grid(row = 5, column = 3, columnspan = 2, padx = 10)

    def clickAC100(self,):
        global moneyA, chipA
        moneyA = moneyA - 100
        chipA = chipA + 100

        global moneyA_name
        moneyA_name = tk.Label(self.texasGame, text = ' $' + str(moneyA) + ' ', font = 'Arial -24', fg = 'black')
        moneyA_name.config(bg='#FFFF83')
        moneyA_name.grid(row = 2, column = 2, pady = 10)

        totalChipA.config(bg='#EAFFB6', text = ' 下注金額  \n  $' + str(chipA) + ' ', font = 'Arial -24', fg='black')
        totalChipA.grid(row = 5, column = 3, columnspan = 2, padx = 10)

    def clickBC10(self,):
        global moneyB, chipB
        moneyB = moneyB - 10
        chipB = chipB + 10

        moneyB_name = tk.Label(self.texasGame, text = ' $' + str(moneyB) + ' ', font = 'Arial -24', fg = 'black')
        moneyB_name.config(bg='#FFFF83')
        moneyB_name.grid(row = 2, column = 8, pady = 10)

        totalChipB.config(bg='#EAFFB6', text = ' 下注金額  \n  $' + str(chipB) + ' ', font = 'Arial -24', fg='black')
        totalChipB.grid(row = 5, column = 9, columnspan = 2, padx = 10)

    def clickBC25(self,):
        global moneyB, chipB
        moneyB = moneyB - 25
        chipB = chipB + 25

        moneyB_name = tk.Label(self.texasGame, text = ' $' + str(moneyB) + ' ', font = 'Arial -24', fg = 'black')
        moneyB_name.config(bg='#FFFF83')
        moneyB_name.grid(row = 2, column = 8, pady = 10)

        totalChipB.config(bg='#EAFFB6', text = ' 下注金額  \n  $' + str(chipB) + ' ', font = 'Arial -24', fg='black')
        totalChipB.grid(row = 5, column = 9, columnspan = 2, padx = 10)

    def clickBC50(self,):
        global moneyB, chipB
        moneyB = moneyB - 50
        chipB = chipB + 50

        moneyB_name = tk.Label(self.texasGame, text = ' $' + str(moneyB) + ' ', font = 'Arial -24', fg = 'black')
        moneyB_name.config(bg='#FFFF83')
        moneyB_name.grid(row = 2, column = 8, pady = 10)

        totalChipB.config(bg='#EAFFB6', text = ' 下注金額  \n  $' + str(chipB) + ' ', font = 'Arial -24', fg='black')
        totalChipB.grid(row = 5, column = 9, columnspan = 2, padx = 10)

    def clickBC100(self,):
        global moneyB, chipB
        moneyB = moneyB - 100
        chipB = chipB + 100

        moneyB_name = tk.Label(self.texasGame, text = ' $' + str(moneyB) + ' ', font = 'Arial -24', fg = 'black')
        moneyB_name.config(bg='#FFFF83')
        moneyB_name.grid(row = 2, column = 8, pady = 10)

        totalChipB.config(bg='#EAFFB6', text = ' 下注金額  \n  $' + str(chipB) + ' ', font = 'Arial -24', fg='black')
        totalChipB.grid(row = 5, column = 9, columnspan = 2, padx = 10)
    
    global countBet
    countBet = 1
    def clickBetA(self,):
        #time.sleep(1)
        global countBet

        ac10 = tk.Button(self.texasGame, state = tk.DISABLED)
        ac10.config(bg='#B7F2FF', text = ' $10 ', font = 'Arial -18', fg = 'black', command = self.clickAC10)
        ac10.grid(row = 3, column = 0, padx=5, pady=10)

        ac25 = tk.Button(self.texasGame, state = tk.DISABLED)
        ac25.config(bg='#FFBAD7', text = ' $25 ', font = 'Arial -18', fg = 'black', command = self.clickAC25)
        ac25.grid(row = 3, column = 1, padx=5, pady=10)

        ac50 = tk.Button(self.texasGame, state = tk.DISABLED)
        ac50.config(bg='#003C76', text = ' $50 ', font = 'Arial -18', fg = 'white', command = self.clickAC50)
        ac50.grid(row = 3, column = 2, padx=5, pady=10)

        ac100 = tk.Button(self.texasGame, state = tk.DISABLED)
        ac100.config(bg='black', text = ' $100 ', font = 'Arial -18', fg = 'white', command = self.clickAC100)
        ac100.grid(row = 3, column = 3, padx=5, pady=10)

        betA = tk.Button(self.texasGame, state = tk.DISABLED)
        betA.config(bg='#FCFFDF',text = '下注', font = 'Arial -22', fg='black', command = self.clickBetA)
        betA.grid(row = 3, column = 4, padx = 10)

        aCard1 = tk.Button(self.texasGame, state = tk.DISABLED)
        aCard1.config(bg='white',text = '      \n      ', font = 'Arial -26', fg='#EFEFEF')
        aCard1.grid(row = 5, column = 1, padx = 10, pady=10)

        aCard2 = tk.Button(self.texasGame, state = tk.DISABLED)
        aCard2.config(bg='white',text = '      \n      ', font = 'Arial -26', fg='#EFEFEF')
        aCard2.grid(row = 5, column = 2, padx = 10, pady=10)

        bCard1 = tk.Button(self.texasGame, state = tk.DISABLED)
        bCard1.config(bg='white',text = textB1, font = 'Arial -26', fg='black', command = self.clickBcard1)
        bCard1.grid(row = 5, column = 7, padx = 10, pady=10)

        bCard2 = tk.Button(self.texasGame, state = tk.DISABLED)
        bCard2.config(bg='white',text = textB2, font = 'Arial -26', fg='black', command = self.clickBcard2)
        bCard2.grid(row = 5, column = 8, padx = 10, pady=10)

        betB = tk.Button(self.texasGame)
        betB.config(bg='#FCFFDF',text = '下注', font = 'Arial -22', fg='black', command = self.clickBetB)
        betB.grid(row = 3, column = 10, padx = 10)

        bc10 = tk.Button(self.texasGame)
        bc10.config(bg='#B7F2FF', text = ' $10 ', font = 'Arial -18', fg = 'black', command = self.clickBC10)
        bc10.grid(row = 3, column = 6, padx=5, pady=10)

        bc25 = tk.Button(self.texasGame)
        bc25.config(bg='#FFBAD7', text = ' $25 ', font = 'Arial -18', fg = 'black', command = self.clickBC25)
        bc25.grid(row = 3, column = 7, padx=5, pady=10)

        bc50 = tk.Button(self.texasGame)
        bc50.config(bg='#003C76', text = ' $50 ', font = 'Arial -18', fg = 'white', command = self.clickBC50)
        bc50.grid(row = 3, column = 8, padx=5, pady=10)

        bc100 = tk.Button(self.texasGame)
        bc100.config(bg='black', text = ' $100 ', font = 'Arial -18', fg = 'white', command = self.clickBC100)
        bc100.grid(row = 3, column = 9, padx=5, pady=10)

        gameState = tk.Label(self.texasGame, text = '\n玩家🎃請下注', font = 'Arial -28', fg = '#52387B')
        gameState.config(bg='#EFEFEF')
        gameState.grid(row = 6, column = 0, columnspan = 11)

    def clickBetB(self,):

        global countBet 
        global textP1, textP2, textP3, textP4, textP5, textA1, textA2, textB1, textB2
        if countBet == 1:
            countBet = countBet + 1
            textP2 =  texasPoker.strColor(board2) + '\n' + texasPoker.strPoint(board2)
            public2 = tk.Button(self.texasGame, state = tk.DISABLED)
            public2.config(bg='white',text = textP2, font = 'Arial -26', fg='black', command = self.clickPublic2)
            public2.grid(row = 1, column = 4, padx = 10, pady=40)

            bc10 = tk.Button(self.texasGame, state = tk.DISABLED)
            bc10.config(bg='#B7F2FF', text = ' $10 ', font = 'Arial -18', fg = 'black', command = self.clickBC10)
            bc10.grid(row = 3, column = 6, padx=5, pady=10)

            bc25 = tk.Button(self.texasGame, state = tk.DISABLED)
            bc25.config(bg='#FFBAD7', text = ' $25 ', font = 'Arial -18', fg = 'black', command = self.clickBC25)
            bc25.grid(row = 3, column = 7, padx=5, pady=10)

            bc50 = tk.Button(self.texasGame, state = tk.DISABLED)
            bc50.config(bg='#003C76', text = ' $50 ', font = 'Arial -18', fg = 'white', command = self.clickBC50)
            bc50.grid(row = 3, column = 8, padx=5, pady=10)

            bc100 = tk.Button(self.texasGame, state = tk.DISABLED)
            bc100.config(bg='black', text = ' $100 ', font = 'Arial -18', fg = 'white', command = self.clickBC100)
            bc100.grid(row = 3, column = 9, padx=5, pady=10)

            ac10 = tk.Button(self.texasGame)
            ac10.config(bg='#B7F2FF', text = ' $10 ', font = 'Arial -18', fg = 'black', command = self.clickAC10)
            ac10.grid(row = 3, column = 0, padx=5, pady=10)

            ac25 = tk.Button(self.texasGame)
            ac25.config(bg='#FFBAD7', text = ' $25 ', font = 'Arial -18', fg = 'black', command = self.clickAC25)
            ac25.grid(row = 3, column = 1, padx=5, pady=10)

            ac50 = tk.Button(self.texasGame)
            ac50.config(bg='#003C76', text = ' $50 ', font = 'Arial -18', fg = 'white', command = self.clickAC50)
            ac50.grid(row = 3, column = 2, padx=5, pady=10)

            ac100 = tk.Button(self.texasGame)
            ac100.config(bg='black', text = ' $100 ', font = 'Arial -18', fg = 'white', command = self.clickAC100)
            ac100.grid(row = 3, column = 3, padx=5, pady=10)

            betA = tk.Button(self.texasGame)
            betA.config(bg='#FCFFDF',text = '下注', font = 'Arial -22', fg='black', command = self.clickBetA)
            betA.grid(row = 3, column = 4, padx = 10)

            gameState = tk.Label(self.texasGame, text = '\n玩家👻請下注', font = 'Arial -28', fg = '#52387B')
            gameState.config(bg='#EFEFEF')
            gameState.grid(row = 6, column = 0, columnspan = 11)

            bCard1 = tk.Button(self.texasGame, state = tk.DISABLED)
            bCard1.config(bg='white',text = '      \n      ', font = 'Arial -26', fg='#EFEFEF')
            bCard1.grid(row = 5, column = 7, padx = 10, pady=10)

            bCard2 = tk.Button(self.texasGame, state = tk.DISABLED)
            bCard2.config(bg='white',text = '      \n      ', font = 'Arial -26', fg='#EFEFEF')
            bCard2.grid(row = 5, column = 8, padx = 10, pady=10)
            
            aCard1 = tk.Button(self.texasGame, state = tk.DISABLED)
            aCard1.config(bg='white',text = textA1, font = 'Arial -26', fg='black', command = self.clickAcard1)
            aCard1.grid(row = 5, column = 1, padx = 10, pady=10)

            aCard2 = tk.Button(self.texasGame, state = tk.DISABLED)
            aCard2.config(bg='white',text = textA2, font = 'Arial -26', fg='black', command = self.clickAcard2)
            aCard2.grid(row = 5, column = 2, padx = 10, pady=10)


        elif countBet == 2:
            countBet = countBet + 1
            textP3 =  texasPoker.strColor(board3) + '\n' + texasPoker.strPoint(board3)
            public3 = tk.Button(self.texasGame, state = tk.DISABLED)
            public3.config(bg='white',text = textP3, font = 'Arial -26', fg='black', command = self.clickPublic3)
            public3.grid(row = 1, column = 5, padx = 10, pady=40)

            bc10 = tk.Button(self.texasGame, state = tk.DISABLED)
            bc10.config(bg='#B7F2FF', text = ' $10 ', font = 'Arial -18', fg = 'black', command = self.clickBC10)
            bc10.grid(row = 3, column = 6, padx=5, pady=10)

            bc25 = tk.Button(self.texasGame, state = tk.DISABLED)
            bc25.config(bg='#FFBAD7', text = ' $25 ', font = 'Arial -18', fg = 'black', command = self.clickBC25)
            bc25.grid(row = 3, column = 7, padx=5, pady=10)

            bc50 = tk.Button(self.texasGame, state = tk.DISABLED)
            bc50.config(bg='#003C76', text = ' $50 ', font = 'Arial -18', fg = 'white', command = self.clickBC50)
            bc50.grid(row = 3, column = 8, padx=5, pady=10)

            bc100 = tk.Button(self.texasGame, state = tk.DISABLED)
            bc100.config(bg='black', text = ' $100 ', font = 'Arial -18', fg = 'white', command = self.clickBC100)
            bc100.grid(row = 3, column = 9, padx=5, pady=10)

            ac10 = tk.Button(self.texasGame)
            ac10.config(bg='#B7F2FF', text = ' $10 ', font = 'Arial -18', fg = 'black', command = self.clickAC10)
            ac10.grid(row = 3, column = 0, padx=5, pady=10)

            ac25 = tk.Button(self.texasGame)
            ac25.config(bg='#FFBAD7', text = ' $25 ', font = 'Arial -18', fg = 'black', command = self.clickAC25)
            ac25.grid(row = 3, column = 1, padx=5, pady=10)

            ac50 = tk.Button(self.texasGame)
            ac50.config(bg='#003C76', text = ' $50 ', font = 'Arial -18', fg = 'white', command = self.clickAC50)
            ac50.grid(row = 3, column = 2, padx=5, pady=10)

            ac100 = tk.Button(self.texasGame)
            ac100.config(bg='black', text = ' $100 ', font = 'Arial -18', fg = 'white', command = self.clickAC100)
            ac100.grid(row = 3, column = 3, padx=5, pady=10)

            betA = tk.Button(self.texasGame)
            betA.config(bg='#FCFFDF',text = '下注', font = 'Arial -22', fg='black', command = self.clickBetA)
            betA.grid(row = 3, column = 4, padx = 10)

            gameState = tk.Label(self.texasGame, text = '\n玩家👻請下注', font = 'Arial -28', fg = '#52387B')
            gameState.config(bg='#EFEFEF')
            gameState.grid(row = 6, column = 0, columnspan = 11)

            bCard1 = tk.Button(self.texasGame, state = tk.DISABLED)
            bCard1.config(bg='white',text = '      \n      ', font = 'Arial -26', fg='#EFEFEF')
            bCard1.grid(row = 5, column = 7, padx = 10, pady=10)

            bCard2 = tk.Button(self.texasGame, state = tk.DISABLED)
            bCard2.config(bg='white',text = '      \n      ', font = 'Arial -26', fg='#EFEFEF')
            bCard2.grid(row = 5, column = 8, padx = 10, pady=10)
            
            aCard1 = tk.Button(self.texasGame, state = tk.DISABLED)
            aCard1.config(bg='white',text = textA1, font = 'Arial -26', fg='black', command = self.clickAcard1)
            aCard1.grid(row = 5, column = 1, padx = 10, pady=10)

            aCard2 = tk.Button(self.texasGame, state = tk.DISABLED)
            aCard2.config(bg='white',text = textA2, font = 'Arial -26', fg='black', command = self.clickAcard2)
            aCard2.grid(row = 5, column = 2, padx = 10, pady=10)

        elif countBet == 3:
            countBet = countBet + 1
            textP4 =  texasPoker.strColor(board4) + '\n' + texasPoker.strPoint(board4)
            public4 = tk.Button(self.texasGame, state = tk.DISABLED)
            public4.config(bg='white',text = textP4, font = 'Arial -26', fg='black', command = self.clickPublic4)
            public4.grid(row = 1, column = 6, padx = 10, pady=40)

            bc10 = tk.Button(self.texasGame, state = tk.DISABLED)
            bc10.config(bg='#B7F2FF', text = ' $10 ', font = 'Arial -18', fg = 'black', command = self.clickBC10)
            bc10.grid(row = 3, column = 6, padx=5, pady=10)

            bc25 = tk.Button(self.texasGame, state = tk.DISABLED)
            bc25.config(bg='#FFBAD7', text = ' $25 ', font = 'Arial -18', fg = 'black', command = self.clickBC25)
            bc25.grid(row = 3, column = 7, padx=5, pady=10)

            bc50 = tk.Button(self.texasGame, state = tk.DISABLED)
            bc50.config(bg='#003C76', text = ' $50 ', font = 'Arial -18', fg = 'white', command = self.clickBC50)
            bc50.grid(row = 3, column = 8, padx=5, pady=10)

            bc100 = tk.Button(self.texasGame, state = tk.DISABLED)
            bc100.config(bg='black', text = ' $100 ', font = 'Arial -18', fg = 'white', command = self.clickBC100)
            bc100.grid(row = 3, column = 9, padx=5, pady=10)

            ac10 = tk.Button(self.texasGame)
            ac10.config(bg='#B7F2FF', text = ' $10 ', font = 'Arial -18', fg = 'black', command = self.clickAC10)
            ac10.grid(row = 3, column = 0, padx=5, pady=10)

            ac25 = tk.Button(self.texasGame)
            ac25.config(bg='#FFBAD7', text = ' $25 ', font = 'Arial -18', fg = 'black', command = self.clickAC25)
            ac25.grid(row = 3, column = 1, padx=5, pady=10)

            ac50 = tk.Button(self.texasGame)
            ac50.config(bg='#003C76', text = ' $50 ', font = 'Arial -18', fg = 'white', command = self.clickAC50)
            ac50.grid(row = 3, column = 2, padx=5, pady=10)

            ac100 = tk.Button(self.texasGame)
            ac100.config(bg='black', text = ' $100 ', font = 'Arial -18', fg = 'white', command = self.clickAC100)
            ac100.grid(row = 3, column = 3, padx=5, pady=10)

            betA = tk.Button(self.texasGame)
            betA.config(bg='#FCFFDF',text = '下注', font = 'Arial -22', fg='black', command = self.clickBetA)
            betA.grid(row = 3, column = 4, padx = 10)

            gameState = tk.Label(self.texasGame, text = '\n玩家👻請下注', font = 'Arial -28', fg = '#52387B')
            gameState.config(bg='#EFEFEF')
            gameState.grid(row = 6, column = 0, columnspan = 11)

            bCard1 = tk.Button(self.texasGame, state = tk.DISABLED)
            bCard1.config(bg='white',text = '      \n      ', font = 'Arial -26', fg='#EFEFEF')
            bCard1.grid(row = 5, column = 7, padx = 10, pady=10)

            bCard2 = tk.Button(self.texasGame, state = tk.DISABLED)
            bCard2.config(bg='white',text = '      \n      ', font = 'Arial -26', fg='#EFEFEF')
            bCard2.grid(row = 5, column = 8, padx = 10, pady=10)
            
            aCard1 = tk.Button(self.texasGame, state = tk.DISABLED)
            aCard1.config(bg='white',text = textA1, font = 'Arial -26', fg='black', command = self.clickAcard1)
            aCard1.grid(row = 5, column = 1, padx = 10, pady=10)

            aCard2 = tk.Button(self.texasGame, state = tk.DISABLED)
            aCard2.config(bg='white',text = textA2, font = 'Arial -26', fg='black', command = self.clickAcard2)
            aCard2.grid(row = 5, column = 2, padx = 10, pady=10)

        elif countBet == 4:
            countBet = countBet + 1
            textP5 =  texasPoker.strColor(board5) + '\n' + texasPoker.strPoint(board5)
            public5 = tk.Button(self.texasGame, state = tk.DISABLED)
            public5.config(bg='white',text = textP5, font = 'Arial -26', fg='black', command = self.clickPublic5)
            public5.grid(row = 1, column = 7, padx = 10, pady=40)

            bc10 = tk.Button(self.texasGame, state = tk.DISABLED)
            bc10.config(bg='#B7F2FF', text = ' $10 ', font = 'Arial -18', fg = 'black', command = self.clickBC10)
            bc10.grid(row = 3, column = 6, padx=5, pady=10)

            bc25 = tk.Button(self.texasGame, state = tk.DISABLED)
            bc25.config(bg='#FFBAD7', text = ' $25 ', font = 'Arial -18', fg = 'black', command = self.clickBC25)
            bc25.grid(row = 3, column = 7, padx=5, pady=10)

            bc50 = tk.Button(self.texasGame, state = tk.DISABLED)
            bc50.config(bg='#003C76', text = ' $50 ', font = 'Arial -18', fg = 'white', command = self.clickBC50)
            bc50.grid(row = 3, column = 8, padx=5, pady=10)

            bc100 = tk.Button(self.texasGame, state = tk.DISABLED)
            bc100.config(bg='black', text = ' $100 ', font = 'Arial -18', fg = 'white', command = self.clickBC100)
            bc100.grid(row = 3, column = 9, padx=5, pady=10)

            ac10 = tk.Button(self.texasGame)
            ac10.config(bg='#B7F2FF', text = ' $10 ', font = 'Arial -18', fg = 'black', command = self.clickAC10)
            ac10.grid(row = 3, column = 0, padx=5, pady=10)

            ac25 = tk.Button(self.texasGame)
            ac25.config(bg='#FFBAD7', text = ' $25 ', font = 'Arial -18', fg = 'black', command = self.clickAC25)
            ac25.grid(row = 3, column = 1, padx=5, pady=10)

            ac50 = tk.Button(self.texasGame)
            ac50.config(bg='#003C76', text = ' $50 ', font = 'Arial -18', fg = 'white', command = self.clickAC50)
            ac50.grid(row = 3, column = 2, padx=5, pady=10)

            ac100 = tk.Button(self.texasGame)
            ac100.config(bg='black', text = ' $100 ', font = 'Arial -18', fg = 'white', command = self.clickAC100)
            ac100.grid(row = 3, column = 3, padx=5, pady=10)

            betA = tk.Button(self.texasGame)
            betA.config(bg='#FCFFDF',text = '下注', font = 'Arial -22', fg='black', command = self.clickBetA)
            betA.grid(row = 3, column = 4, padx = 10)

            gameState = tk.Label(self.texasGame, text = '\n玩家👻請下注', font = 'Arial -28', fg = '#52387B')
            gameState.config(bg='#EFEFEF')
            gameState.grid(row = 6, column = 0, columnspan = 11)

            bCard1 = tk.Button(self.texasGame, state = tk.DISABLED)
            bCard1.config(bg='white',text = '      \n      ', font = 'Arial -26', fg='#EFEFEF')
            bCard1.grid(row = 5, column = 7, padx = 10, pady=10)

            bCard2 = tk.Button(self.texasGame, state = tk.DISABLED)
            bCard2.config(bg='white',text = '      \n      ', font = 'Arial -26', fg='#EFEFEF')
            bCard2.grid(row = 5, column = 8, padx = 10, pady=10)
            
            aCard1 = tk.Button(self.texasGame, state = tk.DISABLED)
            aCard1.config(bg='white',text = textA1, font = 'Arial -26', fg='black', command = self.clickAcard1)
            aCard1.grid(row = 5, column = 1, padx = 10, pady=10)

            aCard2 = tk.Button(self.texasGame, state = tk.DISABLED)
            aCard2.config(bg='white',text = textA2, font = 'Arial -26', fg='black', command = self.clickAcard2)
            aCard2.grid(row = 5, column = 2, padx = 10, pady=10)

        elif countBet == 5:

            # 原始code
            betB = tk.Button(self.texasGame, state = tk.DISABLED)
            betB.config(bg='#FCFFDF',text = '下注', font = 'Arial -22', fg='black')
            betB.grid(row = 3, column = 10, padx = 10)

            gameState = tk.Label(self.texasGame, text = '\n玩家👻請挑出最佳牌型組合', font = 'Arial -28', fg = '#52387B')
            gameState.config(bg='#EFEFEF')
            gameState.grid(row = 6, column = 0, columnspan = 11)

            bc10 = tk.Button(self.texasGame, state = tk.DISABLED)
            bc10.config(bg='#B7F2FF', text = ' $10 ', font = 'Arial -18', fg = 'black', command = self.clickBC10)
            bc10.grid(row = 3, column = 6, padx=5, pady=10)

            bc25 = tk.Button(self.texasGame, state = tk.DISABLED)
            bc25.config(bg='#FFBAD7', text = ' $25 ', font = 'Arial -18', fg = 'black', command = self.clickBC25)
            bc25.grid(row = 3, column = 7, padx=5, pady=10)

            bc50 = tk.Button(self.texasGame, state = tk.DISABLED)
            bc50.config(bg='#003C76', text = ' $50 ', font = 'Arial -18', fg = 'white', command = self.clickBC50)
            bc50.grid(row = 3, column = 8, padx=5, pady=10)

            bc100 = tk.Button(self.texasGame, state = tk.DISABLED)
            bc100.config(bg='black', text = ' $100 ', font = 'Arial -18', fg = 'white', command = self.clickBC100)
            bc100.grid(row = 3, column = 9, padx=5, pady=10)

            finishA = tk.Button(self.texasGame)
            finishA.config(bg='white', text = '完成', font = 'Arial -20', fg = 'black', command = self.clickFinishA)
            finishA.grid(row = 2, column = 4, padx=5, pady=10)

            bCard1 = tk.Button(self.texasGame, state = tk.DISABLED)
            bCard1.config(bg='white',text = '      \n      ', font = 'Arial -26', fg='#EFEFEF')
            bCard1.grid(row = 5, column = 7, padx = 10, pady=10)

            bCard2 = tk.Button(self.texasGame, state = tk.DISABLED)
            bCard2.config(bg='white',text = '      \n      ', font = 'Arial -26', fg='#EFEFEF')
            bCard2.grid(row = 5, column = 8, padx = 10, pady=10)
            
            aCard1 = tk.Button(self.texasGame)
            aCard1.config(bg='white',text = textA1, font = 'Arial -26', fg='black', command = self.clickAcard1)
            aCard1.grid(row = 5, column = 1, padx = 10, pady=10)

            aCard2 = tk.Button(self.texasGame)
            aCard2.config(bg='white',text = textA2, font = 'Arial -26', fg='black', command = self.clickAcard2)
            aCard2.grid(row = 5, column = 2, padx = 10, pady=10)

            public1 = tk.Button(self.texasGame)
            public1.config(bg='white',text = textP1, font = 'Arial -26', fg='black', command = self.clickPublic1)
            public1.grid(row = 1, column = 3, padx = 10, pady=40)

            public2 = tk.Button(self.texasGame)
            public2.config(bg='white',text = textP2, font = 'Arial -26', fg='black', command = self.clickPublic2)
            public2.grid(row = 1, column = 4, padx = 10, pady=40)
            
            public3 = tk.Button(self.texasGame)
            public3.config(bg='white',text = textP3, font = 'Arial -26', fg='black', command = self.clickPublic3)
            public3.grid(row = 1, column = 5, padx = 10, pady=40)

            public4 = tk.Button(self.texasGame)
            public4.config(bg='white',text = textP4, font = 'Arial -26', fg='black', command = self.clickPublic4)
            public4.grid(row = 1, column = 6, padx = 10, pady=40)

            public5 = tk.Button(self.texasGame)
            public5.config(bg='white',text = textP5, font = 'Arial -26', fg='black', command = self.clickPublic5)
            public5.grid(row = 1, column = 7, padx = 10, pady=40)

    def clickFinishA(self,):
        global count
        count = 10
        global textP1, textP2, textP3, textP4, textP5, textA1, textA2, textB1, textB2

        finishA = tk.Button(self.texasGame, state = tk.DISABLED)
        finishA.config(bg='white', text = '完成', font = 'Arial -20', fg = 'black')
        finishA.grid(row = 2, column = 4, padx=5, pady=10)

        public1 = tk.Button(self.texasGame)
        public1.config(bg='white',text = textP1, font = 'Arial -26', fg='black', command = self.clickPublic1)
        public1.grid(row = 1, column = 3, padx = 10, pady=40)

        public2 = tk.Button(self.texasGame)
        public2.config(bg='white',text = textP2, font = 'Arial -26', fg='black', command = self.clickPublic2)
        public2.grid(row = 1, column = 4, padx = 10, pady=40)
        
        public3 = tk.Button(self.texasGame)
        public3.config(bg='white',text = textP3, font = 'Arial -26', fg='black', command = self.clickPublic3)
        public3.grid(row = 1, column = 5, padx = 10, pady=40)

        public4 = tk.Button(self.texasGame)
        public4.config(bg='white',text = textP4, font = 'Arial -26', fg='black', command = self.clickPublic4)
        public4.grid(row = 1, column = 6, padx = 10, pady=40)

        public5 = tk.Button(self.texasGame)
        public5.config(bg='white',text = textP5, font = 'Arial -26', fg='black', command = self.clickPublic5)
        public5.grid(row = 1, column = 7, padx = 10, pady=40)

        aCard1 = tk.Button(self.texasGame, state = tk.DISABLED)
        aCard1.config(bg='white',text = '      \n      ', font = 'Arial -26', fg='#EFEFEF')
        aCard1.grid(row = 5, column = 1, padx = 10, pady=10)

        aCard2 = tk.Button(self.texasGame, state = tk.DISABLED)
        aCard2.config(bg='white',text = '      \n      ', font = 'Arial -26', fg='#EFEFEF')
        aCard2.grid(row = 5, column = 2, padx = 10, pady=10)

        bCard1 = tk.Button(self.texasGame)
        bCard1.config(bg='white',text = textB1, font = 'Arial -26', fg='black', command = self.clickBcard1)
        bCard1.grid(row = 5, column = 7, padx = 10, pady=10)

        bCard2 = tk.Button(self.texasGame)
        bCard2.config(bg='white',text = textB2, font = 'Arial -26', fg='black', command = self.clickBcard2)
        bCard2.grid(row = 5, column = 8, padx = 10, pady=10)

        HideA1 = tk.Label(self.texasGame)
        HideA1.config(bg='white',text = '       \n       ', font = 'Arial -26', fg='black')
        HideA1.grid(row = 4, column = 0, padx = 10)

        HideA2 = tk.Label(self.texasGame)
        HideA2.config(bg='white',text = '       \n       ', font = 'Arial -26', fg='black')
        HideA2.grid(row = 4, column = 1, padx = 10)

        HideA3 = tk.Label(self.texasGame)
        HideA3.config(bg='white',text = '       \n       ', font = 'Arial -26', fg='black')
        HideA3.grid(row = 4, column = 2, padx = 10)

        HideA4 = tk.Label(self.texasGame)
        HideA4.config(bg='white',text = '       \n       ', font = 'Arial -26', fg='black')
        HideA4.grid(row = 4, column = 3, padx = 10)

        HideA5 = tk.Label(self.texasGame)
        HideA5.config(bg='white',text = '       \n       ', font = 'Arial -26', fg='black')
        HideA5.grid(row = 4, column = 4, padx = 10)

        finishB = tk.Button(self.texasGame)
        finishB.config(bg='white', text = '完成', font = 'Arial -20', fg = 'black', command = self.clickFinishB)
        finishB.grid(row = 2, column = 10, padx=5, pady=10)

        gameState = tk.Label(self.texasGame, text = '\n玩家🎃請挑出最佳牌型組合', font = 'Arial -28', fg = '#52387B')
        gameState.config(bg='#EFEFEF')
        gameState.grid(row = 6, column = 0, columnspan = 11)

    def clickFinishB(self,):
        global A1, A2, A3, A4, A5
        global a1,a2,a3,a4,a5

        finishB = tk.Button(self.texasGame, state = tk.DISABLED)
        finishB.config(bg='white', text = '完成', font = 'Arial -20', fg = 'black')
        finishB.grid(row = 2, column = 10, padx=5, pady=10)

        public1 = tk.Button(self.texasGame, state = tk.DISABLED)
        public1.config(bg='white',text = textP1, font = 'Arial -26', fg='black', command = self.clickPublic1)
        public1.grid(row = 1, column = 3, padx = 10, pady=40)

        public2 = tk.Button(self.texasGame, state = tk.DISABLED)
        public2.config(bg='white',text = textP2, font = 'Arial -26', fg='black', command = self.clickPublic2)
        public2.grid(row = 1, column = 4, padx = 10, pady=40)
        
        public3 = tk.Button(self.texasGame, state = tk.DISABLED)
        public3.config(bg='white',text = textP3, font = 'Arial -26', fg='black', command = self.clickPublic3)
        public3.grid(row = 1, column = 5, padx = 10, pady=40)

        public4 = tk.Button(self.texasGame, state = tk.DISABLED)
        public4.config(bg='white',text = textP4, font = 'Arial -26', fg='black', command = self.clickPublic4)
        public4.grid(row = 1, column = 6, padx = 10, pady=40)

        public5 = tk.Button(self.texasGame, state = tk.DISABLED)
        public5.config(bg='white',text = textP5, font = 'Arial -26', fg='black', command = self.clickPublic5)
        public5.grid(row = 1, column = 7, padx = 10, pady=40)

        bCard1 = tk.Button(self.texasGame, state = tk.DISABLED)
        bCard1.config(bg='white',text = textB1, font = 'Arial -26', fg='black', command = self.clickBcard1)
        bCard1.grid(row = 5, column = 7, padx = 10, pady=10)

        bCard2 = tk.Button(self.texasGame, state = tk.DISABLED)
        bCard2.config(bg='white',text = textB2, font = 'Arial -26', fg='black', command = self.clickBcard2)
        bCard2.grid(row = 5, column = 8, padx = 10, pady=10)

        aCard1 = tk.Button(self.texasGame, state = tk.DISABLED)
        aCard1.config(bg='white',text = textA1, font = 'Arial -26', fg='black', command = self.clickAcard1)
        aCard1.grid(row = 5, column = 1, padx = 10, pady=10)

        aCard2 = tk.Button(self.texasGame, state = tk.DISABLED)
        aCard2.config(bg='white',text = textA2, font = 'Arial -26', fg='black', command = self.clickAcard2)
        aCard2.grid(row = 5, column = 2, padx = 10, pady=10)


        #global textA1, textA2, textP1, textP2, textP3, textP4, textP5
        global a1,a2,a3,a4,a5

        if a1 == 1:
            t1 = textP1
        elif a1 == 2:
            t1 = textP2
        elif a1 == 3:
            t1 = textP3
        elif a1 == 4:
            t1 = textP4
        elif a1 == 5:
            t1 = textP5
        elif a1 == 6:
            t1 = textA1
        elif a1 == 7:
            t1 = textA2
        else:
            t1 = '       \n       '

        if a2 == 1:
            t2 = textP1
        elif a2 == 2:
            t2 = textP2
        elif a2 == 3:
            t2 = textP3
        elif a2 == 4:
            t2 = textP4
        elif a2 == 5:
            t2 = textP5
        elif a2 == 6:
            t2 = textA1
        elif a2 == 7:
            t2 = textA2
        else:
            t2 = '       \n       '

        if a3 == 1:
            t3 = textP1
        elif a3 == 2:
            t3 = textP2
        elif a3 == 3:
            t3 = textP3
        elif a3 == 4:
            t3 = textP4
        elif a3 == 5:
            t3 = textP5
        elif a3 == 6:
            t3 = textA1
        elif a3 == 7:
            t3 = textA2
        else:
            t3 = '       \n       '

        if a4 == 1:
            t4 = textP1
        elif a4 == 2:
            t4 = textP2
        elif a4 == 3:
            t4 = textP3
        elif a4 == 4:
            t4 = textP4
        elif a4 == 5:
            t4 = textP5
        elif a4 == 6:
            t4 = textA1
        elif a4 == 7:
            t4 = textA2
        else:
            t4 = '       \n       '

        if a5 == 1:
            t5 = textP1
        elif a5 == 2:
            t5 = textP2
        elif a5 == 3:
            t5 = textP3
        elif a5 == 4:
            t5 = textP4
        elif a5 == 5:
            t5 = textP5
        elif a5 == 6:
            t5 = textA1
        elif a5 == 7:
            t5 = textA2
        else:
            t5 = '       \n       '

        A1 = tk.Label(self.texasGame)
        A1.config(bg='white',text = t1, font = 'Arial -26', fg='black')
        A1.grid(row = 4, column = 0, padx = 10)

        A2 = tk.Label(self.texasGame)
        A2.config(bg='white',text = t2, font = 'Arial -26', fg='black')
        A2.grid(row = 4, column = 1, padx = 10)

        A3 = tk.Label(self.texasGame)
        A3.config(bg='white',text = t3, font = 'Arial -26', fg='black')
        A3.grid(row = 4, column = 2, padx = 10)

        A4 = tk.Label(self.texasGame)
        A4.config(bg='white',text = t4, font = 'Arial -26', fg='black')
        A4.grid(row = 4, column = 3, padx = 10)

        A5 = tk.Label(self.texasGame)
        A5.config(bg='white',text = t5, font = 'Arial -26', fg='black')
        A5.grid(row = 4, column = 4, padx = 10)

        global A_point, A_ht, B_point, B_ht
        winner = texasPoker.whoWin(A_ht, B_ht, A_point, B_point)

        global moneyA, moneyB, chipA, chipB
        if winner == 0:
            gameState = tk.Label(self.texasGame, text = '\n👻👻👻獲勝! 獲得所有籌碼!', font = 'Arial -28', fg = '#52387B')
            gameState.config(bg='#EFEFEF')
            gameState.grid(row = 6, column = 0, columnspan = 11)

            moneyA = chipA + chipB + moneyA
            moneyB = moneyB

            #global moneyA_name
            moneyA_name = tk.Label(self.texasGame, text = ' $' + str(moneyA) + ' ', font = 'Arial -24', fg = 'black')
            moneyA_name.config(bg='#FFFF83')
            moneyA_name.grid(row = 2, column = 2, pady = 10)

            moneyB_name = tk.Label(self.texasGame, text = ' $' + str(moneyB) + ' ', font = 'Arial -24', fg = 'black')
            moneyB_name.config(bg='#FFFF83')
            moneyB_name.grid(row = 2, column = 8, pady = 10)

            playAgain = tk.Button(self.texasGame)
            playAgain.config(bg = 'white', text = '再玩一次', font = 'Arial -24', fg = '#5F6594', command = self.playAgain)
            playAgain.grid(row = 6, column = 0, columnspan = 2)

            quitGame = tk.Button(self.texasGame)
            quitGame.config(bg = 'white', text = '結束遊戲', font = 'Arial -24', fg = '#5F6594', command = self.quitGame)
            quitGame.grid(row = 6, column = 9, columnspan = 2)


        elif winner == 1:
            gameState = tk.Label(self.texasGame, text = '\n🎃🎃🎃獲勝! 獲得所有籌碼!', font = 'Arial -28', fg = '#52387B')
            gameState.config(bg='#EFEFEF')
            gameState.grid(row = 6, column = 2, columnspan = 7)

            playAgain = tk.Button(self.texasGame)
            playAgain.config(bg = 'white', text = '再玩一次', font = 'Arial -24', fg = '#5F6594', command = self.playAgain)
            playAgain.grid(row = 6, column = 0, columnspan = 2)

            quitGame = tk.Button(self.texasGame)
            quitGame.config(bg = 'white', text = '結束遊戲', font = 'Arial -24', fg = '#5F6594', command = self.quitGame)
            quitGame.grid(row = 6, column = 9, columnspan = 2)

            moneyB = chipA + chipB + moneyB
            moneyA = moneyA

            moneyA_name = tk.Label(self.texasGame, text = ' $' + str(moneyA) + ' ', font = 'Arial -24', fg = 'black')
            moneyA_name.config(bg='#FFFF83')
            moneyA_name.grid(row = 2, column = 2, pady = 10)
            
            moneyB_name = tk.Label(self.texasGame, text = ' $' + str(moneyB) + ' ', font = 'Arial -24', fg = 'black')
            moneyB_name.config(bg='#FFFF83')
            moneyB_name.grid(row = 2, column = 8, pady = 10)

    def quitGame(self,):
        self.texasGame.quit()

    def playAgain(self,):
        global countBet 
        countBet = 1

        global count
        count = 0

        global poker
        poker = list(range(52))
        for i in range(52):
            color = i//13+1
            point = i%13+1
            poker[i] = (point,color)
        random.shuffle(poker)

        global playerA, playerA1, playerA2
        playerA = poker[:2]
        playerA.sort()
        playerA1 = poker[0]
        playerA2 = poker[1]

        global playerB, playerB1, playerB2
        playerB = poker[2:4]
        playerB.sort()
        playerB1 = poker[2]
        playerB2 = poker[3]

        global board, board1, board2, board3, board4, board5
        board = poker[4:9]
        board1 = poker[4]
        board2 = poker[5]
        board3 = poker[6]
        board4 = poker[7]
        board5 = poker[8]

        playerA_point = texasPoker.POINT(playerA)
        playerB_point = texasPoker.POINT(playerB)
        board_point = texasPoker.POINT(board)

        #牌型判斷
        global A_point, A_ht
        A_point,A_ht = texasPoker.PC(playerA_point,board_point,playerA,board)
        
        global B_point, B_ht
        B_point,B_ht = texasPoker.PC(playerB_point,board_point,playerB,board)

        self.texasGame.destroy()
        texasGame(self.master)

if __name__ == '__main__':    
    root = tk.Tk()
    basedesk(root)
    root.mainloop()
