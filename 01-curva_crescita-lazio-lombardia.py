# importo librerie
import json
import urllib.request
import datetime
import pylab as pl 

# importo librerie interne
from lib.convertIntoDate import convertIntoDate

# leggo il file json
url = "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-regioni.json"
urllib.request.urlretrieve(url, 'data/andamento.json')

import codecs
with codecs.open('data/andamento.json', 'r', 'utf-8-sig') as j:
    andamento = json.load(j)


# estraggo dati regione lombardia
lombardia = [x for x in andamento if x["denominazione_regione"] == 'Lombardia' ]
# estraggo dati regione lazio
lazio = [x for x in andamento if x["denominazione_regione"] == 'Lazio']

start_lazio = datetime.datetime(2020, 3, 11)
end_lazio = datetime.datetime.now()

start_lombardia = datetime.datetime(2020, 2, 24)
end_lombardia = start_lombardia + datetime.timedelta((end_lazio - start_lazio).days)


# estraggo array di casi
y_lombardia = [int(x['totale_attualmente_positivi']) for x in lombardia if start_lombardia <= convertIntoDate(x['data']) <= end_lombardia]
y_lazio = [int(x['totale_attualmente_positivi']) for x in lazio if start_lazio <= convertIntoDate(x['data']) <= end_lazio]

print(y_lombardia)
print(y_lazio)
# disegno grafico 
pl.xlabel('numero di giorni')
pl.ylabel('totale attualmente positivi')
pl.plot([i for i in range(len(y_lombardia))], y_lombardia, '-^r')
for a,b in zip([i for i in range(len(y_lombardia))],  y_lombardia): 
    if a == len(y_lombardia)-1:
        pl.text(a, b, str(b))
pl.plot([i for i in range(len(y_lazio))], y_lazio, '-^c')
for a,b in zip([i for i in range(len(y_lazio))],  y_lazio): 
    if a == len(y_lazio)-1:
        pl.text(a, b, str(b))
pl.show()