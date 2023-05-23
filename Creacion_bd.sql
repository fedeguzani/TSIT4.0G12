create database big_bread_sa;

//el siguiente codigo es para utilizarlo desde python //

CREATE TABLE productos (
  id INT PRIMARY KEY ,
  nombre VARCHAR(100) NOT NULL,
  descripcion VARCHAR(255),
  precio DECIMAL(10, 2) NOT NULL
);
CREATE TABLE insumos (
  id INT PRIMARY KEY ,
  nombre VARCHAR(100) NOT NULL,
  descripcion VARCHAR(255)
);
CREATE TABLE produccion_diaria (
  id INT PRIMARY KEY ,
  fecha DATE NOT NULL,
  cantidad INT NOT NULL
);
CREATE TABLE recetas (
  id INT PRIMARY KEY ,
  producto_id INT NOT NULL,
  insumo_id INT NOT NULL,
  cantidad DECIMAL(10, 2) NOT NULL,
  FOREIGN KEY (producto_id) REFERENCES productos(id),
  FOREIGN KEY (insumo_id) REFERENCES insumos(id)
);
