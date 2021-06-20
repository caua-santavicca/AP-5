class Character:
    def __init__(self, gear: int, name: str, relic: int = 0) -> None:
        self.__gear: int = gear
        self.__relic = relic
        self.__name: str = name

    @property
    def gear(self) -> int:
        return self.__gear

    @property
    def relic(self):
        return self.__relic

    @property
    def name(self):
        return self.__name
