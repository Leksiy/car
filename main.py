from random import randint
from colorama import Fore as color

class Game:
    def __init__(self):

        door_count = input('Количество дверей (Enter = 3) ')
        if door_count == '':
            door_count = 3
        else:
            door_count = int(door_count)
        if door_count < 3:
            door_count = 3

        change = input('Менять ли дверь? (y/n) (Enter = y) ')
        if change == '' or change == 'y':
            change = True
        else:
            change = False

        round = input('Количество игр (Enter = 100) ')
        if round == '':
            round = 100
        else:
            round = int(round)
        if round < 1:
            round = 1

        self.ROUND = round
        self.DOOR_COUNT = door_count
        self.DOOR_CHANGE = change
        self.count_win = 0
        self.count_loose = 0

    def result(self):
        print(f'Количество дверей {self.DOOR_COUNT}')
        print(f'Смена двери {"Да" if self.DOOR_CHANGE else "Нет"}')
        print(f'Выигрышей: {self.count_win}')
        print(f'Проигрышей: {self.count_loose}')

    def round(self, n):
        print(f'Раунд - {n + 1} ', end = '')
        door_car = randint(1, self.DOOR_COUNT)
        door_select = randint(1, self.DOOR_COUNT)
        print(f'Автомобиль за дверью {door_car}, игрок выбрал {door_select} ', end = '')
        if self.DOOR_CHANGE:
            if door_car == door_select:
                self.count_loose += 1
                print(color.RED, 'Проиграл', end='')
            else:
                self.count_win += 1
                print(color.GREEN, 'Выиграл', end='')
        else:
            if door_car == door_select:
                self.count_win += 1
                print(color.GREEN, 'Выиграл', end='')
            else:
                self.count_loose += 1
                print(color.RED, 'Проиграл', end='')
        print(color.RESET)

    def game_start(self):
        for i in range(self.ROUND):
            self.round(i)
        self.result()
        self.game_end()

    def game_end(self):
        print('Конец игры')


if __name__ == '__main__':
    game = Game()
    game.game_start()
