import requests
import time
import json

def fetch_card_details(card_name):
    """Fetch card details from the Scryfall API."""
    url = f"https://api.scryfall.com/cards/named?exact={card_name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        card_info = {
            "name": data.get("name", "Unknown Card"),
            "mana_cost": data.get("mana_cost", "N/A"),
            "type_line": data.get("type_line", "Unknown Type"),
            "oracle_text": data.get("oracle_text", "No description available."),
            "power": data.get("power", "-") if "power" in data else None,
            "toughness": data.get("toughness", "-") if "toughness" in data else None
        }
        return card_info
    else:
        print(f"Error fetching {card_name}: {response.status_code}")
        return None

def process_decklist(input_file, output_file):
    """Reads a decklist, fetches descriptions, and saves them to an output file."""
    with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
        for line in infile:
            if line.strip():  # Skip empty lines
                parts = line.strip().split(" ", 1)
                if len(parts) > 1:
                    _, card_name = parts  # Ignore quantity, only take name
                else:
                    card_name = parts[0]

                card_info = fetch_card_details(card_name)
                if card_info:
                    # Formatting output
                    outfile.write(f"**{card_info['name']}**\n")
                    outfile.write(f"Mana Cost: {card_info['mana_cost']}\n")
                    outfile.write(f"Type: {card_info['type_line']}\n")
                    if card_info["power"] is not None and card_info["toughness"] is not None:
                        outfile.write(f"Power/Toughness: {card_info['power']}/{card_info['toughness']}\n")
                    outfile.write(f"Text: {card_info['oracle_text']}\n")
                    outfile.write("-" * 40 + "\n\n")  # Separator
                time.sleep(0.1)  # Avoid rate-limiting

if __name__ == "__main__":
    input_file = "deck.txt"  # Change this to your input file
    output_file = "details.txt"
    
    process_decklist(input_file, output_file)
    print(f"Decklist with descriptions saved to {output_file}")
