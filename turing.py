import unittest
import math

def turing(alphabet, states, tape, start_state=None):
    current = start_state or "q0" 
    tape = list(tape)
    ind = 1
    while True:
        if current == "qn" or current == "qy":
            break
        flag = False
        for was, to_change, to_go, next_state in states[current]:
            if was == tape[ind]:
                assert was in alphabet and to_change in alphabet 
                tape[ind] = to_change
                # print("".join(tape), ind, current)
                current = next_state
                ind += to_go
                flag = True
                break
        assert flag, (ind, tape[ind], states[current])
    return "".join(tape), current, ind



class TestTuring(unittest.TestCase):
    def test_unary_minus_one(self):
        alphabet = ["1", "#", " "]
        states = {
            "q0": [("1","1", 1, "q0"), ("#", "#", -1, "q1")], 
            "q1": [("1", "#", -1, "qy")]}
        test_cases = [("#1#", "###"), ("#111#", "#11##"), ("#11#", "#1##"), ("#1111#", "#111##")]
        for test_data, expected in test_cases:
            with self.subTest(i=test_data):
                self.assertEqual(turing(alphabet, states, test_data)[0], expected)

    def test_positive_is_power_of_three(self):
        alphabet = ["1", "#", "0"]
        states = {
            "q0": [("0","0", 1, "q0"), ("1", "1", 1, "q1"), ("#", "#", -1, "q3")], 
            "q1": [("0","0", 1, "q1"), ("1","0", 1, "q2"), ("#", "#", -1, "q7")],
            "q2": [("0", "0", 1, "q2"), ("1", "0", 1, "q0"), ("#", "#", -1, "q7")],
            "q3": [("0", "#", -1, "q3"), ("1", "1", -1, "q4")],
            "q4": [("0", "0", -1, "q4"), ("1", "1", -1, "q4"), ("#", "#", 1, "q0")],
            "q7": [("1", "1", -1, "q8"), ("0", "0", 0, "q10")],
            "q8": [("#", "#", 0, "qy"), ("1", "1", 0, "q9"), ("0", "0", 0, "q9")],
            "q9": [("0", "0", 1, "q10")],
            "q10": [("1", "#", -1, "q10"), ("0", "#", -1, "q10"), ("#", "#", 0, "qn")],
        }
        for test, expected in [(1,1), (3,1), (9,1), (81,1), (243, 1), (729,1)]:
            with self.subTest(i=test):
                res = turing(alphabet, states, "#" + "1"*test + "#")[0]
                self.assertEqual(res.count("1"), expected) 
                self.assertEqual(res.count("0"), 0)

    def test_negative_is_power_of_three(self):
        alphabet = ["1", "#", "0"]
        states = {
            "q0": [("0","0", 1, "q0"), ("1", "1", 1, "q1"), ("#", "#", -1, "q3")], 
            "q1": [("0","0", 1, "q1"), ("1","0", 1, "q2"), ("#", "#", -1, "q7")],
            "q2": [("0", "0", 1, "q2"), ("1", "0", 1, "q0"), ("#", "#", -1, "q7")],
            "q3": [("0", "#", -1, "q3"), ("1", "1", -1, "q4")],
            "q4": [("0", "0", -1, "q4"), ("1", "1", -1, "q4"), ("#", "#", 1, "q0")],
            "q7": [("1", "1", -1, "q8"), ("0", "0", 0, "q10")],
            "q8": [("#", "#", 0, "qy"), ("1", "1", 0, "q9"), ("0", "0", 0, "q9")],
            "q9": [("0", "0", 1, "q10")],
            "q10": [("1", "#", -1, "q10"), ("0", "#", -1, "q10"), ("#", "#", 0, "qn")],
        }
        for i in range(82, 244):
            with self.subTest(i=i):
                res = turing(alphabet, states, "#" + "1"*i + "#")[0]
                self.assertEqual(res.count("1"), 0) 
                self.assertEqual(res.count("0"), 0)

if __name__ == "__main__":
    unittest.main()
