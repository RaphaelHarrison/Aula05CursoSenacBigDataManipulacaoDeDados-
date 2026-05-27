/*
ALTER TABLE tb_alugados
ADD CONSTRAINT fk_usuario
FOREIGN KEY (id_usuario) REFERENCES tb_usuarios(id_usuario);

ALTER TABLE tb_itens_alugados
ADD CONSTRAINT fk_livro
FOREIGN KEY (id_livro) REFERENCES tb_livros(id_livro);

ALTER TABLE tb_itens_alugados
ADD CONSTRAINT fk_alugados
FOREIGN KEY (id_aluguel) REFERENCES tb_alugados(id_aluguel);
*/

SELECT 	
	tb_livros.titulo, 
	tb_itens_alugados.id_aluguel,
	tb_itens_alugados.id_aluguel,
	tb_alugados.data_aluguel,
    tb_alugados.data_devolucao,
    tb_alugados.valor,
    tb_usuarios.id_usuario,
    tb_usuarios.nome
    
FROM 
	tb_livros

JOIN tb_itens_alugados 
	ON tb_itens_alugados.id_livro = tb_livros.id_livro

JOIN tb_alugados 
	ON tb_alugados.id_aluguel = tb_itens_alugados.id_aluguel

JOIN tb_usuarios 
	ON tb_usuarios.id_usuario = tb_alugados.id_usuario

WHERE tb_alugados.data_devolucao BETWEEN "2024-11-01" AND "2024-11-30"