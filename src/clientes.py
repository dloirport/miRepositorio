#! /usr/bin/python
# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
# -*- coding: utf-8 -*-


from conexion import bd

#modulos que manejan grabar y borrar clientes, y limpiar formularios
# control de dni


def Grabarcli(dni, apel, nom, dir, loc, pro, cp, mov, tel, mail, no):
    cursor = bd.cursor()
    registro = (dni, apel, nom, dir, loc, pro, cp, mov, tel, mail, no)
    if dni != "" and  apel != "":
        cursor.executemany("""INSERT INTO clientes(dnicli,apelcli,nomcli,dircli,poblic,procli,cpcli,movcli,telcli,mailcli,pubcli) VALUES (?,?,?,?,?,?,?,?,?,?,?);""", (registro,))
        bd.commit()
    else:
       return False

def limpiarcli(dni, apel, nom, dir, loc, pro, cp, mov, tel, mail):
    dni.set_text("")
    apel.set_text("")
    dir.set_text("")
    nom.set_text("")
    loc.set_text("")
    pro.set_text("")
    cp.set_text("")
    mov.set_text("")
    tel.set_text("")
    mail.set_text("")

def validoDNI(dni):
    tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
    dig_ext = "XYZ"
    reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}
    numeros = "1234567890"
    dni = dni.upper()
    if len(dni) == 9:
        dig_control = dni[8]
        dni = dni[:8]
        if dni[0] in dig_ext:
            dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
        return len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni)%23] == dig_control
    return False

def mostrar(lista, trewCliente):
    lista.clear()
    cursor = bd.cursor()
    sql = """ SELECT dnicli, apelcli, nomcli, movcli FROM clientes ORDER BY apelcli"""
    cursor.execute(sql)
    datos = cursor.fetchall()
    datos = filter(None, datos)
    for fila in datos:
        if fila != None:
            lista.append(fila)
        else:
            print"error"
        trewCliente.show()

def Borrarcli(dni):
    dni = str(dni)
    cursor = bd.cursor()
    cursor.execute(""" DELETE FROM clientes WHERE dnicli=? """, (dni,))
    bd.commit()
    
    