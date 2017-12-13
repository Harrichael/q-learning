
from src.map.map import Map

if __name__ == '__main__':
    with open('maps/basement.json') as f:
        basement = Map.from_json_text(f.read())

    print(basement)

