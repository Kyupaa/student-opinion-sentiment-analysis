import pandas as pd #biblioteca que se utilia para trabajar con datos estrucurados, principalmente tablas, tipo para el excel del kaggle

def cargar_datos():

    #carga/lee el dataset
    df = pd.read_excel("finalDataset0.2.xlsx")
    #mostrar las primeras filas y columnas para confirmar que si se cargaron bien
    print(df.head())
    print(df.columns)
    #crear los arrays
    comentarios = []
    etiquetas = []
    #crear etiquetas y comentarios o sea tuplas
    pares = [
        ("teaching", "teaching.1"),
        ("coursecontent", "coursecontent.1"),
        ("examination", "Examination"),
        ("labwork", "labwork.1"),
        ("library_facilities", " library_facilities"),
        ("extracurricular", "extracurricular.1")
    ]
    # buscar filas donde existan tanto etiquetta como comentario y los guarda, para prepararlos
    for columna_etiqueta, columna_comentario in pares:

        for etiqueta, comentario in zip( #recorrer etiqueta y comentario de par
            df[columna_etiqueta],
            df[columna_comentario]
        ):
            if pd.notna(etiqueta) and pd.notna(comentario): ##recorrer el CONTENIDO de los pares
                comentarios.append(comentario)
                etiquetas.append(etiqueta)

    print("Total de comentarios:", len(comentarios))

    return comentarios, etiquetas