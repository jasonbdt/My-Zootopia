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
    for animal in animals_data:
        print(f"Name: {animal['name']}")
        print(f"Diet: {animal['characteristics']['diet']}")
        print(f"Location: {animal['locations'][0]}")

        if 'type' in animal['characteristics']:
            print(f"Type: {animal['characteristics']['type']}")
        print()


if __name__ == '__main__':
    main()

