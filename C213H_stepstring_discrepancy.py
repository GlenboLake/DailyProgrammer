'''
http://www.reddit.com/r/dailyprogrammer/comments/358pfk/20150508_challenge_213_hard_stepstring_discrepancy/

Define the discrepancy of a string of any two symbols (I'll use a and b) to be
the absolute difference between the counts of each of the two symbols in the
string. For example, all of the following strings have a discrepancy of 3:

  aaa 
  bbb 
  abbbb 
  aababaa 
  baababbababababababbbaabbaaaabaaabbaa 

Define a stepstring of a string to be any string that can be formed by starting
at any position x in the string, stepping through the string n characters at a
time, and ending before any position y. In python, this is any string that can
be formed using slice notation s[x:y:n]. For example, some stepstrings of the
string "abcdefghij" are:

  d
  defg
  acegi
  bdfhj
  dfh
  beh
  ai
  abcdefghij

Your problem is, given a string of up to 10,000 characters, find the largest
discrepancy of any stepstring of the string. For instance, this string:
  bbaaabababbaabbaaaabbbababbaabbbaabbaaaaabbababaaaabaabbbaaa 
has this string as a stepstring (corresponding to the python slice notation s[4:56:4]):
  aaaabaaaaabaa 
which has a discrepancy of 9. Furthermore, no stepstring has a discrepancy
greater than 9. So the correct solution for this string is 9.

Challenge input_:
http://pastebin.com/raw.php?i=Xt3BV8nK
Challenge output:
113
117
121
127
136
136
138
224
'''

def discrepancy(string):
    freq = {}
    for ch in string:
        if freq.has_key(ch):
            freq[ch] += 1
        else:
            freq[ch] = 1
    counts = freq.values()
    return abs(counts[0] - counts[1])

def stepstrings(string):
    # Single-length separately avoids repetition
    for i in range(len(string)):
        print(i)
    for start in range(len(string)):
        for step in range(1, len(string) - start):
            for end in range(start + step + 1, len(string) + 1):
                print(start, end, step)
                #print string[start:end:step]


if __name__ == '__main__':
    input_ = open('input/stepstring.txt', 'r').readlines()
    input_ = '''bbaaabababbaabbaaaabbbababbaabbbaabbaaaaabbababaaaabaabbbaaa
bbaaaababbbaababbbbabbabababababaaababbbbbbaabbaababaaaabaaa
aaaababbabbaabbaabbbbbbabbbaaabbaabaabaabbbaabababbabbbbaabb
abbabbbbbababaabaaababbbbaababbabbbabbbbaabbabbaaabbaabbbbbb'''
    stepstrings('abcde')
#    for s in stepstrings('12345'):
#        print s
