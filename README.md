# 📚 CRUD com Python & MySQL

> Implementação enxuta e profissional das operações **Create – Read – Update – Delete** usando Python 3.10+ e MySQL 8.x.  
> Demonstra boas práticas de conexão, consultas parametrizadas e organização em camadas.

---

## 🚀 Tecnologias & Ferramentas
| Stack | Versão/Lib |
|-------|------------|
| **Python** | 3.10 ou superior |
| **MySQL** | 8.x |
| **mysql-connector-python** | Driver oficial |
| **python-dotenv** | Variáveis de ambiente |
| **pytest** | Testes unitários |
| **logging** | Logs estruturados |

---

## ⚙️ Configuração do Ambiente

```bash
# 1 — clone o repositório
git clone https://github.com/<usuario>/python-mysql-crud.git
cd python-mysql-crud

# 2 — crie e ative o ambiente virtual
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 3 — instale as dependências
pip install -r requirements.txt

# 4 — configure credenciais
cp .env.example .env             # edite USER, PASSWORD, HOST, DB

> Implementação enxuta e profissional das operações **Create – Read – Update – Delete** usando Python 3.10+ e MySQL 8.x.  
> Demonstra boas práticas de conexão, consultas parametrizadas e organização em camadas.

---

src/
 ├── db/
 │   ├── connection.py      # pool de conexões
 │   └── migrations.sql     # criação das tabelas
 ├── models/                # dataclasses ou Pydantic
 ├── repositories/          # funções CRUD (DAO)
 ├── services/              # regras de negócio
 └── main.py                # entry-point

tests/                       # cobertura com pytest
.env.example                 # stub de variáveis de ambiente
requirements.txt
README.md

🧰 Operações CRUD

Operação	Função	Trecho SQL	Descrição

Create	create_employee(data)	INSERT INTO employees ...	Insere novo registro
Read	get_employee(emp_id)	SELECT * FROM employees WHERE id = %s	Busca registro
Update	update_employee(emp_id, data)	UPDATE employees SET ...	Atualiza registro
Delete	delete_employee(emp_id)	DELETE FROM employees WHERE id = %s	Remove registro



---

▶️ Executando o Projeto

# inicializa as tabelas (opcional)
mysql -u root -p < src/db/migrations.sql

# roda a aplicação
python src/main.py