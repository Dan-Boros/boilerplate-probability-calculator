import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **balls):
        self.contents = self._set_content(balls)
    
    def _set_content(self, balls=None):

        if not balls:
            return ["red"]

        cont = []
        for ballColour, amount in balls.items():
            colour = [ballColour] * amount
            cont += colour

        return cont
    
    def draw(self, amount):
        # Randomly picks "amount" of balls from content and removes it with pop()
        if len(self.contents) == 0:
            return []
        
        random_index = random.randint(0, len(self.contents) - 1)
        pickedItem = self.contents.pop(random_index)
        if amount == 1:
            return [pickedItem]
        
        else:
            return [pickedItem] + self.draw(amount - 1)
        

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    number_of_occurence = 0
    for e in range(num_experiments):
        newHat = copy.deepcopy(hat)
        drawnBalls = newHat.draw(num_balls_drawn)
        isExpectedBallsDrawn = _checkIfItemsAreInList(drawnBalls, expected_balls)
        if isExpectedBallsDrawn:
            number_of_occurence += 1

    return number_of_occurence / num_experiments

def _checkIfItemsAreInList(actual, expected):
    for name, amount in expected.items():
        if actual.count(name) < amount:
            return False

    return True

