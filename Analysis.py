#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 20:08:55 2024

@author: juanjo

Data Analysis: Matemática para Ingeniería 2020-2024

-----------------------------------------------------------------------------
1- Importing and cleaning data: data is stored in Excel .xlsx files, and it has
way more informatin than needed. It will be organized in columns as follows:
    cols: Alumno | Legajo | 1P1F | 1P2F | 2P1F | 2P2F | F1 | F2 | Final |
          Condicion | Año | Tipo_Cursada | Virtual
"""
import pandas as pd

path = r""

"""
File: 1_Verano_2020.xlsx
"""
with pd.ExcelFile(path + "1_Verano_2020.xlsx") as file:
    data1 = file.parse("Parciales", skiprows=[0,1], usecols= "B:AF", header=0)

# Filtering rows with students only
data1 = data1[ data1["Alumno"].isnull() == False ]

# Filtering columns
columns = ["Alumno", "Legajo", "Nota", "Nota.1",\
           "Nota.3", "Nota.4", "Nota.6", "Nota.7",\
           "Unnamed: 30", "Unnamed: 31"]
    
data1 = data1[columns]

# Renaming columns
new_columns = {"Nota" : "1P1F",
               "Nota.1" : "1P2F",
               "Nota.3" : "2P1F",
               "Nota.4" : "2P2F",
               "Nota.6" : "F1",
               "Nota.7" : "F2",
               "Unnamed: 30" : "Condicion",
               "Unnamed: 31" : "Final"}

data1.rename(columns = new_columns, inplace=True)

# Adding columns: Año, Tipo_Cursada, Virtual
data1[["Año", "Tipo_Cursada", "Virtual"]] = 2020, "Verano", "No"

"""
File: 2_Intensiva_2020.xlsx
"""
with pd.ExcelFile(path + "2_Intensiva_2020.xlsx") as file:
    data2 = file.parse("Hoja1", skiprows=[0], usecols= "A:X", header=0)
    
# Filtering columns
columns = ["Alumno", "Legajo/DNI", "Parcial", "Recup.", \
           "Parcial.1", "Recup..1", "1° parcial", "2° parcial",\
           "Unnamed: 20", "Unnamed: 22", "Unnamed: 23"]

data2 = data2[columns]

# Renaming columns
new_columns = {"Parcial" : "1P1F",
               "Legajo/DNI" : "Legajo",
               "Recup." : "1P2F",
               "Parcial.1" : "2P1F",
               "Recup..1" : "2P2F",
               "1° parcial" : "F1",
               "2° parcial" : "F2",
               "Unnamed: 20" : "Oral",
               "Unnamed: 22" : "Final",
               "Unnamed: 23" : "Condicion"}

data2.rename(columns = new_columns, inplace=True)

# Adding columns: Año, Tipo_Cursada, Virtual    
data2[["Año", "Tipo_Cursada", "Virtual"]] = 2020, "Anticipada", "Si"

"""
In the following, I will use a function to perform data transform.
"""
# Cleaning data function:

def data_cleaner(data, columns_names, year, tipo_cursada, es_virtual):
    """

    Parameters
    ----------
    data : pandas DataFrame
        Table imported from Excel file
    columns_names : dictionary
        To be used for filtering and renaming of columns.
        Format: {old_name : new_name}
    year : integer
    tipo_cursada : string
        Options: Verano, Intensiva, 1er Semestre
    is_virtual : string
        If it was an online course, select "Yes". Otherwise, select "No"

    Returns
    -------
    pandas DataFrame

    """
    # Filtering rows with students only (first column)
    table = data[ data.iloc[:,0].isnull() == False ]
    # Filtering columns:
    table = table[columns_names.keys()]
    # Renaming columns:
    table.rename( columns=columns_names, inplace=True )
    # Adding columns: Año, Tipo_cursada, Virtual:
    table[["Año", "Tipo_Cursada", "Virtual"]] = year, tipo_cursada, es_virtual
    
    return table

"""
File: 3_Anticipada_2021.xlsx
"""
with pd.ExcelFile(path + "3_Anticipada_2021.xlsx") as file:
    data3 = file.parse("Seguimiento y Resumen", skiprows=[0,1], usecols= "A:AB", header=0)

# Columns names:
columns = {"Alumno" : "Alumno",
           "Legajo" : "Legajo",
           "Parcial" : "1P1F",
           "Recup." : "1P2F",
           "Parcial.1" : "2P1F",
           "Recup..1" : "2P2F",
           "1° parcial" : "F1",
           "2° parcial" : "F2",
           "Unnamed: 24" : "Oral",
           "Unnamed: 26" : "Final",
           "Unnamed: 27" : "Condicion"}

data3 = data_cleaner(data3, columns, 2021, "Anticipada", "Sí")

"""
File: 4_Verano_2022.xlsx
"""
with pd.ExcelFile(path + "4_Verano_2022.xlsx") as file:
    data4 = file.parse("Seguimiento y Resumen", skiprows=[0,1], usecols= "A:Y", header=0)

# Columns names:
columns = {"Alumno" : "Alumno",
           "Legajo" : "Legajo",
           "Parcial" : "1P1F",
           "Recup." : "1P2F",
           "Parcial.1" : "2P1F",
           "Recup..1" : "2P2F",
           "1° parcial" : "F1",
           "2° parcial" : "F2",
           "Unnamed: 23" : "Final",
           "Unnamed: 24" : "Condicion"}

data4 = data_cleaner(data4, columns, 2022, "Verano", "No")

"""
File: 5_G1_1erSem_2022.xlsx
"""
with pd.ExcelFile(path + "5_G1_1erSem_2022.xlsx") as file:
    data5 = file.parse("Seguimiento y Resumen", skiprows=[0,1], usecols= "A:W", header=0)

# Columns names:
columns = {"Alumno" : "Alumno",
           "Legajo" : "Legajo",
           "Parcial" : "1P1F",
           "Recup." : "1P2F",
           "Parcial.1" : "2P1F",
           "Recup..1" : "2P2F",
           "1° parcial" : "F1",
           "2° parcial" : "F2",
           "Unnamed: 21" : "Final",
           "Unnamed: 22" : "Condicion"}

data5 = data_cleaner(data5, columns, 2022, "1er Semestre", "No")
data5["Grupo"] = "G1"

"""
File: 6_G7_1erSem_2022.xlsx
"""
with pd.ExcelFile(path + "6_G7_1erSem_2022.xlsx") as file:
    data6 = file.parse("Seguimiento y Resumen", skiprows=[0,1], usecols= "A:W", header=0)

# Columns names:
columns = {"Alumno" : "Alumno",
           "Legajo" : "Legajo",
           "Parcial" : "1P1F",
           "Recup." : "1P2F",
           "Parcial.1" : "2P1F",
           "Recup..1" : "2P2F",
           "1° parcial" : "F1",
           "2° parcial" : "F2",
           "Unnamed: 21" : "Final",
           "Unnamed: 22" : "Condicion"}

data6 = data_cleaner(data6, columns, 2022, "1er Semestre", "No")
data6["Grupo"] = "G7"

"""
File: 7_Anticipada_2022.xlsx
"""
with pd.ExcelFile(path + "7_Anticipada_2022.xlsx") as file:
    data7 = file.parse("Seguimiento y Resumen", skiprows=[0,1], usecols= "A:W", header=0)

# Columns names:
columns = {"Apellido y Nombre" : "Alumno",
           "Legajo/DNI" : "Legajo",
           "Parcial" : "1P1F",
           "Recup." : "1P2F",
           "Parcial.1" : "2P1F",
           "Recup..1" : "2P2F",
           "1° parcial" : "F1",
           "2° parcial" : "F2",
           "Unnamed: 21" : "Final",
           "Unnamed: 22" : "Condicion"}

data7 = data_cleaner(data7, columns, 2022, "Anticipada", "No")

"""
File: 8_1erSem_2023.xlsx
"""
with pd.ExcelFile(path + "8_1erSem_2023.xlsx") as file:
    data8 = file.parse("Resumen", skiprows=[0,1], usecols= "A:O", header=0)

# Columns names:
columns = {"Apellido y Nombre" : "Alumno",
           "Legajo" : "Legajo",
           "Parcial" : "1P1F",
           "Recup." : "1P2F",
           "Parcial.1" : "2P1F",
           "Recup..1" : "2P2F",
           "1° parcial" : "F1",
           "2° parcial" : "F2",
           "Unnamed: 13" : "Final",
           "Unnamed: 14" : "Condicion"}

data8 = data_cleaner(data8, columns, 2023, "1er Semestre", "No")

"""
File: 9_Anticipada_2023.xlsx
"""
with pd.ExcelFile(path + "9_Anticipada_2023.xlsx") as file:
    data9 = file.parse("Resumen", skiprows=[0,1], usecols= "A:O", header=0)

# Columns names:
columns = {"Apellido y Nombre" : "Alumno",
           "Legajo/DNI" : "Legajo",
           "Parcial" : "1P1F",
           "Recup." : "1P2F",
           "Parcial.1" : "2P1F",
           "Recup..1" : "2P2F",
           "1° parcial" : "F1",
           "2° parcial" : "F2",
           "Unnamed: 13" : "Final",
           "Unnamed: 14" : "Condicion"}

data9 = data_cleaner(data9, columns, 2023, "Anticipada", "No")

"""
File: 10_Verano_2024.xlsx
"""
with pd.ExcelFile(path + "10_Verano_2024.xlsx") as file:
    data10 = file.parse("Resumen", skiprows=[0,1], usecols= "A:P", header=0)

# Columns names:
columns = {"Apellido y Nombre" : "Alumno",
           "Legajo" : "Legajo",
           "Parcial" : "1P1F",
           "Recup." : "1P2F",
           "Parcial.1" : "2P1F",
           "Recup..1" : "2P2F",
           "1° parcial" : "F1",
           "2° parcial" : "F2",
           "Unnamed: 14" : "Final",
           "Unnamed: 15" : "Condicion"}

data10 = data_cleaner(data10, columns, 2024, "Verano", "No")

"""
File: 11_1erSem_2024.xlsx
"""
with pd.ExcelFile(path + "11_1erSem_2024.xlsx") as file:
    data11 = file.parse("Resumen", skiprows=[0,1], usecols= "A:P", header=0)

# Columns names:
columns = {"Apellido y Nombre" : "Alumno",
           "Legajo/DNI" : "Legajo",
           "Parcial" : "1P1F",
           "Recup." : "1P2F",
           "Parcial.1" : "2P1F",
           "Recup..1" : "2P2F",
           "1° parcial" : "F1",
           "2° parcial" : "F2",
           "Unnamed: 14" : "Final",
           "Unnamed: 15" : "Condicion"}

data11 = data_cleaner(data11, columns, 2024, "1er Semestre", "No")

"""
File: 12_Anticipada_2024.xlsx
"""
with pd.ExcelFile(path + "12_Anticipada_2024.xlsx") as file:
    data12 = file.parse("Resumen", skiprows=[0,1], usecols= "E:T", header=0)

# Columns names:
columns = {"Apellido y Nombre" : "Alumno",
           "Legajo/DNI" : "Legajo",
           "Parcial" : "1P1F",
           "Recup." : "1P2F",
           "Parcial.1" : "2P1F",
           "Recup..1" : "2P2F",
           "1° parcial" : "F1",
           "2° parcial" : "F2",
           "Unnamed: 18" : "Final",
           "Unnamed: 19" : "Condicion"}

data12 = data_cleaner(data12, columns, 2024, "Anticipada", "No")

# Creating a unique dataset:
all_data = pd.concat([eval("data" + str(i)) for i in range (1,13)]\
                     , ignore_index = True)

"""
-----------------------------------------------------------------------------
2- Transforming data types and values
"""

# Some numeric values are stored as strings, and there are some categories like
# "Anulado" that have to be interpreted as 0. Moreover, there are numeric values
# with wrong decimal separator that have to be corrected.

# Collecting errors:    
numeric_columns = ["1P1F", "1P2F", "2P1F", "2P2F", "F1", "F2"]
errors = []
for column in numeric_columns:
    try:
        all_data[column].astype("float")       
    except:
        for element in all_data[column]:
            try:
                float(element)
            except:
                errors.append(element)

# Correcting wrong decimal separator:  
for column in numeric_columns:
    wrong_rows = all_data[column].isin(errors)
    corrected_values = all_data[wrong_rows][column].str.replace(",", ".")
    positions = list(corrected_values.index)
    all_data.loc[positions, column] = corrected_values

# Setting non-numeric values to 0:
for column in numeric_columns:
    wrong_rows = all_data[column].isin(errors)
    positions = list(all_data[wrong_rows].index)
    all_data.loc[positions, column] = 0

# Converting numeric columns to float
for column in numeric_columns:
    try:
        all_data[column] = all_data[column].astype("float")
        print(column, "succesfully converted to float")
    except:
        print("type convertion failed")

# Creating categorical column: Tipo_Cursada
all_data["Tipo_Cursada"] = all_data["Tipo_Cursada"].astype("category")

# Setting normalized categories for column "Condicion". The categories are:
# Libre < Abandonó < Desaprobado < Promocionado
# There are some inconsistencies: Desaprobó|Desaprobado, Promocionó|Promocionado
# Fixing inconsistencies:
all_data["Condicion"].replace({"Desaprobó" : "Desaprobado",
                               "Promocionó" : "Promocionado"}\
                              , inplace = True)

# Creating categorical column: Condicion
all_data["Condicion"] = all_data["Condicion"].astype("category")
all_data["Condicion"] = all_data["Condicion"].cat.set_categories(
                            ["Libre", "Abandonó", "Desaprobado", "Promocionado"],
                            ordered = True)

"""
3- Hiding personal data
The "Alumno" and "Legajo" columns are confidential. I will remove those columns
"""

all_data = all_data.drop(columns = ["Alumno", "Legajo"])

# Inpsecting dtypes of final dataset
print(all_data.dtypes)

# Exporting to a txt. file
all_data.to_csv("Mate_PI_2020_2024.csv")