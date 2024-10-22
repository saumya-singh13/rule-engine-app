# Rule Evaluation Engine

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [Dependencies](#dependencies)
5. [Installation](#installation)
6. [Usage](#usage)
7. [Input Rules](#input-rules)
8. [Design Choices](#design-choices)
9. [Contributing](#contributing)

## Overview
This project implements a 3-tier rule evaluation engine that allows users to input rules and check user's eligibility based on specified criteria. The engine evaluates logical conditions using AND and OR operators, supporting nested rule evaluations for complex decision-making scenarios.

## Features
- User Interface to input rules
- Evaluation of user eligibility based on defined rules
- Support for logical operations: AND, OR
- Nested rule evaluation
- Supports combined rules

## Prerequisites
Before running the application, ensure you have the following installed:
- Python 3.x

## Dependencies
To set up and run the application, the following dependencies are required:
- Flask: A lightweight WSGI web application framework for Python.
  
You can install the required libraries using pip:

```bash
pip install -r requirements.txt
```

## Installation
Follow these steps to set up the Rule Evaluation Engine on your local machine:

- Clone the Repository: Clone the repository to your local machine using Git:

```bash
git clone https://github.com/saumya-singh13/rule-engine-app.git
```
- Navigate to the Project Directory: Change to the project directory:

```bash
cd rule-engine-app
```
- Install Dependencies: Install the required dependencies listed in requirements.txt:

```bash
pip install -r requirements.txt
```
## Usage
- Run the Application: Start the Flask web server by running:

```bash
python -m backend.app
```
## Input Rules:

- Enter your rules in the provided text input field. Ensure the rules follow the specified format (e.g., age > 30 AND department = 'Marketing').
Input Attributes:

- Fill in the attributes (e.g., age, department, salary, experience) in the respective fields in JSON format.
- Evaluate:

- Click the Evaluate button to check eligibility based on the rules and attributes you provided. The results will be displayed on the screen.
## Design Choices
- Modular Design: The application follows a modular design pattern for better maintainability and ease of testing. Each component, including the rule parser, evaluator, and user interface, api is encapsulated and have a seperate file

- Abstract Syntax Tree (AST): The use of an Abstract Syntax Tree for rule evaluation allows for efficient processing of complex logical expressions. This structure enables easy manipulation and evaluation of nested rules.

- Flask Framework: The application leverages the Flask web framework due to its simplicity and flexibility, making it easy to set up a web server and handle user input.

## Contributing
Contributions are welcome! If you have suggestions for improvements or new features, feel free to submit a pull request or open an issue.
