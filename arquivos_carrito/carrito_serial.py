
import sys,os

from os.path import dirname, realpath, sep, pardir
sys.path.append(dirname(realpath(__file__)) + sep + pardir + sep + "lib")

from tkinter import *
import time
import serial
import serial.tools.list_ports


global v

v=1000
hbut=420

bgd="#65beff"



root=Tk()
root.title("Carrito")
root.geometry("625x575")
root.resizable(0,0)
root.config(bg=bgd)







class Application:
    def __init__(self, master=None):

        #Definir imagem dos botões
        self.botaojogar = PhotoImage(file="botao_jogar2.gif")
        self.botaosobre = PhotoImage(file="botao_sobre2.gif")
        self.botaovarredura = PhotoImage(file="botao_varredura2.gif")
        self.botaosair = PhotoImage(file="botao_sair2.gif")
        self.menu = PhotoImage(file="menu_principal.gif")


        #IMAGEM

        self.widget0 = Label(master)
        self.widget0["width"]=610
        self.widget0["height"]=407
        self.widget0["image"]=self.menu
        self.widget0["bd"]=0
        self.widget0["bg"]=bgd
        self.widget0.pack()


        # BOTÃO SAIR

        self.widget1 = Frame(master)
        self.widget1["width"]=125
        self.widget1["height"]=125
        self.widget1["bg"] = "red"



        self.sair = Button(self.widget1)
        self.sair["image"]=self.botaosair
        self.sair["command"] = self.widget1.quit
        self.sair.pack()


        #Botão JOGAR
        self.widget2 = Frame(master)
        self.widget2["width"]=125
        self.widget2["height"] = 125
        self.widget2["bg"] = "red"




        self.jogar = Button(self.widget2)

        self.jogar["image"]=self.botaojogar
        self.jogar["command"]=self.telajog
        self.jogar.pack()

        #Botão SOBRE O JOGO
        self.widget3 = Frame(master)
        self.widget3["width"] = 125
        self.widget3["height"] = 125
        self.widget3["bg"] = "red"


        self.sobre_o = Button(self.widget3)
        self.sobre_o["width"] = 125
        self.sobre_o["height"]=125
        self.sobre_o["command"]=self.telasobre
        self.sobre_o["image"]=self.botaosobre
        self.sobre_o.pack()


        #Botão VARREDURA
        self.widget4 = Frame(master)
        self.widget4["width"] = 125
        self.widget4["height"] = 125
        self.widget4["bg"] = "red"


        self.varredura=Button(self.widget4)
        self.varredura["command"]=self.telavar
        self.varredura["image"]=self.botaovarredura
        self.varredura.pack()





        self.var1()


    def telasobre(self):



        self.widget1.place(x=475, y=hbut)
        self.widget2.place(x=25, y=hbut)
        self.widget3.place(x=175, y=hbut)
        self.widget4.place(x=325, y=hbut)

        Application4(self)

    def telajog(self):



        Application3(self)

    def telavar(self):


        Application2(self)





    def var1(self):
        self.widget1["bd"] = 4
        self.widget2["bd"] = 0
        self.widget3["bd"] = 0
        self.widget4["bd"] = 0

        #Setando tecla Enter como meio de comando
        self.sair.focus_set()
        root.bind("<Return>", lambda e: quit())

        self.widget1.place(x=475, y=hbut)
        self.widget2.place(x=25,y=hbut)
        self.widget3.place(x=175, y=hbut)
        self.widget4.place(x=325, y=hbut)
        self.widget4.after(v, self.var2)

    def var2(self):
        self.widget1["bd"] = 0
        self.widget2["bd"] = 4
        self.widget3["bd"] = 0
        self.widget4["bd"] = 0

        self.jogar.focus_set()
        root.bind("<Return>", lambda e: Application3())

        self.widget1.place(x=475, y=hbut)
        self.widget2.place(x=25, y=hbut)
        self.widget3.place(x=175, y=hbut)
        self.widget4.place(x=325, y=hbut)

        self.widget4.after(v,self.var3)



    def var3(self):
        self.widget1["bd"] = 0
        self.widget2["bd"] = 0
        self.widget3["bd"] = 4
        self.widget4["bd"] = 0

        self.sobre_o.focus_set()
        root.bind("<Return>", lambda e: Application4())

        self.widget1.place(x=475, y=hbut)
        self.widget2.place(x=25, y=hbut)
        self.widget3.place(x=175, y=hbut)
        self.widget4.place(x=325, y=hbut)

        self.widget4.after(v,self.var4)

    def var4(self):
        self.widget1["bd"] = 0
        self.widget2["bd"] = 0
        self.widget3["bd"] = 0
        self.widget4["bd"] = 4

        self.varredura.focus_set()

        root.bind("<Return>", lambda e: Application2())
        self.widget1.place(x=475, y=hbut)
        self.widget2.place(x=25, y=hbut)
        self.widget3.place(x=175, y=hbut)
        self.widget4.place(x=325, y=hbut)

        self.widget4.after(v,self.var1)



variable=StringVar()
variable.set("1seg")



class Application2:


    def __init__(self,master2=None):

        new = Toplevel(bg=bgd)
        new.title("Varredura Automática")
        new.geometry("850x400")

        # Impedir o usuário de utilizar a janela principal enquanto outra janela está aberta
        new.transient(root)
        new.grab_set()
        new.resizable(0,0)





        self.widget7 = Frame(new,bg=bgd)
        self.widget7["height"]=30
        self.widget7.grid(row=2,column=1,columnspan=1)
        self.title = Label(self.widget7,bg=bgd)
        self.title["text"] = "MUDE A VELOCIDADE DA VARREDURA"
        self.title["font"]=("Comic Sans MS","20")
        self.title["pady"]=3
        self.title["fg"]="white"
        self.title.pack()









        self.vazio6 = Frame(new,bg="#65beff")
        self.vazio6["height"] = 70
        self.vazio6["width"] = 70
        self.vazio6.grid(column=2, row=2)
        self.vazio7 = Frame(new,bg="#65beff")
        self.vazio7["height"] = 70
        self.vazio7["width"] = 70
        self.vazio7.grid(column=3, row=2)

        self.vazio8 = Frame(new,bg="#65beff")
        self.vazio8["height"] = 70
        self.vazio8["width"] = 70
        self.vazio8.grid(row=0, column=9, rowspan=4, columnspan=3)




        #Output
        self.wtexto = Frame(new)
        self.wtexto["height"] = 100
        self.wtexto["width"] = 70
        self.wtexto["bg"]=bgd
        self.wtexto.place(x=590,y=50)
        self.texto=Label(self.wtexto)
        self.texto["relief"]="solid"
        self.texto["font"]=("Comic Sans MS","18")
        self.texto["textvariable"]=variable
        self.texto.pack()

        #Botão +
        self.widgetmais=Frame(new)
        self.widgetmais["bg"] = "red"


        self.plus = PhotoImage(file="70421.gif")
        self.mas=Button(self.widgetmais)
        self.mas["width"] = 100
        self.mas["height"] = 100
        self.mas["image"]=self.plus
        if v== 1000:
            self.mas["command"] = self.temp1
        if v == 1250:
            self.mas["command"] = self.temp2
        if v == 1500:
            self.mas["command"] = self.temp3
        if v == 1750:
            self.mas["command"] = self.temp4
        if v == 2000:
            self.mas["command"] = self.nada
        self.mas.pack()


        #Botão -
        self.widgetmenos=Frame(new)
        self.widgetmenos["bg"] = "red"

        self.minus=PhotoImage(file="minus.gif")
        self.menos=Button(self.widgetmenos)
        self.menos["width"]=100
        self.menos["height"]=100
        self.menos["image"]=self.minus
        self.menos["relief"]="flat"
        if v==1000:
            self.menos["command"] = self.nada
        if v==1250:
            self.menos["command"]=self.temp0
        if v==1500:
            self.menos["command"]=self.temp1
        if v==1750:
            self.menos["command"]=self.temp2
        if v==2000:
            self.menos["command"]=self.temp3
        self.menos.pack()


        def kitar():
            new.destroy()
        #Botao OK

        self.widgetok=Frame(new)
        self.widgetok["bg"]="red"
        self.widgetok.place(x=210,y=280)
        self.ok=Button(self.widgetok)
        self.ok["width"]=10
        self.ok["height"]=4
        self.ok["text"]="OK"
        self.ok["font"]=("Calibri","14")

        self.ok["command"]=kitar
        self.ok.pack()






        self.can=Canvas(new,height=197,width=197)
        self.can["relief"]="solid"
        self.can["bd"]=2
        self.can["bg"]="white"
        self.can.place(x=520,y=100)
        self.ret=self.can.create_rectangle(0,0,100,100,fill="red")
        self.can.create_line(100,0,100,205,fill="black",width=2)
        self.can.create_line(0,100,205,100,fill="black",width=2)



        self.varr()








    # Varredura automática
    def varr(self):


        self.widgetmais["bd"] = 4
        self.widgetmenos["bd"] = 0
        self.widgetok["bd"] = 0



        self.can.move(self.ret,100,0)


        self.widgetmais.place(x=100,y=120)
        self.widgetmenos.place(x=300,y=120)
        self.mas.focus_set()


        self.widgetmenos.after(v, self.varr2)

    def varr2(self):
        self.widgetmais["bd"] = 0
        self.widgetmenos["bd"] = 4
        self.widgetok["bd"] = 0
        self.can.move(self.ret,0,100)
        self.widgetmais.place(x=100,y=120)
        self.widgetmenos.place(x=300,y=120)

        self.menos.focus_set()


        self.widgetmenos.after(v, self.varr3)

    def varr3(self):
        self.widgetmais["bd"] = 0
        self.widgetmenos["bd"] = 0
        self.widgetok["bd"] = 4
        self.can.move(self.ret, -100, 0)



        self.widgetmais.place(x=100,y=120)
        self.widgetmenos.place(x=300,y=120)

        self.ok.focus_set()

        self.widgetmenos.after(v, self.varr4)

    def varr4(self):
        self.widgetmais["bd"] = 4
        self.widgetmenos["bd"] = 0
        self.widgetok["bd"] = 0

        self.can.move(self.ret, 0, -100)
        print(v)
        self.widgetmais.place(x=100,y=120)
        self.widgetmenos.place(x=300,y=120)
        self.mas.focus_set()
        self.widgetmenos.after(v, self.varr5)

    def varr5(self):
        self.widgetmais["bd"] = 0
        self.widgetmenos["bd"] = 4
        self.widgetok["bd"] = 0
        self.can.move(self.ret,100,0)


        self.widgetmais.place(x=100,y=120)
        self.widgetmenos.place(x=300,y=120)

        self.menos.focus_set()
        self.widgetmenos.after(v, self.varr6)

    def varr6(self):
        self.widgetmais["bd"] = 0
        self.widgetmenos["bd"] = 0
        self.widgetok["bd"] = 4
        self.can.move(self.ret,0,100)
        self.ok.focus_set()
        self.widgetmais.place(x=100,y=120)
        self.widgetmenos.place(x=300,y=120)

        self.widgetmenos.after(v, self.varr7)

    def varr7(self):
        self.widgetmais["bd"] = 4
        self.widgetmenos["bd"] = 0
        self.widgetok["bd"] = 0

        self.can.move(self.ret, -100, 0)

        print(v)
        self.widgetmais.place(x=100,y=120)
        self.widgetmenos.place(x=300,y=120)
        self.mas.focus_set()
        self.widgetmenos.after(v, self.varr8)

    def varr8(self):
        self.widgetmais["bd"] = 0
        self.widgetmenos["bd"] = 4
        self.widgetok["bd"] = 0
        self.can.move(self.ret, 0, -100)

        self.widgetmais.place(x=100,y=120)
        self.widgetmenos.place(x=300,y=120)
        self.menos.focus_set()
        self.widgetmenos.after(v, self.varr9)

    def varr9(self):
        self.widgetmais["bd"] = 0
        self.widgetmenos["bd"] = 0
        self.widgetok["bd"] = 4
        self.ok.focus_set()
        self.can.move(self.ret,100,0)


        self.widgetmais.place(x=100,y=120)
        self.widgetmenos.place(x=300,y=120)



        self.widgetmenos.after(v, self.varr10)

    def varr10(self):
        self.widgetmais["bd"] = 4
        self.widgetmenos["bd"] = 0
        self.widgetok["bd"] = 0
        self.can.move(self.ret,0,100)

        self.widgetmais.place(x=100,y=120)
        self.widgetmenos.place(x=300,y=120)
        print(v)
        self.mas.focus_set()
        self.widgetmenos.after(v, self.varr11)

    def varr11(self):
        self.widgetmais["bd"] = 0
        self.widgetmenos["bd"] = 4
        self.widgetok["bd"] = 0
        self.can.move(self.ret, -100, 0)

        self.widgetmais.place(x=100,y=120)
        self.widgetmenos.place(x=300,y=120)
        self.menos.focus_set()
        self.widgetmenos.after(v, self.varr12)

    def varr12(self):
        self.widgetmais["bd"] = 0
        self.widgetmenos["bd"] = 0
        self.widgetok["bd"] = 4
        self.ok.focus_set()
        self.can.move(self.ret, 0, -100)

        self.widgetmais.place(x=100,y=120)
        self.widgetmenos.place(x=300,y=120)

        self.widgetmenos.after(v, self.varr)

    def temp0(self):
        global v
        if v == 1250:
            self.temp2()
        if v == 1500:
            self.temp3()
        if v == 1750:
            self.temp4()
        if v == 2000:
            self.nada()
        v=1000
        variable.set("1 seg")
        self.texto.pack()
        self.mas["command"]=self.temp1
        self.menos["command"]=self.nada



    def nada(self):
        pass

    def temp1(self):
        global v
        if v==1250:
            self.temp2()
        if v==1500:
            pass
        if v==1750:
            self.temp4()
        if v==2000:
            self.nada()

        v = 1250
        variable.set("1,25 seg")


        self.texto.pack()
        self.mas["command"] = self.temp2
        self.menos["command"]=self.temp0



    def temp2(self):
        global v
        if v == 1250:
            pass
        if v == 1500:
            self.temp3()
        if v == 1750:
            self.temp4()
        if v == 2000:
            self.nada()
        v=1500
        variable.set("1,5 seg")
        self.texto.pack()
        self.mas["command"]=self.temp3
        self.menos["command"]=self.temp1


    def temp3(self):
        global v
        if v == 1250:
            self.temp2()
        if v == 1500:
            pass
        if v == 1750:
            self.temp4()
        if v == 2000:
            pass
        v=1750
        variable.set("1,75 seg")
        self.texto.pack()
        self.mas["command"]=self.temp4
        self.menos["command"]=self.temp2



    def temp4(self):
        global v
        if v == 1250:
            self.temp2()
        if v == 1500:
            self.temp3()
        if v == 1750:
            pass
        if v == 2000:
            self.nada()
        v=2000
        variable.set("2 seg")
        self.texto.pack()
        self.mas["command"]=self.nada
        self.menos["command"]=self.temp3



class Application3:


    def __init__(self, master3=None):

        self.ser = serial.Serial('COM3', baudrate=9600, timeout=1)

        time.sleep(1)
        jogar=Toplevel(bg=bgd)
        jogar.title("Carrito")
        jogar.geometry("400x500")
        jogar.transient(root)
        jogar.grab_set()
        jogar.focus_set()
        jogar.resizable(0,0)
        ports = list(serial.tools.list_ports.comports())
        for p in ports:
            z = str(p.description)
            if "Arduino Uno" in z == True:
                print(p.device)
            else:
                print(p.device +" não contém Arduino")
            print(p.description)




        def xau():
            jogar.destroy()

        self.widget0 = Frame(jogar)
        self.widget0["bg"]="red"
        self.widget0["width"]=100
        self.widget0["height"]=100
        self.widget0.place(x=150, y=325)

        self.ok=Button(self.widget0)
        self.ok["text"]="OK"
        self.ok["font"]="Calibri","14"
        self.ok["width"]=10
        self.ok["height"]=4

        self.ok["command"]=xau
        self.ok.pack()


        self.widget1 = Frame(jogar)
        self.widget1["bg"] = "red"
        self.widget1["height"]=100
        self.widget1["width"]=100


        self.cima=PhotoImage(file="up.gif")
        self.up=Button(self.widget1)
        self.up["width"]=100
        self.up["height"]=100
        self.up["image"]=self.cima
        self.up["command"]=self.motorup
        self.up.pack()

        self.widget2 = Frame(jogar)
        self.widget2["bg"]="red"


        self.baixo=PhotoImage(file="down.gif")
        self.down=Button(self.widget2)
        self.down["width"]=100
        self.down["height"]=100
        self.down["image"]=self.baixo
        self.down["command"]=self.motordown
        self.down.pack()

        self.widget3 = Frame(jogar)
        self.widget3["bg"]="red"


        self.esq=PhotoImage(file="left.gif")
        self.left=Button(self.widget3)
        self.left["width"]=100
        self.left["height"]=100
        self.left["image"]=self.esq
        self.left["command"]=self.motorleft
        self.left.pack()

        self.widget4=Frame(jogar)
        self.widget4["bg"]="red"


        self.dir=PhotoImage(file="right.gif")
        self.right=Button(self.widget4)
        self.right["width"]=100
        self.right["height"]=100
        self.right["image"]=self.dir
        self.right["command"]=self.motorright
        self.right.pack()

        self.var1()

    def var1(self):

        self.widget1["bd"] = 4
        self.widget2["bd"] = 0
        self.widget3["bd"] = 0
        self.widget4["bd"] = 0
        self.widget0["bd"] = 0

        self.widget1.place(x=150, y=50)
        self.widget2.place(x=150, y=165)
        self.widget3.place(x=35, y=165)
        self.widget4.place(x=265, y=165)
        self.widget0.place(x=150, y=325)


        self.up.focus_set()
        self.up.after(v, self.var2)


    def var2(self):
        self.widget1["bd"] = 0
        self.widget2["bd"] = 0
        self.widget3["bd"] = 4
        self.widget4["bd"] = 0
        self.widget0["bd"] = 0

        self.widget1.place(x=150, y=50)
        self.widget2.place(x=150, y=165)
        self.widget3.place(x=35, y=165)
        self.widget4.place(x=265, y=165)
        self.widget0.place(x=150, y=325)

        self.left.focus_set()


        self.left.after(v, self.var3)

    def var3(self):
        self.widget1["bd"] = 0
        self.widget2["bd"] = 4
        self.widget3["bd"] = 0
        self.widget4["bd"] = 0
        self.widget0["bd"] = 0



        self.widget1.place(x=150, y=50)
        self.widget2.place(x=150, y=165)
        self.widget3.place(x=35, y=165)
        self.widget4.place(x=265, y=165)
        self.widget0.place(x=150, y=325)

        self.down.focus_set()
        self.down.after(v, self.var4)


    def var4(self):
        self.widget1["bd"] = 0
        self.widget2["bd"] = 0
        self.widget3["bd"] = 0
        self.widget4["bd"] = 4
        self.widget0["bd"] = 0


        self.widget1.place(x=150, y=50)
        self.widget2.place(x=150, y=165)
        self.widget3.place(x=35, y=165)
        self.widget4.place(x=265, y=165)
        self.widget0.place(x=150, y=325)

        self.right.focus_set()

        self.right.after(v, self.var5)


    def var5(self):
        self.widget1["bd"] = 0
        self.widget2["bd"] = 0
        self.widget3["bd"] = 0
        self.widget4["bd"] = 0
        self.widget0["bd"] = 4

        self.widget1.place(x=150, y=50)
        self.widget2.place(x=150, y=165)
        self.widget3.place(x=35, y=165)
        self.widget4.place(x=265, y=165)
        self.widget0.place(x=150, y=325)

        self.ok.focus_set()
        root.bind("<Return>", lambda e: xau())
        self.ok.after(v,self.var1)






    def motorup(self):
        if self.ser.is_open == False:
                self.ser.open()
        else:
            pass
        self.ser.write(b'0')

        self.ser.close()


    def motordown(self):
        if self.ser.is_open == False:
                self.ser.open()
        else:
            pass
        self.ser.write(b'1')

        self.ser.close()

    def motorleft(self):
        if self.ser.is_open == False:
                self.ser.open()
        else:
            pass
        self.ser.write(b'2')

        self.ser.close()

    def motorright(self):
        if self.ser.is_open == False:
                self.ser.open()
        else:
            pass
        self.ser.write(b'3')

        self.ser.close()


class Application4:
    def __init__(self, master4=None):
        sobre=Toplevel(bg=bgd)
        sobre.title("Sobre o jogo")
        sobre.transient(root)
        sobre.grab_set()
        sobre.focus_set()
        sobre.resizable(0,0)

        self.widget1=Frame(sobre)
        self.widget1.pack()

        def xau():
            sobre.destroy()


        self.texto=Label(self.widget1)
        self.texto["font"]=("Calibri","14")
        self.texto["fg"]="white"
        self.texto["bg"]=bgd
        self.texto["text"]=("Carrito é um jogo de simulação cujo objetivo é auxiliar no desenvolvimento\n de crianças portadoras de deficiências."
                            " Feito por Vanderlei de Oliveira Júnior como tema\n de seu Trabalho de Graduação com a orientação da professora Erica Regina Daruichi Ma-\nchado."
                            "\n O objetivo do jogo é controlar um carrinho com auxílio de recurso de Tecnologia Assis-\ntiva, a varredura automática, que"
                            " possibilita a substituição do mouse por dispositivos\n adaptados para mesma função."
                            "\n"
                            "\n"
                            "\n"
                            "     Laboratório de Tecnologia Assistiva Digital, FEIS-UNESP, 2020")

        self.widget2 = Frame(sobre)
        self.widget2["bg"]="red"
        self.widget2["bd"] = 4
        self.widget2.pack()
        self.botoo=Button(self.widget2)
        self.botoo["width"]=5
        self.botoo["height"]=2
        self.botoo["text"]="OK"
        self.botoo["command"]=xau
        self.botoo.pack()
        self.botoo.focus_set()


        self.texto.pack()





















if __name__ == '__main__':
    b = Application(root)
    root.mainloop()

