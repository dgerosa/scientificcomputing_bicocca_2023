import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from functools import partial


class game_of_life:
    r"""Play Game of Life"""

    def __init__(self, size, initstate, epochs):
        self.size = size
        self.grid = initstate
        self.epochs = epochs
        

    def find_neighbours(self):
        neighbours = []
        Xs, Ys = np.meshgrid(np.arange(0, self.size[0]), np.arange(0, self.size[1]))
        for x, y in zip(Xs.flatten(), Ys.flatten()):
                xs = x+np.array([-1,0,1])
                ys = y+np.array([-1,0,1])
                X_, Y_ = np.meshgrid(xs[(xs>=0) & (xs<self.size[0])], ys[(ys>=0) & (ys<self.size[1])])
                neighbours += [[[x_, y_] for x_,y_ in zip(X_.flatten(), Y_.flatten()) if [x_,y_]!=[x,y]]]
        self.neighbours = neighbours
    
    
    def next_gen(self, frame, ax, art):
        next_state = self.grid.copy()
        Xs, Ys = np.meshgrid(np.arange(0, self.size[0]), np.arange(0, self.size[1]))
        for x, y in zip(Xs.flatten(), Ys.flatten()):
            n_neighbours = np.sum([self.grid[el[0], el[1]]for el in self.neighbours[x+y*self.size[0]]])
            if self.grid[x,y] == 1:
                if n_neighbours < 2 or n_neighbours > 3:
                    next_state[x,y] = 0
            else:
                if n_neighbours == 3:
                    next_state[x,y] = 1   
        self.grid = next_state
        art = ax.matshow(self.grid, animated=True)
        return art
        
    
    def play(self):
        self.find_neighbours()
        
        fig = plt.figure(figsize=(5,5*self.size[0]/self.size[1]))
        ax = fig.add_subplot(111)
        ax.axis('off')
        showstate = ax.matshow(self.grid, animated=True)
        
        anim = animation.FuncAnimation(fig=fig, func=partial(self.next_gen, ax=ax, art=showstate), frames=self.epochs, blit=False)
        plt.show()
        return anim  


def main():
    size = (60,40)
    init = np.random.choice([0,1], size=size, p=(0.5, 0.5))
    GoL = game_of_life(size, init, 200)
    anim = GoL.play()
    plt.show()