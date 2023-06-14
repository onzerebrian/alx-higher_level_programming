#!/usr/bin/python3
def uniq_add(my_list=[]):
    _uniq=[]
    for i in my_list:
        x = i
        v = 0
        for m in _uniq:
            if m == x:
                v += 1
        if v == 0:
            _uniq.append(i)
    s_um = 0
    for i in _uniq:
        s_um += i
    return s_um
