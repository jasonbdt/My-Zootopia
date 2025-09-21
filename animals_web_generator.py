import json

def load_data(file_path: str):
    """Loads a JSON file"""
    try:
        with open(file_path, "r") as file_obj:
            return json.load(file_obj)
    except FileNotFoundError:
        print(f"File {file_path} doesn't exist!")

def main() -> None:
    animals_data = load_data('animals_data.json')

    try:
        with open('animals_template.html', 'r') as file_obj:
            html_content = file_obj.read()
    except FileNotFoundError:
        print("File animals_template.html doesn't exist!")

    output = ""
    for animal in animals_data:
        output += '<li class="cards__item">'
        output += f'<div class="card__title">{animal['name']}</div>\n'
        output += '<p class="card__text">'
        output += f"<strong>Diet:</strong> {animal['characteristics']['diet']}<br />\n"
        output += f"<strong>Location:</strong> {animal['locations'][0]}<br />\n"

        if 'type' in animal['characteristics']:
            output += f"<strong>Type:</strong> {animal['characteristics']['type']}\n"
        output += "</p></li>\n"

    if html_content:
        html_content = html_content.replace('__REPLACE_ANIMALS_INFO__', output)
        with open('animals.html', 'w') as file_obj:
            file_obj.write(html_content)

    print(output, end="")


if __name__ == '__main__':
    main()

