from collections import Counter #biblioteca para contar cuantas veces aparece un elemento
import re #trabajar con expresiones regulares //// secuencia de caracteres que forma un patrón de búsqueda para encontrar, validar o reemplazar textos
def palabras_frecuentes(comentarios):
    texto_completo = " ".join(comentarios).lower() #une todos los comentarios con un espacio entre ellos
    palabras = re.findall(r"\b[a-z]+\b", texto_completo) #palabras que solo contengan caracteres alfabeticos

    palabras_comunes = {
        "the", "and", "is", "are", "to", "of", "a", "in", "for",
        "it", "this", "that", "was", "were", "on", "with", "i",
        "we", "they", "he", "she", "our", "their", "very", "my",
        "as", "be", "but", "or", "not", "have", "has", "had",
        "also", "all", "good"
    }
    # eliminar palabras comunes, las que estan en la lista
    palabras_filtradas = [
        palabra for palabra in palabras
        if palabra not in palabras_comunes
    ]
    # contar frecuencia de las palabras
    frecuencias = Counter(palabras_filtradas)


    print("\n--- PALABRAS MÁS FRECUENTES ---")
    for palabra, cantidad in frecuencias.most_common(15):
        print(palabra, ":", cantidad)

    return frecuencias
    