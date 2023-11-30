import random

ONE_CAT = '/img/one.jpg'
PLAY_CAT = '/img/play.jpg'
SLEEP_CAT = '/img/sleep.jpg'


class CatDB:
    name = ''
    age = 1
    satiety = 40
    happiness = 40
    is_sleeping = False
    photo = ONE_CAT

    @classmethod
    def feed(cls):
        if not cls.is_sleeping and cls.satiety <= 100:
            cls.satiety += 15
            cls.happiness += 5
            if cls.satiety > 100:
                cls.satiety = 100
                cls.happiness -= 30
                if cls.happiness < 30:
                    cls.sleep()
        cls.get_photo()

    @classmethod
    def play(cls):
        if not cls.is_sleeping:
            cls.happiness += 15
            cls.satiety -= 10
            if random.randint(1, 3) == 1:
                cls.happiness = 0
        elif cls.is_sleeping:
            cls.wake_up()
        cls.get_photo()

    @classmethod
    def sleep(cls):
        if not cls.is_sleeping:
            cls.is_sleeping = True
            cls.satiety += 10
            cls.happiness += 10
        cls.get_photo()

    @classmethod
    def wake_up(cls):
        if cls.is_sleeping:
            cls.is_sleeping = False
            cls.happiness -= 5

    @classmethod
    def get_satiety(cls):
        return max(0, min(cls.satiety, 100))

    @classmethod
    def get_happiness(cls):
        return max(0, min(cls.happiness, 100))

    @classmethod
    def get_photo(cls):
        if cls.is_sleeping:
            cls.photo = SLEEP_CAT
        elif not cls.is_sleeping and cls.get_happiness() > 40:
            cls.photo = PLAY_CAT
        else:
            cls.photo = ONE_CAT

    @classmethod
    def get_info(cls):
        return (f"Name: {cls.name}, "
                f"Age: {cls.age}, "
                f"Satiety: {cls.satiety}, "
                f"Happiness: {cls.happiness}, "
                f"Sleeping: {cls.is_sleeping}, "
                f"Photo: {cls.photo}")
