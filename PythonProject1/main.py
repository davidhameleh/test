import random
from typing import Any
import time



def time_it(func):
    def actual_function(*args):
        before=time.time()
        func(*args)
        after=time.time()
        print(f"The function took {after-before} seconds, it was {func.__name__}")
        return after-before
    return actual_function

@time_it
def start_simulation_gemini():
        attempts = a
        plate_length = p
        simulation_67_gemini(attempts, plate_length)
@time_it
def start_simulation_david():
        attempts = a
        plate_length = p
        simulation_67_david(attempts, plate_length)

def simulation_67_gemini(attempts: int, plate_length: int) -> float:
    count_67_found = 0

    for _ in range(attempts):
        # Generate full plate as a string directly
        plate = "".join(str(random.randint(0, 9)) for _ in range(plate_length))
        if "67" in plate:
            count_67_found += 1

    chance_of_finding_67 = (count_67_found / attempts) * 100
    print(f"Based on the simulations, the chance to find '67' is {chance_of_finding_67:.4f}%!")
    return chance_of_finding_67

def simulation_67_david(attempts :int ,plate_length: int):
    count_67_found = 0
    total_attempts = 0
    for i in range(attempts):
        license_plate = []
        for j in range(plate_length): # Setting up the random license plate
            license_plate.append(random.randint(0,9))
        if has_67(license_plate):
            count_67_found+=1
        total_attempts +=1
    chance_of_finding_67 = (count_67_found / total_attempts) *100
    print(f"Based on the simulation, the chance to find 67 is {chance_of_finding_67}% ! ")
    return chance_of_finding_67


def has_67(license_plate: list[Any]): # Finding out if the 67 exists
    for idx in range(len(license_plate)):
        if idx != len(license_plate) - 1:
             current_ = license_plate[idx]
             next_ = license_plate[idx + 1]
             if current_ == 6 and next_ == 7:
                return True
    return False


if __name__ == '__main__':
    a = 1000000  # num of attempts
    p = 8  # num of plates
    time_david = float(start_simulation_david())
    time_gemini =float(start_simulation_gemini())
    if time_gemini-time_david>0:
        print("David won")
    else:
        print("Gemini won")

