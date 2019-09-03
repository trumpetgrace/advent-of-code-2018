import numpy as np
from collections import defaultdict

with open("input6.txt") as f:
    lines = f.readlines()
lines = [x.strip() for x in lines]


def largest_area(coords_list):
    coords = np.array([coord.split(', ') for coord in coords_list], dtype="int16")
    min_x, min_y = np.min(coords, axis=0)
    max_x, max_y = np.max(coords, axis=0)
    areas = defaultdict(int)
    infinite_areas = []
    for i in range(min_x, max_x + 1):
        for j in range(min_y, max_y + 1):
            dist = np.abs(coords - [i, j])
            dist = np.sum(dist, axis=1)
            min_dist = np.argmin(dist)
            if not np.count_nonzero(dist[min_dist:] == dist[min_dist]) == 1:
                min_dist = None
            areas[min_dist] += 1
            if i == min_x or i == max_x or j == min_y or j == max_y:
                infinite_areas.append(min_dist)
    return max(areas[coord] for coord in areas if coord not in infinite_areas)


def largest_region_within_distance(coords_list, distance):
    coords = np.array([coord.split(', ') for coord in coords_list], dtype="int16")
    min_x, min_y = np.min(coords, axis=0)
    max_x, max_y = np.max(coords, axis=0)
    count = 0
    for i in range(min_x, max_x + 1):
        for j in range(min_y, max_y + 1):
            if sum(abs(coord[0] - i) + abs(coord[1] - j) for coord in coords) < distance:
                count += 1
    return count


if __name__ == "__main__":
    print(largest_area(lines))
    print(largest_region_within_distance(lines, 10000))
