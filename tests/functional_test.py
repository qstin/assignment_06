import random
import unittest

from .. import point


class TestFunctionalPointPattern(unittest.TestCase):

    def setUp(self):
        random.seed(12345)
        i = 0
        self.points = []
        marks = ['ying', 'yang', 'black', 'white']
        rand_marks = []
        for mark in range(100):
            rand_marks.append(random.choice(marks))
        while i < 100:
            seed = point.Point(round(random.random(),2),
                    round(random.random(),2), rand_marks[i])
            self.points.append(seed)
            n_additional = random.randint(5,10)
            i += 1
            c = random.choice([0,1])
            if c:
                for j in range(n_additional):
                    x_offset = random.randint(0,10) / 100
                    y_offset = random.randint(0,10) / 100
                    pt = point.Point(round(seed.x + x_offset, 2), round(seed.y +
                        y_offset,2), random.choice(marks))
                    self.points.append(pt)
                    i += 1
                    if i == 100:
                        break
            if i == 100:
                break

    def test_point_pattern(self):
        """
        This test checks that the code can compute an observed mean
         nearest neighbor distance and then use Monte Carlo simulation to
         generate some number of permutations.  A permutation is the mean
         nearest neighbor distance computed using a random realization of
         the point process.
        """
        random.seed()  # Reset the random number generator using system time
        # I do not know where you have moved
        # avarege_nearest_neighbor_distance, so update the point_pattern module
        observed_avg = point.average_nearest_neighbor_distance(self.points)
        self.assertAlmostEqual(0.02779598180193161, observed_avg, 3)

        # Again, update the point_pattern module name for where you have placed the point_pattern module
        # Also update the create_random function name for whatever you named the function to generate
        # random points
        marks = ['ying', 'yang', 'black', 'white'] 
        rand_points = point.create_random_marked_points(100, marks)
        self.assertEqual(100, len(rand_points))

        # As above, update the module and function name.
        permutations = point.permutations(99)
        self.assertEqual(len(permutations), 99)
        self.assertNotEqual(permutations[0], permutations[1])

        # As above, update the module and function name.
        lower, upper = point.compute_critical(permutations)
        self.assertTrue(lower > 0.03)
        self.assertTrue(upper < 0.07)
        self.assertTrue(observed_avg < lower or observed_avg > upper)

        # As above, update the module and function name.
        significant = point.check_significant(lower, upper, observed_avg)
        self.assertTrue(significant)

        self.assertTrue(True)
