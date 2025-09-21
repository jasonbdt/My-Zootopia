from typing import Any
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


def serialize_animal(animal_obj: dict[str, Any]) -> str:
    output = ''
    try:
        name, locations = animal_obj['name'], animal_obj['locations']
        diet, lifespan, skin_type = (animal_obj['characteristics'].get('diet', 'N/A'),
                                     animal_obj['characteristics'].get('lifespan', 'N/A'),
                                     animal_obj['characteristics'].get('skin_type', 'N/A'))
    except KeyError:
        print("Fatal error occurred, unable to serialize animal!")
    else:
        lifespan = lifespan.replace('–', '-')

        output += '<li class="cards__item">'
        output += f'<div class="card__title">{name}</div>\n'
        output += '<div class="card__text"><ul>'
        output += f"<li><strong>Diet:</strong> {diet}</li>\n"
        output += f"<li><strong>Location:</strong> {", ".join(locations)}</li>\n"
        output += f"<li><strong>Life span:</strong> {lifespan}</li>\n"
        output += f"<li><strong>Skin type:</strong> {skin_type}</li>\n"

        if 'type' in animal_obj['characteristics']:
            animal_type = animal_obj['characteristics']['type']
            output += f"<li><strong>Type:</strong> {animal_type}</li>\n"
        output += "</ul></div></li>\n"

        return output

    return ""


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

