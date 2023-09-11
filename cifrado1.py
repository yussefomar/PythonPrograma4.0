
from tkinter import *
from tkinter import messagebox

def limpiar_frame(frame):
    # Elimina todos los widgets del frame
    for widget in frame.winfo_children():
        widget.destroy()
        
def cifrado_cesar(mensaje, clave):
    
   
    mensaje_mayus=mensaje.upper()
    acum_msg_codificado=''
    for letra in mensaje_mayus:
        if(letra!=' '):
            letra_codificada=chr(ord(letra)+clave)
            acum_msg_codificado+=letra_codificada
        else:     
            acum_msg_codificado+=' '
         

    return acum_msg_codificado
    
mensaje='HOLA MUNDO'
print(cifrado_cesar(mensaje,3))


def cifrado_atbash(mensaje):
    clave=1
    codificador={}
    acum_mensaje=''
    abecedario='ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
    for letra in abecedario:
        codificador[letra]=abecedario[-clave]
        clave=clave+1
        
    for letra in mensaje.upper():
        if(letra!=' '):
            acum_mensaje+= codificador[letra]
        else:
            acum_mensaje+=' '
    return acum_mensaje

def guardar_mensaje(frame):
    mensaje = msg.get()
    
    limpiar_frame(frame)
    mostrar_op_cifrado(frame)
    
def cesar_codificado(frame):
    limpiar_frame(frame) 
    msg_codificado.set(cifrado_cesar(msg.get( ), 3))
    mostrar_resp_cifrado(frame)
     

def altbash_codificado(frame):
    limpiar_frame(frame)
    
    msg_codificado.set(cifrado_atbash(msg.get( )))
    mostrar_resp_cifrado(frame)
      
    
def mostrar_op_cifrado(frame):
    label_mensaje=Label(frame,text="Que cifrador deseas usar")
    label_mensaje.grid(row=0, column=0,padx=12, pady=15)
     
     
    button_enviar1=Button(frame,text="Cesar", command=lambda:cesar_codificado(frame))
    button_enviar1.grid(row=3, column=0,padx=12, pady=15)
    button_enviar2=Button(frame,text="Atbash", command=lambda:altbash_codificado(frame))
    button_enviar2.grid(row=3, column=1,padx=12, pady=15)

def mostrar_resp_cifrado(frame):
    label_mensaje=Label(frame,text=msg_codificado.get())
    label_mensaje.grid(row=0, column=0,padx=12, pady=15)
     
def mensaje_inicial(frame):
    label_mensaje=Label(frame,text="engrese el mensaje")
    label_mensaje.grid(row=0, column=0,padx=12, pady=15)
    entry_mensaje=Entry(frame,textvariable=msg)
    entry_mensaje.grid(row=1, column=0,padx=12,pady=15)
    button_enviar=Button(frame,text="enviar", command=lambda:guardar_mensaje(frame))
    button_enviar.grid(row=3, column=0,padx=12,pady=15)     
      
    
ventana=Tk()
msg = StringVar()
msg_codificado = StringVar()
frame=Frame(ventana, width=500, height=500)
frame.pack()
mensaje_inicial(frame)



 
