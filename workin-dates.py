import pandas as pd

## Removing the limits of visible columns
pd.set_option('display.max_columns', None)

## Adding this option, we can adjust the float format, by only using 2 decimals characters.
pd.set_option("displau.float_format", "{:.2f}".format)

## Reading the data.
path_data = "../data-analysis/pastas/2023_Viagem.csv"
df_viagens = pd.read_csv(path_data, encoding="Windows-1252", sep=";", decilam=",")

## Creating a new column, with all of the expenses.
df_viagens["Despesas"] = df_viagens["Valor diárias"] + df_viagens["Valor passagens"] + df_viagens["Valor outros gastos"]

## Here were changing the dates, which has string values, to datetime.
df_viagens["Período - Data de início"] = pd.to_datetime(df_viagens["Período - Data de início"],format="%d/%m/%Y")
df_viagens["Período - Data de fim"] = pd.to_datetime(df_viagens["Período - Data de fim"],format="%d/%m/%Y")

## Here we get the months names  that the trip started
df_viagens["Mês da viagem"] = df_viagens["Período - Data de início"].dt_month_name()

## Here we collect the amount of days of the trip. Returning in days.
df_viagens["Dias da viagem"] =  df_viagens["Período - Data de fim"] - df_viagens["Período - Data de início"].dt.days # Here only getting the numbers of days.

