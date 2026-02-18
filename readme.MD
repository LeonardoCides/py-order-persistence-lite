# SQLite Sales Order Manager

A clean and modular Python implementation for managing sales orders using a local SQLite database. This project demonstrates database initialization, connection handling, and data persistence (CRUD basics).

## 🚀 Features

- **Automated Schema Setup**: Automatically creates the `pedidos` (orders) table if it doesn't exist.
- **Relational Mapping**: Stores user IDs, product names, values, and payment reference IDs.
- **Status Tracking**: Default status management for orders (set to 'pendente' by default).
- **Resource Management**: Proper connection opening and closing to prevent database locks.

## 🛠️ Technologies

- **Language:** Python 3.x
- **Database:** SQLite3 (Standard Library)

## 📁 Project Structure

- `database.py`: Core functions to connect, initialize, and save data.
- `main.py`: Entry point to test the database operations.
- `vendas.db`: (Generated) Local SQLite database file.

## ⚙️ How to Run

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/sqlite-sales-manager.git](https://github.com/your-username/sqlite-sales-manager.git)
   python main.py
```
**Verify:**
`A file named vendas.db will be created in your root folder. You can use a tool like DB Browser for SQLite to view the data.`

---

## 💡 Próximos passos para o seu "Daily Commit":

Para manter a sequência de commits nos próximos dias usando esse mesmo projeto, você pode:

1.  **Dia 2:** Adicionar uma função `buscar_pedido(id)` para ler dados.
2.  **Dia 3:** Adicionar uma função `atualizar_status(id, novo_status)` para dar o "update".
3.  **Dia 4:** Criar uma função `deletar_pedido(id)`.
4.  **Dia 5:** Refatorar o código para usar uma **Classe** (Programação Orientada a Objetos).

**Quer que eu prepare o arquivo `.gitignore` para garantir que o arquivo `vendas.db` não seja enviado por erro e "suje" seu repositório?**
