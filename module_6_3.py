# Задача "Ошибка эволюции"

import random

class Animal:
    live = True                                        # живой
    sound = None                                       # издаёт звуки
    _DEGREE_OF_DANGER = 0                              # уровень агрессивности
    def __init__(self, speed):
        self.speed = speed                             # скорость
        self._cords = [0, 0, 0]                        # координаты в пространстве

    def move(self, dx, dy, dz):
        if self._cords[2] + self.speed * dz < 0:
            print("It's too deep, i can't dive :(")    # "Здесь слишком глубоко, я не могу нырнуть :("
        else:
            self._cords[0] += self.speed * dx
            self._cords[1] += self.speed * dy
            self._cords[2] += self.speed * dz
        return self._cords
    def get_cords(self):
        print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")             # "Извини, я настроен миролюбиво :)"
        else:
            print("Be careful, i'm attacking you 0_0")  # "Будь осторожен, я атакую тебя 0_0"
    def speak(self):
        print(f'{self.sound}')

class Bird(Animal):
    beak = True
    def lay_eggs(self):
        print(f'Here are(is) {random.randrange(1, 5)} eggs for you') # "Здесь... яиц для тебя"

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3
    def dive_in(self, dz):
        self._cords[2] = self._cords[2] - abs(dz) * self.speed / 2    # Изменение координаты при нырянии
        return self._cords[2]

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(PoisonousAnimal, AquaticAnimal, Bird):
    sound = "Click-click-click"

db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()
