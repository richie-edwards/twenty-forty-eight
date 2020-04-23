import unittest
import merge


class CloseGapsTest(unittest.TestCase):
    def test_no_gaps(self):
        my_line = [2, 2, 2, 2]
        expected = [2, 2, 2, 2]
        self.assertEqual(expected, merge.close_gaps(my_line))

    def test_gap_at_end(self):
        my_line = [2, 2, 2, 0]
        expected = [2, 2, 2, 0]
        self.assertEqual(expected, merge.close_gaps(my_line))

    def test_sparsed_gaps(self):
        my_line = [0, 2, 0, 8]
        expected = [2, 8, 0, 0]
        self.assertEqual(expected, merge.close_gaps(my_line))

    def test_value_at_end(self):
        my_line = [0, 0, 0, 2]
        expected = [2, 0, 0, 0]
        self.assertEqual(expected, merge.close_gaps(my_line))


class MergeLineTest(unittest.TestCase):
    def test_double_merge(self):
        my_line = [2, 2, 4, 4]
        expected = [4, 8, 0, 0]
        self.assertEqual(expected, merge.merge(my_line))

    def test_merge_past_empty(self):
        my_line = [2, 0, 2, 2]
        expected = [4, 2, 0, 0]
        self.assertEqual(expected, merge.merge(my_line))

    def test_no_merge(self):
        my_line = [0, 2, 0, 8]
        expected = [2, 8, 0, 0]
        self.assertEqual(expected, merge.merge(my_line))

    def test_empty_then_merge(self):
        my_line = [0, 8, 8, 16]
        expected = [16, 16, 0, 0]
        self.assertEqual(expected, merge.merge(my_line))

    def test_center_merge(self):
        my_line = [8, 16, 16, 8]
        expected = [8, 32, 8, 0]
        self.assertEqual(expected, merge.merge(my_line))

    def test_end_merge(self):
        my_line = [0, 0, 4, 4]
        expected = [8, 0, 0, 0]
        self.assertEqual(expected, merge.merge(my_line))


if __name__ == '__main__':
    unittest.main()
