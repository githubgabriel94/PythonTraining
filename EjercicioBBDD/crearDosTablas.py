import sqlite3
import random

categorias = [('Fácil'), ('Intermedio'), ('Avanzado')]
cursos = [('Python'), ('Java'), ('iOS'), ('Android'), ('SQL'), ('React'), ('UE5')]

conexion = sqlite3.connect("Trainning")

cursor = conexion.cursor()

def crearBBDD():
    cursor.execute("CREATE TABLE IF NOT EXISTS categorias (id INTEGER PRIMARY KEY AUTOINCREMENT ,nombre VARCHAR(100) UNIQUE NOT NULL)")
    cursor.execute("CREATE TABLE IF NOT EXISTS cursos (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre VARCHAR(100) UNIQUE NOT NULL, categoria_id INTEGER NOT NULL, FOREIGN KEY(categoria_id) REFERENCES categoria(id))")

def cargarTablaCategorias(cat):
    try:
        cursor.execute("INSERT INTO categorias (nombre) VALUES (?)", (cat,))
        conexion.commit()
    except sqlite3.IntegrityError as e:
        print("Error insertando nueva categoría: " , e)

cat = cursor

def cargarCursos(cur, cat):
    try:
        cursor.execute("INSERT INTO cursos (nombre, categoria_id) VALUES (?, ?)", (cur, cat))
        conexion.commit()
    except sqlite3.IntegrityError as e:
        print("Error insertando nuevo curso: " , e)

def recuperarCursosPorCategoria(cat):
        cursor.execute("SELECT id FROM categorias WHERE nombre = ?", (cat,))
        resultadoId = cursor.fetchone()
        for c in resultadoId:
            cursor.execute("SELECT * FROM cursos WHERE categoria_id = ?", (c,))
            resultadoCursos = cursor.fetchall()
            if not resultadoCursos:
                print("No hay ningun curso con esta categoría.")
                categoriaExiste()
            else:
                print(resultadoCursos)
    

crearBBDD()

for categoria in categorias:
    cargarTablaCategorias(categoria)

for curso in cursos:
    categoria = random.choice(categorias)
    cursor.execute("SELECT id FROM categorias WHERE nombre = ?", (categoria,))
    resultado = cursor.fetchone()
    for c in resultado:
        cargarCursos(curso, c)

def categoriaExiste():
    categoriaUsuario = input("De que categoría quieres ver los cursos?: ")
    if categoriaUsuario in categorias:
        recuperarCursosPorCategoria(categoriaUsuario)
    else: 
        print("La categoría solicitada no existe.")
        categoriaExiste()

categoriaExiste()

conexion.close()