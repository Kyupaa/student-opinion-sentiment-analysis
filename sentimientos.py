from textblob import TextBlob #libreria para analizar el sentimiento de los comentarios
#textblob ya trae su diccionario de palabras para poder medir la polaridad equivalente a su decimal segun las palabras
import pandas as pd #trabajar con datos y tablas, por el excel
def analizar_sentimientos(comentarios):
    resultados = []
    # analizar con textblol
    for comentario in comentarios:
        analisis = TextBlob(str(comentario))
        polaridad = analisis.sentiment.polarity

        if polaridad > 0:
            sentimiento = "POSITIVO"
        elif polaridad < 0:
            sentimiento = "NEGATIVO"
        else:
            sentimiento = "NEUTRAL"
        resultados.append(
            (comentario, polaridad, sentimiento)
        )

    resultados_df = pd.DataFrame( #crea la tabla
        resultados,
        columns=["comentario", "polaridad", "sentimiento"]
    )
    return resultados_df

def analizar_nuevo_comentario(comentario):
    analisis = TextBlob(str(comentario))
    polaridad = analisis.sentiment.polarity

    if polaridad > 0:
        sentimiento = "POSITIVO"
    elif polaridad < 0:
        sentimiento = "NEGATIVO"
    else:
        sentimiento = "NEUTRAL"

    return polaridad, sentimiento