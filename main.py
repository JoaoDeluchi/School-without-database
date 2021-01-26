from App import create_app
import uvicorn

if __name__ == '__main__':
    app = create_app()
    uvicorn.run(app, host="0.0.0.0", port=8000)

	# - Cadastrar o gabarito de cada prova;
	# - Cadastrar as respostas de cada aluno para cada prova;
	# - Verificar a nota final de cada aluno;
	# - Listar os alunos aprovados;

	# Restrições
	# - A nota total da prova é sempre maior que 0 e menor que 10.
	# - A quantidade máxima de alunos é 100.
	# - O peso de cada questão é sempre um inteiro maior que 0.
	# - Os alunos aprovados tem média de notas maior do que 7.
	# - A entrada e saída de dados deverá ser em JSON.
