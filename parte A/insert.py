''''
este script permite a un usuario insertar un nuevo medio de prensa en la base de datos. A través de un terminal, el script realiza una serie de preguntas al usuario. Por ejemplo:
“Indica la información del nuevo medio que quieres añadir con el formato siguiente: nombre, ciudad, region, pais, continente, año de creación”
“Indica una URL de una noticia de este medio”
“Indica la expresión XPATH que permite leer el título de la fecha”

'''





import mysql.connector

# Establecer la conexión con la base de datos
conn = mysql.connector.connect(
    host='tu_host',
    user='tu_usuario',
    password='tu_contraseña',
    database='tu_base_de_datos'
)
cursor = conn.cursor()

# Función para insertar un nuevo registro en la tabla mediosPrensa
def insertar_medio_prensa(nombre_medio, ubicacion, cobertura):
    sql = "INSERT INTO mediosPrensa (nombre_medio, ubicacion, cobertura) VALUES (%s, %s, %s)"
    values = (nombre_medio, ubicacion, cobertura)
    cursor.execute(sql, values)
    conn.commit()

# Función para insertar un nuevo registro en la tabla fundador
def insertar_fundador(nombre_fundador, año_fundado):
    sql = "INSERT INTO fundador (nombre_fundadores, añoFundado) VALUES (%s, %s)"
    values = (nombre_fundador, año_fundado)
    cursor.execute(sql, values)
    conn.commit()

# Función para insertar un nuevo registro en la tabla redesSociales
def insertar_red_social(red_social, seguidores, actualizacion_seguidores, nombre_medio):
    sql = "INSERT INTO redesSociales (redSocial, seguidores, actualizacionSeguidores, nombre_medio) VALUES (%s, %s, %s, %s)"
    values = (red_social, seguidores, actualizacion_seguidores, nombre_medio)
    cursor.execute(sql, values)
    conn.commit()

# Función para insertar un nuevo registro en la tabla sitioWeb
def insertar_sitio_web(nombre_sitio_web, nombre_medio):
    sql = "INSERT INTO sitioWeb (nombre_sitioWeb, nombre_medio) VALUES (%s, %s)"
    values = (nombre_sitio_web, nombre_medio)
    cursor.execute(sql, values)
    conn.commit()

# Función para insertar un nuevo registro en la tabla categoria
def insertar_categoria(nombre_categoria, URL, XPATH, nombre_sitio_web):
    sql = "INSERT INTO categoria (nombre_categoria, URL, XPATH, nombre_sitioWeb) VALUES (%s, %s, %s, %s)"
    values = (nombre_categoria, URL, XPATH, nombre_sitio_web)
    cursor.execute(sql, values)
    conn.commit()

# Función para insertar un nuevo registro en la tabla noticia
def insertar_noticia(URL_noticia, XPATH_titulo, XPATH_fecha, XPATH_contenido, nombre_sitio_web):
    sql = "INSERT INTO noticia (URL_noticia, XPATH_titulo, XPATH_fecha, XPATH_contenido, nombre_sitioWeb) VALUES (%s, %s, %s, %s, %s)"
    values = (URL_noticia, XPATH_titulo, XPATH_fecha, XPATH_contenido, nombre_sitio_web)
    cursor.execute(sql, values)
    conn.commit()

# Cerrar la conexión con la base de datos
conn.close()
