"Test cases for a star"
import unittest

import numpy as np
import a_star


class TestCases(unittest.TestCase):
    "Class for testing a star"

    def test_when_route_exists(self):
        "Test case for when route exists"
        grid = np.load("data/walkable_data_7.npy")

        start = (1833, 855)
        goal = (1833, 886)
        expected_route = [
            (1833, 855), (1833, 856), (1833, 857), (1833, 858), (1833, 859),
            (1833, 860), (1833, 861), (1833, 862), (1833, 863), (1832, 864), 
            (1832, 865), (1832, 866), (1832, 867), (1832, 868), (1832, 869), 
            (1832, 870), (1832, 871), (1832, 872), (1832, 873), (1832, 874), 
            (1832, 875), (1832, 876), (1832, 877), (1832, 878), (1832, 879), 
            (1832, 880), (1832, 881), (1832, 882), (1832, 883), (1832, 884), 
            (1832, 885), (1833, 886)]       
        route = a_star.find_route(grid, start, goal)
        self.assertEqual(route, expected_route)

    def test_when_route_does_not_exist(self):
        "Test case for when route does not exists"
        grid = np.load("data/walkable_data_7.npy")

        start = (1154, 1141)
        goal = (1134, 1175)

        route = a_star.find_route(grid, start, goal)
        self.assertEqual(route, False)


if __name__ == '__main__':
    unittest.main()
