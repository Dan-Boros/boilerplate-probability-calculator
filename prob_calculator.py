import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **balls):
        self.content = self._set_content(balls)
    
    def _set_content(self, balls=None):

        if not balls:
            return ["Red"]

        cont = []
        for ballColour, amount in balls.items():
            colour = [ballColour] * amount
            cont += colour

        return cont
        

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass