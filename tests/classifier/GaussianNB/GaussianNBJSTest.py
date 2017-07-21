# -*- coding: utf-8 -*-

from unittest import TestCase

from sklearn.naive_bayes import GaussianNB

from ..Classifier import Classifier
from ...language.JavaScript import JavaScript


class GaussianNBJSTest(JavaScript, Classifier, TestCase):

    def setUp(self):
        super(GaussianNBJSTest, self).setUp()
        self.mdl = GaussianNB()

    def tearDown(self):
        super(GaussianNBJSTest, self).tearDown()
