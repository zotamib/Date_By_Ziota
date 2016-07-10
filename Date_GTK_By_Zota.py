#!/usr/bin/python
#UTILIZA ESTE SCRIPT PARA IMPRIMIR LA FECHA ACTUAL EN PANTALLA.
#SUPPORT zuno_systems@hotmail.com
#Powered By Zota.

import gtk

import time



Fecha = time.strftime("%d/%m/%y")

Zota= gtk.Window()

Hoy = gtk.Label(Fecha)

Zota.add(Hoy)

Zota.show_all()

gtk.main()
