from random import uniform, gauss, random
from math import sqrt, sin, cos, pi, exp
from time import time

"""https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection#Given_two_points_on_each_line"""
"""https://en.wikipedia.org/wiki/Normal_distribution"""
"""http://www.cim.mcgill.ca/~yiannis/particletutorial.pdf"""


class Space:

    def __init__(self, n, coordinates):
        '''
        В нас кімната задається координатами стін x та y
        А n це кількісь цих координат
        '''
        self.n = n
        self.x = []
        self.y = []

        coordinates = coordinates.split()

        for i in range(0, 2 * n, 2):
            self.x.append(int(coordinates[i]))
            self.y.append(int(coordinates[i + 1]))
    
    def bound(self):
        return min(self.x), min(self.y), max(self.x), max(self.y)

    def diagonal(self):
        '''
        Беремо крайні значення по x та y, щоб знайти координати прямокутника описаного навколо приміщення
        '''
        min_x, min_y, max_x, max_y = self.bound()
        '''
        Для зручності обрахунків беремо діагональ
        '''
        return sqrt((max_x - min_x) ** 2 + (max_y - min_y) ** 2)

    def distance(self, robot, angle):
        '''
        Функція для пошуку показника для одного з променів лідару
        Відстан будемо рахувати від роботу до точки перетину з найближчою стіною
        Для цього промінь лідара робимо відрізком довжина якого рівна розмірам прямокутника описаного навколо приміщення
        '''

        #координати робота
        x3, y3 = robot.x, robot.y

        #координати кінця відрізка який ми будуємо на промені лідара
        dist = self.diagonal()
        x4, y4 = robot.x + self.diagonal() * cos(angle), robot.y + self.diagonal() * sin(angle)


        for i in range(self.n):
            #Відрізок сторони це сусідні по списку координати
            x1, y1 = self.x[i], self.y[i]
            if i == self.n - 1:
                x2, y2 = self.x[0], self.y[0]
            else:
                x2, y2 = self.x[i + 1], self.y[i + 1]

            #перевірка на парлельність
            if (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4) != 0:
                #параметри базьє
                t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
                u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))

                #чи налажать одному та іншому відрізків точка перетину
                if 0 <= t <= 1 and 0 <= u <= 1:
                    point1 = x1 + t * (x2 - x1), y1 + t * (y2 - y1)
                    point2 = x3 + u * (x4 - x3), y3 + u * (y4 - y3)
                else:
                    point1 = None

                #відстань - показник променя лідару
                if point1:
                    new_dist = sqrt((robot.x - point1[0]) ** 2 + (robot.y - point1[1]) ** 2)
                    if new_dist < dist:
                        dist = new_dist
        return dist


class Robot:

    def __init__(self, space, x=None, y=None, sl=0.1, sx=0.1, sy=0.1, k=36):
        self.space = space
        bound = self.space.bound()

        #якщо не введені координати то задаємо їх випадковим чином в межах прямокутника описаного навколо приміщення
        self.x = x if x else uniform(bound[0], bound[2])
        self.y = y if y else uniform(bound[1], bound[3])

        #вага
        self.w = 1
        self.real = False
        self.distances = []

        #шум вимірів лідару та координат розміщення
        self.l_noise = sl
        self.x_noise = sx
        self.y_noise = sy
        self.k = k


    def move(self, x, y):
        '''
        Просте переміщення по координатам
        '''
        self.x += x
        self.y += y

        #якщо це не реальний робот то переміщення з шумом щоб розсіювати точки для правильного пошуку розташування
        if not self.real:
            self.x += gauss(0, self.x_noise)
            self.y += gauss(0, self.y_noise)

    def sense(self, step):
        '''
        В загальному пошук показників лідару
        '''
        #Якщо в нас якесь значення має step то ми беремо не умі промені лідару, а з певним кроком

        self.distances = []
        for a in range(0, self.k, step):
            angle = a * 360 / self.k * pi / 180
            #Пошук відстані для конкретного променя це функція класу Space
            self.distances.append(self.space.distance(self, angle))

    @staticmethod
    def gaussian(x, noise, rx):
        '''
        Вага для одного виміру одного променя лідару
        '''
        return exp(-((x - rx) ** 2) / (noise ** 2) / 2) / sqrt(2 * pi * (noise ** 2))


    def probability(self, rx):
        res = 1
        for j in range(len(rx)):
            res *= self.gaussian(self.distances[j], self.l_noise, rx[j])
        '''
        Результуюча вага це перемножені усі ваги
        '''
        self.w = res



def generate_robots(n, space, sl, sx, sy, k):
    '''
    Генеруємо перших роботів з певними значенями шумів та лідаром з k променями в нашому просторі
    '''
    robots = []
    for _ in range(n):
        robot = Robot(space, sl=sl, sx=sx, sy=sy, k=k)
        robots.append(robot)
    return robots

def sense(robots, real_x, step):
    max_w = 0
    # маємо показники реального робота і якщо step то берем тільки значення з певним кроком
    real_x = [real_x[i] for i in range(0, robots[0].k, step)]

    for r in robots:
        r.sense(step)
        r.probability(real_x)

        if r.w > max_w:
            max_w = r.w
    #знайшли найблільшу вагу

    return max_w


def weight_func(w):
    return sqrt(w)

def create_robots(robots, space, decrease=False):
    '''
    Створюємо нових роботів на наступний крок
    '''
    new_robots = []

    # Маємо a замість w
    a = [weight_func(r.w) for r in robots]

    # Нормалізуємо значення ваг до кількості роботів
    # Тобто щоб сумма всіх значень була рівна N
    # І ті що  матимуть значення більше 1 будуть відповідати більшій вірогідності
    total_a = sum(a)
    a = [el * len(robots) / total_a for el in a]

    for i in range(len(a)):
        # Якщо нормалізована вага більша 1 то створюємо k або k/10 копій робота
        if a[i] >= 1:
            #Менше коли це перший крок для пришвидшення роботи алгоритму бо ми маємо багато роботів 
            if decrease:
                k = int(a[i] / 10)
            else:
                k = int(a[i])

            for _ in range(k):
                new_robots.append(Robot(space, robots[i].x, robots[i].y, sl=robots[i].l_noise, sx=robots[i].x_noise,
                                        sy=robots[i].y_noise, k=robots[i].k))
        else:
            # Якщо значення мале було то в залежності від random залишаємо або викидаємо цього робота
            if random() < a[i]:
                new_robots.append(Robot(space, robots[i].x, robots[i].y, sl=robots[i].l_noise, sx=robots[i].x_noise,
                                        sy=robots[i].y_noise, k=robots[i].k))

    return new_robots

def move(move_x, move_y, robots):
    for r in robots:
        r.move(move_x, move_y)




def main():

    #задаємо приміщення по координатах
    space = Space(int(input()), input())

    #кількість кроків і кількість променів лідару
    m, k = input().split()
    m, k = int(m), int(k)
    #похибки вимірювань лідару та переміщення
    sl, sx, sy = input().split()
    sl, sx, sy = float(sl), float(sx), float(sy)
    #на початкові координати нам байдуже алгоритм робимо так ніби їх нема
    inp = input().split()

    #Якщо променів лідару дуже багато то генеруємо менше точок, щоб вписуватись в допустимий час виконання алгоритму
    if k < 50:
        n, step = 5000, 1
    else:
        n, step = 3000, 18
    #Перших роботів створюємо з додатковим шумом щоб вони точно не оминули допустимий окіл реального значенння
    robots = generate_robots(n, space, sl * 5, sx * 2, sy * 2, k)

    for i in range(m + 1):
        #маємо показники реального робота
        real_x = [float(el) for el in input().split()]

        #обраховуємо max вагу для дебагу, якщо вона 0 то шось не так
        max_w = sense(robots, real_x, step)

        if max_w == 0:
            print([round(el, 1) for el in real_x])
            for r in robots:
                print([round(el, 1) for el in r.distances])

        #якщо це перша ітерація то нових роботів створюємо менше для швидкодії алгоритму
        if i == 0:
            robots = create_robots(robots, space, decrease=True)
        else:
            robots = create_robots(robots, space)


        #Якщо це не остання ітерація то пересуваємо роботів
        if i != m:
            move_x, move_y = input().split()
            move_x, move_y = float(move_x), float(move_y)
            move(move_x, move_y, robots)

        #Додаємо шум, якщо це перша ітерація то шум уже заданий вище
        if i == 0:
            for r in robots:
                r.l_noise = sl
                r.x_noise = sx
                r.y_noise = sy


    '''
    Фінальне значення беремо як середнє значення точок
    '''
    print(sum(r.x for r in robots) / len(robots), end=' ')
    print(sum(r.y for r in robots) / len(robots))

if __name__ == '__main__':
    main()