# -*- coding: utf-8 -*-

from unittest import TestCase
import numpy as np
import random

from sklearn.svm.classes import NuSVC

from ..Classifier import Classifier
from ...language.C import C


class NuSVCCTest(C, Classifier, TestCase):

    def setUp(self):
        super(NuSVCCTest, self).setUp()
        self.mdl = NuSVC(kernel='rbf', gamma=0.001, random_state=0)

    def tearDown(self):
        super(NuSVCCTest, self).tearDown()
