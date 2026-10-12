from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
#biblioteca para el machine learning y analisis de modelos para medir el desempe;o del programa
def evaluar_clasificacion(etiquetas, predicciones):
    # convertir las etiquetas originales a sentimientos
    etiquetas_sentimiento = []

    for etiqueta in etiquetas:
        if etiqueta == 1:
            etiquetas_sentimiento.append("POSITIVO")
        elif etiqueta == 0:
            etiquetas_sentimiento.append("NEUTRAL")
        elif etiqueta == -1:
            etiquetas_sentimiento.append("NEGATIVO")
    print("\nPrimeras etiquetas originales:")
    print(etiquetas_sentimiento[:10])

    #calcular metricas
    accuracy = accuracy_score(  #porcentaje de todas las predicciones fueron correctas
        etiquetas_sentimiento,
        predicciones
    )

    precision = precision_score( #de lo que dijo, que realmente era lo que dijo jasjdsd / positivo era realmente positivo?
        etiquetas_sentimiento,
        predicciones,
        average="weighted", #de las tres categorias obtiene un promedio dandole mas peso a la que tenga mas registros, en este caso positivo
        zero_division=0 #evitar una division entre cero que pueda causar error
    )

    recall = recall_score( #de los casos que pertenecian a una categoria, cuantas logro encontrar realmente el sistema / de todos los positivos cuantos logre encontrar?
        etiquetas_sentimiento,
        predicciones,
        average="weighted",
        zero_division=0
    )

    f1 = f1_score( #promedia recall y precision
        etiquetas_sentimiento,
        predicciones,
        average="weighted",
        zero_division=0
    )

    print("\n--- EVALUACIÓN DEL SISTEMA ---")
    print("Accuracy:", accuracy)
    print("Precision:", precision)
    print("Recall:", recall)
    print("F1-score:", f1)

    return accuracy, precision, recall, f1