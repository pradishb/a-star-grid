"Test cases for a star"
import unittest

import numpy as np
import a_star


class TestCases(unittest.TestCase):
    "Class for testing a star"

    def test_when_route_exists(self):
        "Test case for when route exists"
        grid = np.load("data/walkable_data.npy")

        start = (508, 1260)
        goal = (556, 1277)

        expected_route = [
            (508, 1260), (509, 1260), (510, 1260), (511, 1260),
            (512, 1260), (513, 1260), (514, 1260), (515, 1259),
            (516, 1258), (517, 1258), (518, 1258), (519, 1258),
            (520, 1258), (521, 1258), (522, 1258), (523, 1258),
            (524, 1258), (525, 1258), (526, 1258), (527, 1258),
            (528, 1258), (529, 1258), (530, 1258), (531, 1259),
            (532, 1260), (533, 1260), (534, 1260), (535, 1261),
            (536, 1261), (537, 1261), (538, 1261), (539, 1262),
            (540, 1263), (541, 1264), (542, 1265), (543, 1266),
            (544, 1267), (545, 1268), (546, 1269), (547, 1270),
            (548, 1271), (549, 1272), (550, 1273), (551, 1274),
            (552, 1275), (553, 1276), (554, 1276), (555, 1276),
            (556, 1277)]

        route = a_star.find_route(grid, start, goal)
        self.assertEqual(route, expected_route)

    def test_when_route_does_not_exist(self):
        "Test case for when route does not exists"
        grid = np.load("data/walkable_data.npy")

        start = (1154, 1141)
        goal = (1134, 1175)

        route = a_star.find_route(grid, start, goal)
        self.assertEqual(route, False)


if __name__ == '__main__':
    unittest.main()
