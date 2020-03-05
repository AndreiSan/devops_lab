#!/usr/bin/env python
# --------------------------------------------------------------------
# Program by Batura A.
# Version           Date                Info
#   1.0             2020           Initial version
# --------------------------------------------------------------------


from unittest import TestCase

import task11


class Testleap(TestCase):

    def setUp(self):
        """Init"""

    def test_leap(self):
        """Test for leap year def"""
        self.assertFalse(task11.leap(1900))
        self.assertTrue(task11.leap(2020))
        self.assertTrue(task11.leap(800))

    def tearDown(self):
        """Finish"""
