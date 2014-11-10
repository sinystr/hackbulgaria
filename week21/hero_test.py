import hero
import unittest


class HeroTest(unittest.TestCase):
    def setUp(self):
        self.bron_hero = hero.Hero("Bron", 100, "Dragonslayer")

    def test_hero_init(self):
        self.assertEqual(self.bron_hero.name, "Bron")
        self.assertEqual(self.bron_hero.health, 100)
        self.assertEqual(self.bron_hero.nickname, "Dragonslayer")

    def test_known_as(self):
        self.assertEqual(self.bron_hero.known_as(), "Bron the Dragonslayer")

    def test_get_health(self):
        self.assertEqual(self.bron_hero.get_health(), 100)

    def test_is_alive(self):
        self.assertTrue(self.bron_hero.is_alive())
        self.bron_hero.health = 0
        self.assertFalse(self.bron_hero.is_alive())

    def test_take_damage(self):
        self.bron_hero.take_damage(10)
        self.assertEqual(self.bron_hero.health, 90)

    def test_take_damage_float(self):
        self.bron_hero.take_damage(1.5)
        self.assertEqual(self.bron_hero.health, 98.5)

    def test_take_damage_while_dead(self):
        self.bron_hero.health = 0
        self.bron_hero.take_damage(1.5)
        self.assertEqual(self.bron_hero.health, 0)

    def test_take_healing_dead(self):
        self.bron_hero.health = 0
        self.assertFalse(self.bron_hero.take_healing(100))

    def test_take_more_healing(self):
        self.bron_hero.health = 100
        self.bron_hero.take_healing(40)
        self.assertEqual(self.bron_hero.health, 100)

    def test_just_take_healing(self):
        self.bron_hero.health = 10
        self.bron_hero.take_healing(30)
        self.assertEqual(self.bron_hero.health, 40)


if __name__ == '__main__':
    unittest.main()
