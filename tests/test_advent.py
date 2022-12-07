import unittest

import aoc_2015.aoc_01.a as _aoc_2015_01_a
import aoc_2015.aoc_01.b as _aoc_2015_01_b
import aoc_2015.aoc_02.a as _aoc_2015_02_a
import aoc_2015.aoc_02.b as _aoc_2015_02_b
import aoc_2015.aoc_03.a as _aoc_2015_03_a
import aoc_2015.aoc_03.b as _aoc_2015_03_b
import aoc_2015.aoc_04.a as _aoc_2015_04_a
import aoc_2015.aoc_04.b as _aoc_2015_04_b
import aoc_2015.aoc_05.a as _aoc_2015_05_a
import aoc_2015.aoc_05.b as _aoc_2015_05_b
import aoc_2015.aoc_06.a as _aoc_2015_06_a
import aoc_2015.aoc_06.b as _aoc_2015_06_b
import aoc_2015.aoc_07.a as _aoc_2015_07_a

import aoc_2020.aoc_01.a as _aoc_2020_01_a
import aoc_2020.aoc_01.b as _aoc_2020_01_b
import aoc_2020.aoc_02.a as _aoc_2020_02_a
import aoc_2020.aoc_02.b as _aoc_2020_02_b
import aoc_2020.aoc_03.a as _aoc_2020_03_a
import aoc_2020.aoc_03.b as _aoc_2020_03_b
import aoc_2020.aoc_04.a as _aoc_2020_04_a
import aoc_2020.aoc_04.b as _aoc_2020_04_b
import aoc_2020.aoc_05.a as _aoc_2020_05_a
import aoc_2020.aoc_05.b as _aoc_2020_05_b
import aoc_2020.aoc_06.a as _aoc_2020_06_a
import aoc_2020.aoc_06.b as _aoc_2020_06_b

import aoc_2021.aoc_01.a as _aoc_2021_01_a
import aoc_2021.aoc_01.b as _aoc_2021_01_b
import aoc_2021.aoc_02.a as _aoc_2021_02_a
import aoc_2021.aoc_02.b as _aoc_2021_02_b
import aoc_2021.aoc_03.a as _aoc_2021_03_a
import aoc_2021.aoc_03.b as _aoc_2021_03_b
import aoc_2021.aoc_04.a as _aoc_2021_04_a
import aoc_2021.aoc_04.b as _aoc_2021_04_b
import aoc_2021.aoc_05.a as _aoc_2021_05_a
import aoc_2021.aoc_05.b as _aoc_2021_05_b

import aoc_2022.aoc_01.a as _aoc_2022_01_a
import aoc_2022.aoc_01.b as _aoc_2022_01_b
import aoc_2022.aoc_02.a as _aoc_2022_02_a
import aoc_2022.aoc_02.b as _aoc_2022_02_b
import aoc_2022.aoc_03.a as _aoc_2022_03_a
import aoc_2022.aoc_03.b as _aoc_2022_03_b
import aoc_2022.aoc_04.a as _aoc_2022_04_a
import aoc_2022.aoc_04.b as _aoc_2022_04_b
import aoc_2022.aoc_05.a as _aoc_2022_05_a
import aoc_2022.aoc_05.b as _aoc_2022_05_b
import aoc_2022.aoc_06.a as _aoc_2022_06_a
import aoc_2022.aoc_06.b as _aoc_2022_06_b
import aoc_2022.aoc_07.a as _aoc_2022_07_a
import aoc_2022.aoc_07.b as _aoc_2022_07_b


class TestAdventOfCode2015(unittest.TestCase):
    def test_2015_01_a(self):
        self.assertEqual(_aoc_2015_01_a.aoc_2015_01_a(), 74)

    def test_2015_01_b(self):
        self.assertEqual(_aoc_2015_01_b.aoc_2015_01_b(), 1795)

    def test_2015_02_a(self):
        self.assertEqual(_aoc_2015_02_a.aoc_2015_02_a(), 1598415)

    def test_2015_02_b(self):
        self.assertEqual(_aoc_2015_02_b.aoc_2015_02_b(), 3812909)

    def test_2015_03_a(self):
        self.assertEqual(_aoc_2015_03_a.aoc_2015_03_a(), 2081)

    def test_2015_03_b(self):
        self.assertEqual(_aoc_2015_03_b.aoc_2015_03_b(), 2341)

    def test_2015_04_a(self):
        self.assertEqual(_aoc_2015_04_a.aoc_2015_04_a(), 346386)

    def test_2015_04_b(self):
        self.assertEqual(_aoc_2015_04_b.aoc_2015_04_b(), 9958218)

    def test_2015_04_b_execution_time(self):
        import time
        start_time = time.time()
        _aoc_2015_04_b.aoc_2015_04_b()
        time_taken = time.time() - start_time
        self.assertLessEqual(time_taken, 10, "Takes too long to execute")

    def test_2015_05_a(self):
        self.assertEqual(_aoc_2015_05_a.aoc_2015_05_a(), 255)

    def test_2015_05_b(self):
        self.assertEqual(_aoc_2015_05_b.aoc_2015_05_b(), 55)

    def test_2015_06_a(self):
        self.assertEqual(_aoc_2015_06_a.aoc_2015_06_a(), 569999)

    def test_2015_06_b(self):
        self.assertEqual(_aoc_2015_06_b.aoc_2015_06_b(), 17836115)

    def test_2015_07_a(self):
        self.assertEqual(_aoc_2015_07_a.aoc_2015_07_a(), 111)


class TestAdventOfCode2020(unittest.TestCase):
    def test_2020_01_a(self):
        self.assertEqual(_aoc_2020_01_a.aoc_2020_01_a(), 996996)

    def test_2020_01_b(self):
        self.assertEqual(_aoc_2020_01_b.aoc_2020_01_b(), 9210402)

    def test_2020_01_b_execution_time(self):
        import time
        start_time = time.time()
        _aoc_2020_01_b.aoc_2020_01_b()
        time_taken = time.time() - start_time
        self.assertLessEqual(time_taken, 1, "Takes too long to execute")

    def test_2020_02_a(self):
        self.assertEqual(_aoc_2020_02_a.aoc_2020_02_a(), 550)

    def test_2020_02_b(self):
        self.assertEqual(_aoc_2020_02_b.aoc_2020_02_b(), 634)

    def test_2020_03_a(self):
        self.assertEqual(_aoc_2020_03_a.aoc_2020_03_a(), 159)

    def test_2020_03_b(self):
        self.assertEqual(_aoc_2020_03_b.aoc_2020_03_b(), 6419669520)

    def test_2020_04_a(self):
        self.assertEqual(_aoc_2020_04_a.aoc_2020_04_a(), 228)

    def test_2020_04_b(self):
        self.assertEqual(_aoc_2020_04_b.aoc_2020_04_b(), 175)

    def test_2020_05_a(self):
        self.assertEqual(_aoc_2020_05_a.aoc_2020_05_a(), 894)

    def test_2020_05_b(self):
        self.assertEqual(_aoc_2020_05_b.aoc_2020_05_b(), 579)

    def test_2020_06_a(self):
        self.assertEqual(_aoc_2020_06_a.aoc_2020_06_a(), 6506)

    def test_2020_06_b(self):
        self.assertEqual(_aoc_2020_06_b.aoc_2020_06_b(), 3243)


class TestAdventOfCode2021(unittest.TestCase):
    def test_2021_01_a(self):
        self.assertEqual(_aoc_2021_01_a.aoc_2021_01_a(), 1759)

    def test_2021_01_b(self):
        self.assertEqual(_aoc_2021_01_b.aoc_2021_01_b(), 1805)

    def test_2021_02_a(self):
        self.assertEqual(_aoc_2021_02_a.aoc_2021_02_a(), 2117664)

    def test_2021_02_b(self):
        self.assertEqual(_aoc_2021_02_b.aoc_2021_02_b(), 2073416724)

    def test_2021_03_a(self):
        self.assertEqual(_aoc_2021_03_a.aoc_2021_03_a(), 4160394)

    def test_2021_03_b(self):
        self.assertEqual(_aoc_2021_03_b.aoc_2021_03_b(), 4125600)

    def test_2021_04_a(self):
        self.assertEqual(_aoc_2021_04_a.aoc_2021_04_a(), 6592)

    def test_2021_04_b(self):
        self.assertEqual(_aoc_2021_04_b.aoc_2021_04_b(), 31755)

    def test_2021_05_a(self):
        self.assertEqual(_aoc_2021_05_a.aoc_2021_05_a(), 5169)

    def test_2021_05_b(self):
        return
        self.assertEqual(_aoc_2021_05_b.aoc_2021_05_b(), 31755)


class TestAdventOfCode2022(unittest.TestCase):
    def test_2022_01_a(self):
        self.assertEqual(_aoc_2022_01_a.aoc_2022_01_a(), 72511)

    def test_2022_01_b(self):
        self.assertEqual(_aoc_2022_01_b.aoc_2022_01_b(), 212117)

    def test_2022_02_a(self):
        self.assertEqual(_aoc_2022_02_a.aoc_2022_02_a(), 12794)

    def test_2022_02_b(self):
        self.assertEqual(_aoc_2022_02_b.aoc_2022_02_b(), 14979)

    def test_2022_03_a(self):
        self.assertEqual(_aoc_2022_03_a.aoc_2022_03_a(), 8202)

    def test_2022_03_b(self):
        self.assertEqual(_aoc_2022_03_b.aoc_2022_03_b(), 2864)

    def test_2022_04_a(self):
        self.assertEqual(_aoc_2022_04_a.aoc_2022_04_a(), 464)

    def test_2022_04_b(self):
        self.assertEqual(_aoc_2022_04_b.aoc_2022_04_b(), 770)

    def test_2022_05_a(self):
        self.assertEqual(_aoc_2022_05_a.aoc_2022_05_a(), "VRWBSFZWM")

    def test_2022_05_b(self):
        self.assertEqual(_aoc_2022_05_b.aoc_2022_05_b(), "RBTWJWMCF")

    def test_2022_06_a(self):
        self.assertEqual(_aoc_2022_06_a.aoc_2022_06_a(), 1625)

    def test_2022_06_b(self):
        self.assertEqual(_aoc_2022_06_b.aoc_2022_06_b(), 2250)

    def test_2022_07_a(self):
        self.assertEqual(_aoc_2022_07_a.aoc_2022_07_a(), 1611443)

    def test_2022_07_b(self):
        self.assertEqual(_aoc_2022_07_b.aoc_2022_07_b(), 1)


if __name__ == '__main__':
    unittest.main()
