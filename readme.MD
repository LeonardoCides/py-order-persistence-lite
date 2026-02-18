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
```
