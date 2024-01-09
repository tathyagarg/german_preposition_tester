from data_holder import *
import random

def quiz():
    correct = 0
    total = 0
    streak = 0
    max_streak = 0
    while True:
        word = random.choice(WORDS)
        if word in DUPLICATES: answer = DUPLICATES[word]
        else: 
            if (answer := Preposition.query(word)) == -1:
                raise ValueError(f"Unexpected error when finding answer for {word}!")
            answer = [answer]

        inp = input(f"Enter preposition for {word!r}: ")
        if inp.lower() == 'x':
            break
        total += 1
        if inp in answer:
            streak += 1
            correct += 1
            print(f"Correct!\nScore: {correct}\nStreak: {streak}")
        else:
            max_streak = max(max_streak, streak)
            streak = 0
            print(f"Incorrect!\nScore: {correct}\nStreak: {streak}\nCorrect answer was: {', '.join(answer)}")
    print(f"Final Score: {correct}\nPercent Correct: {correct/total*100:.2f}\nHighest streak: {max_streak}")

quiz()
