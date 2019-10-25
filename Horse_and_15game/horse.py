from collections import deque
import time


def is_digit(digit):
        try:
            n = int(digit)
            return n
        except ValueError:
            return("Invalid input")


def check_coordinate(coordinates_dict):
    for value in coordinates_dict.values():
        if value == "Invalid input" or value < 0:
            print("Wrong coordinate type")
            return False
    if coordinates_dict['horse_x'] > coordinates_dict['W'] or coordinates_dict['apple_x'] > coordinates_dict['W']:
        return False
    if coordinates_dict['horse_y'] > coordinates_dict['H'] or coordinates_dict['apple_y'] > coordinates_dict['H']:
        return False
    return True


def add_edge(vertex_1, vertex_2):
    graph[vertex_1].add(vertex_2)
    graph[vertex_2].add(vertex_1)


def BFS_and_Li_algorithm(created_graph, horse_x, horse_y, apple_x, apple_y):
    distances = {v: None for v in graph}
    parents = {v: None for v in graph}

    start_vertex = (horse_x, horse_y)
    end_vertex = (apple_x, apple_y)

    distances[start_vertex] = 0
    queue = deque([start_vertex])

    while queue:
        cur_v = queue.popleft()
        for neigh_v in created_graph[cur_v]:
            if distances[neigh_v] is None:
                distances[neigh_v] = distances[cur_v] + 1
                parents[neigh_v] = cur_v
                queue.append(neigh_v)

    path_to_food = [end_vertex]
    parent = parents[end_vertex]
    while parent is not None:
        path_to_food.append(parent)
        parent = parents[parent]
    return path_to_food


start_time = time.time()

coordinates_dict = dict.fromkeys(['W', 'H', 'horse_x', 'horse_y', 'apple_x', 'apple_y'])

with open("coordinates_file.txt", "r") as file:
    coordinates = file.readline().split(' ')
    if len(coordinates) >= 6:
        coordinates_dict['W'] = is_digit(coordinates[0])
        coordinates_dict['H'] = is_digit(coordinates[1])
        coordinates_dict['horse_x'] = is_digit(coordinates[2])
        coordinates_dict['horse_y'] = is_digit(coordinates[3])
        coordinates_dict['apple_x'] = is_digit(coordinates[4])
        coordinates_dict['apple_y'] = is_digit(coordinates[5])

    else:
        print("Wrong amount of coordinates!")
    if check_coordinate(coordinates_dict):
        graph = dict()
        for i in range(coordinates_dict['W']):
            for j in range(coordinates_dict['H']):
                graph[(i, j)] = set()
        for i in range(coordinates_dict['W']):
            for j in range(coordinates_dict['H']):
                v1 = (i, j)
                v2 = ''
                if 0 <= i + 2 < coordinates_dict['W'] and 0 <= j + 1 < coordinates_dict['H']:
                    v2 = (i+2, j+1)
                    add_edge(v1, v2)
                if 0 <= i - 2 < coordinates_dict['W'] and 0 <= j + 1 < coordinates_dict['H']:
                    v2 = (i-2, j+1)
                    add_edge(v1, v2)
                if 0 <= i + 1 < coordinates_dict['W'] and 0 <= j + 2 < coordinates_dict['H']:
                    v2 = (i+1, j+2)
                    add_edge(v1, v2)
                if 0 <= i - 1 < coordinates_dict['W'] and 0 <= j + 2 < coordinates_dict['H']:
                    v2 = (i-1, j+2)
                    add_edge(v1, v2)
        path = BFS_and_Li_algorithm(graph,coordinates_dict['horse_x'], coordinates_dict['horse_y'],
                             coordinates_dict['apple_x'], coordinates_dict['apple_y'])

        print("--- %s seconds ---" % (time.time() - start_time))
        print(path[::-1])
        print(len(path))
        print(graph)
        print(coordinates_dict)

