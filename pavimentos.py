# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
from math import log, exp, log10
#creando la ventana
ventana=Tk()
ventana.title("Crear archivo de datos")
ventana.geometry("500x500")

#creando las pestaÃ±as
notebook=ttk.Notebook(ventana)
notebook.pack(fill='both', expand='yes')
intro=ttk.Frame(notebook)
pes0=ttk.Frame(notebook)
pes1=ttk.Frame(notebook)
pes5=ttk.Frame(notebook)
notebook.add(intro, text='Introducción')
notebook.add(pes0, text='Tránsito')
notebook.add(pes1, text='Espesor')
notebook.add(pes5, text='Costos')

##############################################################
####################Introduccion PESTANHA #########################
##############################################################
etiquetat=Label(intro,text="Diseño de Pavimento Rígido",font=("Helvetica", 15)).place(x=110,y=30)
etiquetaparra=Label(intro,text="Universidad Nacional de Colombia, sede Medellín \n Facultad \
de minas \n Elaborado por: Daniel Parra Holguín y Sebastian Cifuentes Cuaran \n 2017",).place(x=60,y=60)
etiquetacred=Label(intro,text="Este programa fue elaborado como parte de un trabajo para \
el curso de pavimentos. \nEn él, se encuentran varios de los cálculos estudiados en la materia; \
se trabaja el \nestudio de tránsito, el diseño de pavimentos rígidos y se añade también \
una opción \npara el cálculo de los costos asociados a los materiales de un kilómetro de carretera."\
                   ,justify="left").place(x=20,y=130)

etiquetainst=Label(intro,text="INSTRUCCIONES: \n 1)   Utilice como separador \
decimal el punto (.).\n 2)   No utilice separador de miles para ningún caso, por ejemplo, para un \
número de \n ejes equivalentes de 20 millones escriba: 20000000. \n 3)   En la etiqueta \
tránsito, encontrará un campo donde se le pide ingresar la lista de \n tránsitos \
promedios diarios (TPD), si posee la lista en una hoja de cálculo o bloc de \n notas \
copie y pegue la lista en el campo, es indiferente si tiene los datos como \n columna o fila. \
Si no posee los datos en una lista, escriba los TPD separados por un \n espacio. \n \
4)   El programa se activa una vez estén todos los campos necesarios diligenciados, \n \
se seleccione una de las alternativas para calcular y presione el botón amarillo. Tanto \n \
el número de ejes equivalentes como el espesor aparecerán en la pantalla del \n programa, \
si esto no ocurre posiblemente uno de los campos necesarios no fue \n llenado correctamente. \n \
5)   Recuerde que la suma de la distribución de camiones debe ser 100%. De igual \n manera, \
el programa imprimirá en pantalla la suma de las distribuciones ingresadas \n para su \
verificación.",justify="left").place(x=20,y=200)

#CANVAS
canvas=Canvas(pes0, width=500, height=500)
canvas.place(x=0, y=0)
"""Cuadrado uno"""
canvas.create_line(10,30, 450, 30, fill="#bebebe")
canvas.create_line(450,30, 450, 145)
canvas.create_line(450,145, 10, 145)
canvas.create_line(10,145, 10, 20,fill="#bebebe")
"""Cuadrado dos"""
canvas.create_line(10,160, 450, 160, fill="#bebebe")
canvas.create_line(450,160, 450, 255)
canvas.create_line(450,255, 10, 255)
canvas.create_line(10,255, 10, 160,fill="#bebebe")
"""Cuadrado tres"""
canvas.create_line(10,270, 450, 270, fill="#bebebe")
canvas.create_line(450,270, 450, 350)
canvas.create_line(450,350, 10, 350)
canvas.create_line(10,350, 10, 270,fill="#bebebe")

#Datos que ingresa el usuario
buses=DoubleVar()
camiones=DoubleVar()
n=IntVar()
lista=StringVar()
dist=StringVar()
FA=ttk.Combobox(pes0)
FC=ttk.Combobox(pes0)
C2P=DoubleVar()
C2G=DoubleVar()
C3=DoubleVar()
C3S2=DoubleVar()
C3S3=DoubleVar()
Ini=IntVar()
Fin=IntVar()
opcionTPD=IntVar()
TPDdado=IntVar()

#Parametros, valores fijos
FEC=[1.5, 3.2, 4.72, 6.15, 5.08, 0.9]

def regresion ():
    #obteniendo datos de la lista
    gString=lista.get().split()
    gFloat=[]
    for i in range (0,len(gString)):
        gFloat.append(float(gString[i]))
    #regresion
    N=len(gFloat)
    Sumx=0
    Sumlogy=0
    Sumx2=0
    Sumxlogy=0
    for i in range (0, len(gFloat)):
        Sumx+=float(i)
        logy=log(gFloat[i])
        Sumlogy+=logy
        Sumx2+=(float(i))**2
        Sumxlogy+=i*logy
    a=(Sumlogy*Sumx2-Sumx*Sumxlogy)/(N*Sumx2-(Sumx)**2)
    a=exp(a)
    b=(N*Sumxlogy-Sumx*Sumlogy)/(N*Sumx2-(Sumx)**2)
    b=exp(b)
    r=b-1
    if opcionTPD.get()==1:
        TPD=a*(b)**(Fin.get()-Ini.get())
    else:
        TPD=TPDdado.get()
    return (TPD,r)
    
def Fcamioncamion():
	dist=leerdist()
	fcc=0
	for i in range (0,len(dist)):
		c=float(dist[i])*FEC[i]/100
		fcc+=c
	return (fcc)

def leerdist():#lectura de las distribuciones para calcular Fcamion
    dFloat=[]
    dFloat.append(C2P.get())
    dFloat.append(C2G.get())
    dFloat.append(C3.get())
    dFloat.append(C3S2.get())
    dFloat.append(C3S3.get())
    return (dFloat)

def Fcamion():
    fcc=Fcamioncamion()
    fc=(fcc*camiones.get()+FEC[-1]*buses.get())/(camiones.get()+buses.get())
    return (fc)   

def Fdireccion():
    if FA.get()=='Dos direcciones: 50%':
        A=50
    else:
        A=100
    return (A)

def Fcarril():
    if FC.get()=='Un carril 100%':
        B=100
    elif FC.get()=='Dos carriles: 90%':
        B=90
    elif FC.get()=='Tres carriles: 70%':
        B=70
    else:
        B=40
    return (B)
 
def N():
    TPD,r=regresion()
    Fc=Fcamion()
    A=Fdireccion()
    B=Fcarril()
    N=TPD*A/100.*B/100.*365.*((1+r)**n.get()-1.)/log(1+r)*Fc
    imprimirN(N)
    return (N)

def imprimirN(N):
    etiqueta=Label(pes0, text= "W18 ="+(str)("{0:.0F}".format(N))).place(x=160, y=430)
    etiquetaW18=Label(pes1, text="W18 calculado:  "+(str)("{0:.0F}".format(N)))\
             .place(x=20, y=39)
    etiquetaDist=Label(pes0, text="SUMA DISTRIBUCIONES = "+(str)("{0:.1F}".format(sumaDist()))\
                       +" %").place(x=20, y=105)
def sumaDist():
    D=leerdist()
    d=0
    for i in range (0, len(D)):
        c=D[i]
        d+=c
    return d
#composicion del tránsito
etiquetaTitu=Label(pes0,text="Composición del tránsito").place(x=10,y=20)
#TPD dado
etiquetaTPD=Label(pes0,text="TPD (si lo tiene):").place(x=20, y=40)
cajaTPD=Entry(pes0, textvariable=TPDdado, width=6).place(x=160,y=40)
#buses        
etiquetaB=Label(pes0, text="Porcentaje de buses:").place(x=20, y=60)
cajaB=Entry(pes0, textvariable=buses, width=6).place(x=160,y=60)
#camiones
etiquetaCamio=Label(pes0, text="Porcentaje de camiones:").place(x=20,y=80)
CajaCamio=Entry(pes0, textvariable=camiones,width=6).place(x=160,y=80)
#distribuciones
etiquetaD=Label(pes0,text="Distribución de \n camiones [%]: ").place (x=210, y=40)
ListaDist=[]
etiqueta1=Label(pes0,text="C2P").place (x=300, y=40)
cajadist1=Entry(pes0, textvariable=C2P, width=10).place(x=340, y=40)

etiqueta2=Label(pes0,text="C2G").place (x=300, y=60)
cajadist2=Entry(pes0, textvariable=C2G, width=10).place(x=340, y=60)

etiqueta3=Label(pes0,text="C3").place (x=300, y=80)
cajadist3=Entry(pes0, textvariable=C3, width=10).place(x=340, y=80)

etiqueta4=Label(pes0,text="C3-S2").place (x=300, y=100)
cajadist4=Entry(pes0, textvariable=C3S2, width=10).place(x=340, y=100)

etiqueta5=Label(pes0,text="C3-S3").place (x=300, y=120)
cajadist5=Entry(pes0, textvariable=C3S3, width=10).place(x=340, y=120)

#Informacion del proyecto
etiquetaproy=Label(pes0, text="Informacion del proyecto").place(x=10, y=150)
#periodo de diseÃ±o
etiquetan=Label(pes0, text="Periodo de diseÃ±o:").place(x=20, y=170)
Cajan=Entry(pes0, textvariable=n, width=5).place(x=210, y=170)
#Ano de inicio del proyecto
etiquetaini=Label(pes0, text="Año de inicio del proyecto:").place(x=20,y=190)
CajaIni=Entry(pes0, textvariable=Fin,width=5).place(x=210, y=190)
#Factor direccion
EtiquetaFA=Label(pes0, text="Ingrese el factor direcciÃ³n en %:").place(x=20,y=210)
FA['values']=('Una direccion: 100%', 'Dos direcciones: 50%' )
FA.place(x=210,y=210)
FA.current(1)
#factor carril
EtiquetaFC=Label(pes0, text="Ingrese el factor carril en %:").place(x=20,y=230)
FC['values']=('Un carril 100%', 'Dos carriles: 90%','Tres carriles: 70%',\
              'cuatro carriles: 40%')
FC.place(x=210,y=230)
FC.current(1)

#Datos para la regresión
etiquetaregre=Label(pes0, text="Datos requeridos para la regresion").place(x=10, y=260)
#Inicio fin, para calcular TPD
etiquetaini=Label(pes0, text="Año inicial de datos:").place(x=20,y=280)
CajaIni=Entry(pes0, textvariable=Ini,width=5).place(x=133, y=280)
#TPD
etiquetatpd=Label(pes0, text="Copie y pegue la lista de TPD:").place(x=20, y=300)
etiquetatpd=Label(pes0, text="(No utilice separador de miles)",\
                  font=("Helvetica",8)).place(x=180, y=300)
cajatpd=Entry(pes0, textvariable=lista, width=70).place(x=20, y=320)

#Radiobutton por si el usuario tiene el TPD
botonNO=Radiobutton(pes0, text="Hallar número de ejes \n equivalentes con la regresion",value=1,\
                    variable=opcionTPD,activebackground="#bebebe").place(x=20, y=355)
botonSI=Radiobutton(pes0, text="Hallar número de ejes \n equivalentes con el TPD dado", value=2,\
                    variable=opcionTPD, activebackground="#bebebe").place(x=210,y=355)

#boton para calcular ejes equivalentes con regresion
boton=Button(pes0, text="Calcular ejes equivalentes", command=N, bg="yellow").place(x=150,y=400)

##############################################################
####################SEGUNDA PESTANHA #########################
##############################################################

#Variables que ingresa el usuario
S0=DoubleVar()
Pi=DoubleVar()
Pf=DoubleVar()
Ec=DoubleVar()
K=DoubleVar()
canvas=Canvas(pes1, width=500, height=500)
canvas.place(x=0, y=0)
"""Cuadrado 1.1"""
canvas.create_line(10,30, 200, 30, fill="#bebebe")
canvas.create_line(200,30, 200, 85)
canvas.create_line(200,85, 10, 85)
canvas.create_line(10,85, 10, 20,fill="#bebebe")
"""Cuadrado 1.2"""
canvas.create_line(220,30, 470, 30, fill="#bebebe")
canvas.create_line(470,30, 470, 85)
canvas.create_line(470,85, 210, 85)
canvas.create_line(210,85, 210, 20,fill="#bebebe")
"""Cuadrado 2.1"""
canvas.create_line(10,100, 200, 100, fill="#bebebe")
canvas.create_line(200,100, 200, 145)
canvas.create_line(200,145, 10, 145)
canvas.create_line(10,145, 10, 100,fill="#bebebe")
"""Cuadrado 2.2"""
canvas.create_line(220,100, 470, 100, fill="#bebebe")
canvas.create_line(470,100, 470, 145)
canvas.create_line(470,145, 210, 145)
canvas.create_line(210,145, 210, 20,fill="#bebebe")
"""Cuadrado 3.1"""
canvas.create_line(10,160, 210, 160, fill="#bebebe")
canvas.create_line(210,160, 210, 265)
canvas.create_line(210,265, 10, 265)
canvas.create_line(10,265, 10, 160,fill="#bebebe")
"""Cuadrado 3.2"""
canvas.create_line(230,160, 470, 160, fill="#bebebe")
canvas.create_line(470,160, 470, 265)
canvas.create_line(470,265, 220, 265)
canvas.create_line(220,265,220,160,fill="#bebebe")
"""Cuadrado 4"""
canvas.create_line(10,280, 470, 280, fill="#bebebe")
canvas.create_line(470,280, 470, 345)
canvas.create_line(470,345, 10, 345)
canvas.create_line(10,345, 10, 280,fill="#bebebe")
#creacion combobox
W18=IntVar()
opcionW18=IntVar()
calificacion=ttk.Combobox(pes1)
tiempo=ttk.Combobox(pes1)
confiabilidad=ttk.Combobox(pes1)
Mres=ttk.Combobox(pes1, width=8)
tipo=ttk.Combobox(pes1,width=15)
soporte=ttk.Combobox(pes1,width=15)
Eci=DoubleVar()
jotadado=DoubleVar()
opcionjota=IntVar()
#Número de ejes equivalentes
etiquetatitu=Label(pes1, text="Número de ejes equivalentes:").place(x=10, y=20)
etiquetaW18=Label(pes1, text="W18 (si lo tiene):").place(x=20,y=63)
cajaW18=Entry(pes1,textvariable=W18, width=10).place(x=120,y=63)
def Zetar():
    if confiabilidad.get()=="50% Zr=0.000":
        Zr=0.000
    elif confiabilidad.get()=="75% Zr=-0.674":
        Zr=-0.674
    elif confiabilidad.get()=="80% Zr=-0.841":
        Zr=-0.841
    elif confiabilidad.get()=="85% Zr=-1.037":
        Zr=-1.037
    elif confiabilidad.get()=="90% Zr=-1.282":
        Zr=-1.282
    elif confiabilidad.get()=="95% Zr=-1.645":
        Zr=-1.645
    elif confiabilidad.get()=="99% Zr=-2.327":
        Zr=-2.327
    else:
        Zr=-3.090
    return Zr
def Cde():
    if calificacion.get() == "Excelente":
        if tiempo.get()== "<1%":
            Cd=1.225
        elif tiempo.get() == "1-5%":
            Cd=1.175
        elif tiempo.get() == "5-25%":
            Cd=1.125
        else:
            Cd=1.1
    elif calificacion.get() == "Bueno":
        if tiempo.get() == "<1%":
            Cd= 1.175
        elif tiempo.get() == "1-5%":
            Cd=1.125
        elif tiempo.get() == "5-25%":
            Cd=1.05
        else:
            Cd=1.0
    elif calificacion.get() == "Regular":
        if tiempo.get()== "<1%":
            Cd=1.125
        elif tiempo.get()== "1-5%":
            Cd=1.05
        elif tiempo.get() == "5-25%":
            Cd=0.95
        else:
            Cd=0.9
    elif calificacion.get() == "Pobre":
        if tiempo.get() == "<1%":
            Cd= 1.05
        elif tiempo.get() == "1-5%":
            Cd=0.95
        elif tiempo.get() == "5-25%":
            Cd=0.85
        else:
            Cd=0.8
    else:
        if tiempo.get() == "<1%":
            Cd=0.95
        elif tiempo.get() == "1-5%":
            Cd=0.85
        elif tiempo.get() == "5-25%":
            Cd=0.75
        else:
            Cd=0.7
    return Cd

def Jota():
    N=Wu18()
    if tipo.get()=="Con pasadores":
        if soporte.get()=="SI":
            J=2.7
        else:
            J=3.2
    elif tipo.get()=="Con refuerzo continuo":
        if soporte.get()=="SI":
            if N <= 300000:
                J=2.8
            elif  300000>N and N<=1000000 :
                J=3.0
            elif 1000000>N and N<=3000000:
                J=3.1
            elif 3000000>N and N<=10000000:
                J=3.2
            elif 10000000>N and N<=30000000:
                J=3.4
            else:
                J=3.6
        else:
            if N <= 300000 :
                J=3.2
            elif  300000>N and N<=1000000 :
                J=3.4
            elif 1000000>N and N<=3000000:
                J=3.6
            elif 3000000>N and N<=10000000:
                J=3.8
            elif 10000000>N and N<=30000000:
                J=4.1
            else:
                J=4.3
    elif tipo.get()=="Sin pasadores":
        if soporte.get()=="SI":
            if 3000000>N and N<=10000000:
                J=2.5
            elif 10000000>N and N<=30000000:
                J=2.6
            else:
                J=2.6
        else:
            if 3000000>N and N<=10000000:
                J=2.9
            elif 10000000>N and N<=30000000:
                J=3.0
            else:
                J=3.1
    return (J)

def Mr():
    
    if Mres.get()=='MR-37':
        Sc=3.7*145.038
    elif Mres.get()=='MR-39':
        Sc=3.9*145.038
    elif Mres.get()=='MR-41':
        Sc=4.1*145.038
    elif Mres.get()=='MR-43':
        Sc=4.3*145.038
    else:
        Sc=4.5*145.038
    return (Sc)
def Ece():
    E=57000*(Eci.get()*145.03775)**0.5
    return E

def jotaopcional():
    if opcionjota.get()==2:
        J=jotadado.get()
    else:
        J=Jota()
    return J
    
etiquetatitu=Label(pes1, text="Confiabilidad (R) y desviación estándar (So)").place(x=210,y=20)
#confiabilidad
etiquetaConf=Label(pes1, text="Zr").place(x=220,y=40)
confiabilidad['values']=("50% Zr=0.000","75% Zr=-0.674","80% Zr=-0.841", "85% Zr=-1.037",\
                         "90% Zr=-1.282", "95% Zr=-1.645","99% Zr=-2.327",\
                         "99.9% Zr=-3.090")
confiabilidad.place(x=240,y=40)
confiabilidad.current(0)

#S0
etiqueta3=Label(pes1,text="S0 ").place(x=220,y=63)
caja3=Entry(pes1,textvariable=S0, width=5).place(x=240,y=63)

#Serviciabilidad
etiquetaser=Label(pes1,text="Serviciabilidad inicial y final").place(x=10, y =90)
etiqueta4=Label(pes1,text="PSI inicial ").place(x=20,y=115)
caja4=Entry(pes1,textvariable=Pi,width=4).place (x=77,y=115)

etiqueta5=Label(pes1,text="PSI final ").place(x=110,y=115)
caja5=Entry(pes1,textvariable=Pf,width=4).place (x=160,y=115)

#CBR de la subrasante
etiquetatitu=Label(pes1, text="Módulo de reacción de la subrasante").place(x=210,y=90)
etiquetaCBR=Label(pes1,text="k [pci]:").place(x=220,y=115)
cajaCBR=Entry(pes1,textvariable=K).place(x=275,y=115)

#Coeficiente Sc
etiquetatitu=Label(pes1, text="Información del concreto").place(x=10,y=150)
EtiquetaMR=Label(pes1, text="Tipo de concreto \n que utilizará (Sc'): ").place(x=20,y=170)
Mres['values']=("MR-37", "MR-39", "MR-41", "MR-43", "MR-45")
Mres.place(x=130,y=177)
Mres.current(1)

#Valor Ec
etiqueta9=Label(pes1,text="Resistencia \n a la compresión \n del concreto [Mpa]: ").place(x=20,y=210)
caja9=Entry(pes1,textvariable=Eci, width=10).place(x=135,y=218)

#Para J
etiquetaJCd=Label(pes1, text="Coeficiente de transmisión de cargas ( J )").place(x=220,y=150)
etiquetaC=Label(pes1, text="Tipo de losa ").place(x=230,y=190)
tipo['values']=('Con pasadores','Con refuerzo continuo','Sin pasadores')
tipo.place(x=325,y=190)
tipo.current(0)
etiquetaT=Label(pes1, text="Soporte Lateral ").place(x=230,y=210)
soporte['values']=('SI','NO')
soporte.place(x=325,y=210)
soporte.current(0)
botonJota=Radiobutton(pes1, text="No tengo jota",value=1,\
                    variable=opcionjota,activebackground="#bebebe").place(x=225, y=167)
botonJotaNO=Radiobutton(pes1, text="Tengo Jota",value=2,\
                    variable=opcionjota,activebackground="#bebebe").place(x=225, y=240)
cajajota=Entry(pes1, textvariable=jotadado, width=5).place(x=325, y=240)

#Cd
etiquetaCd=Label(pes1, text="Coeficiente de drenaje (Cd)").place(x=10,y=270)
etiquetaC=Label(pes1, text="Calificacion del drenaje: ").place(x=20,y=290)
calificacion['values']=('Excelente','Bueno','Regular','Pobre','Muy pobre')
calificacion.place(x=220,y=290)
calificacion.current(0)
etiquetaT=Label(pes1, text="Tiempo de exposición a humedad: ").place(x=20,y=310)
tiempo['values']=("<1%","1-5%","5-25%",">25%")
tiempo.place(x=220,y=310)
tiempo.current(0)

def cm(i):
    centi=i*2.54
    return centi
def imprimirD(i):
    etiqueta=Label(pes1,text="       D = "+(str)("{0:.2F}".format(i))+ " pulg = "+\
                   (str)("{0:.1F}".format(cm(i)))+" cm       ",font=("Helvetica",10))\
                   .place(x=150, y=440)

def Wu18():
    if opcionW18.get()==1:
        W8=N()
    else:
        W8=W18.get()
    return W8

def solucion():
    Zr=Zetar()
    So=S0.get()
    delPSI=Pi.get()-Pf.get()
    pt=Pf.get()
    Sc=Mr()
    Cd=Cde()
    J=jotaopcional()
    Ec=Ece()
    k=K.get()
    i=0
    W18=log10(Wu18())
    dominio=0
    while dominio<=0:
        i+=0.1
        dominio=i**0.75-18.42/((Ec/k)**0.25)
    t2=Zr*So-0.06+log10(delPSI/(4.5-1.5))/(1+1.624*(10**7)/(i+1)**8.46)+\
        7.35*log10(i+1)+(4.22-0.32*pt)*log10(Sc*Cd*(i**0.75-1.132)/(215.63*J*(i**0.75-18.42/(Ec/k)**0.25)))
    
    T=t2
    s=0
    while abs(T-W18)>0.001:
        s+=1
        i+=0.001
        t2=Zr*So+7.35*log10(i+1)+(4.22-0.32*pt)*log10(Sc*Cd*(i**0.75-1.132)/(215.63*J*(i**0.75-18.42/(Ec/k)**0.25)))-\
            0.06+log10(delPSI/(4.5-1.5))/(1+1.624*(10**7)/(i+1)**8.46)
        T=t2
        if s==100000:
            T=W18
    if s==100000:
        s=0
    else:
        imprimirD(i)
    return i


#Radiobutton por si el usuario tiene el W18
botonNO=Radiobutton(pes1, text="Hallar espesor con \n W18 calculado",value=1,\
                    variable=opcionW18,activebackground="#bebebe").place(x=80, y=355)
botonSI=Radiobutton(pes1, text="Hallar espesor con \n W18 dado", value=2,\
                    variable=opcionW18, activebackground="#bebebe").place(x=240,y=355)

boton = Button(pes1, text = "Calcular D", command=solucion,bg="yellow").place(x=200,y=400)

##############################################################
####################TERCERA PESTANHA #########################
##############################################################
#SI LE PONES A LA PESTAÑA NUEVA pes5 NO TENDRÍAS QUE MODIFICAR NADA


#Titulo de la caja
etiquetacostos=Label(pes5, text ='Calcular precio por km de pavimento').place(x=10, y=20)

#Caja
canvas=Canvas(pes5, width=500, height=500)
canvas.place(x=0, y=0)

canvas.create_line(10,30, 450, 30, fill="#bebebe")
canvas.create_line(450,30, 450, 145)
canvas.create_line(450,145, 10, 145)
canvas.create_line(10,145, 10, 30,fill="#bebebe")

sub=DoubleVar()
ps=DoubleVar()
pc=DoubleVar()
ca=DoubleVar()
#titulo
etiquetatitu=Label(pes5, text="Costos por kilómetro de vía").place(x=10, y=20)

#Para la subrasante
etiquetasub=Label(pes5, text='Espesor de la \nsub base [cm]').place (x=30, y=50)
cajasub=Entry(pes5, textvariable=sub, width=10).place(x=140, y=60)

etiquetasubp=Label(pes5, text='Precio de la sub base \n[pesos/metro cúbico]').place (x=220, y=50)
cajasub=Entry(pes5, textvariable=ps, width=10).place(x=360, y=60)

#ParaElConcreto
etiquetacos=Label(pes5, text='Defina ancho \n de carril [m]').place (x=30, y=100)
cajacos=Entry(pes5, textvariable=ca, width=10).place(x=140, y=110)

etiquetacos=Label(pes5, text='Precio del concreto \n[pesos/metro cúbico]').place (x=220, y=100)
cajacos=Entry(pes5, textvariable=pc, width=10).place(x=360, y=110)
#Funcion Costos


def imprimirPrecio(total,volS,volC):
    precio=Label(pes5,text="Costos = "+(str)("{0:.0F}".format(total))+ " COP \n \
                 Volumen de sub-base = "+(str)("{0:.0F}".format(volS))+" m^3 \n \
                 Volumen de concreto = "+(str)("{0:.0F}".format(volC))+ " m^3",\
                 font=("Helvetica",10)).place(x=70, y=240)
def costos():
    D=float(("{0:.1F}".format(cm(solucion()))))
    print (D)
    subra=sub.get()
    precioS=ps.get()
    precioC=pc.get()
    carril=ca.get()
    volS=carril*1000*subra/100
    cs=volS*precioS
    volC=carril*1000*D/100
    cc=volC*precioC
    total=cs+cc
    imprimirPrecio(total,volS,volC)

boton = Button(pes5, text = "Calcular costos", command=costos, bg="yellow").place(x=200,y=180)

ventana.mainloop()

