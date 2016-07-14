#!/usr/bin/env python
"""Test the use of flags when from __future__ import unicode_literals is on."""



import unittest
import gflags


gflags.DEFINE_string('seen_in_crittenden', 'alleged mountain lion',
                    'This tests if unicode input to these functions works.')


class FlagsUnicodeLiteralsTest(unittest.TestCase):

  def testUnicodeFlagNameAndValueAreGood(self):
    alleged_mountain_lion = gflags.FLAGS.seen_in_crittenden
    self.assertTrue(
        isinstance(alleged_mountain_lion, type('')),
        msg='expected flag value to be a {} not {}'.format(
            type(''), type(alleged_mountain_lion)))
    self.assertEqual(alleged_mountain_lion, 'alleged mountain lion')


if __name__ == '__main__':
  unittest.main()
