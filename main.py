class Game:
    def __init__(self):
        self.door_count = input('Количество дверей (Enter = 3) ')
        if self.door_count == '':
            self.door_count = 3
        else:
            self.door_count = int(self.door_count)
        if self.door_count < 3:
            self.door_count = 3
        self.change = input('Менять ли дверь? (y/n) (Enter = y) ')
        if self.change == '' or self.change == 'y':
            self.change = True
        else:
            self.change = False
        self.win_count = 0
        self.loose_count = 0

    def result(self):
        print(f'Количество дверей {self.door_count}')
        print(f'Смена двери {"Да" if self.change else "Нет"}')

    def game_start(self):
        self.result()
        self.game_end()

    def game_end(self):
        print('Конец игры')


if __name__ == '__main__':
    game = Game()
    game.game_start()
