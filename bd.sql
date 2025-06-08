CREATE TABLE edificio (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

CREATE TABLE piso (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    id_edificio INT,
    FOREIGN KEY (id_edificio) REFERENCES edificio(id) ON DELETE CASCADE
);

CREATE TABLE area (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    id_piso INT,
    id_edificio INT,
    FOREIGN KEY (id_piso) REFERENCES piso(id) ON DELETE CASCADE,
    FOREIGN KEY (id_edificio) REFERENCES edificio(id) ON DELETE CASCADE
);