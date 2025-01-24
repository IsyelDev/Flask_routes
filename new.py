from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista en memoria para almacenar usuarios
users = [
    {"id": 1, "username": "manuel", "telefono": 123458},
    {"id": 2, "username": "erika", "telefono": 123458910}
]

# Ruta para obtener información de un usuario por ID
@app.route("/users/<int:user_id>")
def get_user(user_id):
    # Buscar el usuario por su ID
    user = next((user for user in users if user["id"] == user_id), None)

    # Si no se encuentra el usuario, devolver error 404
    if user is None:
        return jsonify({"message": "User not found"}), 404

    # Obtener parámetro 'query' de los parámetros de la solicitud
    query = request.args.get("query")
    if query:
        user["query"] = query  # Agregar 'query' al usuario

    return jsonify(user), 200


# Ruta para crear un nuevo usuario
@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()  # Obtener los datos JSON enviados en la solicitud

    # Crear un nuevo usuario con un ID único
    new_id = max([user["id"] for user in users]) + 1 if users else 1  # Genera un ID único
    data['id'] = new_id
    data['status'] = "user created"  # Agregar un estado de creación al usuario

    # Agregar el usuario a la lista
    users.append(data)

    return jsonify(data), 201  # Devolver respuesta con código 201 (Creado)

# Iniciar la aplicación
if __name__ == "__main__":
    app.run(debug=True)
