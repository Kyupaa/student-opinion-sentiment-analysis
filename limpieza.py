import re  # para trabajar con expresiones regulares

def limpiar_comentarios(comentarios):

    textos_limpios = []
    for comentario in comentarios:
        texto = comentario.lower()
        # Eliminar signos de puntuación y números
        texto = re.sub(
            r'[^a-záéíóúüñ\s]',
            '',
            texto
        )
        # Separar el texto en palabras
        palabras = texto.split()
        # Palabras que no aportan mucho al análisis
        palabras_comunes = {
            "the", "and", "is", "are", "to", "of", "a", "in",
            "for", "it", "this", "that", "was", "were", "on",
            "with", "i", "we", "they", "he", "she", "our",
            "their", "very", "as", "be", "but", "or", "not",
            "have", "has", "had", "my"
        }
        # Eliminar palabras comunes
        palabras_importantes = [
            palabra for palabra in palabras
            if palabra not in palabras_comunes
        ]
        # Volver a unir las palabras
        textos_limpios.append(
            " ".join(palabras_importantes)
        )

    return textos_limpios