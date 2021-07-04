class Mods:

    def __init__(self, speed: int, primary: str, dot: int, tier: str, slot: str, mod_set: str, mod_id: str,
                 character: str, roll: int):
        self.__speed = speed
        self.__primary = primary
        self.__dot = dot
        self.__tier = tier
        self.__slot = slot
        self.__mod_set = mod_set
        self.__id = mod_id
        self.__character = character
        self.__speed_roll = roll

    @property
    def speed(self):
        return self.__speed

    @property
    def primary(self):
        return self.__primary

    @property
    def dot(self):
        return self.__dot

    @property
    def tier(self):
        return self.__tier

    @property
    def slot(self):
        return self.__slot

    @property
    def mod_set(self):
        return self.__mod_set

    @property
    def id(self):
        return self.__id

    @property
    def character(self):
        return self.__character

    @property
    def speed_roll(self):
        return self.__speed_roll
