'''
A very simple program which tell user its grade when he/she enter its score.
'''

print('Range: 0-1')
score = input("Enter Score: ")

try:
    s = float(score)
except:
    print('Only Integers are Allowed.')
    quit()

if s >= 0.9:
    print('A')
elif s >= 0.8:
    print('B')
elif s >= 0.7:
    print('C')
elif s >= 0.6:
    print('D')
elif s < 0.6:
    print('F')