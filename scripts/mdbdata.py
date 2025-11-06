import pyodbc

db_path = r"C:\Users\Jouke\Desktop\Emergo Dataset\DemoDataBetsyBike.mdb"

try:
    conn = pyodbc.connect(
        fr"Driver={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={db_path};"
    )
    print("✅ Verbinding gelukt!")
    cursor = conn.cursor()
    for row in cursor.tables(tableType='TABLE'):
        print("Tabel:", row.table_name)
    conn.close()
except Exception as e:
    print("❌ Foutmelding:", e)
