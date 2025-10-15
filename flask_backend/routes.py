from flask import Flask, request, jsonify
from db_config import get_connection

app = Flask(__name__)

# Crear estudiante
@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, age, email) VALUES (%s, %s, %s)",
                   (data['name'], data['age'], data['email']))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Student added successfully"}), 201

# Obtener todos los estudiantes
@app.route('/students', methods=['GET'])
def get_students():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(students)

# Obtener un estudiante por ID 
@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM students WHERE id = %s", (id,))
    student = cursor.fetchone()
    cursor.close()
    conn.close()
    if student:
        return jsonify(student)
    else:
        return jsonify({"error": "Student not found"}), 404

# Actualizar estudiante
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.get_json()
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET name=%s, age=%s, email=%s WHERE id=%s",
                   (data['name'], data['age'], data['email'], id))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Student updated successfully"})

# Eliminar estudiante
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id=%s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Student deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)
