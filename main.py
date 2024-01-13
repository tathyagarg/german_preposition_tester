from data_holder import *
import random

class Quiz:
    instance = None
    ctsm = ['correct', 'total', 'streak', 'max_streak']
    def __init__(self, func):
        self.correct = 0
        self.total = 0
        self.streak = 0
        self.max_streak = 0
        self.send = ''

        Quiz.instance = self
    
    def finish_init(self, correct, wrong, finish):
        self.correct_str, self.correct_ctsm = correct
        self.wrong_str, self.wrong_ctsm = wrong
        self.finish_str, self.finish_ctsm = finish

        self.correct_ctsm_map = lambda: self.ctsm_map(self.correct_ctsm)
        self.wrong_ctsm_map = lambda: self.ctsm_map(self.wrong_ctsm)
        self.finish_ctsm_map = lambda: self.ctsm_map(self.finish_ctsm)

        Quiz.instance = self
        return self

    def default_finish_init(self):
        return self.finish_init(
            ("Correct!\nScore: {0}\nTotal: {1}\nStreak: {2}", [0, 1, 2, -1]),
            ("Wrong...\nScore: {0}\nTotal: {1}", [0, 1, -1, -1]),
            ("Final Stats:\nScore: {0}\nTotal: {1}\nMaximum Streak: {2}", [0, 1, -1, 2])
        )

    @classmethod
    def fetch(cls): return cls.instance or ValueError("Error: Quiz not instantiated")

    def ctsm_map(self, ctsm: list[int]):
        return list(dict(sorted({k: getattr(self, Quiz.ctsm[i]) for k, i in enumerate(ctsm) if k != -1}.items())).values())

    def run_correct(self):
        print(self.correct_str.format(*(self.correct_ctsm_map())) + self.send)
        print("="*10)
        self.send = ''
        return self

    def run_wrong(self): 
        print(self.wrong_str.format(*(self.wrong_ctsm_map())) + self.send)
        print("="*10)
        self.send = ''
        return self
    
    def run_finish(self): 
        print(self.finish_str.format(*(self.finish_ctsm_map())) + self.send)
        self.send = ''
        return self

    def set(self, attr, val):
        setattr(self, attr, val)
        return self

    def add(self, attr, amt):
        return self.set(attr, getattr(self, attr) + amt)

def quiz(word_list: list[str]):
    me = Quiz.instance.default_finish_init()
    while True:
        word = random.choice(word_list)
        if word in DUPLICATES: answer = DUPLICATES[word] + SIMPLIFIED_DUPLICATES[word]
        else: 
            if (answer := Preposition.all_query(word)) == -1:
                raise ValueError(f"Unexpected error when finding answer for {word}!")

        inp = input(f"Enter preposition for {word!r}: ")
        if inp.lower() == 'x':
            break
        me.add('total', 1)
        if inp in answer:
            me.add('streak', 1).add('correct', 1).run_correct()
        else:
            me.set('max_streak', max(me.max_streak, me.streak)).set('streak', 0).set('send', f"\nCorrect answer was: {', '.join(answer)}").run_wrong()
    if me.total == 0:
        return
    me.set("send", f"\nPercentage: {me.correct/me.total*100:.2f}%").run_finish()


def cases():
    me = Quiz.instance.default_finish_init()
    preposition_list = Preposition.PREPOSITIONS
    preposition_list.remove(Preposition.fetch('als'))
    while True:
        prep = random.choice(Preposition.PREPOSITIONS)
        word = prep.prep
        answer = [['dativ', 'd'], ['akkusativ', 'a']][prep.is_akkusativ]
        me.add('total', 1)
        inp = input(f"Enter case of {word!r}: ")
        if inp.lower() == 'x': break
        if inp.lower() in answer:
            me.add('streak', 1).add('correct', 1).run_correct()
        else:
            me.set('max_streak', max(me.max_streak, me.streak)).set('streak', 0).set('send', f"\nCorrect answer was: {', '.join(answer)}").run_wrong()
    if me.total == 0:
        return
    me.set("send", f"\nPercentage: {me.correct/me.total*100:.2f}%").run_finish()


def main():
    functions = {'Get Ready words only': lambda: quiz(WORDS), 'All Words': lambda: quiz(ALL_WORDS), 'Preposition Cases': cases, 'Quit': quit}
    while True:
        print("="*30)
        print("Choose quiz")
        for i, text in enumerate(list(functions.keys()), 1):
            print(f'{i}: {text}')
        choice = int(input("Enter choice (the number): "))
        while not (1 <= choice <= len(functions)):
            choice = int(input("Invalid! Enter choice: "))
        Quiz(functions[list(functions.keys())[choice-1]])
        functions[list(functions.keys())[choice-1]]()

if __name__ == "__main__": main()

