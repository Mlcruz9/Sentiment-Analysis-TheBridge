import sqlite3
import pandas as pd

# Conectamos con la base de datos
connection = sqlite3.connect("twitter_tb_db")

# Obtenemos un cursor que utilizaremos para hacer las queries
crsr = connection.cursor()
def sql_query(query):

    # Ejecuta la query
    crsr.execute(query)

    # Almacena los datos de la query 
    ans = crsr.fetchall()

    # Obtenemos los nombres de las columnas de la tabla
    names = [description[0] for description in crsr.description]

    return pd.DataFrame(ans,columns=names)