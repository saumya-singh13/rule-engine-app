// Function to create a rule
function createRule() {
    const rule = document.getElementById('singleRuleInput').value;
    fetch('/create_rule', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ rule: rule })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok: ' + response.statusText);
        }
        return response.json();
    })
    .then(data => {
        console.log(data);
        document.getElementById('result').innerText = `Rule created with ID: ${data.rule_id}`;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('result').innerText = 'Error creating rule.';
    });
}

// Function to combine rules
function combineRules() {
    const rules = document.getElementById('combineRulesInput').value.split(',');
    fetch('/combine_rules', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ rules: rules })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok: ' + response.statusText);
        }
        return response.json();
    })
    .then(data => {
        console.log(data);
        document.getElementById('result').innerText = `Combined rule created with ID: ${data.rule_id}`;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('result').innerText = 'Error combining rules.';
    });
}

// Function to evaluate user attributes
function evaluateRule() {
    const attributes = JSON.parse(document.getElementById('userAttributesInput').value);
    const ruleId = document.getElementById('ruleIdInput').value;
    fetch('/evaluate_rule', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ attributes: attributes, rule_id: ruleId })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok: ' + response.statusText);
        }
        return response.json();
    })
    .then(data => {
        console.log(data);
        document.getElementById('result').innerText = `User is eligible: ${data.is_eligible}`; // Make sure this matches the JSON response
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('result').innerText = 'Error evaluating rule.';
    });
}


// Bind functions to button click events
document.getElementById('createRuleButton').onclick = createRule;
document.getElementById('combineRulesButton').onclick = combineRules;
document.getElementById('evaluateRuleButton').onclick = evaluateRule;
