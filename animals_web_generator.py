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


def serialize_animal(animal_obj: dict[str, Any]) -> str | None:
    output = ''
    try:
        name, locations = animal_obj['name'], animal_obj['locations']
        diet, lifespan, skin_type = (
            animal_obj['characteristics'].get('diet', 'N/A'),
            animal_obj['characteristics'].get('lifespan', 'N/A'),
            animal_obj['characteristics'].get('skin_type', 'N/A')
        )
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
    return None


def get_unique_skin_types(animals) -> set[str]:
    unique_skin_types = {
        animal_obj['characteristics']['skin_type'] for animal_obj in animals
        if 'skin_type' in animal_obj['characteristics']
    }
    unique_skin_types.add('N/A')
    return unique_skin_types


def filter_by_skin_type(animal_obj, chosen_skin_type: str) -> bool:
    if chosen_skin_type == "":
        return True
    elif chosen_skin_type == "N/A":
        if 'skin_type' not in animal_obj['characteristics']:
            return True

    if 'skin_type' in animal_obj['characteristics']:
        animal_skin_type = animal_obj['characteristics']['skin_type']
        if animal_skin_type.lower() == chosen_skin_type.lower():
            return True

    return False


def main() -> None:
    animals_data = load_data('animals_data.json')
    html_content = load_data('animals_template.html')

    skin_types = sorted(get_unique_skin_types(animals_data))
    print(f"Available skin types: {", ".join(skin_types)}\n")

    user_choice = input("Please choose a skin type (leave blank for no filter): ")
    filtered_animals = filter(
        lambda animal_obj: filter_by_skin_type(animal_obj, user_choice),
        animals_data
    )

    output = ""
    for animal_obj in filtered_animals:
        output += serialize_animal(animal_obj)

    if html_content:
        html_content = html_content.replace('__REPLACE_ANIMALS_INFO__', output)
        with open('animals.html', 'w') as file_obj:
            file_obj.write(html_content)


if __name__ == '__main__':
    main()

