CREATE DATABASE roldgame;

USE roldgame;

CREATE TABLE login (
    email VARCHAR(255) PRIMARY KEY,
    contrasena VARCHAR(255) NOT NULL
);

CREATE TABLE equipos (
    id_equipo INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255),
    nombre_equipo VARCHAR(255) UNIQUE,
    clase_personaje_1 VARCHAR(255),
    nombre_personaje_1 VARCHAR(255),
    clase_personaje_2 VARCHAR(255),
    nombre_personaje_2 VARCHAR(255),
    clase_personaje_3 VARCHAR(255),
    nombre_personaje_3 VARCHAR(255),
    clase_personaje_4 VARCHAR(255),
    nombre_personaje_4 VARCHAR(255),
    FOREIGN KEY (email) REFERENCES login(email)
);

CREATE TABLE personajes (
    id_personaje INT PRIMARY KEY AUTO_INCREMENT,
    nombre_equipo VARCHAR(255),
    nombre_personaje VARCHAR(255),
    clase_personaje VARCHAR(255),
    nivel INT NOT NULL,
    vida INT NOT NULL,
    resistencia INT NOT NULL,
    dano_condicion INT NOT NULL,
    fuerza INT NOT NULL,
    curacion INT NOT NULL,
    resistencia_condicion INT NOT NULL,
    experiencia INT NOT NULL,
    max_experiencia INT NOT NULL,
    FOREIGN KEY (nombre_equipo) REFERENCES equipos(nombre_equipo)
);


CREATE TABLE items (
    id_item INT PRIMARY KEY AUTO_INCREMENT,
    nombre_equipo VARCHAR(255),
    tipo_item VARCHAR(255),
    nombre_item VARCHAR(255),
    cantidad_item INT NOT NULL,
    FOREIGN KEY (nombre_equipo) REFERENCES equipos(nombre_equipo)
);

CREATE TABLE misiones (
    id_item INT PRIMARY KEY AUTO_INCREMENT,
    nombre_equipo VARCHAR(255),
    mision VARCHAR(255),
    valor_mision INT NOT NULL,
    FOREIGN KEY (nombre_equipo) REFERENCES equipos(nombre_equipo)
);