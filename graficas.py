import matplotlib.pyplot as plt #sirve pa crear la grafica y visualizarla


def generar_grafica(resultados_df): #df y sentimientos se otienen pues de sentimientos.py jaja

    # Contar la cantidad de comentarios por sentimiento tomando en cuenta solo la columna de sentimiento
    conteo_sentimientos = resultados_df["sentimiento"].value_counts()

    print("\nCantidad de comentarios por sentimiento:")
    print(conteo_sentimientos)

    # generamos grafica
    conteo_sentimientos.plot(kind="bar")

    plt.title("Distribución de sentimientos")
    plt.xlabel("Sentimiento")
    plt.ylabel("Cantidad de comentarios")
    plt.xticks(rotation=0) #sin esto las palabras podrian salir inclinadas

    plt.tight_layout()
    plt.show()