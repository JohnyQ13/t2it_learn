fl, fl_num, num = map(int, input().split(' '))
#fl=5, fl_num=4, num=101
def courier(fl, fl_num, num):
    entr_num =fl*fl_num
    entr = num // entr_num
    if num % entr_num:
        entr += 1
entr=6, entr_num=20
    num = num % entr_num
    
    if num == 0:
        fl_rez = fl
    else:
        fl_rez = num // fl_num
        if num % fl_num:
            fl_rez += 1 
    
    return(entr,fl_rez)

print(courier(fl, fl_num, num))

