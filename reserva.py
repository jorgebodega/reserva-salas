import sys, os, yaml, requests, datetime
from lxml import html

################ Manejador de yaml
path = os.path.dirname(os.path.abspath(__file__))
with open(path + '/config.yml', 'r') as configfile:
    config = yaml.load(configfile)
################

################ Inicio de sesion
s = requests.Session()
data = {
    'email':'v130323',
    'password':'149dcf21',
    'login':'onSubmit'
}
s.post("https://web1.fi.upm.es/aulas/index.php", data=data)
################

################ Avanzamos a la pagina de reserva
url_sala = 'https://web1.fi.upm.es/aulas/reservation.php?rid={}'.format(config['Salas'][sys.argv[1]])
url = s.get(url_sala)
################

################ Obtenemos los datos necesarios
################ User_ID
################ CSRF_TOKEN (cambia en cada ejecucion)
xpath_userid = '//*[@id="userName"]'
xpath_token = '//*[@id="csrf_token"]'

tree = html.fromstring(url.content)
userid = tree.xpath(xpath_userid)[0].attrib['data-userid']
token = tree.xpath(xpath_token)[0].attrib['value']
################

################ Dia para la reserva
today = datetime.datetime.today() + datetime.timedelta(days=7)
date = str(today).split(' ')[0]
################

# print (date)
# print(tree.xpath(xpath_userid)[0].attrib['data-userid'])
# print(tree.xpath(xpath_token)[0].attrib['value'])
# print(config['Salas'][sys.argv[1]])

datos_pet = {
    'userId' : userid,
    'scheduleId' : 7,
    'resourceId' : config['Salas'][sys.argv[1]],
    'beginDate' : date,
    'endDate' : date,
    'beginPeriod' : '08:00:00',
    'endPeriod' : '10:00:00',
    'repeatOptions' : 'none',
    'repeatThursday' : 'on',
    'endRepeatDate' : date,
    'reservationTitle' : 'Lo que tu quieras, guapeton',
    'reservationAction' : 'create',
    'seriesUpdateScope' : 'full',
    'CSRF_TOKEN' : tree.xpath(xpath_token)[0].attrib['value']
}

s2 = requests.Session()
peticion = s.post("https://web1.fi.upm.es/aulas/ajax/reservation_save.php", data=datos_pet)

print(peticion.text)
