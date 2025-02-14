from random import randint
from colorama import Fore as color

class Gamer:
    def __init__(self):
        change = input('Менять ли дверь? (y/n) (Enter = y): ').strip() or 'y'
        if change == '' or change == 'y':
            change = True
        else:
            change = False
        self.DOOR_CHANGE = change
        self.count_win = 0
        self.count_loose = 0

class Game:
    def __init__(self):
        door_count = int(input('Количество дверей (Enter = 3): ').strip() or '3')
        if door_count < 3:
            door_count = 3
        round = int(input('Количество игр (Enter = 100): ').strip() or '100')
        if round < 1:
            round = 1
        self.ROUND = round
        self.DOOR_COUNT = door_count

    def result(self, gamer):
        print(f'Количество дверей {self.DOOR_COUNT}')
        print(f'Смена двери {"Да" if gamer.DOOR_CHANGE else "Нет"}')
        print(f'Выигрышей: {gamer.count_win}')
        print(f'Проигрышей: {gamer.count_loose}')

    def round(self, gamer, n):
        print(f'Раунд - {n + 1} ', end = '')
        door_car = randint(1, self.DOOR_COUNT)
        door_select = randint(1, self.DOOR_COUNT)
        print(f'Автомобиль за дверью {door_car}, игрок выбрал {door_select} ', end = '')
        if gamer.DOOR_CHANGE:
            if door_car == door_select:
                gamer.count_loose += 1
                print(color.RED, 'Проиграл', end='')
            else:
                gamer.count_win += 1
                print(color.GREEN, 'Выиграл', end='')
        else:
            if door_car == door_select:
                gamer.count_win += 1
                print(color.GREEN, 'Выиграл', end='')
            else:
                gamer.count_loose += 1
                print(color.RED, 'Проиграл', end='')
        print(color.RESET)

    def game_start(self, gamer):
        for i in range(self.ROUND):
            self.round(gamer, i)
        self.result(gamer)
        self.game_end()

    def game_end(self):
        print('Конец игры')

if __name__ == '__main__':
    gamer = Gamer()
    game = Game()
    game.game_start(gamer)
