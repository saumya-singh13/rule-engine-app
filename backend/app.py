from flask import Flask, request, jsonify, render_template
from .rule_ast import Node
from .rule_engine import create_rule_ast, combine_rules_ast, evaluate_rule
from .database import init_db, save_rule_to_db, get_rule_from_db
import logging

app = Flask(__name__, static_folder='../frontend/static', template_folder='../frontend/templates')
init_db()

# Set up logging
logging.basicConfig(level=logging.DEBUG)

def serialize_node(node):
    """Helper function to serialize a Node for JSON response."""
    if isinstance(node, Node):
        return {
            "node_type": node.type,
            "left": serialize_node(node.left) if node.left else None,
            "right": serialize_node(node.right) if node.right else None
        }
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_rule', methods=['POST'])
def create_rule():
    try:
        data = request.get_json()
        rule_str = data.get('rule')
        if not rule_str:
            return jsonify({"error": "No rule provided."}), 400
        
        rule_ast = create_rule_ast(rule_str)
        rule_id = save_rule_to_db(rule_str)
        return jsonify({"rule_id": rule_id, "ast": serialize_node(rule_ast)}), 201
    except Exception as e:
        logging.error("Error creating rule: %s", str(e))
        return jsonify({"error": str(e)}), 500

@app.route('/combine_rules', methods=['POST'])
def combine_rules():
    try:
        data = request.get_json()
        rules = data.get('rules')
        if not rules or not isinstance(rules, list):
            return jsonify({"error": "No valid rules provided."}), 400
        
        combined_ast = combine_rules_ast(rules)
        combined_rule_str = " AND ".join(rules)
        rule_id = save_rule_to_db(combined_rule_str)
        return jsonify({"rule_id": rule_id, "ast": serialize_node(combined_ast)}), 201
    except Exception as e:
        logging.error("Error combining rules: %s", str(e))
        return jsonify({"error": str(e)}), 500

@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_endpoint():
    try:
        data = request.get_json()
        user_attributes = data.get('attributes')
        rule_id = data.get('rule_id')
        if not user_attributes or not rule_id:
            return jsonify({"error": "Missing attributes or rule_id."}), 400
        
        rule_str = get_rule_from_db(rule_id)
        if not rule_str:
            return jsonify({"error": "Rule not found."}), 404
        
        result = evaluate_rule(rule_str, user_attributes)
        return jsonify({"is_eligible": result}), 200  # Changed from "eligible" to "is_eligible"
    except Exception as e:
        logging.error("Error evaluating rule: %s", str(e))
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
