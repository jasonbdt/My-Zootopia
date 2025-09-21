import json

def load_data(file_path: str):
    """Loads a JSON file"""
    try:
        with open(file_path, "r") as file_obj:
            if file_path.endswith('.json'):
                return json.load(file_obj)
            else:
                return file_obj.read()
    except FileNotFoundError:
        print(f"File {file_path} doesn't exist!")


def serialize_animal(animal_obj) -> str:
    output = ''
    name, diet, location = (animal_obj['name'],
                            animal_obj['characteristics']['diet'],
                            animal_obj['locations'][0])
    output += '<li class="cards__item">'
    output += f'<div class="card__title">{name}</div>\n'
    output += '<p class="card__text">'
    output += f"<strong>Diet:</strong> {diet}<br />\n"
    output += f"<strong>Location:</strong> {location}<br />\n"

    if 'type' in animal_obj['characteristics']:
        animal_type = animal_obj['characteristics']['type']
        output += f"<strong>Type:</strong> {animal_type}\n"
    output += "</p></li>\n"

    return output


def main() -> None:
    animals_data = load_data('animals_data.json')
    html_content = load_data('animals_template.html')

    output = ""
    for animal_obj in animals_data:
        output += serialize_animal(animal_obj)

    if html_content:
        html_content = html_content.replace('__REPLACE_ANIMALS_INFO__', output)
        with open('animals.html', 'w') as file_obj:
            file_obj.write(html_content)


if __name__ == '__main__':
    main()

