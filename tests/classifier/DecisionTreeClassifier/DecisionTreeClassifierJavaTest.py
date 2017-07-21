# -*- coding: utf-8 -*-

from unittest import TestCase

from sklearn.tree import DecisionTreeClassifier

from ..Classifier import Classifier
from ...language.Java import Java


class DecisionTreeClassifierJavaTest(Java, Classifier, TestCase):

    def setUp(self):
        super(DecisionTreeClassifierJavaTest, self).setUp()
        self.mdl = DecisionTreeClassifier(random_state=0)

    def tearDown(self):
        super(DecisionTreeClassifierJavaTest, self).tearDown()
