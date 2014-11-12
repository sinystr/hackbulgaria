import entity
import weapon
import unittest


class EntityTest(unittest.TestCase):
    def setUp(self):
        self.some_person = entity.Entity("Person", 100)
        self.axe = weapon.Weapon("Axe", 25, 0.2)

    def test_init_entity(self):
        self.assertEqual(self.some_person.name, "Person")
        self.assertEqual(self.some_person.health, 100)

    def test_no_weapon(self):
        self.assertFalse(self.some_person.has_weapon())

    def test_equip_weapon(self):
        self.some_person.equip_weapon(self.axe)
        self.assertTrue(self.some_person.has_weapon())

    def test_attack_no_weapon(self):
        self.assertEqual(self.some_person.attack(), 0)

    def test_attack_with_weapon(self):
        self.some_person.equip_weapon(self.axe)
        damage = self.axe.damage
        dmg_done = self.some_person.attack()
        self.assertTrue(dmg_done == damage or dmg_done == damage * 2)

if __name__ == '__main__':
    unittest.main()
