'''
Annie has a whole bunch of puppies. They're lovable but also very rambunctious.
One day, spur of the moment, Annie decides to get them all treats. She is
looking forward to how happy they will all be, and getting ready to serve them
the treats, when she realizes: the treats are not all the same size! This is
disastrous! The puppies, knowing the drill, have already lined themselves up in
a neat line to receive their treats, so Annie must figure out how to best
distribute the unevenly-sized treats so as to make as many puppies happy as
possible. The puppies' jealous reactions to uneven treat distribution is
straightforward:
- If a puppy receives a bigger treat than both its neighbors do, it is happy (+1 happiness).
- If a puppy receives a smaller treat than both its neighbors do, it is sad (-1 happiness).
- If a puppy does not fit in either of the above categories, it is merely
  content. This means any puppy with at least one neighbor with the same size
  treat, or any puppy with one neighbor with a bigger treat and one with a
  smaller treat.
Note that the puppies on either end of the line only have a single neighbor to
look at, so in their case their mood depends on whether that single neighbor
received a bigger, smaller, or equal treat. Write a program for Annie to
recommend a treat distribution that maximizes puppy happiness.

The input is a single line of positive integers representing the sizes of the
treats Annie purchased. For example:
  1 1 1 1 1 2 2 3
Assume there are as many puppies as there are treats. In this case, there are 8
puppies to be served 8 treats of 3 different sizes.

The output must provide two facts. First, it must display what the maximum
achievable happiness is, as a single integer on its own line
  3
Then, it must specify a treat ordering that achieves this number.
  2 1 1 2 1 1 1 3
The puppies on either end of the queue get bigger treats than their sole
neighbors, so they are happy. The one in the middle receives a bigger treat
than both its neighbors, so it as well is happy. No puppy received a treat that
is smaller than both its neighbors', so no puppies are unhappy. Thus, 3 happy
puppies minus 0 unhappy puppies results in 3 happiness.

Pictorally:
 2  1  1  2  1  1  1  3
:) :| :| :) :| :| :| :)
An example of a bad solution would be:
1 2 2 1 1 1 3 1
The puppies on either end of the line are sad, since their only neighbors have bigger treats, while there is a single happy puppy (the one with the size 3 treat), since it was the only one that had a treat bigger than its neighbors'. This results in a sub-optimal score of -1.
Again, pictorally:
 1  2  2  1  1  1  3  1
:( :| :| :| :| :| :) :(
Note that it may be possible for there to be several different orderings of the treats that give the maximum happiness. As long as you print out one of them, it doesn't matter which one.
'''
from itertools import permutations
from datetime import datetime

def possibilities(treats):
    # Get the unique permutations
    return set(permutations(treats))

def calc_happiness(treats):
    happiness = 0
    # Do ends first
    if treats[0] < treats[1]:
        happiness -= 1
    elif treats[0] > treats[1]:
        happiness += 1
    if treats[-1] < treats[-2]:
        happiness -= 1
    elif treats[-1] > treats[-2]:
        happiness += 1
    # Other puppies!
    for item in range(1, len(treats) - 1):
        if treats[item] > treats[item - 1] and treats[item] > treats[item + 1]: happiness += 1
        elif treats[item] < treats[item - 1] and treats[item] < treats[item + 1]: happiness -= 1
    return happiness

def max_happiness(treats):
    options = possibilities(treats)
    print("There are {} orderings".format(len(options)))
    best = []
    most_happy = 0
    for o in options:
        happy = calc_happiness(o)
        if happy > most_happy:
            print("New max happiness found!",happy)
            most_happy = happy
            best = [o]
        elif happy == most_happy:
            best.append(o)
    print(most_happy)
    for b in best:
        print(' '.join(b))

#treats = '1 2 2 3 3 3 4'
treats = '1 1 2 3 3 3 3 4 5 5'
#treats = '1 1 2 2 3 4 4 5 5 5 6 6'
start = datetime.now()
max_happiness(treats.split())
print(datetime.now()-start)