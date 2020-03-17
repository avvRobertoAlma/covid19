# covid19
Simple tool in Python to analyze data and making simple predictions using a Polynomial Regression

## To run

1. Clone repository
2. Install requirements
3. Run Commands (see below)

## 01-curva_crescita-lazio-lombardia.py

- Shows total positive cases between two dates in Lazio and Lombardia.
- Initial date Lombardia (24.02.2020) 
- Initial date Lazio (11.03.2020)

## 02-graph.py

To run: `python3 02-graph.py [-nomeregione] [-tipodati]

> Ex: `python3 02-graph.py 'Lombardia' 'totale_casi'`

### 03-Polynominal_Regression.py

Shows predictions for region and data 

To run: `python3 03-Polynominal_Regression.py [-nomeregione] [-tipodati] [-degree]

> Ex: `python3 02-graph.py 'Lombardia' 'totale_casi' 5`
> If degree is not set, the default value is 5

### 04-Polynominal_Regression_ITA.py

Shows predictions for ITA 

To run: `python3 03-Polynominal_Regression.py [-tipodati] [-degree]

> Ex: `python3 02-graph.py 'totale_casi' 5`
> If degree is not set, the default value is 5

The script always collects updated data from official sources.
