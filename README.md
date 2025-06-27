### CRUD COM PYTHON E MSQL
 
* **Conexão com Banco de Dados MSQL**
* **Criando um Create**
* **Criando um Read**
* **Criando um Update**
* **Criando um Delete**

* **Alimentando , Atualizando e Deletando itens de uma tabela.**

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
