# Developer: UTH
from Tkinter import *
import ttk
import tkFont
import time
import tkMessageBox
import os
import subprocess
import time
import ScrolledText
from string import Template

# Crear Ventana
v0=Tk()
v0.title("Examen Segundo Parcial - II")
v0.geometry("550x350+150+150")
v0.config(background = "#bcd8e4")

#Imagenes
immgON=PhotoImage(file="/home/elvis/on.gif")
immgOff=PhotoImage(file="/home/elvis/off.gif")

#Fuente
textt=tkFont.Font(family="Helvatica",size=12)

# Definicion De Funciones
    
def cerrar():
    v0.destroy()


def openGPIO17():
    g17= Toplevel(v0)
    g17.title("GPIO17-WPI0")
    g17.geometry("450x250+100+130")
    titlevent = label_title=Label(g17,text="GPIO17",font=textt).place(x=140,y=300) 

    def on17r():
        print "ENCENDIDO"
        os.system("sudo /./home/elvis/Escritorio/on17r.sh")

    def off17r():
        print "APAGADO"
        os.system("sudo /./home/elvis/Escritorio/off17r.sh")

    #boton
    btn_on=Button(g17,text="ON",command=on17r).place(x=320,y=120)
    btn_off=Button(g17,text="OFF",command=off17r).place(x=390,y=120)


    def limpiar():
                horaini17.set("")
                minini17.set("")
                minf17.set("")
                horaf17.set("")
                
    def registrar():
            print "Registrado"
            hi17=horaini17.get()
            mi17=minini17.get()
            hf17=horaf17.get()
            mf17=minf17.get()
            tab = " "
            dia="*"
            mes="*"
            ano="*"
            usuario="root"
            path1="/home/elvis/on17r.sh"
            path2="/home/elvis/off17r.sh"

            #ASIGNAR PERMISOS DE ESCRITURA Y EJECUCION
            os.system("sudo chmod -R 777 /etc/cron.d/tarea1_17")
            os.system("sudo chmod -R 777 /etc/cron.d/tarea2_17")

            #cadena
            cadena=(str(mi17)+''+str(tab)+''+str(hi17)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ano)+''+str(tab)+''+str(usuario)+''+str(tab)+''+str(path1))
            cadena2=(str(mf17)+''+str(tab)+''+str(hf17)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ano)+''+str(tab)+''+str(usuario)+''+str(tab)+''+str(path2))
         
            #apertura archivo
            pf=open("/etc/cron.d/tarea1_17","w")
            pf.write(cadena)
            pf.write("\n")
            pf.close()
            time.sleep(0.1)

            pf2=open("/etc/cron.d/tarea2_17","w")
            pf2.write(cadena2)
            pf2.write("\n")
            pf2.close()
            time.sleep(0.1)

            #permiso
            os.system("sudo chmod -R 755 /etc/cron.d/tarea1_17")
            os.system("sudo chmod -R 755 /etc/cron.d/tarea2_17")

            #servicio
            os.system("sudo /etc/init.d/cron restart")

            limpiar()
            tkMessageBox.showinfo("save",message="Tiempo Registrado")

    #variables
    minini17=StringVar()
    horaini17=StringVar()
    minf17=StringVar()
    horaf17=StringVar()

    label_horaini17=Label(g17,text="Hora Inicial:",font=text2).place(x=15,y=10)
    txt_horaini17=Entry(g17,textvariable=horaini17,font=text2).place(x=130,y=10)
    label_horaini17=Label(g17,text="Minuto Inicial:",font=text2).place(x=15,y=50)
    txt_minini17=Entry(g17,textvariable=minini17,font=text2).place(x=130,y=50)
    label_horaf17=Label(g17,text="Hora Final:",font=text2).place(x=15,y=90)
    txt_horaini17=Entry(g17,textvariable=horaf17,font=text2).place(x=130,y=90)
    label_mif17=Label(g17,text="Minuto Final:",font=text2).place(x=15,y=130)
    txt_minini17=Entry(g17,textvariable=minf17,font=text2).place(x=130,y=130)
    btn_guardar17=Button(g17,text="Registrar",command=registrar).place(x=185,y=160)

    def actualizar():
        os.system("sudo /./home/elvis/estado17.sh")
        pf=open("/home/elvis/gpio17.txt","r")
        for linea in pf:
            campo=linea.split("\n")
            campof=campo[0]
            if (campof=="1"):
                                btn_on17=Button(g17,image=immgON).place(x=330,y=10)
                                g17.after(1000,actualizar)
            if (campof=="0"):
                                btn_on17=Button(g17,image=immgOff).place(x=330,y=10)
                                g17.after(1000,actualizar)  
    actualizar()

            
def openGPIO27():
    g27= Toplevel(v0)
    g27.title("GPIO27-WPI2")
    g27.geometry("450x250+100+130")
    titlevent = label_title=Label(g27,text="GPIO17",font=textt).place(x=140,y=10)

    def on27():
        print "ENCENDIDO"
        os.system("sudo /./home/elvis/on27r.sh")

    def off27():
        print "APAGADO"
        os.system("sudo /./home/elvis/off27r.sh")

    #boton
    btn_on=Button(g27,text="ON",command=on27).place(x=320,y=120)
    btn_off=Button(g27,text="OFF",command=off27).place(x=390,y=120)

 
    def limpiar():
                horaini27.set("")
                minini27.set("")
                minf27.set("")
                horaf27.set("")
                
    def registrar():
            print "Registrado"
            hi27=horaini27.get()
            mi27=minini27.get()
            hf27=horaf27.get()
            mf27=minf27.get()
            tab = " "
            dia="*"
            mes="*"
            ano="*"
            usuario="root"
            path1="/home/elvis/on27r.sh"
            path2="/home/elvis/off27r.sh"

            #ASIGNAR PERMISOS DE ESCRITURA Y EJECUCION
            os.system("sudo chmod -R 777 /etc/cron.d/tarea1_27")
            os.system("sudo chmod -R 777 /etc/cron.d/tarea2_27")

            #cadena
            cadena=(str(mi27)+''+str(tab)+''+str(hi27)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ano)+''+str(tab)+''+str(usuario)+''+str(tab)+''+str(path1))
            cadena2=(str(mf27)+''+str(tab)+''+str(hf27)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ano)+''+str(tab)+''+str(usuario)+''+str(tab)+''+str(path2))
         
            #apertura archivo
            pf=open("/etc/cron.d/tarea1_27","w")
            pf.write(cadena)
            pf.write("\n")
            pf.close()
            time.sleep(0.1)

            pf2=open("/etc/cron.d/tarea2_27","w")
            pf2.write(cadena2)
            pf2.write("\n")
            pf2.close()
            time.sleep(0.1)

            #permiso
            os.system("sudo chmod -R 755 /etc/cron.d/tarea1_27")
            os.system("sudo chmod -R 755 /etc/cron.d/tarea2_27")

            #servicio
            os.system("sudo /etc/init.d/cron restart")

            limpiar()
            tkMessageBox.showinfo("save",message="Tiempo Registrado")

    #variables
    minini27=StringVar()
    horaini27=StringVar()
    minf27=StringVar()
    horaf27=StringVar()

    label_horaini27=Label(g27,text="Hora Inicial:",font=text2).place(x=15,y=10)
    txt_horaini27=Entry(g27,textvariable=horaini27,font=text2).place(x=130,y=10)
    label_horaini27=Label(g27,text="Minuto Inicial:",font=text2).place(x=15,y=50)
    txt_minini27=Entry(g27,textvariable=minini27,font=text2).place(x=130,y=50)
    label_horaf27=Label(g27,text="Hora Final:",font=text2).place(x=15,y=90)
    txt_horaini27=Entry(g27,textvariable=horaf27,font=text2).place(x=130,y=90)
    label_mif27=Label(g27,text="Minuto Final:",font=text2).place(x=15,y=130)
    txt_minini27=Entry(g27,textvariable=minf27,font=text2).place(x=130,y=130)
    btn_guardar27=Button(g27,text="Registrar",command=registrar).place(x=185,y=160)
    def actualizar2():
        os.system("sudo /./home/elvis/estado27.sh")
        pf2=open("/home/elvis/gpio27.txt","r")
        for linea2 in pf2:
            campo2=linea2.split("\n")
            campof2=campo2[0]
            if (campof2=="1"):
                                btn_on27=Button(g27,image=immgON).place(x=330,y=10)
                                g27.after(1000,actualizar2)
            if (campof2=="0"):
                                btn_on27=Button(g27,image=immgOff).place(x=330,y=10)
                                g27.after(1000,actualizar2)  
    actualizar2()
   
    
    
def openGPIO21():
    g21= Toplevel(v0)
    g21.title("GPIO21-WPI29")
    g21.geometry("450x250+100+130")
    titlevent = label_title=Label(g21,text="GPIO21",font=textt).place(x=140,y=10)

    def on21():
        print "ENCENDIDO"
        os.system("sudo /./home/elvis/on21r.sh")

    def off21():
        print "APAGADO"
        os.system("sudo /./home/elvis/off21r.sh")

    #boton
    btn_on=Button(g21,text="ON",command=on21).place(x=320,y=120)
    btn_off=Button(g21,text="OFF",command=off21).place(x=390,y=120)

    def limpiar():
                horaini21.set("")
                minini21.set("")
                minf21.set("")
                horaf21.set("")
                
    def registrar():
            print "Registrado"
            hi21=horaini21.get()
            mi21=minini21.get()
            hf21=horaf21.get()
            mf21=minf21.get()
            tab = " "
            dia="*"
            mes="*"
            ano="*"
            usuario="root"
            path1="/home/elvis/on21r.sh"
            path2="/home/elvis/off21r.sh"

            #ASIGNAR PERMISOS DE ESCRITURA Y EJECUCION
            os.system("sudo chmod -R 777 /etc/cron.d/tarea1_21")
            os.system("sudo chmod -R 777 /etc/cron.d/tarea2_21")

            #cadena
            cadena=(str(mi21)+''+str(tab)+''+str(hi21)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ano)+''+str(tab)+''+str(usuario)+''+str(tab)+''+str(path1))
            cadena2=(str(mf21)+''+str(tab)+''+str(hf21)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ano)+''+str(tab)+''+str(usuario)+''+str(tab)+''+str(path2))
         
            #apertura archivo
            pf=open("/etc/cron.d/tarea1_21","w")
            pf.write(cadena)
            pf.write("\n")
            pf.close()
            time.sleep(0.1)

            pf2=open("/etc/cron.d/tarea2_21","w")
            pf2.write(cadena2)
            pf2.write("\n")
            pf2.close()
            time.sleep(0.1)

            #permiso
            os.system("sudo chmod -R 755 /etc/cron.d/tarea1_21")
            os.system("sudo chmod -R 755 /etc/cron.d/tarea2_21")

            #servicio
            os.system("sudo /etc/init.d/cron restart")

            limpiar()
            tkMessageBox.showinfo("save",message="Tiempo Registrado")

    #variables
    minini21=StringVar()
    horaini21=StringVar()
    minf21=StringVar()
    horaf21=StringVar()

    label_horaini21=Label(g21,text="Hora Inicial:",font=text2).place(x=15,y=10)
    txt_horaini21=Entry(g21,textvariable=horaini21,font=text2).place(x=130,y=10)
    label_horaini21=Label(g21,text="Minuto Inicial:",font=text2).place(x=15,y=50)
    txt_minini21=Entry(g21,textvariable=minini21,font=text2).place(x=130,y=50)
    label_horaf21=Label(g21,text="Hora Final:",font=text2).place(x=15,y=90)
    txt_horaini21=Entry(g21,textvariable=horaf21,font=text2).place(x=130,y=90)
    label_mif21=Label(g21,text="Minuto Final:",font=text2).place(x=15,y=130)
    txt_minini21=Entry(g21,textvariable=minf21,font=text2).place(x=130,y=130)
    btn_guardar21=Button(g21,text="Registrar",command=registrar).place(x=185,y=160)
    def actualizar3():
        os.system("sudo /./home/elvis/estado21.sh")
        pf2=open("/home/elvis/gpio21.txt","r")
        for linea2 in pf2:
            campo2=linea2.split("\n")
            campof2=campo2[0]
            if (campof2=="1"):
                                btn_on21=Button(g21,image=immgON).place(x=330,y=10)
                                g21.after(1000,actualizar3)
            if (campof2=="0"):
                                btn_on21=Button(g21,image=immgOff).place(x=330,y=10)
                                g21.after(1000,actualizar3)  
    actualizar3()
        

   
def openGPIO6():
    g6= Toplevel(v0)
    g6.title("GPIO6-WPI22")
    g6.geometry("450x250+100+130")
    titlevent = label_title=Label(g6,text="GPIO6",font=textt).place(x=140,y=10)

    def on6():
        print "ENCENDIDO"
        os.system("sudo /./home/elvis/on6r.sh")

    def off6():
        print "APAGADO"
        os.system("sudo /./home/elvis/off6r.sh")

    #boton
    btn_on=Button(g6,text="ON",command=on6).place(x=320,y=120)
    btn_off=Button(g6,text="OFF",command=off6).place(x=390,y=120)

    def limpiar():
                horaini6.set("")
                minini6.set("")
                minf6.set("")
                horaf6.set("")
                
    def registrar():
            print "Registrado"
            hi6=horaini6.get()
            mi6=minini6.get()
            hf6=horaf6.get()
            mf6=minf6.get()
            tab = " "
            dia="*"
            mes="*"
            ano="*"
            usuario="root"
            path1="/home/elvis/on6r.sh"
            path2="/home/elvis/off6r.sh"

            #ASIGNAR PERMISOS DE ESCRITURA Y EJECUCION
            os.system("sudo chmod -R 777 /etc/cron.d/tarea1_6")
            os.system("sudo chmod -R 777 /etc/cron.d/tarea2_6")

            #cadena
            cadena=(str(mi6)+''+str(tab)+''+str(hi6)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ano)+''+str(tab)+''+str(usuario)+''+str(tab)+''+str(path1))
            cadena2=(str(mf6)+''+str(tab)+''+str(hf6)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ano)+''+str(tab)+''+str(usuario)+''+str(tab)+''+str(path2))
         
            #apertura archivo
            pf=open("/etc/cron.d/tarea1_6","w")
            pf.write(cadena)
            pf.write("\n")
            pf.close()
            time.sleep(0.1)

            pf2=open("/etc/cron.d/tarea2_6","w")
            pf2.write(cadena2)
            pf2.write("\n")
            pf2.close()
            time.sleep(0.1)

            #permiso
            os.system("sudo chmod -R 755 /etc/cron.d/tarea1_6")
            os.system("sudo chmod -R 755 /etc/cron.d/tarea2_6")

            #servicio
            os.system("sudo /etc/init.d/cron restart")

            limpiar()
            tkMessageBox.showinfo("save",message="Tiempo Registrado")

    #variables
    minini6=StringVar()
    horaini6=StringVar()
    minf6=StringVar()
    horaf6=StringVar()

    label_horaini6=Label(g6,text="Hora Inicial:",font=text2).place(x=15,y=10)
    txt_horaini6=Entry(g6,textvariable=horaini6,font=text2).place(x=130,y=10)
    label_horaini6=Label(g6,text="Minuto Inicial:",font=text2).place(x=15,y=50)
    txt_minini6=Entry(g6,textvariable=minini6,font=text2).place(x=130,y=50)
    label_horaf6=Label(g6,text="Hora Final:",font=text2).place(x=15,y=90)
    txt_horaini6=Entry(g6,textvariable=horaf6,font=text2).place(x=130,y=90)
    label_mif6=Label(g6,text="Minuto Final:",font=text2).place(x=15,y=130)
    txt_minini6=Entry(g6,textvariable=minf6,font=text2).place(x=130,y=130)
    btn_guardar6=Button(g6,text="Registrar",command=registrar).place(x=185,y=160)
    def actualizar4():
        os.system("sudo /./home/elvis/estado6.sh")
        pf2=open("/home/elvis/gpio6.txt","r")
        for linea2 in pf2:
            campo2=linea2.split("\n")
            campof2=campo2[0]
            if (campof2=="1"):
                                btn_on6=Button(g6,image=immgON).place(x=330,y=10)
                                g6.after(1000,actualizar4)
            if (campof2=="0"):
                                btn_on6=Button(g6,image=immgOff).place(x=330,y=10)
                                g6.after(1000,actualizar4)  
    actualizar4()

def openGPIO26():
    g26= Toplevel(v0)
    g26.title("GPIO26-WPI25")
    g26.geometry("450x250+100+130")
    titlevent = label_title=Label(g26,text="GPIO26",font=textt).place(x=140,y=10)

    def on26():
        print "ENCENDIDO"
        os.system("sudo /./home/elvis/on26r.sh")

    def off26():
        print "APAGADO"
        os.system("sudo /./home/elvis/off26r.sh")

    #boton
    btn_on=Button(g26,text="ON",command=on26).place(x=320,y=120)
    btn_off=Button(g26,text="OFF",command=off26).place(x=390,y=120)

    def limpiar():
                horaini26.set("")
                minini26.set("")
                minf26.set("")
                horaf26.set("")
                
    def registrar():
            print "Registrado"
            hi26=horaini26.get()
            mi26=minini26.get()
            hf26=horaf26.get()
            mf26=minf26.get()
            tab = " "
            dia="*"
            mes="*"
            ano="*"
            usuario="root"
            path1="/home/elvis/on26r.sh"
            path2="/home/elvis/off26r.sh"

            #ASIGNAR PERMISOS DE ESCRITURA Y EJECUCION
            os.system("sudo chmod -R 777 /etc/cron.d/tarea1_26")
            os.system("sudo chmod -R 777 /etc/cron.d/tarea2_26")

            #cadena
            cadena=(str(mi26)+''+str(tab)+''+str(hi26)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ano)+''+str(tab)+''+str(usuario)+''+str(tab)+''+str(path1))
            cadena2=(str(mf26)+''+str(tab)+''+str(hf26)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ano)+''+str(tab)+''+str(usuario)+''+str(tab)+''+str(path2))
         
            #apertura archivo
            pf=open("/etc/cron.d/tarea1_26","w")
            pf.write(cadena)
            pf.write("\n")
            pf.close()
            time.sleep(0.1)

            pf2=open("/etc/cron.d/tarea2_26","w")
            pf2.write(cadena2)
            pf2.write("\n")
            pf2.close()
            time.sleep(0.1)

            #permiso
            os.system("sudo chmod -R 755 /etc/cron.d/tarea1_26")
            os.system("sudo chmod -R 755 /etc/cron.d/tarea2_26")

            #servicio
            os.system("sudo /etc/init.d/cron restart")

            limpiar()
            tkMessageBox.showinfo("save",message="Tiempo Registrado")

    #variables
    minini26=StringVar()
    horaini26=StringVar()
    minf26=StringVar()
    horaf26=StringVar()

    label_horaini26=Label(g26,text="Hora Inicial:",font=text2).place(x=15,y=10)
    txt_horaini26=Entry(g26,textvariable=horaini26,font=text2).place(x=130,y=10)
    label_horaini26=Label(g26,text="Minuto Inicial:",font=text2).place(x=15,y=50)
    txt_minini26=Entry(g26,textvariable=minini26,font=text2).place(x=130,y=50)
    label_horaf26=Label(g26,text="Hora Final:",font=text2).place(x=15,y=90)
    txt_horaini26=Entry(g26,textvariable=horaf26,font=text2).place(x=130,y=90)
    label_mif26=Label(g26,text="Minuto Final:",font=text2).place(x=15,y=130)
    txt_minini26=Entry(g26,textvariable=minf26,font=text2).place(x=130,y=130)
    btn_guardar26=Button(g26,text="Registrar",command=registrar).place(x=185,y=160)
    def actualizar5():
        os.system("sudo /./home/elvis/estado26.sh")
        pf2=open("/home/elvis/gpio26.txt","r")
        for linea2 in pf2:
            campo2=linea2.split("\n")
            campof2=campo2[0]
            if (campof2=="1"):
                                btn_on6=Button(g26,image=immgON).place(x=330,y=10)
                                g26.after(1000,actualizar5)
            if (campof2=="0"):
                                btn_on26=Button(g26,image=immgOff).place(x=330,y=10)
                                g26.after(1000,actualizar5)  
    actualizar5()

def openGPIO19():
    g19= Toplevel(v0)
    g19.title("GPIO19-WPI24")
    g19.geometry("450x250+100+130")
    titlevent = label_title=Label(g19,text="GPIO19",font=textt).place(x=140,y=10)

    def on19():
        print "ENCENDIDO"
        os.system("sudo /./home/elvis/on19r.sh")

    def off19():
        print "APAGADO"
        os.system("sudo /./home/elvis/off19r.sh")

    #boton
    btn_on=Button(g19,text="ON",command=on19).place(x=320,y=120)
    btn_off=Button(g19,text="OFF",command=off19).place(x=390,y=120)

    def limpiar():
                horaini19.set("")
                minini19.set("")
                minf19.set("")
                horaf19.set("")
                
    def registrar():
            print "Registrado"
            hi19=horaini19.get()
            mi19=minini19.get()
            hf19=horaf19.get()
            mf19=minf19.get()
            tab = " "
            dia="*"
            mes="*"
            ano="*"
            usuario="root"
            path1="/home/elvis/on19r.sh"
            path2="/home/elvis/off19r.sh"

            #ASIGNAR PERMISOS DE ESCRITURA Y EJECUCION
            os.system("sudo chmod -R 777 /etc/cron.d/tarea1_19")
            os.system("sudo chmod -R 777 /etc/cron.d/tarea2_19")

            #cadena
            cadena=(str(mi19)+''+str(tab)+''+str(hi19)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ano)+''+str(tab)+''+str(usuario)+''+str(tab)+''+str(path1))
            cadena2=(str(mf19)+''+str(tab)+''+str(hf19)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ano)+''+str(tab)+''+str(usuario)+''+str(tab)+''+str(path2))
         
            #apertura archivo
            pf=open("/etc/cron.d/tarea1_19","w")
            pf.write(cadena)
            pf.write("\n")
            pf.close()
            time.sleep(0.1)

            pf2=open("/etc/cron.d/tarea2_19","w")
            pf2.write(cadena2)
            pf2.write("\n")
            pf2.close()
            time.sleep(0.1)

            #permiso
            os.system("sudo chmod -R 755 /etc/cron.d/tarea1_19")
            os.system("sudo chmod -R 755 /etc/cron.d/tarea2_19")

            #servicio
            os.system("sudo /etc/init.d/cron restart")

            limpiar()
            tkMessageBox.showinfo("save",message="Tiempo Registrado")

    #variables
    minini19=StringVar()
    horaini19=StringVar()
    minf19=StringVar()
    horaf19=StringVar()

    label_horaini19=Label(g19,text="Hora Inicial:",font=text2).place(x=15,y=10)
    txt_horaini19=Entry(g19,textvariable=horaini19,font=text2).place(x=130,y=10)
    label_horaini19=Label(g19,text="Minuto Inicial:",font=text2).place(x=15,y=50)
    txt_minini19=Entry(g19,textvariable=minini19,font=text2).place(x=130,y=50)
    label_horaf19=Label(g19,text="Hora Final:",font=text2).place(x=15,y=90)
    txt_horaini19=Entry(g19,textvariable=horaf19,font=text2).place(x=130,y=90)
    label_mif19=Label(g19,text="Minuto Final:",font=text2).place(x=15,y=130)
    txt_minini19=Entry(g19,textvariable=minf19,font=text2).place(x=130,y=130)
    btn_guardar19=Button(g19,text="Registrar",command=registrar).place(x=185,y=160)
    def actualizar6():
        os.system("sudo /./home/elvis/estado19.sh")
        pf2=open("/home/elvis/gpio19.txt","r")
        for linea2 in pf2:
            campo2=linea2.split("\n")
            campof2=campo2[0]
            if (campof2=="1"):
                                btn_on19=Button(g19,image=immgON).place(x=330,y=10)
                                g19.after(1000,actualizar6)
            if (campof2=="0"):
                                btn_on19=Button(g19,image=immgOff).place(x=330,y=10)
                                g19.after(1000,actualizar6)  
    actualizar6()

def salir():
    openGPIO17.destroy()
    openGPIO17.update()
    openGPIO27.destroy()
    openGPIO27.update()
    openGPIO21.destroy()
    openGPIO21.update()

#variables golbales
global minini17
global horaini17
global minf17
global horaf17

global minini27
global horaini27
global minf27
global horaf27

global minini21
global horaini21
global minf21
global horaf21

global minini6
global horaini6
global minf6
global horaf6

global minini26
global horaini26
global minf26
global horaf26

global minini19
global horaini19
global minf19
global horaf19

# Tipo De Fuente
text1=tkFont.Font(family="Helvatica",size=12)
text2=tkFont.Font(family="Arial",size=12)

# Zona de Etiquetas
label_title=Label(v0,text="Examen Segundo Parcial - II",font=text1).place(x=140,y=10)


# Botones
btn_gpio17=Button(v0,text="  GPIO 17-WPI 0    ",command=openGPIO17).place(x=200,y=50)
btn_gpio27=Button(v0,text="  GPIO 27-WPI 2    ",command=openGPIO27).place(x=200,y=90)
btn_gpio21=Button(v0,text="  GPIO 21-WPI 29  ",command=openGPIO21).place(x=200,y=130)
btn_gpio6=Button(v0,text="  GPIO 6 -WPI 22   ",command=openGPIO6).place(x=200,y=170)
btn_gpio26=Button(v0,text=" GPIO 26 -WPI 25  ",command=openGPIO26).place(x=200,y=210)
btn_gpio19=Button(v0,text=" GPIO 19 -WPI 24  ",command=openGPIO19).place(x=200,y=250)


v0.mainloop()