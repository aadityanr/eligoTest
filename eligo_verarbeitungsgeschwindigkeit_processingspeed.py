# -*- coding: utf-8 -*-
"""Eligo_Verarbeitungsgeschwindigkeit_ProcessingSpeed.py
The Simplest Case for Practice -Free of Cost

"""

import random
import time

# Define the symbols
symbols = ['●', '▲', '♣', '♦', '▼', '✚', '♥', '⬟', '⬢']

def assign_values():
    random.shuffle(symbols)
    symbol_values = {symbols[i]: i + 1 for i in range(9)}
    return symbol_values

def print_symbols(symbol_values):
    print("Symbols and their values:")
    for i in range(1, 10):
        symbol = list(symbol_values.keys())[list(symbol_values.values()).index(i)]
        print(f"{symbol}: {i}", end=" ")
    print("\n")

def generate_symbol(symbol_values):
    return random.choice(list(symbol_values.keys()))

def generate_question(symbol_values):
    symbol1 = generate_symbol(symbol_values)
    symbol2 = generate_symbol(symbol_values)
    while symbol1 == symbol2:
        symbol2 = generate_symbol(symbol_values)
    return symbol1, symbol2

def main():
    while True:
        symbol_values = assign_values()
        print_symbols(symbol_values)

        symbol1, symbol2 = generate_question(symbol_values)
        value1 = symbol_values[symbol1]
        value2 = symbol_values[symbol2]

        task = random.choice(["larger", "smaller"])
        print(f"Which has the {task} value?")
        print(f"1. {symbol1}   or   2. {symbol2}")
        user_input = input("Your answer (1 or 2): ")

        if task == "larger":
            correct_answer = "1" if value1 > value2 else "2"
        else:
            correct_answer = "1" if value1 < value2 else "2"

        if user_input == correct_answer:
            print("Correct!\n")
        else:
            print(f"Wrong. The correct answer is {correct_answer}\n")

        time.sleep(5)

if __name__ == "__main__":
    main()

