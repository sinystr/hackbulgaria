import weapon
import unittest


class WeaponTest(unittest.TestCase):
    def setUp(self):
        self.axe = weapon.Weapon("Axe", 25, 0.2)

    def test_hero_init(self):
        self.assertEqual(self.axe.type, "Axe")
        self.assertEqual(self.axe.damage, 25)
        self.assertEqual(self.axe.critical_strike_percent, 0.2)

    def test_is_critting(self):
        array_results = []
        for i in range(0, 100):
            array_results.append(self.axe.critical_hit())
        self.assertTrue(True in array_results)

    def test_not_critting(self):
        array_results = []
        for i in range(0, 100):
            array_results.append(self.axe.critical_hit())
        self.assertTrue(False in array_results)



if __name__ == '__main__':
    unittest.main()
