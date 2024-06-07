def print_params(a = 1, b = 'строка', c = True):
    print (a,b,c)

values_list = [1,True,'почему что']
values_dict = {'a':25,'b':"stroca",'c':True}
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2,25)