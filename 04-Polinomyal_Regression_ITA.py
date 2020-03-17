# importo pandas e numpy
import pandas as pd 
import numpy as np 
import json
import urllib.request
import datetime
import pylab as pl 
import sys 

_filtro = sys.argv[1] if len(sys.argv) >= 2 and sys.argv[1] else 'totale_casi'
_degree = int(sys.argv[2]) if len(sys.argv) >= 3 and sys.argv[2] else 5

#importo la funzione train_test_split di scikit_learn
from sklearn.model_selection import train_test_split

from sklearn.preprocessing import PolynomialFeatures

# importo la LinearRegression di scikit learn
from sklearn.linear_model import LinearRegression

# leggo il file json
url = "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-andamento-nazionale.json"
urllib.request.urlretrieve(url, 'data/andamento_ITA.json')

import codecs
with codecs.open('data/andamento_ITA.json', 'r', 'utf-8-sig') as j:
    andamento = json.load(j)

# ottengo dati della regione
regione = [x[_filtro] for x in andamento]
data = [[i, regione[i]] for i in range(len(regione))]

# creo array numpy (una colonna e numero di righe sconosciuto)
X = np.array(data)[:,0].reshape(-1,1)
Y = np.array(data)[:,1].reshape(-1,1)


to_predict_x = [len(regione)+i for i in range(3)]
to_predict_x = np.array(to_predict_x).reshape(-1, 1)

# Polinomyal
p = PolynomialFeatures(degree=_degree)
X_poly = p.fit_transform(X)
to_predict_x_poly = p.transform(to_predict_x)


# istanzio la regressione lineare
lr = LinearRegression()
lr.fit(X_poly, Y)

y_pred_train = lr.predict(X_poly)
y_pred = lr.predict(to_predict_x_poly)

y_total = np.append(y_pred_train, y_pred)
x_total = np.append(X, to_predict_x).reshape(-1, 1)
print(x_total)


import matplotlib.pyplot as plt

plt.title(f'Predizione Nazionale')  
plt.xlabel('giorni')  
plt.ylabel(' '.join(_filtro.split('_'))) 
plt.scatter(X,Y,color="blue")

# regression line
plt.plot(x_total,y_total,color="red")
for a,b in zip([i for i in range(len(y_total))],  y_total): 
    if a == len(y_total)-1:
        pl.text(a, b, str(int(round(b))))
plt.show()
