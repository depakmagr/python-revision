a = 1       ## Global scope

def summ(b, c):                 ## {(b, c) are argument}
    global a
    a = 2
    print("Inside Function",a)
    return b + c

print("Outsider function", a)
# print(summ(4, 8))
summ(4, 8)                  ## {(4, 8) are parameter.}



########################
Types of arguments.
    positional argument:
            def summ(a)

            summ(2)


    default argument:
            def summ(a, b, d=1)

            summ(2, 3)                      #{no need to pass the value.}



    arbitary argument:
            def summ(a, b, d=1, *args, **kwargs):
                 eg:
                    def deeps(*args):
                        print(args)
                        print(type(args))
                        return sum(args)

                    print(deeps(1))
                    print(deeps(1, 2))
                    print(deeps(1, 2, 3))
                    print(deeps(1, 2, 3, 4))
                    print(deeps(1, 2, 3, 4, 5))

#############
                def deeps(**kwargs):
                    print(kwargs)                   #{"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
                    print(type(kwargs))
                    return sum(kwargs.values())

                print(deeps(a=1))
                print(deeps(a=1, b=2))
                print(deeps(a=1, b=2, c=3))
                print(deeps(a=1, b=2, c=3, d=4))
                print(deeps(a=1, b=2, c=3, d=4, e=5))               # {args takes tuple and **kwargs takes dictionary.}


