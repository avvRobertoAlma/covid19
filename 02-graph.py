# importo librerie
import json
import urllib.request
import datetime
import pylab as pl 
import sys

# importo librerie interne
from lib.convertIntoDate import convertIntoDate

# argomenti da linea di comando
_regione = sys.argv[1] if len(sys.argv) >= 2 and sys.argv[1] else 'Lazio'
_filtro = sys.argv[2] if len(sys.argv) >= 3 and sys.argv[2] else 'totale_casi'

# leggo il file json
url = "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-regioni.json"
urllib.request.urlretrieve(url, 'data/andamento.json')

import codecs
with codecs.open('data/andamento.json', 'r', 'utf-8-sig') as j:
    andamento = json.load(j)


# estraggo dati regione 
regione = [x for x in andamento if x["denominazione_regione"] == _regione]

start = datetime.datetime(2020, 2, 24)
end = datetime.datetime.now()

# estraggo array di casi
y_regione = [int(x[_filtro]) for x in regione if start <= convertIntoDate(x['data']) <= end]

# disegno grafico 
pl.xlabel('numero di giorni')
pl.ylabel(' '.join(_filtro.split('_')))
pl.plot([i for i in range(len(y_regione))], y_regione, '-^r')
for a,b in zip([i for i in range(len(y_regione))],  y_regione): 
    if a == 5:
        pl.text(a, b, str(b))
    if a == 10:
        pl.text(a, b, str(b))
    if a == len(y_regione)-1:
        pl.text(a, b, str(b))
pl.show()