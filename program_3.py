# Program #3: Capital Quiz
import random

def capital_quiz():
    states_and_capitals = { "Alabama": "Montgomery", "Alaska": "Juneau", "Arizona": "Phoenix", "Arkansas": "Little Rock",
        "California": "Sacramento", "Colorado": "Denver", "Connecticut": "Hartford", "Delaware": "Dover",
        "Florida": "Tallahassee", "Georgia": "Atlanta", "Hawaii": "Honolulu", "Idaho": "Boise",
        "Illinois": "Springfield", "Indiana": "Indianapolis", "Iowa": "Des Moines", "Kansas": "Topeka",
        "Kentucky": "Frankfort", "Louisiana": "Baton Rouge", "Maine": "Augusta", "Maryland": "Annapolis",
        "Massachusetts": "Boston", "Michigan": "Lansing", "Minnesota": "Saint Paul", "Mississippi": "Jackson",
        "Missouri": "Jefferson City", "Montana": "Helena", "Nebraska": "Lincoln", "Nevada": "Carson City",
        "New Hampshire": "Concord", "New Jersey": "Trenton", "New Mexico": "Santa Fe", "New York": "Albany",
        "North Carolina": "Raleigh", "North Dakota": "Bismarck", "Ohio": "Columbus", "Oklahoma": "Oklahoma City",
        "Oregon": "Salem", "Pennsylvania": "Harrisburg", "Rhode Island": "Providence", "South Carolina": "Columbia",
        "South Dakota": "Pierre", "Tennessee": "Nashville", "Texas": "Austin", "Utah": "Salt Lake City",
        "Vermont": "Montpelier", "Virginia": "Richmond", "Washington": "Olympia", "West Virginia": "Charleston",
        "Wisconsin": "Madison", "Wyoming": "Cheyenne }

    correct = 0
    incorrect = 0
    states = list(states_and_capitals.keys())
    random.shuffle(states)

    for state in states[:15]:  # Quiz with 10 random states
        answer = input(f"What is the capital of {state}? ").strip()
        if answer.lower() == states_and_capitals[state].lower():
            print("Correct!")
            correct += 1
        else:
            print(f"Incorrect! The capital of {state} is {states_and_capitals[state]}.")
            incorrect += 1

    print(f"Quiz complete! You got {correct} correct and {incorrect} incorrect.")


capital_quiz()
