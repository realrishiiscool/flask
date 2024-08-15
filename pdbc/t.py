import mysql.connector
from mysql.connector import Error

def insert_student(first_name, last_name, email, enrollment_date, grade_level):
    try:
        # Establishing the connection
        connection = mysql.connector.connect(
            host='localhost',        # Replace with your host name if different
            user='root',    # Replace with your MySQL username
            password='1234',# Replace with your MySQL password
            database='stdt' # Replace with your database name
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # SQL query to insert data into the students table
            insert_query = """INSERT INTO students (first_name, last_name, email, enrollment_date, grade_level) 
                              VALUES (%s, %s, %s, %s, %s)"""
            
            # Tuple containing the data to be inserted
            student_data = (first_name, last_name, email, enrollment_date, grade_level)

            # Executing the query
            cursor.execute(insert_query, student_data)

            # Committing the transaction
            connection.commit()

            print("Student data inserted successfully")

    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

if __name__ == '__main__':
    insert_student('John', 'Doe', 'john.doe@example.com', '2023-08-01', 10)
