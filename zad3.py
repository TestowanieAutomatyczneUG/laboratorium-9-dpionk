from unittest.mock import *
from unittest import TestCase


class Environment :
    def __init__(self):
        self.played = False

    def getTime(self):
        pass

    def playWavFile(self, file):
        pass

    def wavWasPlayed(self):
        self.played = True

    def resetWav(self):
        self.played = False


class Checker:
    def __init__(self):
        self.environment = Environment()

    def reminder(self, file):
        time = self.environment.getTime()
        if time >= 17:
            self.environment.playWavFile(file)
            self.environment.wavWasPlayed()
        else:
            self.environment.resetWav()

class TestChecker(TestCase):

    def test_checker_1(self):
        test_object = Checker()
        file = 'music.wav'
        
        test_object.environment.getTime = Mock('getTime')
        test_object.environment.getTime.return_value = 17

        test_object.reminder(file)

        self.assertEqual(test_object.environment.played, True)

    def test_checker_2(self):
        test_object = Checker()
        file = 'music.wav'

        test_object.environment.getTime = Mock('getTime')
        test_object.environment.getTime.return_value = 12

        test_object.reminder(file)

        self.assertEqual(test_object.environment.played, False)


    