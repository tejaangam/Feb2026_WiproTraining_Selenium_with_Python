from flask import Flask, request, jsonify

app = Flask(__name__)

customers = {}
customer_id_counter = 1


# STEP 1: Create Customer
@app.route("/customers", methods=["POST"])
def create_customer():
    global customer_id_counter
    data = request.json

    customer = {
        "id": customer_id_counter,
        "name": data["name"],
        "email": data["email"],
        "balance": data["balance"]
    }

    customers[customer_id_counter] = customer
    customer_id_counter += 1

    return jsonify(customer), 201


# STEP 2: Get Customer
@app.route("/customers/<int:cid>", methods=["GET"])
def get_customer(cid):
    customer = customers.get(cid)
    if not customer:
        return jsonify({"message": "Customer not found"}), 404

    return jsonify(customer), 200


# STEP 3: Update Customer
@app.route("/customers/<int:cid>", methods=["PUT"])
def update_customer(cid):
    customer = customers.get(cid)
    if not customer:
        return jsonify({"message": "Customer not found"}), 404

    data = request.json
    customer["email"] = data.get("email", customer["email"])

    return jsonify(customer), 200


# STEP 4: Delete Customer
@app.route("/customers/<int:cid>", methods=["DELETE"])
def delete_customer(cid):
    if cid not in customers:
        return jsonify({"message": "Customer not found"}), 404

    del customers[cid]
    return "", 204


if __name__ == "__main__":
    app.run(debug=True)