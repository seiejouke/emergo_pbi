import pyodbc
import pandas as pd

# === VERBINDING MET ACCESS (.MDB) ===
mdb_path = r"C:\Users\Jouke\Desktop\Emergo Dataset\DemoDataBetsyBike.mdb"
conn_str = (
    r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};"
    fr"DBQ={mdb_path};"
)
conn = pyodbc.connect(conn_str)

# === OPHALEN VAN ALLE TABELLEN ===
cursor = conn.cursor()
tables = [row.table_name for row in cursor.tables(tableType='TABLE')]
print(f"Gevonden tabellen: {tables}")

# === INLADEN VAN ELKE TABEL NAAR EEN DATAFRAME ===
dfs = {}
for table in tables:
    print(f"Inladen van: {table}")
    dfs[table] = pd.read_sql(f"SELECT * FROM [{table}]", conn)

conn.close()
print("Klaar! Alle tabellen zijn ingeladen in pandas.")

# voorbeeld: toegang tot FactSales
df_sales = dfs.get('FactSales')
df_sales.head()
