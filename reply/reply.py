from typing import List, Tuple

# Define a Building class to store its position and weight factors
class Building:
    def __init__(self, x: int, y: int, latency_weight: int, conn_speed_weight: int):
        self.x = x
        self.y = y
        self.latency_weight = latency_weight
        self.conn_speed_weight = conn_speed_weight

# Define an Antenna class to store its position and range/connection speed factors
class Antenna:
    def __init__(self, x: int, y: int, range: int, conn_speed: int):
        self.x = x
        self.y = y
        self.range = range
        self.conn_speed = conn_speed

# Function to compute the distance between two points
def distance(x1: int, y1: int, x2: int, y2: int) -> float:
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

# Function to find the best antenna for a given building
def find_best_antenna(building: Building, antennas: List[Antenna]) -> Antenna:
    best_antenna = None
    best_score = -float('inf')
    for antenna in antennas:
        dist = distance(building.x, building.y, antenna.x, antenna.y)
        if dist <= antenna.range:
            score = (building.latency_weight * antenna.conn_speed) - (dist * building.conn_speed_weight)
            if score > best_score:
                best_antenna = antenna
                best_score = score
    return best_antenna

# Read input data
with open('input.txt') as f:
#with open(input(), 'rU') as f:
    W, H = map(int, f.readline().split())
    N, M, R = map(int, f.readline().split())
    buildings = []
    for i in range(N):
        x, y, latency_weight, conn_speed_weight = map(int, f.readline().split())
        buildings.append(Building(x, y, latency_weight, conn_speed_weight))
        print(buildings)
    antennas = []
    for i in range(M):
        range, conn_speed = map(int, f.readline().split())
        antennas.append(Antenna(-1, -1, range, conn_speed))# initial position is (-1, -1) as it will be computed later
        print(antennas[i].range, antennas[i].conn_speed)

# Find the best antenna for each building
    for building in buildings:
        best_antenna = find_best_antenna(building, antennas)
        if best_antenna is not None:
            if best_antenna.x == -1 and best_antenna.y == -1:
                # if the antenna has not been placed yet, place it at the building position
                best_antenna.x = building.x
                best_antenna.y = building.y
            else:
                # if the antenna has been placed already, update its position to the centroid of the buildings it serves
                n_buildings = 1
                centroid_x = building.x
                centroid_y = building.y
                for other_building in buildings:
                    if other_building != building:
                        dist = distance(other_building.x, other_building.y, best_antenna.x, best_antenna.y)
                        if dist <= best_antenna.range:
                            n_buildings += 1
                            centroid_x += other_building.x
                            centroid_y += other_building.y
                best_antenna.x = int(round(centroid_x / n_buildings))
                best_antenna.y = int(round(centroid_y / n_buildings))
            print(best_antenna.x, best_antenna.y)

# Compute the score
score = 0
for building in buildings:
    best_antenna = find_best_antenna
    print(best_antenna)
    if best_antenna is not None:
        print(best_antenna)
