-- Crear la base de datos
CREATE DATABASE nombre_basedatos;

-- Usar la base de datos
USE nombre_basedatos;

-- Creación de las tablas
CREATE TABLE mediosPrensa (
  nombre_medio VARCHAR(100) PRIMARY KEY,
  ubicacion VARCHAR(100),
  cobertura VARCHAR(100)
);

CREATE TABLE fundador (
  nombre_fundadores VARCHAR(100) PRIMARY KEY,
  añoFundado INTEGER
);

CREATE TABLE redesSociales (
  redSocial VARCHAR(100) PRIMARY KEY,
  seguidores INTEGER,
  actualizacionSeguidores DATE,
  nombre_medio VARCHAR(100),
  FOREIGN KEY (nombre_medio) REFERENCES mediosPrensa(nombre_medio)
);

CREATE TABLE sitioWeb (
  nombre_sitioWeb VARCHAR(100) PRIMARY KEY,
  nombre_medio VARCHAR(100),
  FOREIGN KEY (nombre_medio) REFERENCES mediosPrensa(nombre_medio)
);

CREATE TABLE categoria (
  nombre_categoria VARCHAR(100) PRIMARY KEY,
  URL VARCHAR(100),
  XPATH VARCHAR(100),
  nombre_sitioWeb VARCHAR(100),
  FOREIGN KEY (nombre_sitioWeb) REFERENCES sitioWeb(nombre_sitioWeb)
);

CREATE TABLE noticia (
  URL_noticia VARCHAR(100) PRIMARY KEY,
  XPATH_titulo VARCHAR(100),
  XPATH_fecha VARCHAR(100),
  XPATH_contenido VARCHAR(100),
  nombre_sitioWeb VARCHAR(100),
  FOREIGN KEY (nombre_sitioWeb) REFERENCES sitioWeb(nombre_sitioWeb)
);

-- Creación de la tabla de relación entre fundadores y medios de prensa
CREATE TABLE crea (
  nombre_fundadores VARCHAR(100),
  nombre_medio VARCHAR(100),
  PRIMARY KEY (nombre_fundadores, nombre_medio),
  FOREIGN KEY (nombre_fundadores) REFERENCES fundador(nombre_fundadores),
  FOREIGN KEY (nombre_medio) REFERENCES mediosPrensa(nombre_medio)
);
