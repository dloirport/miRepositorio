# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import os

from conexion import bd
from fpdf import FPDF

def imprimir(fac,mat,dni):
    pdf = FPDF()
    pdf.add_page()
    header(pdf,fac,mat,dni)
    nombreArchivo = 'Factura'+fac+'.pdf'
    
    pdf.output('/home/dloirport/facturas/'+nombreArchivo,dest='F')
    ruta = '/usr/bin/evince /home/dloirport/facturas/'+nombreArchivo
    os.system(ruta)
    
        
def header(pdf,fac,mat,dni):
    pdf.set_font('Arial','B',12)
    pdf.cell(80,10,'EL TALLER DE LAS IDEAS S.L.',0,1,'C')
    pdf.set_font('Arial','',10)
    pdf.cell(80,10,'Calle Senra, 12  Marin (Pontevedra)',0,1,'C')
    pdf.cell(80,10,'C.P: 36911 Tlfo: 986 882 211-656 565 918',0,1,'C')
    pdf.image('logo.png',140,10,60,25,'png','')
    pdf.set_font('Times','B',12)
    pdf.cell(0,10,'Factura numero: %s ' % fac,0,1,'R')
    pdf.line(5,50,200,50)
    pdf.set_font('Times','B',14)
    pdf.cell(60,10,'DATOS CLIENTE:',0,1,'L')
    pdf.set_font('Times','B',12)
    cursor = bd.cursor()
    cursor.execute(""" SELECT dnicli, apelcli, nomcli, dircli, poblic, procli, cpcli FROM clientes WHERE dnicli=?""", (dni,))
    datos = cursor.fetchall()
    for fila in datos:
        #Nombre cliente
        pdf.set_font('Times','B',12)
        pdf.cell(25,10,'Nombre: ',0,0,'L')
        pdf.set_font('Times','',12)
        pdf.cell(25,10,'%s' % fila[1]+',  %s' % fila[2],0,0,'L')
        pdf.set_font('Times','B',12)
        pdf.cell(118,10,'Matricula Vehiculo:',0,0,'R')
        pdf.set_font('Times','U',12)
        pdf.cell(20,10,'%s ' %mat,0,1,'R')
        #pdf.cell(20,10,'%s' % fila[2],0,1,'L')
        #Direccion
        pdf.set_font('Times','B',12)
        pdf.cell(25,10,'Direccion:  ',0,0,'L')
        pdf.set_font('Times','',12)
        pdf.cell(25,10,'%s' % fila[3]+'  %s' % fila[4],0,1,'L')
        #pdf.cell(50,10,'%s' % fila[4],0,0,'R')
        pdf.set_font('Times','B',12)
        #Cod Postal
        pdf.cell(25,10,'Cod. Post: ',0,0,'L')
        pdf.set_font('Times','',12)
        pdf.cell(25,10,'%s' % fila[6] + ' - %s' % fila[5],0,1,'L')
        #pdf.cell(50,10,'%s' % fila[5],0,0,'L')
        pdf.line(5,95,200,95)
        
        #pdf.set_font('Times','B',14)
        pdf.cell(60,10,'',0,1,'L')
        #pdf.set_font('Times','B',12)
        
        #Cabecera de la tabla
        #pdf.cell(0,10,'',0,1,'L')
        pdf.set_font('Times','BI',14)
        pdf.cell(22,10,'Codigo',1,0,'C')
        pdf.cell(122,10,'Concepto',1,0,'C')
        pdf.cell(45,10,'Precio',1,1,'C')
        
        cursor2 = bd.cursor()
        cursor2.execute("""select idv,conceptov,preciov from ventas where idfac=?""",(fac,))
        datos2 = cursor2.fetchall()
       
        
        total = 0
        
        for fila2 in datos2:
            pdf.set_font('Times','',12)
            pdf.cell(22,10,'%s' % fila2[0],1,0,'C')
            pdf.cell(122,10,'%s' % fila2[1],1,0,'C')
            precio=fila2[2]
            pdf.cell(45,10,'%s' % precio,1,1,'C')
            total = total+float(fila2[2])


        #Precio sin IVA
        pdf.cell(144,10,'Total Sin IVA: ',0,0,'R')
        pdf.set_font('Times','I',12)
        totalsiniva = float(total)
        pdf.cell(45,10,'%s' % round(totalsiniva,2),1,1,'C')
        
        #IVA
        pdf.cell(144,10,'IVA(21%): ',0,0,'R')
        pdf.set_font('Times','I',12)
        iva = float(total*0.21)
        pdf.cell(45,10,'%s' % round(iva,2),1,1,'C')
        
        #Imprime total
        pdf.set_font('Times','B',14)
        pdf.cell(144,10,'Total: ',0,0,'R')
        pdf.set_font('Times','BI',14)
        pdf.set_text_color(247,94,37)
        pdf.cell(45,10,'%s' % round(iva+totalsiniva,2) + '$',1,1,'C')
        


    
