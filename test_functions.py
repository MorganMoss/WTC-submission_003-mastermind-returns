import unittest
from unittest.mock import patch
from io import StringIO
import mastermind


class MyTestCase(unittest.TestCase):
    def test_create_code(self):
        for i in range(100):
            code = mastermind.create_code()
            self.assertEqual(4, len(code))
            for j in range(4):
                assert(code[j] in [1,2,3,4,5,6,7,8])
    
    
    def test_check_correctness(self):
        assert(mastermind.check_correctness(0, 4))
        for i in range(4):
            assert(not mastermind.check_correctness(0, i))


    @patch("sys.stdin", StringIO("12345\n123\n1234\n"))
    def test_get_answer_input(self):
        self.assertEqual("1234", mastermind.get_answer_input())


    def test_check_answer(self):
        self.assertEqual((4, 0), mastermind.check_answer([1,2,3,4],"1234"))
        self.assertEqual((0, 4), mastermind.check_answer([1,2,3,4],"4321"))
        self.assertEqual((2, 2), mastermind.check_answer([1,2,3,4],"1243"))
        self.assertEqual((0, 0), mastermind.check_answer([1,2,3,4],"5678"))
    
    
    @patch("sys.stdin", StringIO("1234\n4321\n1243\n5678\n"))
    def test_take_turn(self):
        self.assertEqual((4, 0), mastermind.take_turn([1,2,3,4]))
        self.assertEqual((0, 4), mastermind.take_turn([1,2,3,4]))
        self.assertEqual((2, 2), mastermind.take_turn([1,2,3,4]))
        self.assertEqual((0, 0), mastermind.take_turn([1,2,3,4]))



    