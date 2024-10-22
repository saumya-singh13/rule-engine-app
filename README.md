Eligibility Rule Evaluation Engine
This project implements a rule evaluation engine that determines user eligibility based on customizable rules. Users can input rules through a user interface, and the engine evaluates them against specified user attributes.

Table of Contents
Introduction
Features
Installation
Usage
Design Choices
Dependencies
Running the Application
License
Introduction
The Eligibility Rule Evaluation Engine allows users to define rules in a logical format and evaluate them against user attributes such as age, department, salary, and experience. The engine supports complex expressions with nested parentheses and logical operators (AND, OR).

Features
User-friendly interface for rule input.
Supports logical expressions with multiple conditions.
Evaluates eligibility based on user-defined rules.
Handles nested parentheses and operator precedence.
Outputs eligibility results in real-time.
Installation
To set up the project, follow these steps:

Clone the repository:

bash
Copy code
git clone <your-repository-url>
cd <your-project-directory>
Install the required dependencies (using pip):

bash
Copy code
pip install -r requirements.txt
Usage
Start the application by running:

bash
Copy code
python -m backend.app
Access the user interface through your web browser. Input the rules and user attributes to see the eligibility evaluation.

Design Choices
The application uses a modular architecture with separate components for rule parsing, AST creation, and evaluation.
The rules are parsed using regular expressions to identify operands and operators accurately.
A tree structure is implemented to represent the logical rules and their relationships.
Dependencies
This project requires the following dependencies to be installed:

Python 3.x
Flask (for the web framework)
Any additional libraries specified in requirements.txt.
Running the Application
To run the application, ensure you have the necessary dependencies installed. Start the application by executing:

bash
Copy code
python -m backend.app
This command launches the web server, allowing you to interact with the rule evaluation engine through the user interface.