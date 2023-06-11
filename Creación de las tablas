USE big_bread_s;
CREATE TABLE productos (
  ID int(11) PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(100) NOT NULL,
  descripcion VARCHAR(255),
  precio DECIMAL(10, 2) NOT NULL
);
CREATE TABLE insumos (
  ID int(11) PRIMARY KEY AUTO_INCREMENT ,
  nombre VARCHAR(100) NOT NULL,
  descripcion VARCHAR(255)
);
CREATE TABLE produccion_diaria (
   ID int(11) PRIMARY KEY AUTO_INCREMENT ,
  fecha DATE NOT NULL,
  cantidad INT NOT NULL
);
CREATE TABLE recetas (
   ID int(11) PRIMARY KEY AUTO_INCREMENT ,
  producto_id INT NOT NULL,
  insumo_id INT NOT NULL,
  cantidad DECIMAL(10, 2) NOT NULL,
  FOREIGN KEY (producto_id) REFERENCES productos(id),
  FOREIGN KEY (insumo_id) REFERENCES insumos(id)
);
