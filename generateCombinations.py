import itertools
import csv
import json

def generate_unique_combinations(*arrays):
    combinations = list(itertools.product(*arrays))
    unique_combinations = [comb for comb in combinations if all(element in arr for element, arr in zip(comb, arrays))]
    
    # Sort the combinations based on the order of the first element in each array
    unique_combinations.sort(key=lambda x: tuple(arr.index(x[i]) for i, arr in enumerate(arrays)))
    
    return unique_combinations

def write_to_json(combinations, json_file):
    with open(json_file, 'w') as file:
        json.dump(combinations, file)

def convert_to_csv(json_file, csv_file):
    with open(json_file, 'r') as file:
        combinations = json.load(file)

    with open(csv_file, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(combinations)

# Example usage:
arrays1 = ['00', '0', '2', '4', '6', '8', '10', '12', '0X', '1X', '2X', '3X']
arrays2 = ['Dark Indigo Blue', 'Autumn Blue (Medium Blue)', 'Black']
arrays3 = ['Mid Rise', 'High Rise']
arrays4 = ['Same as the Denim Wash', 'Black Velvet', 'Red Velvet', 'Dark Brown Velvet',
            'Leopard Print', 'Zebra Print', 'Camouflage', 'Glitter Brown-Gold Velvet']
arrays5 = ['Boot Cut', 'Straight', 'Skinny']
arrays6 = ['Hemmed', 'No Hem']

all_unique_combinations = generate_unique_combinations(arrays1, arrays2, arrays3, arrays4, arrays5, arrays6)
write_to_json(all_unique_combinations, 'unique_combinations.json')
convert_to_csv('unique_combinations.json', 'unique_combinations.csv')
