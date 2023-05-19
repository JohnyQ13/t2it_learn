from math import ceil

while True:
    ap, fl_build, ap_fl = map(int,input('Input number apartment, count flour and count ap to flour:').split(' '))
    if ap:
        ap, fl_build, ap_fl = int(ap), int(fl_build), int(ap_fl)
        break
    else:
        print('ERROR: Incoret input')


def find_ap():
    total_fl = ceil(ap / ap_fl)
    entr = ceil(total_fl / fl_build)
    if ceil(ap  % (fl_build * ap_fl) / ap_fl):
        f_fl = ceil(ap  % (fl_build * ap_fl) / ap_fl)
    else:
        f_fl = fl_build

    return f"Entrance num: {entr};\nFlour number: {f_fl}."

print(find_ap())
