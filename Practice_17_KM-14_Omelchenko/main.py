from exp_root.exponentation import exp2, exp3
from exp_root.root import root2, root3
from factorial.factorial import fact
from logarithm.logarithm import log, lg, ln
from math import e


def first_input_check(message):
    print(message)
    while True:
        check = input()
        if check == '1' or check == '2' or check == '3' or check == '4':
            return check
        print("Input is invalid, input should integer from 1 to 4  ")


def two_number_type_input_check(message):
    print(message)
    while True:
        check = input()
        if check == '1' or check == '2':
            return check
        print("Input is invalid, input should integer from 1 to 2  ")


def three_number_type_input_check(message):
    print(message)
    while True:
        check = input()
        if check == '1' or check == '2' or check == '3':
            return check
        print("Input is invalid, input should integer from 1 to 3 ")


def exp_input_check(message):
    print(message)
    while True:
        try:
            check = float(input())
            if check >= 0:
                return check
        except:
            print("Input is invalid, input should number  ")


def root2_and_factorial_input_check(message):
    print(message)
    while True:
        try:
            check = float(input())
            if check >= 0:
                return check
            else:
                raise Exception
        except:
            print("Input is invalid, input should number  ")


def root3_input_check(message):
    print(message)
    while True:
        try:
            check = float(input())
            return check
        except:
            print("Input is invalid, input should number  ")


def log_arg_input_check(message):
    print(message)
    while True:
        try:
            check = float(input())
            if check > 0:
                return check
            else:
                raise Exception
        except:
            print("Input is invalid, input should number and more than 0 ")


def log_base_input_check(message):
    print(message)
    while True:
        try:
            check = float(input())
            if check > 0 and check != 1:
                return check
            else:
                raise Exception
        except:
            print("Input is invalid, base should number and more than 0 and not equal to 1 ")


def main():
    first_check = first_input_check("Press '1' if you want to find exponent of the number\n"
                                    "Press '2' if you want to find root of the number\n"
                                    "Press '3' if you want to find factorial of the number\n"
                                    "Press '4' if you want to find logarithm of the number")

    if first_check == '1':
        exp_check = two_number_type_input_check("Press '1' if you want to square the number\n"
                                                "Press '2' if you want to cube the number")
        if exp_check == '1':
            exp = exp_input_check("Input the number you want to square ")
            print(exp2(exp))
        if exp_check == '2':
            exp = exp_input_check("Input the number you want to cube ")
            print(exp3(exp))

    elif first_check == '2':
        root_check = two_number_type_input_check("Press '1' if you want to square root the number\n"
                                                 "Press '2' if you want to cube root the number")

        if root_check == '1':
            root = root2_and_factorial_input_check("Input the number you want to square root")
            print(root2(root))
        if root_check == '2':
            root = root3_input_check("Input the number you want to cube root")
            if root < 0:
                print(-root3(-root))
            else:
                print(root3(root))
    elif first_check == '3':
        fact_arg = root2_and_factorial_input_check("Input the number you want to square root")
        print(fact(fact_arg))
    elif first_check == '4':
        log_check = three_number_type_input_check("Press '1' if you want to log(a, b)\n"
                                                  "Press '2' if you want to ln(a)\n"
                                                  "Press '3' if you want to lg(a)")
        if log_check == '1':
            log_base = log_base_input_check("Input your base for log")
            log_arg = log_arg_input_check("Input your argument for log")
            print(log(log_base, log_arg))

        if log_check == '2':
            log_arg = log_arg_input_check("Input your argument for log")
            print(ln(log_arg))

        if log_check == '3':
            log_arg = log_arg_input_check("Input your argument for log")
            print(lg(log_arg))


if __name__ == '__main__':
    print('-' * 40)
    main()
