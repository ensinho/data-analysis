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

## By doing this, we first grouped them by "Cargos", and geting all of "Despesas" of each one.
## After this, we added the values, and organizes them as headers of the columns, also sorting them by the most expensive "Despesas".
## But, its sorted reversly and with the numbers disorganized. Lets correct that! 
df_viagens.groupby("Cargo")["Despesas"].sum().reset_index().sort_values(by="Despesas", ascending=False) # We added ascending, to be descendent.

## We can also change the method "sum()" which add the values, to "mean()" that gets the arithimetic mean.
df_viagens.groupby("Cargo")["Despesas"].mean().reset_index().sort_values(by="Despesas", ascending=False) 
## Also theres the mathod "max()" that will get the HIGHEST value in the column, or "min()" that is the lowest.
## And also there is the "first()" and "last()". They get the first or the last occurency in the table.

## The percentage of travels by "Cargo" in the tabvle. Storig in a variable.
percentage_travels = (df_viagens["Cargo"].value_counts(normalize=True) * 100).rename("Proporção de viagens").reset_index()

## Were comparing in the columns to get all of the values lesser than 1%, to be False, then excluded.
## Filtering the values, by > 1%
filter_1Percent = percentage_travels["Proporção de viagens"] > 1

## Now we get the filtered table, with all of the "Cargos" with the values bigger than 1%.
percentage_travels[filter_1Percent]

## This filter checks if in the column "Cargo" starts with "TECNICO".
filter_tecnico = percentage_travels["Cargo"].str.startswith("TECNICO")

## And here we are getting BOTH filters, in the table, to get a more fluid table.
## Note, that we get only "Cargo" "TECNICO".
percentage_travels[filter_tecnico & filter_1Percent]

## Storing in a variable, all of the expenses by "Cargo"
total_expenses_byCargo = df_viagens.groupby("Cargo")["Despesas"].sum().reset_index()

## And applying in the same row, the filter, that checks only the values bigger than 10 million.
## Its very common, to create parameters / filters on the moment, because its probably gonna be used 1 or 2 times max. Sparing some work.
total_expenses_byCargo[total_expenses_byCargo["Despesas"] > 10000000]

## Here, we remove rows that has NaN as values, in the column "Cargo"
df_viagens.dropna(subset="Cargo")

## And here, were changing all of the NaN to a custom string.
df_viagens.fillna("NÃO IDENTIFICADO")

## We can also just rename then in a single column. 
df_viagens["Cargo"] = df_viagens["Cargo"].fillna("NÃO IDENTIFICADO")


