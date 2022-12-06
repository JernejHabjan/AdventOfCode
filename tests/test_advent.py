import unittest

from aoc_2015.aoc_01.a import aoc_2015_01_a
from aoc_2015.aoc_01.b import aoc_2015_01_b
from aoc_2015.aoc_02.a import aoc_2015_02_a
from aoc_2015.aoc_02.b import aoc_2015_02_b
from aoc_2015.aoc_03.a import aoc_2015_03_a
from aoc_2015.aoc_03.b import aoc_2015_03_b
from aoc_2015.aoc_04.a import aoc_2015_04_a
from aoc_2015.aoc_04.b import aoc_2015_04_b
from aoc_2015.aoc_05.a import aoc_2015_05_a
from aoc_2015.aoc_05.b import aoc_2015_05_b
from aoc_2015.aoc_06.a import aoc_2015_06_a
from aoc_2015.aoc_06.b import aoc_2015_06_b
from aoc_2015.aoc_07.a import aoc_2015_07_a

# from aoc_2020.aoc_01.a import aoc_2020_01_a # todo
# from aoc_2020.aoc_01.b import aoc_2020_01_b # todo
from aoc_2020.aoc_02.a import aoc_2020_02_a
from aoc_2020.aoc_02.b import aoc_2020_02_b
from aoc_2020.aoc_03.a import aoc_2020_03_a
from aoc_2020.aoc_03.b import aoc_2020_03_b
from aoc_2020.aoc_04.a import aoc_2020_04_a
from aoc_2020.aoc_04.b import aoc_2020_04_b
from aoc_2020.aoc_05.a import aoc_2020_05_a
from aoc_2020.aoc_05.b import aoc_2020_05_b
from aoc_2020.aoc_06.a import aoc_2020_06_a
from aoc_2020.aoc_06.b import aoc_2020_06_b

from aoc_2021.aoc_01.a import aoc_2021_01_a
from aoc_2021.aoc_01.b import aoc_2021_01_b
from aoc_2021.aoc_02.a import aoc_2021_02_a
from aoc_2021.aoc_02.b import aoc_2021_02_b
from aoc_2021.aoc_03.a import aoc_2021_03_a
from aoc_2021.aoc_03.b import aoc_2021_03_b
from aoc_2021.aoc_04.a import aoc_2021_04_a
from aoc_2021.aoc_04.b import aoc_2021_04_b
from aoc_2021.aoc_05.a import aoc_2021_05_a
from aoc_2021.aoc_05.b import aoc_2021_05_b

from aoc_2022.aoc_01.a import aoc_2022_01_a
from aoc_2022.aoc_01.b import aoc_2022_01_b
from aoc_2022.aoc_02.a import aoc_2022_02_a
from aoc_2022.aoc_02.b import aoc_2022_02_b
from aoc_2022.aoc_03.a import aoc_2022_03_a
from aoc_2022.aoc_03.b import aoc_2022_03_b
from aoc_2022.aoc_04.a import aoc_2022_04_a
from aoc_2022.aoc_04.b import aoc_2022_04_b
from aoc_2022.aoc_05.a import aoc_2022_05_a
from aoc_2022.aoc_05.b import aoc_2022_05_b
from aoc_2022.aoc_06.a import aoc_2022_06_a
from aoc_2022.aoc_06.b import aoc_2022_06_b


class TestAdventOfCode2015(unittest.TestCase):
    def test_2015_01_a(self):
        self.assertEqual(aoc_2015_01_a(), 74)

    def test_2015_01_b(self):
        self.assertEqual(aoc_2015_01_b(), 1795)

    def test_2015_02_a(self):
        self.assertEqual(aoc_2015_02_a(), 1598415)

    def test_2015_02_b(self):
        self.assertEqual(aoc_2015_02_b(), 3812909)

    def test_2015_03_a(self):
        self.assertEqual(aoc_2015_03_a(), 2081)

    def test_2015_03_b(self):
        self.assertEqual(aoc_2015_03_b(), 2341)

    def test_2015_04_a(self):
        self.assertEqual(aoc_2015_04_a(), 346386)

    def test_2015_04_b(self):
        return
        self.assertEqual(aoc_2015_04_b(), 9958218)

    def test_2015_04_b_execution_time(self):
        return
        import time
        start_time = time.time()
        aoc_2015_04_b()
        time_taken = time.time() - start_time
        self.assertLessEqual(time_taken, 5, "Takes too long to execute")

    def test_2015_05_a(self):
        self.assertEqual(aoc_2015_05_a(), 255)

    def test_2015_05_b(self):
        return
        self.assertEqual(aoc_2015_05_b(), 111)

    def test_2015_06_a(self):
        self.assertEqual(aoc_2015_06_a(), 569999)

    def test_2015_06_b(self):
        self.assertEqual(aoc_2015_06_b(), 17836115)

    def test_2015_07_a(self):
        return
        self.assertEqual(aoc_2015_07_a(), 111)


class TestAdventOfCode2020(unittest.TestCase):
    def test_2020_01_a(self):
        pass
        # self.assertEqual(aoc_2020_01_a(), 996996) # todo

    def test_2020_01_b(self):
        pass
        # self.assertEqual(aoc_2020_01_b(), 9210402) # todo

    def test_2020_02_a(self):
        self.assertEqual(aoc_2020_02_a(), 550)

    def test_2020_02_b(self):
        self.assertEqual(aoc_2020_02_b(), 634)

    def test_2020_03_a(self):
        self.assertEqual(aoc_2020_03_a(), 159)

    def test_2020_03_b(self):
        self.assertEqual(aoc_2020_03_b(), 6419669520)

    def test_2020_04_a(self):
        self.assertEqual(aoc_2020_04_a(), 228)

    def test_2020_04_b(self):
        self.assertEqual(aoc_2020_04_b(), 175)

    def test_2020_05_a(self):
        self.assertEqual(aoc_2020_05_a(), 894)

    def test_2020_05_b(self):
        self.assertEqual(aoc_2020_05_b(), 579)

    def test_2020_06_a(self):
        self.assertEqual(aoc_2020_06_a(), 6506)

    def test_2020_06_b(self):
        self.assertEqual(aoc_2020_06_b(), 3243)


class TestAdventOfCode2021(unittest.TestCase):
    def test_2021_01_a(self):
        self.assertEqual(aoc_2021_01_a(), 1759)

    def test_2021_01_b(self):
        self.assertEqual(aoc_2021_01_b(), 1805)

    def test_2021_02_a(self):
        self.assertEqual(aoc_2021_02_a(), 2117664)

    def test_2021_02_b(self):
        self.assertEqual(aoc_2021_02_b(), 2073416724)

    def test_2021_03_a(self):
        self.assertEqual(aoc_2021_03_a(), 4160394)

    def test_2021_03_b(self):
        self.assertEqual(aoc_2021_03_b(), 4125600)

    def test_2021_04_a(self):
        self.assertEqual(aoc_2021_04_a(), 6592)

    def test_2021_04_b(self):
        self.assertEqual(aoc_2021_04_b(), 31755)

    def test_2021_05_a(self):
        self.assertEqual(aoc_2021_05_a(), 5169)

    def test_2021_05_b(self):
        return
        self.assertEqual(aoc_2021_05_b(), 31755)


class TestAdventOfCode2022(unittest.TestCase):
    def test_2022_01_a(self):
        self.assertEqual(aoc_2022_01_a(), 72511)

    def test_2022_01_b(self):
        self.assertEqual(aoc_2022_01_b(), 212117)

    def test_2022_02_a(self):
        self.assertEqual(aoc_2022_02_a(), 12794)

    def test_2022_02_b(self):
        self.assertEqual(aoc_2022_02_b(), 14979)

    def test_2022_03_a(self):
        self.assertEqual(aoc_2022_03_a(), 8202)

    def test_2022_03_b(self):
        self.assertEqual(aoc_2022_03_b(), 2864)

    def test_2022_04_a(self):
        self.assertEqual(aoc_2022_04_a(), 464)

    def test_2022_04_b(self):
        self.assertEqual(aoc_2022_04_b(), 770)

    def test_2022_05_a(self):
        self.assertEqual(aoc_2022_05_a(), "VRWBSFZWM")

    def test_2022_05_b(self):
        self.assertEqual(aoc_2022_05_b(), "RBTWJWMCF")

    def test_2022_06_a(self):
        self.assertEqual(aoc_2022_06_a(), 1625)

    def test_2022_06_b(self):
        self.assertEqual(aoc_2022_06_b(), 2250)


if __name__ == '__main__':
    unittest.main()
