#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from datetime import datetime, timedelta
from json import load
from lxml import html
from requests import Session

################ Manejador de JSON
CONFIG = load(open('CONFIG.json'))
################

################ manejadores
USER = CONFIG['Usuarios'][sys.argv[3]]
SALA = CONFIG['Salas'][sys.argv[1]]
INTER = CONFIG['Intervalos'][sys.argv[2]]
DIAS = sys.argv[4]
FLAG = bool(len(sys.argv) == 6 and sys.argv[5] == '-d')
################

################ Inicio de sesion
SESSION = Session()
login = {
    'email': USER['Usuario'],
    'password': USER['Pass'],
    'login': 'onSubmit'
}
if FLAG: print('Realizando login con usuario: {}'.format(USER['Usuario']))
SESSION.post("https://web1.fi.upm.es/aulas/index.php", data=login)
################

################ Avanzamos a la pagina de reserva
url_sala = 'https://web1.fi.upm.es/aulas/reservation.php?rid={}'.format(SALA)
if FLAG: print('Obteniendo el resultado para la reserva de la sala: {}'.format(sys.argv[1]))
url = SESSION.get(url_sala)
if FLAG: print('Resultado de la petición: {}'.format(url.status_code))
if url.status_code != 200:
    print('Algo fallo!')
    raise Exception
################

################ Obtenemos los datos necesarios
################ User_ID
################ CSRF_TOKEN (cambia en cada ejecucion)
tree = html.fromstring(url.content)
xpath_userid = '//*[@id="userName"]'
xpath_token = '//*[@id="csrf_token"]'

userid = tree.xpath(xpath_userid)[0].attrib['data-userid']
if FLAG: print('Tu UserID: {}'.format(userid))
token = tree.xpath(xpath_token)[0].attrib['value']
if FLAG: print('Token CSRF para la peticion: {}'.format(token))
################

################ Dia para la reserva
today = datetime.today() + timedelta(days=int(DIAS))
date = str(today).split(' ')[0]
if FLAG: print('Dia pedido para la reserva: {}'.format(date))
if FLAG: print('Intervalo pedido para la reserva: {} - {}'.format(INTER['beginPeriod'], INTER['endPeriod']))
################

################ Peticion al servidor
datos_pet = {
    'userId' : userid,
    'scheduleId' : 7,
    'resourceId' : SALA,
    'beginDate' : date,
    'endDate' : date,
    'beginPeriod' : INTER['beginPeriod'],
    'endPeriod' : INTER['endPeriod'],
    'repeatOptions' : 'none',
    'repeatThursday' : 'on',
    'endRepeatDate' : date,
    'reservationTitle' : USER['Title'],
    'reservationAction' : 'create',
    'seriesUpdateScope' : 'full',
    'CSRF_TOKEN' : token
}
peticion = SESSION.post("https://web1.fi.upm.es/aulas/ajax/reservation_save.php", data=datos_pet)
if FLAG: print('Resultado de la query: {}'.format(peticion.status_code))
if FLAG:
    if peticion.status_code == 200:
        print('Peticion correcta. Comprueba que se ha reservado.')
        print('Si se pasa de plazo, has reservado ya o demasiados dias a futuro no reserva.')
    else:
        print('Fallo en la peticion.')
        print(peticion.text)

close_session = SESSION.get('https://web1.fi.upm.es/aulas/logout.php')
if FLAG: print('Cerrando sesión')
################
