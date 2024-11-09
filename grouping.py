import pandas as pd

## Setting the path to our files.
path_data = "../data-analysis/pastas/2023_Viagem.csv"

## Here its possible to set the decimal divisor as ",", that is often used in Brazil !
df_viagens = pd.read_csv(path_data, encoding="Windows-1252", sep=";", decimal=",")

## Here it allows us to see all columns, or rows. Setting a limit or not.
pd.set_option('display.max_columns', None)

## Here we created a New column, named "Despesas", that keep track of the expenses in the file.
df_viagens["Despesas"] = df_viagens["Valor diárias"] + df_viagens["Valor passagens"] + df_viagens["Valor outros gastos"]

## This methos conts how many times, a specific "Cargo" appears in the file.
df_viagens["Cargo"].value_counts()

## Here we use proportion in the numbers  on the file, also possible use *100, to get values > 0.
df_viagens["Cargo"].value_counts(normalize=True)

## In this one, besides finding the full numbers, we renamed the name of the column, "Proporçao", and used them as the headers of the columns
(df_viagens["Cargo"].value_counts(normalize=True) * 100).rename("Proporção de viagens").reset_index()
