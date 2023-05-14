#calculadora funcional usando python y librerias tkinter y math
#link: https://www.youtube.com/watch?v=kbTl3DaFJUk

from tkinter import *

raiz=Tk()

miFrame=Frame(raiz)
miFrame.pack()
operacion=""
i=0
reset_pantalla=False
resultado=0

#--------------PANTALLA-----------------------------------------------------

numeroPantalla=StringVar()


pantalla=Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(background="black", fg="#7c89af", justify="right")

#--------------PULSACIONES TECLADO------------------------------------------

def numeroPulsado(num):
    # global operacion
    # global i
    # global reset_pantalla
    
    # if reset_pantalla!=False:
    #     numeroPantalla.set(num)    
    #     reset_pantalla=False
        
    # else:
    #     if num!="0":
    #         i+=1
    #         if operacion!="":
    #             numeroPantalla.set(num)
    #             operacion=""
    #         else:    
    #             numeroPantalla.set(numeroPantalla.get() + num)
    #     else:
    #         if i>= 1:
    #             i+=1
    #             if operacion!="":
    #                 numeroPantalla.set(num)
    #                 operacion=""
    #             else:    
    #                 numeroPantalla.set(numeroPantalla.get() + num)    
    #         else:
    #             pass
    #         numeroPantalla.set(numeroPantalla.get() + num)
    global operacion
    global reset_pantalla

    if reset_pantalla!=False:
        numeroPantalla.set(num)
        reset_pantalla=False

    else:
        numeroPantalla.set(numeroPantalla.get() + num)
    
#--------------FUNCION SUMA-------------------------------------------------
    
def suma(num):
    global operacion
    global resultado
    global reset_pantalla
    resultado += int(num)#resultado=resultado+int(num)
    operacion="suma"
    reset_pantalla=True    
    numeroPantalla.set(resultado)
    
#--------------FUNCION RESTA-----------------------------------------------
num1=0
contador_resta=0

def resta(num):
	global operacion
	global resultado
	global num1
	global contador_resta
	global reset_pantalla
	if contador_resta==0:
		num1=int(num)
		resultado=num1
	else:
		if contador_resta==1:
			resultado=num1-int(num)
		else:
			resultado=int(resultado)-int(num)	
		numeroPantalla.set(resultado)
		resultado=numeroPantalla.get()

	contador_resta=contador_resta+1
	operacion="resta"
	reset_pantalla=True
    
#--------------FUNCION MULTIPLICACION---------------------------------------
    
def multiplicacion(num):
    global operacion
    global resultado
    resultado *= int(num)#resultado=resultado*int(num)
    operacion="multiplicacion"    
    numeroPantalla.set(resultado)
    
#--------------FUNCION EL_RESULTADO-----------------------------------------

def el_resultado():
    global resultado
    global operacion
    global contador_resta
    global contador_multi
    global contador_divi
 
    if operacion=="suma":
        numeroPantalla.set(resultado+int(numeroPantalla.get()))
        resultado=0
        
    elif operacion=="resta":
        numeroPantalla.set(resultado-int(numeroPantalla.get()))
        resultado=0
        contador_resta=0
    
    elif operacion=="division":
        numeroPantalla.set(resultado/int(numeroPantalla.get()))
        resultado=0
        contador_divi=0
        
    elif operacion=="multiplicacion":
        numeroPantalla.set(resultado*int(numeroPantalla.get()))
        resultado=0
        contador_multi=0


#--------------FILA 1-------------------------------------------------------

boton7=Button(miFrame, text="7", width=3, command=lambda:numeroPulsado("7"))
boton7.grid(row=2, column=1)
boton8=Button(miFrame, text="8", width=3, command=lambda:numeroPulsado("8"))
boton8.grid(row=2, column=2)
boton9=Button(miFrame, text="9", width=3, command=lambda:numeroPulsado("9"))
boton9.grid(row=2, column=3)
botonDiv=Button(miFrame, text="%", width=3)
botonDiv.grid(row=2, column=4)

#--------------FILA 2-------------------------------------------------------

boton4=Button(miFrame, text="4", width=3, command=lambda:numeroPulsado("4"))
boton4.grid(row=3, column=1)
boton5=Button(miFrame, text="5", width=3, command=lambda:numeroPulsado("5"))
boton5.grid(row=3, column=2)
boton6=Button(miFrame, text="6", width=3, command=lambda:numeroPulsado("6"))
boton6.grid(row=3, column=3)
botonMult=Button(miFrame, text="x", width=3, command=lambda:multiplicacion(numeroPantalla.get()))
botonMult.grid(row=3, column=4)

#--------------FILA 3-------------------------------------------------------

boton1=Button(miFrame, text="1", width=3, command=lambda:numeroPulsado("1"))
boton1.grid(row=4, column=1)
boton2=Button(miFrame, text="2", width=3, command=lambda:numeroPulsado("2"))
boton2.grid(row=4, column=2)
boton3=Button(miFrame, text="3", width=3, command=lambda:numeroPulsado("3"))
boton3.grid(row=4, column=3)
botonRest=Button(miFrame, text="-", width=3, command=lambda:resta(numeroPantalla.get()))
botonRest.grid(row=4, column=4)

#--------------FILA 4-------------------------------------------------------

boton0=Button(miFrame, text="0", width=3, command=lambda:numeroPulsado("0"))
boton0.grid(row=5, column=1)
botonComa=Button(miFrame, text=",", width=3, command=lambda:numeroPulsado(","))
botonComa.grid(row=5, column=2)
botonIgual=Button(miFrame, text="=", width=3, command=lambda:el_resultado())
botonIgual.grid(row=5, column=3)
botonSuma=Button(miFrame, text="+", width=3, command=lambda:suma(numeroPantalla.get()))
botonSuma.grid(row=5, column=4)



raiz.mainloop()