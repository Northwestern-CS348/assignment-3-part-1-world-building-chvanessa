import unittest
import read, copy
from logical_classes import *
from kb_and_inference_engine import *
from game_masters import *

class KBTest(unittest.TestCase):

    def checkKb(self, kb, required, forbidden):
        for v in required:
            self.assertTrue(kb.kb_ask(parse_input(v)), \
                'Expected Fact cannot be found in KB: "%s"' % str(v))
        for v in forbidden:
            self.assertFalse(kb.kb_ask(parse_input(v)), \
                'Unexpected Fact found in KB: "%s"' % str(v))

    def checkMovables(self, gm, expected):
        movables = gm.getMovables()
        if expected:
            self.assertTrue(movables, \
                'None of the expected Facts with MOVABLE predicate ' \
                'can be found: "%s"' % [str(x) for x in expected])
            for e in expected:
                self.assertTrue(parse_input(e).statement in movables,\
                    'Expected Fact with MOVABLE predicate '\
                    'cannot be found in KB: "%s"' % str(e))
        else:
            self.assertFalse(movables, \
                'Unexpecting Facts with MOVABLE predicate: %s'\
                    % [str(x) for x in movables])

    def test01(self):
        th = TowerOfHanoiGame()
        th.read('hanoi_all_disks_on_peg_one.txt')
        expectedMovables = [
            'fact: (movable disk1 peg1 peg2)',
            'fact: (movable disk1 peg1 peg3)',
        ]
        self.checkMovables(th, expectedMovables)

    def test02(self):
        th = TowerOfHanoiGame()
        th.read('hanoi_all_disks_on_peg_one.txt')
        required = [
            'fact: (on disk1 peg1)',
            'fact: (on disk2 peg1)',
            'fact: (on disk3 peg1)',
            'fact: (on disk4 peg1)',
            'fact: (on disk5 peg1)',
        ]
        forbidden = [
            'fact: (movable disk1 peg1 peg1)',
            'fact: (movable disk2 peg1 peg2)',
            'fact: (movable disk3 peg1 peg3)',
            'fact: (movable disk4 peg1 peg2)',
            'fact: (movable disk5 peg1 peg3)',
        ]
        self.checkKb(th.kb, required, forbidden)

    def test03(self):
        th = TowerOfHanoiGame()
        th.read('hanoi_two_smallest_on_peg_three.txt')
        expectedMovables = [
            'fact: (movable disk1 peg3 peg1)',
            'fact: (movable disk1 peg3 peg2)',
            'fact: (movable disk3 peg1 peg2)',
        ]
        self.checkMovables(th, expectedMovables)

    def test04(self):
        th = TowerOfHanoiGame()
        th.read('hanoi_two_smallest_on_peg_three.txt')
        required = [
            'fact: (on disk1 peg3)',
            'fact: (on disk2 peg3)',
            'fact: (on disk3 peg1)',
            'fact: (on disk4 peg1)',
            'fact: (on disk5 peg1)',
        ]
        forbidden = [
            'fact: (movable disk1 peg3 peg3)',
            'fact: (movable disk2 peg3 peg1)',
            'fact: (movable disk2 peg3 peg2)',
            'fact: (movable disk2 peg3 peg3)',
            'fact: (movable disk3 peg1 peg3)',
            'fact: (movable disk4 peg1 peg1)',
            'fact: (movable disk4 peg1 peg2)',
            'fact: (movable disk4 peg1 peg3)',
            'fact: (movable disk5 peg1 peg3)',
        ]
        self.checkKb(th.kb, required, forbidden)

    def test05(self):
        th = TowerOfHanoiGame()
        th.read('hanoi_smallest_on_three_second_smallest_on_two.txt')
        expectedMovables = [
            'fact: (movable disk1 peg3 peg1)',
            'fact: (movable disk1 peg3 peg2)',
            'fact: (movable disk2 peg2 peg1)',
        ]
        self.checkMovables(th, expectedMovables)

    def test06(self):
        th = TowerOfHanoiGame()
        th.read('hanoi_smallest_on_three_second_smallest_on_two.txt')
        required = [
            'fact: (on disk1 peg3)',
            'fact: (on disk2 peg2)',
            'fact: (on disk3 peg1)',
            'fact: (on disk4 peg1)',
            'fact: (on disk5 peg1)',
        ]
        forbidden = [
            'fact: (movable disk1 peg3 peg3)',
            'fact: (movable disk2 peg2 peg2)',
            'fact: (movable disk2 peg2 peg3)',
            'fact: (movable disk3 peg1 peg1)',
            'fact: (movable disk3 peg1 peg2)',
            'fact: (movable disk3 peg1 peg3)',
            'fact: (movable disk4 peg1 peg2)',
            'fact: (movable disk5 peg1 peg3)',
        ]
        self.checkKb(th.kb, required, forbidden)

    def test07(self):
        th = TowerOfHanoiGame()
        th.read('puzzle8_top_right_empty.txt')
        expectedMovables = [
            'fact: (movable tile4 pos2 pos1 pos3 pos1)',
            'fact: (movable tile8 pos3 pos2 pos3 pos1)',
        ]
        self.checkMovables(th, expectedMovables)

    def test08(self):
        p8 = Puzzle8Game()
        p8.read('puzzle8_top_right_empty.txt')
        required = []
        forbidden = [
            'fact: (movable tile1 pos1 pos1 pos1 pos1)',
            'fact: (movable tile1 pos2 pos2 pos2 pos2)',
            'fact: (movable tile1 pos2 pos2 pos2 pos1)',
            'fact: (movable tile1 pos2 pos2 pos1 pos2)',
            'fact: (movable tile1 pos2 pos2 pos2 pos3)',
            'fact: (movable tile1 pos2 pos2 pos3 pos2)',
            'fact: (movable tile1 pos2 pos2 pos1 pos1)',
            'fact: (movable tile1 pos2 pos2 pos3 pos1)',
            'fact: (movable tile1 pos2 pos2 pos1 pos3)',
            'fact: (movable tile1 pos2 pos2 pos3 pos3)',
            'fact: (movable tile5 pos1 pos1 pos3 pos1)',
            'fact: (movable tile5 pos1 pos1 pos3 pos3)',
        ]
        self.checkKb(p8.kb, required, forbidden)

    def test09(self):
        th = TowerOfHanoiGame()
        th.read('puzzle8_center_empty.txt')
        expectedMovables = [
            'fact: (movable tile2 pos2 pos1 pos2 pos2)',
            'fact: (movable tile8 pos1 pos2 pos2 pos2)',
            'fact: (movable tile6 pos2 pos3 pos2 pos2)',
            'fact: (movable tile4 pos3 pos2 pos2 pos2)',
        ]
        self.checkMovables(th, expectedMovables)

    def test10(self):
        p8 = Puzzle8Game()
        p8.read('puzzle8_center_empty.txt')
        required = []
        forbidden = [
            'fact: (movable tile1 pos1 pos1 pos2 pos2)',
            'fact: (movable tile3 pos3 pos1 pos2 pos2)',
            'fact: (movable tile7 pos3 pos1 pos2 pos2)',
            'fact: (movable tile5 pos3 pos3 pos2 pos2)',
            'fact: (movable tile1 pos1 pos1 pos3 pos1)',
            'fact: (movable tile1 pos1 pos1 pos3 pos3)',
            'fact: (movable tile5 pos3 pos3 pos3 pos3)',
        ]
        self.checkKb(p8.kb, required, forbidden)


if __name__ == '__main__':
    unittest.main()
