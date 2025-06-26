import typing as T
from math import pi as PI

def circle_area(diameter: int|float) -> float:
    return PI * ((.5 * diameter) ** 2)

a: float

a = circle_area(20)
print(a)
a = circle_area(.8)
print(a)

b: str
b = circle_area(25)
print(b)

class Cat:
    pass

class Dog:
    def bark(self):
        print("woof! woof!")

d1 = Dog()
d2 = Dog()
c1 = Cat()

def adopt(animal: Dog|Cat):
    print(f"adopting {animal}")

adopt(d1)
adopt(d2)
adopt(c1)
adopt("abc")

def whatever(x: T.Any):
    pass

def get_values() -> list[int]:
    return [1, 2, 3]

def get_info() -> tuple[int,int,str]:
    return 2, 4, "eight"

def get_other_info() -> tuple[str, ...]:
    return "a", "b", "c"

#  list[dict[str,tuple[int,str]]]
x: Dog|Cat
y: str|None


def read_files(file_list: T.Iterable[str]):
    for file_name in file_list:
        print(f"reading {file_name}")

