USE bd_sistema_ouvidoria;

CREATE TABLE Manifestacoes (
    Codigo INT AUTO_INCREMENT,
    Titulo VARCHAR(100) NOT NULL,
    Descricao VARCHAR(300) NOT NULL,
    Autor VARCHAR(50) NOT NULL,
    Tipo VARCHAR(30) NOT NULL,
    PRIMARY KEY (Codigo)
);
