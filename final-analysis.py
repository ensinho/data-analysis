## Loading Data ##

## We´re using pandas to recieve and manipulate data!
import pandas as pd
## graphs library
import matplotlib.pyplot as plt # type: ignore

## manipulating the year of the graphs
ano = 2023

## Setting the path to our files.
path_data = f"../data-analysis/pastas/{ano}_Viagem.csv"

## Creating an output path
path_output = f"../data-analysis/pastas/tabela{ano}.xlsx"

## creating a pathh  to the figure
path_figure = f"../data-analysis/pastas/figure{ano}.png"


## On the pandas, we use encoding to submit the format of coding in the file
## And the sep, its the separator used, in case its unusual.
df_viagens = pd.read_csv(path_data, encoding="Windows-1252", sep=";")

## Here it allows us to see all columns, or rows. Setting a limit or not.
pd.set_option('display.max_columns', None)
## Adding this option, we can adjust the float format, by only using 2 decimals characters.
pd.set_option("display.float_format", "{:.2f}".format)


## Creating a new column, with all of the expenses.
df_viagens["Despesas"] = df_viagens["Valor diárias"] + df_viagens["Valor passagens"] + df_viagens["Valor outros gastos"]

## We can also just rename then in a single column. 
df_viagens["Cargo"] = df_viagens["Cargo"].fillna("NÃO IDENTIFICADO")

## Here were changing the dates, which has string values, to datetime.
df_viagens["Período - Data de início"] = pd.to_datetime(df_viagens["Período - Data de início"],format="%d/%m/%Y")
df_viagens["Período - Data de fim"] = pd.to_datetime(df_viagens["Período - Data de fim"],format="%d/%m/%Y")

## Here we get the months names  that the trip started
df_viagens["Mês da viagem"] = df_viagens["Período - Data de início"].dt_month_name()
## Here we collect the amount of days of the trip. Returning in days.
df_viagens["Dias da viagem"] =  df_viagens["Período - Data de fim"] - df_viagens["Período - Data de início"].dt.days # Here only getting the numbers of days.

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

## Getting on the final table - consolidated and filtered
df_final = df_travels_consolidates[filter].sort_values(by="n_travels", ascending=False)

## creating the figure
fig, ax = plt.subplots(figsize=(16,6))

## horizontals bars with
ax.barh(df_final["Cargo"], df_final["n_travels"], color="#536674")
## inverting the y axis
ax.invert_yaxis()
## setting the backgroundcolor
ax.set_facecolor("#fff")

## defying the title of the fig
fig.suptitle("Viagens por carbo público (2023)")

## creating a subtitle text
plt.figtext(0.65,0.89,"Fonte: Portal da Transparência", fontsize=8)

## a grid to give a north
plt.grid(color="gray", linestyle="--", linewidth=0.5)

## setting the fontsize of the y labls
plt.yticks(fontsize=8)

## creating a text for the numbers in the x axis
plt.xlabel("Número de viagens")

## saving the figure
plt.savefig(path_figure, bbox_inches="tight")

### We can also merge two tables, for instance: df_viagens.merge(df_passagens) 
### If we add a new path_data, with the 2023_passagens.csv

## converting this path to an excel table 
df_final.to_excel(path_output, index="False")

