import math
import time


class Main:
    def __init__(self) -> None:
        self.drinks = [
            {"name": "Soda", "price": 3},
            {"name": "Cola", "price": 2},
            {"name": "Lemon-Lime Soda", "price": 5},
            {"name": "Root Beer", "price": 6},
            {"name": "Cream Soda", "price": 9},
            {"name": "Orange Soda", "price": 12},
            {"name": "Ginger Ale", "price": 3},
            {"name": "Tonic Water", "price": 1},
            {"name": "Club Soda", "price": 8},
            {"name": "Grape Soda", "price": 10},
        ]
        self.valid_notes = [100, 50, 20, 10, 5, 1]
        self.max_input = len(self.drinks) - 1
        self.selected = None

    def print_centered(self, sentences: list):
        for sentence in sentences:
            print(sentence.center(self.max_length))

    def print_semicolon_format(self, sentences: list, title=False, hide_column=False):
        # Find the maximum length of the words before the colons
        max_length = max(len(sentence.split(":")[0]) for sentence in sentences)

        if title:
            first_sentence = True
        else:
            first_sentence = False

        for sentence in sentences:
            word, value = sentence.split(":")
            if first_sentence == True or hide_column:
                first_sentence = False
                print("{:<{width}}   {}".format(word, value.strip(), width=max_length))
            else:
                print("{:<{width}} : {}".format(word, value.strip(), width=max_length))

    def get_valid_selection(self):
        while True:
            try:
                num = int(input("\nInput Number: "))
                if num < 0 or num > self.max_input:
                    raise Exception("Selection not found. Please enter a valid number")
                return num

            except ValueError:
                print("Invalid input. Please enter a valid number.")
            except Exception as e:
                print(e)

    def get_valid_amount(self):
        while True:
            try:
                num = int(input("\nInput Amount: "))
                if num < self.selected.get("price"):
                    raise Exception(
                        "Insufficient Amount. Please input an amount that is more than the price stated."
                    )
                print("Payment Accepted!")
                return num

            except ValueError:
                print("Invalid input. Amount must be a whole number.")
            except Exception as e:
                print(e)

    def dispense_change(self, amount: int):
        balance = amount - self.selected.get("price")
        if balance == 0:
            return print("\nExact amount received. No change required.")

        change = {}
        for note in self.valid_notes:
            if balance >= note:
                note_count = int(math.floor(balance / note))
                change[note] = note_count
                balance -= note_count * note

        print("\nDispensing change...")
        time.sleep(2)
        print("\nHere is your change\n")
        sentences = []
        sentences.append(f"Note: Count")
        for note, count in change.items():
            sentences.append(f"${note}: {count}")
        self.print_semicolon_format(sentences, True, True)

    def handle(self):
        # Prints Selection
        sentences = [
            "Welcome to Abdul Rahman's Drinks Vending Machine!",
            "Browse our latest selection selection below:\n",
        ]
        self.max_length = max(len(sentence) for sentence in sentences)
        self.print_centered(sentences)

        selections = []
        selections.append("No Drink: Price")
        for i, drink in enumerate(self.drinks):
            selections.append(f"{i}. {drink.get('name')}: ${drink.get('price')} ")
        self.print_semicolon_format(selections, True, True)

        # Retrieve selection input
        selected = self.get_valid_selection()
        self.selected = self.drinks[selected]
        print("")
        sentences = [
            f"You have chosen: {self.selected.get('name')}",
            f"Total price: ${self.selected.get('price')}\n",
        ]
        self.print_semicolon_format(sentences)

        # Retrieve payment and dispense change
        amount = self.get_valid_amount()
        time.sleep(1)
        print(f"\nDispensing drink...")
        time.sleep(2)
        print(f"\nSuccesfully dispensed a {self.selected.get('name')}")
        time.sleep(1)
        self.dispense_change(amount)

        print(f"\nEnjoy your {self.selected.get('name')}! Please come again!")


if __name__ == "__main__":
    instance = Main()
    instance.handle()
