from random import randint
import src.screen as screen


class Entity:
    # class principale des joueurs / mobs ...
    tex = ["█"]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velX = 0
        self.velY = 0

    def update(self, dt):
        self.x += self.velX * dt
        self.y += self.velY * dt

    def draw(self):
        for y in range(len(self.__class__.tex)):
            for x in range(len(self.__class__.tex[0])):
                screen.placerPixel(
                    x + self.x, y + self.y, self.__class__.tex[y][x])


class Ship(Entity):
    # joueur
    tex = ["    ^    ",
           " |  █  | ",
           "<██---██>",
           "   ███   "]
    maxSpeed = 100

    def update(self, dt):

        if -5 > self.x:
            self.x = screen.width
        if self.x > screen.width:
            self.x = -5
        super().update(dt)


class Bullet(Entity):
    # balle
    def __init__(self, x, y):
        super().__init__(x, y)
        self.shot = False
    tex = ["█",
           "█"]

    def reset(self, x, y):
        self.x = x + 4
        self.y = y
        self.shot = False
        self.velY = 0


class Mob(Entity):
    # classe principale des mobs
    tex = ["█"]

    def update(self, dt):
        return super().update(dt)

    def collision(self, x, y):
        if self.x - 0.5 < x < self.x + \
                len(self.__class__.tex[0]) and self.y < y < self.y + len(self.__class__.tex):
            return True
        return False


class Mob1(Mob):
    tex = ["  ▀█   █▀  ",
           " ██ ███ ██ ",
           "███████████",
           "█ ██   ██ █",
           "   ██ ██   "]


class Mob2(Mob):
    tex = ["    ▄█▄    ",
           "  ▄█████▄  ",
           "▄██ ███ ██▄",
           "███▀███▀███",
           " █       █ "]


class Mob3(Mob):
    tex = ["    ▄█▄    ",
           "▄█████████▄",
           "██  ███  ██",
           "█████ █████",
           "  █  █  █  "]


class texte(Entity):
    # affiche des textes
    tex = [["███████╗██████╗  █████╗  ██████╗███████╗        ██╗███╗   ██╗██╗   ██╗ █████╗ ██████╗ ███████╗██████╗ ███████╗",
           "██╔════╝██╔══██╗██╔══██╗██╔════╝██╔════╝        ██║████╗  ██║██║   ██║██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔════╝",
            "███████╗██████╔╝███████║██║     █████╗          ██║██╔██╗ ██║██║   ██║███████║██║  ██║█████╗  ██████╔╝███████╗",
            "╚════██║██╔═══╝ ██╔══██║██║     ██╔══╝          ██║██║╚██╗██║╚██╗ ██╔╝██╔══██║██║  ██║██╔══╝  ██╔══██╗╚════██║",
            "███████║██║     ██║  ██║╚██████╗███████╗███████╗██║██║ ╚████║ ╚████╔╝ ██║  ██║██████╔╝███████╗██║  ██║███████║",
            "╚══════╝╚═╝     ╚═╝  ╚═╝ ╚═════╝╚══════╝╚══════╝╚═╝╚═╝  ╚═══╝  ╚═══╝  ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝╚══════╝", ],
           ["       _             ",
           " _ __ | | __ _ _   _ ",
            "| '_ \\| |/ _` | | | |",
            "| |_) | | (_| | |_| |",
            "| .__/|_|\\__,_|\\__, |",
            "|_|            |___/ "],
           ["  _ __ ___   ___ _ __  _   _ ",
           " | '_ ` _ \\ / _ \\ '_ \\| | | |",
            " | | | | | |  __/ | | | |_| |",
            " |_| |_| |_|\\___|_| |_|\\__,_|"],
           ["█████████████████████████",
           "█        _              █",
            "█  _ __ | | __ _ _   _  █",
            "█ | '_ \\| |/ _` | | | | █",
            "█ | |_) | | (_| | |_| | █",
            "█ | .__/|_|\\__,_|\\__, | █",
            "█ |_|            |___/  █",
            "█                       █",
            "█████████████████████████"],
           ["████████████████████████████████",
           "█  _ __ ___   ___ _ __  _   _  █",
            "█ | '_ ` _ \\ / _ \\ '_ \\| | | | █",
            "█ | | | | | |  __/ | | | |_| | █",
            "█ |_| |_| |_|\\___|_| |_|\\__,_| █",
            "█                              █",
            "████████████████████████████████"],
           ["  ▄████  ▄▄▄       ███▄ ▄███▓▓█████        ▒█████   ██▒   █▓▓█████  ██▀███  ",
           " ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀       ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒",
            "▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███         ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒",
            "░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄       ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  ",
            "░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒      ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒",
            " ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░      ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░",
            "  ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░        ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░",
            "░ ░   ░   ░   ▒   ░      ░      ░         ░ ░ ░ ▒       ░░     ░     ░░   ░ ",
            "      ░       ░  ░       ░      ░  ░          ░ ░        ░     ░  ░   ░     ",
            "                                                        ░                   "],
           ["   ___        _   _             ",
           "  / _ \\ _ __ | |_(_) ___  _ __  ",
            " | | | | '_ \\| __| |/ _ \\| '_ \\ ",
            " | |_| | |_) | |_| | (_) | | | |",
            "  \\___/| .__/ \\__|_|\\___/|_| |_|",
            "       |_|                      "],
           ["███████████████████████████████████",
           "█   ___        _   _              █",
            "█  / _ \\ _ __ | |_(_) ___  _ __   █",
            "█ | | | | '_ \\| __| |/ _ \\| '_ \\  █",
            "█ | |_| | |_) | |_| | (_) | | | | █",
            "█  \\___/| .__/ \\__|_|\\___/|_| |_| █",
            "█       |_|                       █",
            "█                                 █",
            "███████████████████████████████████"]]

    def draw(self, id, x, y):
        self.x = x
        self.y = y
        for y in range(len(self.__class__.tex[id])):
            for x in range(len(self.__class__.tex[id][0])):
                screen.placerPixel(
                    x + self.x,
                    y + self.y,
                    self.__class__.tex[id][y][x])

    def set(self, text, x, y):
        i = 0
        for letter in text:
            i += 1
            screen.placerPixel(x + i - 1, y, letter)

    def getCenterX(self, id):
        return (screen.width - len(self.__class__.tex[id][0])) // 2


class Explosion:
    # crée une explosion quand un mob meurt
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 0

    def update(self, dt):
        self.r += dt * 30
        for y in range(round(-0.5 * self.r), round(0.5 * self.r)):
            for x in range(round(-self.r), round(self.r)):
                if 0.5 * x**2 + y**2 < 0.3 * self.r**2:
                    char = randint(0, 15)
                    if char < 3:
                        screen.placerPixel(
                            self.x + x + 5, self.y + y + 3, '-|+'[char])
