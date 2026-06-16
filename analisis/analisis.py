#Instalamos las librerias necesarias
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns 

# Código de prueba para verificar que todo está correcto
print("¡Librerías importadas con éxito!")
print(f"Versión de Pandas: {pd.__version__}")
print(f"Versión de Seaborn: {sns.__version__}")

#Cargar los datos
df = pd.read_csv("Top5_League_Players_2017to2024_dataset.csv", sep=';')

#Logica de filtrado
filtro_avanzado = df["pos_"].str.startswith("DF", na=False)
df_filtrado = df[filtro_avanzado]
suma_dinero = df_filtrado["Performance_Gls"].sum()

print("---- Repprte Automatizado ----")
print(f"Monto analizado: USD {suma_dinero: .2f} millones")

#Condicional
if Default_limite_alto := (suma_dinero > 150):
    print("¡Alerta! El monto total supera el limite establecido.")
    print("Requiere revision inmediata")
elif suma_dinero < 100:
    print("Aviso: mercado moderado/alto")
    print("Monitorear comportamiento prox tris")
else:
    print("Mercado estable, sin alertas por el momento.")

#-------------------------------------------------------------
#Grafico de barras usando toda DF
#-------------------------------------------------------------
print("\n[Generando GRAFICO de Barras]")
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10,6))
sns.barplot(
    data=df,
    x="pos_",
    y="Performance_Gls",
    estimator=sum,
    errorbar=None,
    palette="viridis",

)
plt.title("Comparativa de Mercado por tipo de Hardware", fontsize=14)
plt.xticks(rotation=90)

#Guardando grafico generado
plt.savefig("grafico_barra.png", dpi=300)
plt.close()

print("\n¡Hecho! los graficos se guardaron correctamente en tu carpeta")