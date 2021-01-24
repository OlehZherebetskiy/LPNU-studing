from random import uniform, gauss, random
from math import sqrt, sin, cos, pi, exp
from time import time
# import matplotlib.pyplot as plt


class Space:
    def __init__(self, n, coordinates):
        self.n = n
        self.x = []
        self.y = []

        coordinates = coordinates.split()
        for i in range(0, 2 * n, 2):
            self.x.append(int(coordinates[i]))
            self.y.append(int(coordinates[i + 1]))

    def distance(self, robot, angle):
        """https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection#Given_two_points_on_each_line"""

        dist = self.diagonal()
        x3, y3 = robot.x, robot.y
        x4, y4 = robot.x + self.diagonal() * cos(angle), robot.y + self.diagonal() * sin(angle)

        for i in range(self.n):
            x1, y1 = self.x[i], self.y[i]
            if i == self.n - 1:
                x2, y2 = self.x[0], self.y[0]
            else:
                x2, y2 = self.x[i + 1], self.y[i + 1]

            if (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4) != 0:  # not parallel
                t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
                u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))

                if 0 <= t <= 1 and 0 <= u <= 1:
                    point1 = x1 + t * (x2 - x1), y1 + t * (y2 - y1)
                    point2 = x3 + u * (x4 - x3), y3 + u * (y4 - y3)
                else:
                    point1 = None

                if point1:
                    new_dist = sqrt((robot.x - point1[0]) ** 2 + (robot.y - point1[1]) ** 2)
                    if new_dist < dist:
                        dist = new_dist
        return dist

    def bound(self):
        return min(self.x), min(self.y), max(self.x), max(self.y)

    def diagonal(self):
        min_x, min_y, max_x, max_y = self.bound()
        return sqrt((max_x - min_x) ** 2 + (max_y - min_y) ** 2)

    # def plot(self):
    #     for i in range(self.n):
    #         if i == self.n - 1:
    #             plt.plot([self.x[i], self.x[0]], [self.y[i], self.y[0]], 'k')
    #         else:
    #             plt.plot([self.x[i], self.x[i + 1]], [self.y[i], self.y[i + 1]], 'k')


class Robot:
    def __init__(self, space, x=None, y=None, sl=0.1, sx=0.1, sy=0.1, k=36):
        self.space = space
        bound = self.space.bound()

        self.x = x if x else uniform(bound[0], bound[2])
        self.y = y if y else uniform(bound[1], bound[3])

        self.w = 1
        self.real = False
        self.distances = []

        self.l_noise = sl
        self.x_noise = sx
        self.y_noise = sy
        self.k = k

    def __str__(self):
        return f'x: {self.x} y: {self.y} sl: {self.l_noise} sx: {self.x_noise} sy: {self.y_noise} k: {self.k} ' \
               f' dist: {self.distances}'

    # def plot(self):
    #     if self.real:
    #         plt.plot(self.x, self.y, 'Dk')
    #     else:
    #         plt.plot(self.x, self.y, '.y')

    def move(self, x, y):
        self.x += x
        self.y += y
        if not self.real:
            self.x += gauss(0, self.x_noise)
            self.y += gauss(0, self.y_noise)

    def sense(self, step):
        self.distances = []
        for a in range(0, self.k, step):
            angle = a * 360 / self.k * pi / 180
            self.distances.append(self.space.distance(self, angle))

    @staticmethod
    def gaussian(x, noise, rx):
        """https://en.wikipedia.org/wiki/Normal_distribution"""
        return exp(-((x - rx) ** 2) / (noise ** 2) / 2) / sqrt(2 * pi * (noise ** 2))

    def probability(self, rx):
        res = 1
        for j in range(len(rx)):
            res *= self.gaussian(self.distances[j], self.l_noise, rx[j])
        self.w = res


def generate_robots(n, space, sl, sx, sy, k):
    robots = []
    for _ in range(n):
        robot = Robot(space, sl=sl, sx=sx, sy=sy, k=k)
        robots.append(robot)
    return robots


def sense(robots, real_x, step):
    max_w = 0
    real_x = [real_x[i] for i in range(0, robots[0].k, step)]

    for r in robots:
        r.sense(step)
        r.probability(real_x)

        if r.w > max_w:
            max_w = r.w
    return max_w


def weight_func(w):
    return sqrt(w)


def create_robots(robots, space, decrease=False):
    """http://www.cim.mcgill.ca/~yiannis/particletutorial.pdf"""
    new_robots = []

    # create a instead of w using weight function
    a = [weight_func(r.w) for r in robots]

    # normalize a so they sum up to amount of robots
    total_a = sum(a)
    a = [el * len(robots) / total_a for el in a]

    for i in range(len(a)):
        # if a is >= 1 then create k or k/10 copies of this robot
        if a[i] >= 1:
            if decrease:
                k = int(a[i] / 10)
            else:
                k = int(a[i])

            for _ in range(k):
                new_robots.append(Robot(space, robots[i].x, robots[i].y, sl=robots[i].l_noise, sx=robots[i].x_noise,
                                        sy=robots[i].y_noise, k=robots[i].k))
        else:
            # with probability a create 1 robot or not
            if random() < a[i]:
                new_robots.append(Robot(space, robots[i].x, robots[i].y, sl=robots[i].l_noise, sx=robots[i].x_noise,
                                        sy=robots[i].y_noise, k=robots[i].k))

    return new_robots


def move(move_x, move_y, robots):
    for r in robots:
        r.move(move_x, move_y)


def plot_robots(robots):
    for r in robots:
        r.plot()


def main():
    # start = time()
    # create space
    space = Space(int(input()), input())
    # space.plot()

    # input data
    m, k = input().split()
    m, k = int(m), int(k)
    sl, sx, sy = input().split()
    sl, sx, sy = float(sl), float(sx), float(sy)
    inp = input().split()

    # create first robots
    if k < 50:
        n, step = 5000, 1
    else:
        n, step = 3000, 18
    robots = generate_robots(n, space, sl * 5, sx * 2, sy * 2, k)
    # plot_robots(robots)
    # plt.show()

    for i in range(m + 1):
        # sense
        real_x = [float(el) for el in input().split()]
        max_w = sense(robots, real_x, step)

        if max_w == 0:
            print([round(el, 1) for el in real_x])
            for r in robots:
                print([round(el, 1) for el in r.distances])

        # create new robots
        if i == 0:
            robots = create_robots(robots, space, decrease=True)
        else:
            robots = create_robots(robots, space)

        # space.plot()
        # plot_robots(robots)
        # plt.show()

        # move new robots
        if i != m:
            move_x, move_y = input().split()
            move_x, move_y = float(move_x), float(move_y)
            move(move_x, move_y, robots)

        # after first iteration set real noise
        if i == 0:
            for r in robots:
                r.l_noise = sl
                r.x_noise = sx
                r.y_noise = sy

        # space.plot()
        # plot_robots(robots)
        # plt.show()

    # result
    print(sum(r.x for r in robots) / len(robots), end=' ')
    print(sum(r.y for r in robots) / len(robots))

    #  print('time', time() - start, 'sec')
    # answers = [[2.99802, 3.03753], [1.9406, 8.00725], [1.59266, 8.63027], [3.62952, 15.1485]]
    # print(sum(r.x for r in robots) / len(robots) - answers[test_num - 1][0])
    # print(sum(r.y for r in robots) / len(robots) - answers[test_num - 1][1])


if __name__ == '__main__':
    main()

