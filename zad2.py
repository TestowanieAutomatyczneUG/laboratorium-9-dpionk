from unittest.mock import *
from unittest import TestCase

class Car:

    def needsFuel(self):
        pass

    def getEngineTemperature(self):
        pass

    def driveTo(self, destination):
        pass

class test_Car(TestCase):

    def test_needsFuel(self):
        test_object = Car()
        test_object.needsFuel = Mock(name = 'needsFuel')
        test_object.needsFuel.return_value = True

        self.assertEqual(test_object.needsFuel(), True)

    def test_getEngineTemperature(self):
        test_object = Car()
        test_object.getEngineTemperature = Mock(name='getEngineTemperature')
        test_object.getEngineTemperature.return_value = 50

        self.assertEqual(test_object.getEngineTemperature(), 50)

    def test_driveTo(self):
        test_object = Car()
        test_object.driveTo = Mock(name='driveTo')
        test_object.driveTo.return_value = 'Destination ok'

        self.assertEqual(test_object.driveTo('Warsaw'), 'Destination ok')


