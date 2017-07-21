# -*- coding: utf-8 -*-

from unittest import TestCase

from sklearn.ensemble import RandomForestClassifier

from ..Classifier import Classifier
from ...language.C import C


class RandomForestClassifierCTest(C, Classifier, TestCase):

    def setUp(self):
        super(RandomForestClassifierCTest, self).setUp()
        self.mdl = RandomForestClassifier(n_estimators=100, random_state=0)

    def tearDown(self):
        super(RandomForestClassifierCTest, self).tearDown()
