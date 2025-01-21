import sys
from pprint import pprint


class Pedestrian:
    def __init__(self):
        self.pos = 0
        self.v = 5
        self.go = False
        self.crossing_time = 1.44


class Car:
    def __init__(self):
        self.width = 2
        self.length = 5
        self.v = 20


def main():
    file_name = sys.argv[1]
    contents = read_data(file_name)
    data = parse_data(contents)

    run(data)


def run(data: dict):
    pedestrian = Pedestrian()
    car = Car()

    # ---- simulation for first car ----
    # this is a simulation for a car that is on the same lane as the pedestrian
    # if distance from pedestrian is at least 8m, pedestrian should pass now
    # if distance is less than 8m, pedestrian should wait till car is at 3m
    min_dist = 8
    next_min_dist = 3
    time = 0

    # get first lane car
    # if there's no car just return 0
    cars = data.get('cars')
    first_car = 0 if cars[0] == 0 else cars[0][0]

    print(f"time: {time} ns, car distance: {first_car}")

    if first_car >= 8:
        pedestrian.go = True
    else:
        # find the next possible time, when pedestrian can start moving
        # since they are on the same traffic belt, it can start moving once the cars
        # tail is at distance 0 - when car passes 5m from pedestrian
        # calculate time it takes for the car to drive current distance + 5m
        dist = first_car + 5
        passing_time = t(x=dist, v=car.v)
        print("passing time: ", passing_time, "ns")
        time += passing_time
    
    if pedestrian.go:
        pedestrian.pos += 2
        time += pedestrian.crossing_time
    
    print(f"time: {time}, pedestrian position: {pedestrian.pos}")
    
    # next car
    # ...

# functions for time, speed and distance
def t(x:int, v:int) -> int: return x / v
def v(x:int, t:int) -> int: return x / t
def x(v:int, t:int) -> int: return v * t


def read_data(file_name: str) -> list:
    """ Reads and returns contents as integers from a file """
    contents = []
    with open(file_name, "r") as file:
        contents = [[int(e) for e in line.split()] for line in file.readlines()]

    return contents


def parse_data(data: list) -> dict:
    """ Parses data and classifies given data as instructions specify """
    road = data[0]
    cars = [line[1:] for line in data[1:]]

    # fix empty lists where there are no cars
    # transform nanometers to meters. 1 nm = 1e-9 m
    for group in range(len(cars)):
        if not cars[group]:
            cars[group] = [0]
        for dist in range(len(group)):
            group[dist] = group[dist] * 1e-9

    return {'road': road, 'cars': cars}


if __name__ == "__main__":
    main()