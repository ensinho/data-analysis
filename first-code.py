## Loading Data ##

## We´re using pandas to recieve and manipulate data!
import pandas as pd

## Setting the path to our files.
path_data = "../data-analysis/pastas/2023_Viagem.csv"

## On the pandas, we use encoding to submit the format of coding in the file
## And the sep, its the separator used, in case its unusual.
df_viagens = pd.read_csv(path_data, encoding="Windows-1252", sep=";")

## Here it allows us to see all columns, or rows. Setting a limit or not.
pd.set_option('display.max_columns', None)

## Here were only getting this column in specific, also possible with rows.
print(df_viagens["Nome do órgão superior"])


## Creating an array of getting the public organs, and their respective expenses.
columns = ["Nome do órgão superior", "Valor diárias"]
print(df_viagens[columns])

## Panda methods ##

## This one, transforms all of the string into upper case.
print(df_viagens["Nome do órgão superior"].str.upper())

## This one gets the length of each string in the element
print(df_viagens["Nome do órgão superior"].str.len())

## We can use multiple methods on the same element -- On this case
## it replaced the titles of the elements, to an abbreviation. To be more flexible.
print(df_viagens["Nome do órgão superior"].str.upper().str.replace('MINISTÉRIO', 'MIN.'))

## here we can see all of the types in the file.
df_viagens.info()

## Now lets try to calculate all of the expenses ( more than one column ) in each row!
## Were also changing the "," often used in brazilian methods to count money
df_viagens["Valor diárias"] = df_viagens["Valor diárias"].str.replace("," , ".").astype(float)
df_viagens["Valor passagens"] = df_viagens["Valor passagens"].str.replace("," , ".").astype(float)
df_viagens["Valor devolução"] = df_viagens["Valor devolução"].str.replace("," , ".").astype(float)
df_viagens["Valor outros gastos"] = df_viagens["Valor outros gastos"].str.replace("," , ".").astype(float)

print(df_viagens[["Valor diárias","Valor passagens","Valor devolução", "Valor outros gastos"]])

## Here we added the expenses, after changing text changes and changing the type!
## Note: We can use all of operators in any column in the file. like +,-, /
## And using in multiples columns at the same formula!

print(df_viagens["Valor diárias"] + df_viagens["Valor passagens"])
