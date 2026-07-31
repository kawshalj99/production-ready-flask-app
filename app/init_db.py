from app.database import get_connection


def initialize_database():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100)
        )
    """)

    cursor.execute("""
    INSERT INTO users (name)
    SELECT 'DevOps Engineer'
    WHERE NOT EXISTS (
        SELECT 1
        FROM users
        WHERE name = 'DevOps Engineer'
    )
    """)

    connection.commit()

    cursor.close()
    connection.close()


if __name__ == "__main__":
    initialize_database()