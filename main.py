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
        self.CHANGE = change
        self.win_count = 0
        self.loose_count = 0

    def result(self):
        print(f'Количество дверей {self.DOOR_COUNT}')
        print(f'Смена двери {"Да" if self.CHANGE else "Нет"}')
        print(f'Выигрышей: {self.win_count}')
        print(f'Проигрышей: {self.loose_count}')

    def round(self):
        self.win_count += 1

    def game_start(self):
        for i in range(self.ROUND):
            self.round()
        self.result()
        self.game_end()

    def game_end(self):
        print('Конец игры')


if __name__ == '__main__':
    game = Game()
    game.game_start()
