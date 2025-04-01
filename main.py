import yaml
import random
from jinja2 import Template

# Load the user prompt template from a YAML file
def load_template(path='user_prompt.yml'):
    with open(path, 'r') as f:
        data = yaml.safe_load(f)
    return data['user_prompt']  # Extract just the template string

# Load all persona entries from the personas YAML file
def load_personas(path='personas.yml'):
    with open(path, 'r') as f:
        return yaml.safe_load(f)  # Returns a list of dicts, one per persona

# Use Jinja2 to fill in the template with persona values
def generate_prompt(template_str, persona):
    template = Template(template_str)
    return template.render(**persona)

# Main logic to tie it all together
def main():
    # Step 1: Load the user prompt template
    template_str = load_template()

    # Step 2: Load a list of personas
    personas = load_personas()

    # Step 3: Pick one persona at random
    persona = random.choice(personas)

    # Step 4: Generate the full user prompt using the selected persona
    prompt = generate_prompt(template_str, persona)

    # Step 5: Display the final result
    print("🎯 Generated User Prompt:\n")
    print(prompt)

# Run the main function when the script is executed directly
if __name__ == "__main__":
    main()
