from time import sleep

print('{:=^60}'.format(' \033[34mLançamento de fogos de artifício\033[m '))
for i in range(10, -1, -1):
    sleep(1)
    print('{}...'.format(i))
print('BOOM')







