# Put and delete- HTTP verbs for RESTful APIs
from flask import Flask, request, jsonify

app = Flask(__name__)   

#Inital data
items = [
    {"id": 1, "name": "Item 1", "description": "This is item 1"},
    {"id": 2, "name": "Item 2", "description": "This is item 2"},
    {"id": 3, "name": "Item 3", "description": "This is item 3"}
]

@app.route('/')
def home():
    return "Welcome to the Item API! Use /items endpoint to interact."

# Get retrie all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# Get a single item by ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item:
        return jsonify(item)
    return jsonify({"error": "Item not found"}), 404

# post create a new item
@app.route('/items', methods=['POST'])
def create_item():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400 #400 means bad request
    new_item = {"id": items[-1]["id"] + 1 if items else 1,
                "name": request.json.get("name"),
                "description": request.json.get("description")}
    items.append(new_item)
    return jsonify(new_item), 201 #201 means created

# put update an existing item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400
    item["name"] = request.json.get("name", item["name"])
    item["description"] = request.json.get("description", item["description"])
    return jsonify(item) 

# delete an item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    return jsonify({"message": "Item deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True)