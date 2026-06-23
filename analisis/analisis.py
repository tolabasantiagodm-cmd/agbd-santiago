#Tolaba Santiago - 5to B

#Instalamos las librerias necesarias
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns 

# Cambia la línea de carga de datos para incluir la ruta completa:
df = pd.read_csv("/home/etec/Documentos/agbd-santiago/analisis/Top5_League_Players_2017to2024_dataset.csv", sep=';')

# --- 1. Filas y Columnas ---
filas, columnas = df.shape #!
print("---------------------------------------------")
print(f"La tabla contiene {filas:,} filas y {columnas} columnas")
print("---------------------------------------------")

#--- 2. Coincidencia Exacta ---
liga_objetivo = "La Liga"
filtro_exacto = df["league"] == liga_objetivo
df_liga = df[filtro_exacto]

total_jugadores_liga = len(df_liga)
goles_totales_liga = pd.to_numeric(df_liga["Performance_Gls"], errors='coerce').sum()

print("\n---- Coincidencia Exacta ----")
print(f"Liga seleccionada: {liga_objetivo}")
print(f"Cantidad de registros encontrados: {total_jugadores_liga} jugadores")
print(f"Total de goles anotados en esta liga: {goles_totales_liga:.0f} goles")
print("-----------------------------------------")

#--- 3. Texto Parcial ---
team_parcial = "Arsenal"
filtrito = df["team"] == team_parcial
df_team = df[filtrito]

cantidad_jugadores = len(df_team)

print(f"\n---- Texto Parcial ---")
print(f"Equipo seleccionado: {team_parcial}")
print(f"Total de jugadores en el Arsenal: {cantidad_jugadores}")
print("-----------------------------------------")

#Logica de filtrado
filtro_defensores = df["pos_"].str.startswith("DF", na=False)
df_filtrado = df[filtro_defensores]

# Línea 13 corregida (con 'P' mayúscula y la 'r' de Performance):
goles_defensores = pd.to_numeric(df_filtrado["Performance_Gls"], errors='coerce').sum()

print("---- Goles totales de defensores ----")
print(f"Goles totales anotados por defensores: {goles_defensores: .0f} goles")

#Condicional
if goles_defensores > 150:
    print("¡Alerta! El aporte goleador defensivo es excepcionalmente alto.")
    print("Requiere revisión inmediata del departamento de 'Scouting'.")
elif goles_defensores < 100:
    print("Aviso: Rendimiento goleador defensivo bajo")
    print("Monitorear comportamiento el proximo trimestre")
else:
    print("Aporte goleador estable dentro de los parámetros normales.")

#-------------------------------------------------------------
#            Grafico de barras usando toda DF
#-------------------------------------------------------------
print("\n[Generando GRAFICO de Barras]")
sns.set_theme(style="whitegrid")

plt.figure(figsize=(12,6))

sns.barplot(
    data=df,
    x="pos_",
    y="Performance_Gls",  # <--- Asegúrate de que aquí también diga Performance_Gls
    estimator=sum,
    errorbar=None,
    palette="viridis",
    hue="pos_",
    legend=False
)

plt.title("Comparativa de Goles Totales por Posición de Juego (2017-2024)", fontsize=14)
plt.xlabel("Posición en el Campo", fontsize=12)
plt.ylabel("Total de Goles Anotados", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()

#Guardando grafico generado
plt.savefig("grafico_goles_por_posicion.png", dpi=300)
plt.close()

print("\n¡Hecho! El gráfico 'grafico_goles_por_posicion.png' se guardó correctamente en tu carpeta.")