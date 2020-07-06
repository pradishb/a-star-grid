'''Testing module'''
import cv2
import numpy

from a_star import a_star, create_visualizer


def main():
    '''Main function of the testing module'''
    image = cv2.imread('assets/map.png', cv2.IMREAD_COLOR)
    visualize = create_visualizer(image)
    image = numpy.all(image == (0, 255, 255), axis=2)
    route = a_star(image, (33, 8), (42, 114))
    visualize(route)


if __name__ == '__main__':
    main()
