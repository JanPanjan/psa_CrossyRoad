from dataclasses import dataclass
from parser import Parser


@dataclass
class Pedestrian:
    v = 5 / 3.6 # 5 km/h <=> 5/3.6 m/s <=> 5/3.6 nm/ps
    crossing_t = 2 / v # time to cross one lane


@dataclass
class Car:
    width = 2e-9 #nm
    length = 5e-9 #nm
    v = 20 / 3.6


if __name__ == "__main__":
    file_name = "crossy_road/src/data.txt"
    contents = Parser.read_data(file_name)
    data = Parser.parse_data(contents)