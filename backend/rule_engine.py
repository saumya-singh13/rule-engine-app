from .rule_ast import Node  # Assuming Node is defined in rule_ast module
import re
def create_rule_ast(rule_str: str) -> Node:
    operators = {'AND': 'operator', 'OR': 'operator'}
    operand_pattern = r'([a-zA-Z_][a-zA-Z0-9_]*\s*(=|==|>|<|>=|<=|!=)\s*(\'[^\']*\'|"[^"]*"|\d+))'
    
    # Tokenize input string
    tokens = re.split(r'(\s+AND\s+|\s+OR\s+|\(|\))', rule_str.replace(' ', ''))

    def parse_tokens(tokens):
        output = []  # Holds the resulting AST nodes
        operators_stack = []  # Holds operators and parentheses

        for token in tokens:
            token = token.strip()
            if not token:  # Skip empty tokens
                continue
            if token in operators:  # Handle operators
                while (operators_stack and operators_stack[-1] in operators):
                    right = output.pop() if output else None
                    left = output.pop() if output else None
                    op = operators_stack.pop()
                    output.append(Node(op, left, right))
                operators_stack.append(token)
            elif token == '(':
                operators_stack.append(token)
            elif token == ')':
                while operators_stack and operators_stack[-1] != '(':
                    right = output.pop() if output else None
                    left = output.pop() if output else None
                    op = operators_stack.pop()
                    output.append(Node(op, left, right))
                if not operators_stack:
                    raise ValueError("Invalid rule structure: unmatched parentheses.")
                operators_stack.pop()  # Pop the '('
            elif re.match(operand_pattern, token):  # Handle operands
                output.append(Node("operand", token))
            else:
                raise ValueError(f"Invalid token encountered: {token}")

        # Final processing to combine any remaining expressions
        while operators_stack:
            if not output:
                raise ValueError("Invalid rule structure: incomplete expression.")
            right = output.pop()
            left = output.pop() if output else None
            op = operators_stack.pop()
            output.append(Node(op, left, right))

        if len(output) != 1:
            raise ValueError("Invalid rule structure: incomplete expression.")

        return output[0]

    return parse_tokens(tokens)

def combine_rules_ast(rule_str_list: list) -> Node:
    # Combine multiple rule strings into a single AST
    combined_node = None

    for rule in rule_str_list:
        node = create_rule_ast(rule)
        if combined_node is None:
            combined_node = node
        else:
            combined_node = Node("OR", combined_node, node)  # Combine with OR operator

    return combined_node

def evaluate_rule(rule_str: str, attributes: dict) -> bool:
    # Evaluate the rule against the provided attributes
    root = create_rule_ast(rule_str)

    def evaluate_node(node: Node) -> bool:
        if node.type == "operand":
            # The operand is expected to be in the format: "attribute operator value"
            match = re.match(r'([a-zA-Z_][a-zA-Z0-9_]*)\s*(=|==|>|<|>=|<=|!=)\s*(\'[^\']*\'|"[^"]*"|\d+)', node.left)
            if match:
                attr, op, value = match.groups()
                value = value.strip('"').strip("'")  # Remove surrounding quotes
                if attr not in attributes:
                    return False

                attr_value = attributes[attr]
                if op in ['=', '==']:
                    return attr_value == value
                elif op == '>':
                    return attr_value > float(value)
                elif op == '<':
                    return attr_value < float(value)
                elif op == '>=':
                    return attr_value >= float(value)
                elif op == '<=':
                    return attr_value <= float(value)
                elif op == '!=':
                    return attr_value != value
        elif node.type == "operator":
            left_eval = evaluate_node(node.left)
            right_eval = evaluate_node(node.right)
            if node.left and node.right:
                if node.left == "AND":
                    return left_eval and right_eval
                elif node.left == "OR":
                    return left_eval or right_eval
        return True

    return evaluate_node(root)