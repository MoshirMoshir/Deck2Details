import requests
import time
import sys
from collections import defaultdict

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
    """Reads a decklist, fetches descriptions, and saves them to an output file with a progress indicator."""
    
    # Read all card names and quantities
    card_counts = defaultdict(int)
    
    with open(input_file, "r", encoding="utf-8") as infile:
        for line in infile:
            if line.strip():  # Ignore empty lines
                parts = line.strip().split(" ", 1)
                if len(parts) > 1 and parts[0].isdigit():
                    quantity = int(parts[0])
                    card_name = parts[1]
                else:
                    quantity = 1
                    card_name = parts[0]

                card_counts[card_name] += quantity  # Aggregate card quantities

    total_cards = len(card_counts)
    processed_cards = 0

    with open(output_file, "w", encoding="utf-8") as outfile:
        outfile.write(f"Total unique cards: {total_cards}\n")
        outfile.write(f"Total deck size: {sum(card_counts.values())}\n")
        outfile.write("=" * 40 + "\n\n")

        for card_name, quantity in card_counts.items():
            card_info = fetch_card_details(card_name)
            processed_cards += 1

            if card_info:
                # Formatting output
                outfile.write(f"**{card_info['name']}** (x{quantity})\n")
                outfile.write(f"Mana Cost: {card_info['mana_cost']}\n")
                outfile.write(f"Type: {card_info['type_line']}\n")
                if card_info["power"] is not None and card_info["toughness"] is not None:
                    outfile.write(f"Power/Toughness: {card_info['power']}/{card_info['toughness']}\n")
                outfile.write(f"Text: {card_info['oracle_text']}\n")
                outfile.write("-" * 40 + "\n\n")  # Separator

            # Print progress indicator
            sys.stdout.write(f"\rProcessing card {processed_cards}/{total_cards}...")
            sys.stdout.flush()

            time.sleep(0.11)  # Avoid rate-limiting

    print(f"\nDecklist with descriptions saved to {output_file}")

if __name__ == "__main__":
    input_file = "deck.txt"  # Uses deck.txt as input
    output_file = "details.txt"  # Saves output to details.txt
    
    process_decklist(input_file, output_file)
