# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
# -*- coding: utf-8 -*-

from conexion import bd

#modulos que dan de alta facturas (falta borrarlas) y gestion de formularios de 
#facturas y ventas
#modulos que dan de alta ventas o servicios en una factur (falta borrarlos)
#aqui puede ir la gestion de la impresion de la factura

def Grabarfac(dnifac, matrifac, marcafac, modelfac, fechafac):
    cursor = bd.cursor()
    registrofac = (dnifac, matrifac, marcafac, modelfac, fechafac)
    if dnifac != "" and  matrifac != "":
        cursor.executemany("""INSERT INTO facturas(dnifac,matrifac, modelfac,marcafac,fechafac) VALUES (?,?,?,?,?);""", (registrofac,))
        bd.commit()
    else:
       return False

def limpiarfac(idfac, dnifac, matrifac, marcafac, modelfac, fechafac):
    idfac.set_text("")
    dnifac.set_text("")
    matrifac.set_text("")
    marcafac.set_text("")
    modelfac.set_text("")
    fechafac.set_text("")
   
def mostrar(listafac, trewFactura, data):
    listafac.clear()
    data = str(data)
    cursor = bd.cursor()
    cursor.execute(""" SELECT idfac, dnifac, matrifac, marcafac, modelfac, fechafac FROM facturas WHERE dnifac=?""", (data,))
    datos = cursor.fetchall()
    datos = filter(None, datos)
    for fila in datos:
        if fila != None:
            listafac.append(fila)
        else:
            print"error"
        trewFactura.show()
        
def Grabarven(dataf, concepto, precio):
    cursor = bd.cursor()
    registroven = (dataf, concepto, precio)
    if concepto != "":
        cursor.executemany("""INSERT INTO ventas(idfac, conceptov, preciov) VALUES (?,?,?);""", (registroven,))
        bd.commit()
    else:
       return False
 
def limpiarven(conce, precio):
     conce.set_text("")
     precio.set_text("")
     
def mostrarven(listaven, trewVentas, dataf):
    listaven.clear()
    dataf = str(dataf)
    cursor = bd.cursor()
    cursor.execute(""" SELECT idv, conceptov, preciov FROM ventas WHERE idfac=?""", (dataf,))
    datosv = cursor.fetchall()
    datosv = filter(None, datosv)
    for fila in datosv:
        if fila != None:
            listaven.append(fila)
        else:
            print"error"
        trewVentas.show() 
    
