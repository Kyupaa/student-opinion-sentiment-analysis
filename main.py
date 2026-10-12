from datos import cargar_datos
from limpieza import limpiar_comentarios
from sentimientos import analizar_sentimientos, analizar_nuevo_comentario
from frecuencia import palabras_frecuentes
from evaluacion import evaluar_clasificacion
from graficas import generar_grafica


def mostrar_menu():

    print("\n========================================")
    print("   ANÁLISIS DE OPINIONES ESTUDIANTILES")
    print("========================================")

    print("1. Limpiar textos")
    print("2. Analizar sentimientos")
    print("3. Clasificar comentarios")
    print("4. Palabras más frecuentes")
    print("5. Evaluar clasificación")
    print("6. Generar gráfica")
comentarios, etiquetas = cargar_datos() #funcion para devolver los comentarios y etiquetas

resultados_df = None


while True:

    mostrar_menu()

    opcion = input("\nSelecciona una opción: ")

    match opcion:

        case "1":
            textos_limpios = limpiar_comentarios(comentarios)

            print("\n--- EJEMPLOS DE TEXTOS LIMPIOS ---")

            for i in range(min(10, len(comentarios))): #como max ense;a 10 comentarios pero si hay menos muestra los que haya

                print("\nTexto original:")
                print(comentarios[i])

                print("Texto limpio:")
                print(textos_limpios[i])

                print("-" * 50)


        case "2":
            resultados_df = analizar_sentimientos(comentarios)

            print("\n--- ANÁLISIS DE SENTIMIENTOS ---")

            for _, fila in resultados_df.head(10).iterrows():

                print("-" * 50)
                print("Comentario:", fila["comentario"])
                print("Polaridad:", fila["polaridad"])
                print("Sentimiento:", fila["sentimiento"])

            print("\nAnálisis completado.")


        case "3":
            if resultados_df is None:

                print("\nPrimero debes analizar los sentimientos.")

            else:

                print("\n--- CLASIFICACIÓN DE COMENTARIOS ---")

                conteo = resultados_df["sentimiento"].value_counts()

                print(conteo)


        case "4":
            palabras_frecuentes(comentarios)


        case "5":
            if resultados_df is None:

                print("\nPrimero debes analizar los sentimientos.")

            else:

                predicciones = resultados_df["sentimiento"].tolist()

                evaluar_clasificacion(
                    etiquetas,
                    predicciones
                )


        case "6":
            if resultados_df is None:

                print("\nPrimero debes analizar los sentimientos.")

            else:

                generar_grafica(resultados_df)


        case "7":
            comentario = input(
                "\nEscribe el comentario que deseas analizar:\n"
            )

            if comentario.strip() == "":

                print("\nNo escribiste ningún comentario.")

            else:

                polaridad, sentimiento = analizar_nuevo_comentario(
                    comentario
                )

                print("\n--- RESULTADO ---")
                print("Comentario:", comentario)
                print("Polaridad:", round(polaridad, 2))
                print("Sentimiento:", sentimiento)


        case "0":
            print("\nPrograma finalizado.")
            break


        case _:
            print("\nOpción no válida.")