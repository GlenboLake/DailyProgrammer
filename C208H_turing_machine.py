'''
http://www.reddit.com/r/dailyprogrammer/comments/31aja8/20150403_challenge_208_hard_the_universal_machine/

Imagine an infinitely long, one-dimensional list of symbols. The list is
infinite in both directions, and each symbol is indexed by a number, where the
middle of the list is zero. This is called a tape. The symbols on the tape can
be any symbol from an alphabet, which is just a set of possible symbols. If our
example alphabet consists of the symbols 0, 1 and #, then a valid tape would
look like:

  #0110#10101#111#01##
  |

(The | marks the location of the middle of the tape, position zero.) Of course,
we can't represent an infinite tape at once. Therefore, we add another possible
symbol to our alphabet, _ (underscore), to denote the lack of a symbol. This _
symbol fills the rest of the tape, all the way out to infinity, like so
(ellipsis denotes repeat):

  . . . _________________#0110#10101#111#01##_________________ . . .
                         |

Now, imagine we have a machine that can look at this tape, but it can only see
one symbol on the tape at once. To look at this tape, it has a read head. In
our tape diagrams, the read head is marked with a caret (^). For example,
here's the read head at position 7:

  #0110#10101#111#01##
  |      ^

This read head can move one symbol to the left or right, but it can't skip
ahead arbitrarily or jump to a specific location. Besides the read head, the
machine also has a state. This is just an alphanumeric string, with no spaces,
like a variable of the machine. It could be Red, it could be Clockwise, it
could be Catch22, it could be Tgnqovjaxbg, as long as it's alphanumeric.

Now, this machine is capable of performing a step. A step will change the
symbol under the read head to another symbol from the alphabet, and then either
move the read head left or right. The type of step that happens depends on the
current state, and the current symbol under the read head. We can define a rule
for our machine which says something like this:

  If the current symbol under the read head is p, and the current state is A,
  then change the state to B, change the symbol under the read head to q and
  move the read head in direction d.

p and q can be the same symbol, and A and B can be the same state. For example:

  If the current symbol under the read head is 0, and the current state is
  State1, then change the state to State1, change the symbol under the read
  head to 1 and move the read head left.

This rule is called a transition function, and the typical notation is:

delta(A, p) = (B, q, d)

So our example rule is:

delta(State1, 0) = (State1, 1, <)

So, if our machine is in the state State1 and our tape looks like this:
  #0110#10101#111#01##
  |      ^

Then, after applying our transition function above, we're now in State1 (again)
and the tape now looks like this:
  #0110#11101#111#01##
  |     ^

You'll typically have quite a few transition functions to cover every possible
state/symbol combination. After each step, the machine compares the new state
to a special state known as the accepting state. If the current state is the
accepting state, then the machine stops, as the computation is complete.

Whew, that's a lot of information! Here's the synopsis of what you need to
describe one of these machines:
- The alphabet: all possible symbols (along with _, which is implicitly part of
  the alphabet.)
- The tape at the start of the computation.
- The starting position of the read head on the tape; this is assumed to be zero.
- The list of possible states that our machine can be in.
- The starting state, and the accepting state.
- A list of transition functions, that cover every possible symbol/state
  combination on the given tape.
This type of machine is known as a Turing machine, named after the famous
groundbreaking computer scientist and mathematician Alan Turing. It sounds
hopelessly verbose in practice, but a Turing machine is insanely useful as a
theoretical model for computation. To gloss over quite a few details: if a
machine can simulate any such Turing machine as described above, then it's
described as Turing-complete. Today, you'll be writing a program to simulate a
turing machine given the above required parameters; therefore, you'll need to
use a Turing-complete language to solve this challenge. :)

INPUT:
First, you will be given the alphabet of a Turing machine (excluding _, which
is always part of the alphabet) as a sequence of non-whitespace characters.
Next, you will be given a space-separated list of possible states for the
machine. You will then be given the initial state and the accepting state on
two lines. After this, you will be given the initial tape to use. The first
character is assumed to be at position 0, with following characters at
successive locations. Finally, you're given a list of transition rules. These
are in the format:
  StateBefore SymbolBefore = StateAfter SymbolAfter DirectionToMove

Example:
  01
  Mov B Bi OK
  Mov
  OK
  01100100
  Mov 0 = Mov 0 >
  Mov 1 = Mov 1 >
  Mov _ = B _ <
  B 0 = B 0 <
  B 1 = Bi 1 <
  B _ = OK _ >
  Bi 0 = Bi 1 <
  Bi 1 = Bi 0 <
  Bi _ = OK _ >
'''
with open('input/turing3.txt') as f:
    alphabet = list(f.readline().rstrip())
    states = f.readline().rstrip().split()
    state = f.readline().rstrip()
    accept = f.readline().rstrip()
    tape = dict(enumerate(f.readline().rstrip()))
    rules = {(A, p): (B, q, d) for A, p, _, B, q, d in map(str.split, f.readlines())}
head = 0

while state != accept:
    state, tape[head], direction = rules[(state, tape.get(head, '_'))]
    head += 1 if direction == '>' else -1

s = ''
for item in range(min(tape.keys()), max(tape.keys())+1):
    ch = tape.get(item, '_')
    s += ch
print(s)
s = ''
for item in range(min(tape.keys()), max(tape.keys())+1):
    s += '|' if item == 0 else '^' if item == head else ' '
print(s)