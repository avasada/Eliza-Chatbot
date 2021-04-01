import reference
import re
import random


def main():
    print("Hello. How are you feeling today?")
 
    while True:
        statement = input("> ")
        print(translate(statement))
        if statement == "quit":
            break


def translate(statement):
    statement = statement.replace("!", " ")
    statement = statement.replace(".", " ")
    for key in reference.psychobabble_responses:
        match = re.search(reference.psychobabble_patterns[key], statement)
        if match:
            response = random.choice(reference.psychobabble_responses[key])
            return(reference.format_response(match, response))
            
main()