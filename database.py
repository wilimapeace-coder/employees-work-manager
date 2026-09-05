import sqlite3

def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    
    # Create Employees Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            employee_id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            department TEXT NOT NULL,
            position TEXT NOT NULL
        )
    ''')
    
    # Create Tasks/Work Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id TEXT,
            description TEXT NOT NULL,
            deadline TEXT NOT NULL,
            priority TEXT NOT NULL,
            status TEXT DEFAULT 'Pending',
            FOREIGN KEY (employee_id) REFERENCES employees (employee_id)
        )
    ''')
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("Database and tables created successfully!")
