'''15.1 A number raised to the third power is a cube.
Plot the first five cubic numbers, and then plot the first
5000 cubic numbers.'''
import pygal

from matplotlib import pyplot as plt

x_values = [1, 2, 3, 4, 5]
cubes = [1, 8, 27, 64, 125]

plt.scatter(x_values, cubes, edgecolor='none', s=40)

plt.title("Cubes", fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Cube of Value', fontsize=14)
plt.tick_params(axis='both', labelsize=14)

plt.show()

x_values = list(range(5001))
cubes = [x**3 for x in x_values]

plt.scatter(x_values, cubes, edgecolor='none', s=40)

plt.title("Cubes", fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Cube of Value', fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.axis([0, 5100, 0, 5100**3])

plt.show()

'''15.2 Apply a colormap to your cubes plot.'''

x_values = list(range(5001))
cubes = [x**3 for x in x_values]

plt.scatter(x_values, cubes, edgecolor='none', c=cubes, cmap=plt.cm.BuGn, s=40)

plt.title("Cubes", fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Cube of Value', fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.axis([0, 5100, 0, 5100**3])

plt.show()

'''15.3 Modify rw_visual.py by replacing plt.scatter() 
with plt.plot(). to simulate the path of a pollen grain 
on the surface of a drop of water, pass in the rw.x_values 
and rw.y_values, and include a linewidth argument. 
Use 5000 instead of 50,000 points.'''
'''
from random_walk import RandomWalk

while True:
    rw = RandomWalk(5000)
    rw.fill_walk()

    plt.figure(dpi=128, figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values, linewidth=1)

    plt.scatter(0, 0, c='green', edgecolors='none', s=75)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
                s=75)

    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
'''
'''15.5 The method fill_walk() is lengthy. Create a new method 
called get_step() to determine the direction and distance for each 
step, and then calculate the step. You should end up with two calls
 to get_step() in fill_walk():'''
'''
from random import choice

class RandomWalk():
    def __init__(self, num_points=5000):
        self.num_points = num_points

        # All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance
        return step

    def fill_walk(self):
        while len(self.x_values) < self.num_points:

            x_step = self.get_step()
            y_step = self.get_step()

            if x_step == 0 and y_step == 0:
                continue

            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
'''
'''15.6 Modify die.py and dice_visual.py by replacing 
the list we used to set the value of hist.x_labels with a 
loop to generate this list automatically. If you’re comfortable
 with list comprehensions, try replacing the other for loops in 
 die_visual.py and dice_visual.py with comprehensions as well.'''

#import pygal

from die import Die

die = Die()

results = [die.roll() for roll_num in range(1000)]

frequencies = [results.count(value) for value in range(1, die.num_sides + 1)]

hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = [str(x) for x in range(1, die.num_sides + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')

from die import Die

die_1 = Die()
die_2 = Die()

results = [die_1.roll() + die_2.roll() for roll_num in range(1000)]

max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result + 1)]

hist = pygal.Bar()

hist.title = "Results of rolling two D6 dice 1000 times."
hist.x_labels = [str(x) for x in range(2, max_result + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6', frequencies)
hist.render_to_file('dice_visual.svg')

'''15-7 Create a simulation showing what happens if you roll
 two eight-sided dice 1000 times. Increase the number of rolls
  gradually until you start to see the limits of your system’s 
  capabilities.'''

from die import Die

die_1 = Die(8)
die_2 = Die(8)

results = []
for roll_num in range(1000000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()

hist.title = "Results of rolling two D8 dice 1,000,000 times."
hist.x_labels = [str(x) for x in range(2, max_result + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D8 + D8', frequencies)
hist.render_to_file('dice_visual.svg')

'''5-8. If you roll three D6 dice, the smallest number you 
can roll is 3 and the largest number is 18. Create a 
visualization that shows what happens when you roll three D6 dice.'''

die_1 = Die()
die_2 = Die()
die_3 = Die()

results = []
for roll_num in range(1000000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(3, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()

hist.title = "Results of rolling three D6 dice 1,000,000 times."
hist.x_labels = [str(x) for x in range(3, max_result + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6 + D6', frequencies)
hist.render_to_file('dice_visual.svg')

'''5-9. When you roll two dice, you usually add the two 
numbers together to get the result. Create a visualization 
that shows what happens if you multiply these numbers instead.'''

die_1 = Die()
die_2 = Die()

results = []
for roll_num in range(1000000):
    result = die_1.roll() * die_2.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides * die_2.num_sides
for value in range(1, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()

hist.title = "Results of multiplying two D6 dice. (1,000,000 rolls)"
hist.x_labels = [str(x) for x in range(1, max_result + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 * D6', frequencies)
hist.render_to_file('dice_visual.svg')