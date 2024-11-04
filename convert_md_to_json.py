import markdown
import json

# Input and output file names
input_file = 'Audit summary.md'  # Name of your MD file
output_file = 'output.json'  # Desired name for the output JSON file

# Read the Markdown file
with open(input_file, 'r', encoding='utf-8') as md_file:
    md_content = md_file.read()

# Convert Markdown to HTML (optional)
html_content = markdown.markdown(md_content)

# Structure the data
data = {
    'markdown': md_content,
    'html': html_content
}

# Convert to JSON and write to a file
with open(output_file, 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

print(f"Conversion complete! JSON file created: {output_file}")

