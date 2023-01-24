import sys
from time import sleep
# unitColor = '\033[5;36m\033[5;47m'
# endColor = '\033[0;0m\033[0;0m'
# count = 45
# for i in range(count):
#     pass
# sys.stdout.write('\n')
unitColor = '\033[5;36m\033[5;47m'
endColor = '\033[0;0m\033[0;0m'
count = 45
for i in range(count):
    incre = int(50.0 / count * i)
    sys.stdout.write('\r' + '|%s%s%s%s| %d%%' % (unitColor, '\033[7m' + ' '*incre + ' \033[27m', endColor, ' '*(50-incre), 2*incre)) if i != count - 1 else sys.stdout.write('\r' + '|%s%s%s| %d%%' % (unitColor, '\033[7m' + ' '*20 + 'COMPLETE!' + ' '*21 + ' \033[27m', endColor, 100))
    sys.stdout.flush()
    sleep(0.1)
sys.stdout.write('\n')