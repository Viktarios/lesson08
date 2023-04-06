#:)
#:(
#:()
#:|
#:/

from random import randrange

MOOD_NUMBER = 5

BAD_MOOD = ":("
HAPPY_MOOD = ":)"
SHOUTED_MOOD = ":()"
NERVOUS_MOOD = ":/"
NEUTRAL_MOOD = ":|"


def detect_mood():

    mood = randrange (MOOD_NUMBER)

    if mood == 1:
        msg  = HAPPY_MOOD
    elif mood == 2:
        msg  = BAD_MOOD
    elif mood == 3:
        msg  = SHOUTED_MOOD
    elif mood == 4:
        msg  = NERVOUS_MOOD
    elif mood == 5:
        msg = NEUTRAL_MOOD
    else :
        msg  = "Error"

    return msg


def main():
    mood = detect_mood()
    print(mood)


main()
