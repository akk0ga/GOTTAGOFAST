import random
import json
import time


class Typing:
    __WORDS_FILE: str = 'Typer/src/words.json'
    __PREPARE_TIME: int = 3

    def __repr__(self):
        return 'build a new typing test'

    def __generate_words_list(self) -> tuple:
        """
        return random list of words
        :return:
        """
        with open(self.__WORDS_FILE, 'r') as f:
            words: list = json.load(f)
            total_words: int = len(words)

            already_chose: list = []
            selected_words: list = []

            for i in range(0, 2):
                i = random.randint(0, total_words)
                if i in already_chose:
                    while i in already_chose:
                        i = random.randint(0, total_words)
                selected_words.append(words[i])
            f.close()

        return tuple(selected_words)

    def start(self):
        """
        start typing test
        :return:
        """
        words_list = self.__generate_words_list()

        print('BE READY')
        for i in range(0, self.__PREPARE_TIME):
            print(self.__PREPARE_TIME-i)
            time.sleep(1)
            i += 1
        print('GOTTA GO FAST')

        t1 = time.time()

        for i in words_list:
            print('=====================================')
            print(i)
            word = input('type here > ')

            while word != i:
                print('WRONG')
                word = input('retry > ')

            print('CORRECT')
            print('=====================================')

        t2 = time.time()
        print(f'YOUR SCORE IS {t2 - t1}')
