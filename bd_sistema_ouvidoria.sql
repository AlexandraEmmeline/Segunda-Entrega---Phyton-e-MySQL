USE bd_sistema_ouvidoria;

CREATE TABLE Manifestacoes (
    Codigo INT AUTO_INCREMENT,
    Titulo VARCHAR(100) NOT NULL,
    Descricao VARCHAR(300) NOT NULL,
    Autor VARCHAR(50) NOT NULL,
    Tipo VARCHAR(30) NOT NULL,
    PRIMARY KEY (Codigo)
);

INSERT INTO Manifestacoes (Titulo, Descricao, Autor, Tipo)
VALUES 
('Demora no atendimento', 'Esperei mais de 30 minutos para ser atendido.', 'João Silva', 'Reclamação');

INSERT INTO Manifestacoes (Titulo, Descricao, Autor, Tipo)
VALUES 
('Ótimo atendimento', 'Gostaria de parabenizar a equipe pelo excelente atendimento.', 'Maria Oliveira', 'Elogio');

INSERT INTO Manifestacoes (Titulo, Descricao, Autor, Tipo)
VALUES 
('Sugestão de melhoria', 'Seria interessante ampliar o horário de atendimento.', 'Carlos Souza', 'Sugestão');
