
# Sternenmuster

# Schreibe ein Python-Programm,
# das folgende Sternchen-Muster auf den Bildschirm schreibt:

"""
* * * *
* * * *
* * * *

*
* *
* * *
* * * *
* * * * *

      *
    * * *
  * * * * *
* * * * * * *
"""

for i in range(1,4):
    print('* '*4)
print()

n = 1
for i in range(1,6):
    print('* '* n)
    n = n + 1
print()

n = 1
m = 6
for i in range(1,5):
    print(' '*m, '* '* n)
    n = n + 2
    m = m - 2
    