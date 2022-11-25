class Hero:
    def __init__(self,speed,night_vision, teleport, invisible):
        self.__speed = speed
        self.__night_vision = night_vision
        self.__teleport = teleport
        self.__invisible = invisible

        def speed(self , speed):
            self.__speed = speed
        def speed1(self):
            return  self.__speed
        def n_vis(self , night_vision):
            self.__night_vision = night_vision
        def n_vis1(self):
            return self.__night_vision
        def teleport(self, teleport):
            self.__teleport = teleport
        def teleport1(self):
            return self.__teleport
        def invis(self, invisible):
            self.__invisible = invisible
        def invis1(self):
            return self.__invisible

Hero(speed=100,night_vision=True,teleport=True,invisible=True)
print(Hero.__str__(f"Hero:  "
                   f"speed 100.  "
                   f"night_vision True.  "
                   f"invisible True."))


