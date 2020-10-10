def func(a, b, c):
    print(a, b, c)


my_dict = {
    'c': "parm-c",
    'a': "parm-a",
    'b': "parm-b",
}

func(**my_dict)

