#!/usr/env/python

import time
import random
import string

domain = ['@finebourbon.us', '@pappyvanwinkle.us', '@finewhiskey.us', '@finewhisky.us', '@tradepappy.us']
namelist = open('name_list.txt', 'r')
name = []

for n in namelist:
    name.append(n.rstrip())

for i in range(0,1200):
    pick_name = ''.join(random.choice(name))
    var_str = ''.join([random.choice(string.lowercase) for i in xrange(4)])
    var_num = str(random.randint(1,1001))

    rand_var = ''.join([random.choice([var_str, var_num])])
    rand_pick_domain = ''.join([random.choice(domain)])

    result = pick_name + rand_var + rand_pick_domain
    print result
#    time.sleep(1)
    i+=1
