-- db/esquema.sql

CREATE TABLE alimentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    kcal_per_100g FLOAT,
    proteinas FLOAT,
    carbohidratos FLOAT,
    grasas FLOAT,
    origen ENUM('usda', 'excel') DEFAULT 'usda'
);

CREATE TABLE micronutrientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    alimento_id INT,
    nombre VARCHAR(255),
    cantidad_mg FLOAT,
    FOREIGN KEY (alimento_id) REFERENCES alimentos(id) ON DELETE CASCADE
);

CREATE TABLE comidas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    fecha DATE,
    hora TIME
);

CREATE TABLE comida_alimentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    comida_id INT,
    alimento_id INT,
    cantidad_g FLOAT,
    FOREIGN KEY (comida_id) REFERENCES comidas(id) ON DELETE CASCADE,
    FOREIGN KEY (alimento_id) REFERENCES alimentos(id) ON DELETE CASCADE
);
