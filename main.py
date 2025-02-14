from random import randint
from colorama import Fore as color_text

class Gamer:
    """
    Класс игрока
    """

    def __init__(self):
        super().__init__()
        change = input('Менять ли дверь? (y/n Enter = y): ').strip() or 'y'
        if change == '' or change == 'y':
            change = True
        else:
            change = False
        round = int(input('Количество попыток (Enter = 100): ').strip() or '100')
        if round < 1:
            round = 1
        self.ROUND = round
        self.DOOR_CHANGE = change
        self.count_win = 0
        self.count_loose = 0

    def __str__(self):
        str = f'Смена двери: {"Да" if gamer.DOOR_CHANGE else "Нет"}\n'
        str += 'Выигрышей: ' + color_text.GREEN + f'{self.count_win}' + color_text.RESET + ', '
        str += 'Проигрышей: ' + color_text.RED + f'{self.count_loose}' + color_text.RESET
        return str

class Game:
    """
    Класс игры
    """

    def __init__(self, gamer):
        door_count = int(input('Количество дверей (Enter = 3): ').strip() or '3')
        if door_count < 3:
            door_count = 3
        self.DOOR_COUNT = door_count
        self.gamer = gamer

    def __str__(self):
        str = f'Количество дверей: {self.DOOR_COUNT}\n'
        str += self.gamer.__str__()
        return str

    def result(self):
        """
        Вывод результата игры
        :return: none
        """
        print(self)

    def round(self, n):
        """
        Расчет раунда игры
        :param n: Номер раунда
        :return: Результат раунда игры
        :rtype: str
        """
        str = f'Раунд: {n + 1}, '
        door_car = randint(1, self.DOOR_COUNT)
        door_select = randint(1, self.DOOR_COUNT)
        str += f'автомобиль за дверью {door_car}, игрок выбрал {door_select}, '
        if self.gamer.DOOR_CHANGE:
            if door_car == door_select:
                self.gamer.count_loose += 1
                str += color_text.RED + 'Проиграл'
            else:
                self.gamer.count_win += 1
                str += color_text.GREEN + 'Выиграл'
        else:
            if door_car == door_select:
                self.gamer.count_win += 1
                str += color_text.GREEN + 'Выиграл'
            else:
                self.gamer.count_loose += 1
                str += color_text.RED + 'Проиграл'
        str += color_text.RESET
        return str

    def game_start(self):
        """
        Запуск игры
        :return: none
        """
        for i in range(self.gamer.ROUND):
            print(self.round(i))
        self.result()
        self.game_end()

    def game_end(self):
        """
        Завершение игры
        :return: none
        """
        print('Конец игры')

if __name__ == '__main__':
    gamer = Gamer()
    game = Game(gamer)
    game.game_start()
