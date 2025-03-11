# Deck2Details

A simple Python program that processes an exported MTG deck in *text format*, fetches each card's information from **Scryfall API**, and outputs a neatly formatted text file with **card descriptions, types, mana costs, power/toughness, and deck size**.

## Features
- Fetches accurate card data from **Scryfall API**  
- **Includes card details**: Type, mana cost, power/toughness, and abilities  
- **Displays total deck size** & unique card count  
- **Live progress indicator** while fetching data  
- **UTF-8 Encoding** to prevent errors with special characters  

---

## **Setup & Requirements**

### 1. Install Python (if not installed)
This script requires **Python 3.7+**.  
Download & install it from: [Python.org](https://www.python.org/downloads/)

### 2. Install Required Libraries
This script depends on **requests** for API fetching. Install it using:

```sh
pip install requests
```

## Instructions

### 1. Export Deck as text/text file

I used archidekt, but most deckbuilders/exporters should have a way to do this;
- make sure that the exported list is formatted as: ``` # Card Name ```
    - There should be no category headers, set identifiers, or anything else
- make sure the text file is called **deck.txt**
  
> Here is an example of how I did it, ensure the settings are the same, then I just copied to clipboard and pasted it in a new text file:

![Image of example](/Example.jpg)

### 2. Place deck.txt into folder with Deck2Details.py

### 3. Run Deck2Details.py

- Open a terminal
- Navigate to the directory (folder) with Deck2Details.py
- run ```python Deck2Details.py```

### 4. Enjoy
The program should now run, and once the list is processed the details.txt will contain every card with now descriptions that you had in the deck.txt

> If you run into any issues, feel free to open an issue with this repository and explain what's up