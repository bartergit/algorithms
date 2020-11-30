import unittest
from testfixtures import compare
import copy

def find_stable_matching(men_preferences, women_preferences):
    men_preferences = copy.deepcopy(men_preferences)
    women_preferences = copy.deepcopy(women_preferences) 
    n = len(men_preferences)
    k = len(women_preferences)
    active_men = [True] * n
    proposals = [[False] * n for i in range(k)]
    while abs(n - k) != sum(active_men) != 0:       # while we have active men
        for man, is_active in enumerate(active_men):
            if is_active:   # in state of "maybe"                    
                man_pref = men_preferences[man]
                proposals[man_pref.pop(0)][man] = True      #make proposals
        active_men = [True] * n
        for woman, _ in enumerate(proposals):
            for man in women_preferences[woman]:
                if proposals[woman][man]:
                    proposals[woman] = [False] * n
                    proposals[woman][man] = True
                    active_men[man] = False   # mark first encountered man as "maybe" if no proposals
                    break
    stable_matching = []
    for woman, woman_proposal in enumerate(proposals):
        for man, yes in enumerate(woman_proposal):
            if yes:
                stable_matching.append((man, woman))
    return stable_matching


class TestMarriage(unittest.TestCase):
    def setUp(self):
        self.minus_one = lambda arr: list(map(lambda x: list(map(lambda y: y - 1, x)), arr))
        pass
    def test_marriage(self):
        men_preferences = [[2,1,3,4], [4, 1, 2, 3], [1, 3, 2, 4], [2, 3, 1, 4]]
        women_preferences = [[1, 3, 2, 4], [3, 4, 1, 2], [4, 2, 3, 1], [3, 2, 1, 4]]
        men_preferences = self.minus_one(men_preferences)
        women_preferences = self.minus_one(women_preferences)
        self.assertCountEqual(find_stable_matching(men_preferences, women_preferences), [(0,0),(1,3),(2,2),(3,1)])
        self.assertCountEqual(find_stable_matching(women_preferences, men_preferences), [(0,0),(1,2),(2,3),(3,1)])

    def test_unequal_marriage(self):
        men_preferences = [[0,2,1],[1,0,2]]
        women_preferences = [[1,0], [0, 1], [0,1]] 
        self.assertCountEqual(find_stable_matching(men_preferences, women_preferences), [(0,0), (1,1)])
        self.assertCountEqual(find_stable_matching(women_preferences, men_preferences), [(2,0),(0,1)])





if __name__ == "__main__":
    unittest.main()