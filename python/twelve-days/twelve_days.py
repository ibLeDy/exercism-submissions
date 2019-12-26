from typing import List

NUMBER = [
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eighth",
    "ninth",
    "tenth",
    "eleventh",
    "twelfth",
]

DAYS = [
    "twelve Drummers Drumming",
    "eleven Pipers Piping",
    "ten Lords-a-Leaping",
    "nine Ladies Dancing",
    "eight Maids-a-Milking",
    "seven Swans-a-Swimming",
    "six Geese-a-Laying",
    "five Gold Rings",
    "four Calling Birds",
    "three French Hens",
    "two Turtle Doves",
]

def recite(start: int, end:int) -> List[str]:
    result = []

    for day in range(start - 1, end):
        nth = NUMBER[day]
        spacer = " "

        if day:
            spacer += ", ".join(DAYS[len(DAYS) - day:]) + ", and "

        result.append(
            f"On the {nth} day of Christmas my true love gave to me:" \
            f"{spacer}a Partridge in a Pear Tree.")
    
    return result
