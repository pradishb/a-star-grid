'''Module for a star algorithm for grid'''
import heapq
import numpy as np
import cv2


__all__ = ['a_star', 'create_visualizer']

FOUR_DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
EIGHT_DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]


def heuristic(coordinates_1, coordinates_2):
    '''Heuristic function of the algorithm'''
    return np.sqrt((coordinates_2[0] - coordinates_1[0]) ** 2 +
                   (coordinates_2[1] - coordinates_1[1]) ** 2)


def create_route(start, current, came_from):
    '''Creates route from came_from data'''
    data = []
    while current in came_from:
        data.append(current)
        current = came_from[current]
    return [start] + data[::-1]


def a_star(grid, start, goal, diagonals=False):
    '''The main algorithm function'''
    neighbors = EIGHT_DIRECTIONS if diagonals else FOUR_DIRECTIONS

    close_set = set()
    came_from = {}
    gscore = {start: 0}
    fscore = {start: heuristic(start, goal)}
    oheap = []

    heapq.heappush(oheap, (fscore[start], start))

    while oheap:

        current = heapq.heappop(oheap)[1]

        if current == goal:
            return create_route(start, current, came_from)

        close_set.add(current)
        for i, j in neighbors:
            neighbor = current[0] + i, current[1] + j
            tentative_g_score = gscore[current] + heuristic(current, neighbor)
            if 0 <= neighbor[0] < grid.shape[0] and 0 <= neighbor[1] < grid.shape[1]:
                if grid[neighbor[1]][neighbor[0]] == 1:
                    continue
            else:
                # grid bound walls
                continue

            if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                continue

            if tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1]for i in oheap]:
                came_from[neighbor] = current
                gscore[neighbor] = tentative_g_score
                fscore[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(oheap, (fscore[neighbor], neighbor))
    raise RuntimeError('Route does not exist.')


def create_visualizer(image):
    '''Visualizes the route in the graph'''
    image = image.copy()
    title = 'A Star Route Visualizer'
    wait_time = 100

    def visualize(route):
        nonlocal image
        for coordinates in route:
            image[coordinates[1], coordinates[0]] = (0, 0, 255)
        image = cv2.resize(image, None, fx=5, fy=5, interpolation=cv2.INTER_NEAREST)
        cv2.imshow(title, image)
        while True:
            cv2.waitKey(wait_time)
            if cv2.getWindowProperty(title, cv2.WND_PROP_VISIBLE) < 1:
                cv2.destroyAllWindows()
                break
    return visualize
