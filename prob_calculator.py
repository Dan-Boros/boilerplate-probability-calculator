import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **balls):
        self.content = self._set_content(balls)
    
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
        if len(self.content) == 0:
            return []
        
        random_index = random.randint(0, len(self.content) - 1)
        pickedItem = self.content.pop(random_index)
        if amount == 1:
            return [pickedItem]
        
        else:
            return [pickedItem] + self.draw(amount - 1)
        

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass
