import pandas as pd

## Removing the limits of visible columns
pd.set_option('display.max_columns', None)

## Adding this option, we can adjust the float format, by only using 2 decimals characters.
pd.set_option("display.float_format", "{:.2f}".format)

## Reading the data.
path_data = "../data-analysis/pastas/2023_Viagem.csv"
df_viagens = pd.read_csv(path_data, encoding="Windows-1252", sep=";", decilam=",")

## Creating a new column, with all of the expenses.
df_viagens["Despesas"] = df_viagens["Valor diárias"] + df_viagens["Valor passagens"] + df_viagens["Valor outros gastos"]

## Here were changing the dates, which has string values, to datetime.
df_viagens["Período - Data de início"] = pd.to_datetime(df_viagens["Período - Data de início"],format="%d/%m/%Y")
df_viagens["Período - Data de fim"] = pd.to_datetime(df_viagens["Período - Data de fim"],format="%d/%m/%Y")

## We can also just rename then in a single column. 
df_viagens["Cargo"] = df_viagens["Cargo"].fillna("NÃO IDENTIFICADO")

## Here we get the months names  that the trip started
df_viagens["Mês da viagem"] = df_viagens["Período - Data de início"].dt_month_name()

## Here we collect the amount of days of the trip. Returning in days.
df_viagens["Dias da viagem"] =  df_viagens["Período - Data de fim"] - df_viagens["Período - Data de início"].dt.days # Here only getting the numbers of days.

## We can also change the method "sum()" which add the values, to "mean()" that gets the arithimetic mean.
df_viagens.groupby("Cargo")["Despesas"].mean().reset_index()

## Here we aggregate, a new table, basing the data on another columns of the original table, naming them and passing the method used.
df_travels_consolidates = (
    df_viagens ## We get the table
    .groupby("Cargo") ## Sort by "cargo"
    .agg( ## Aggregate these columns
        mean_expenses=("Despesas", "mean"), ## Based on "Dispesas" and the method "mean"
        mean_days=("Dias de viagem", "mean"),
        total_expenses=("Despesas", "sum"),
        frequent_destination=("Destinos", pd.Series.mode), ## Getting the most frequent destinations
        n_travels=("Nome", "count"), ## counting by name
        )
    .reset_index() ## And using them as the columns
 )

## storing the proportion in a variable
df_cargos = df_viagens["Cargo"].value_counts(normalize=True).reset_index()

## Getting a column, getting a parameter, and filtering also, toget only "Cargo"
relevant_cargos = df_cargos.loc[df_cargos["proportion"] > 0.01, "Cargo"]

## Geting a filter, that checks if the column "Cargo" pairs with the previous filter of proportion > 0.01.
filter = df_travels_consolidates["Cargo"].isin(relevant_cargos)

## And here, applying all of the filters in the aggregate table.
df_final = df_travels_consolidates[filter]

## Creating a bar graph
df_final = df_final.sort_values(by="n_travels", ascending=False)
df_final.plot(x="Cargo", y="n_travels", kind="bar")

