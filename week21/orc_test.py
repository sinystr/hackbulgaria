import weapon
import orc
import unittest


class OrcTest(unittest.TestCase):
    def setUp(self):
        self.dregu_orc = orc.Orc("Dregu", 100, 1.4)

    def test_hero_init(self):
        self.assertEqual(self.dregu_orc.name, "Dregu")
        self.assertEqual(self.dregu_orc.health, 100)
        self.assertEqual(self.dregu_orc.berserk_factor, 1.4)

    def test_get_health(self):
        self.assertEqual(self.dregu_orc.get_health(), 100)

    def test_is_alive(self):
        self.assertTrue(self.dregu_orc.is_alive())
        self.dregu_orc.health = 0
        self.assertFalse(self.dregu_orc.is_alive())

    def test_take_damage(self):
        self.dregu_orc.take_damage(10)
        self.assertEqual(self.dregu_orc.health, 90)

    def test_take_damage_float(self):
        self.dregu_orc.take_damage(1.5)
        self.assertEqual(self.dregu_orc.health, 98.5)

    def test_take_damage_while_dead(self):
        self.dregu_orc.health = 0
        self.dregu_orc.take_damage(1.5)
        self.assertEqual(self.dregu_orc.health, 0)

    def test_take_healing_dead(self):
        self.dregu_orc.health = 0
        self.assertFalse(self.dregu_orc.take_healing(100))

    def test_take_more_healing(self):
        self.dregu_orc.health = 100
        self.dregu_orc.take_healing(40)
        self.assertEqual(self.dregu_orc.health, 100)

    def test_just_take_healing(self):
        self.dregu_orc.health = 10
        self.dregu_orc.take_healing(30)
        self.assertEqual(self.dregu_orc.health, 40)

    def test_attack(self):
        damage_done = self.dregu_orc.attack()


if __name__ == '__main__':
    unittest.main()
