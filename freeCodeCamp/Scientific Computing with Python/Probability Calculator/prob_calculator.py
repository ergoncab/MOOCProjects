import copy
import random
from collections import Counter 
# Consider using the modules imported above.

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for item, value in balls.items():
            for _ in range(value):
                self.contents.append(item)


    def draw(self, n_drawn_balls):
        drawn_balls = []

        if n_drawn_balls > len(self.contents):
            n_drawn_balls = len(self.contents)

        for _ in range(n_drawn_balls):
            index = random.randint(0, len(self.contents)-1)
            drawn_balls.append(self.contents.pop(index))

        return drawn_balls



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        results = Counter(drawn_balls)
        
        iter = 0
        for key, value in expected_balls.items():
            if value > results[key]:
                break
            if iter == len(expected_balls) - 1:
                M += 1
            iter += 1


    probability = M/num_experiments
    return probability