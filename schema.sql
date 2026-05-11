-- Tabela de avicultores
CREATE TABLE IF NOT EXISTS tb_avicultor(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    nascimento DATE NOT NULL,
    cpf VARCHAR(11) NOT NULL UNIQUE,
    caf VARCHAR(10) NOT NULL
);

-- Tabela de aviários
CREATE TABLE IF NOT EXISTS tb_aviario(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    capacidade INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS  tb_galpao(
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     identificacao TEXT NOT NULL,
     capacidade INTERGER NOT NULL
);

CREATE TABLE IF NOT EXISTS  tb_avicula(
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     especie TEXT NOT NULL,
     linhagem TEXT NOT NULL
);

