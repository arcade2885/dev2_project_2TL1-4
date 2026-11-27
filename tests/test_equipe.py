import itertools
import unittest
from src.equipe import Equipe, supp_equipe


class TestEquipe(unittest.TestCase):
    def setUp(self):
        Equipe.id = itertools.count(1)

    def test_new_teams_get_unique_ids(self):
        equipe_a = Equipe("A")
        equipe_b = Equipe("B")

        self.assertNotEqual(equipe_a.id, equipe_b.id)

    def test_adding__points_updates_score(self):
        equipe = Equipe("A")

        equipe.ajouterPoints(3)

        self.assertEqual(equipe.scoreTotal, 3)
        
    def test_removing_points_updates_score(self):
        equipe = Equipe("A")
        
        equipe.ajouterPoints(3)
        equipe.retirerPoints(2)
        
        self.assertEqual(equipe.scoreTotal, 1)



if __name__ == "__main__":
    unittest.main()