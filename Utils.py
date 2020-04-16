import math

#max_num_of_iterations = 6
max_num_of_iterations = 15
const = 0.1

def is_converged(new,old,num_of_iterations):
    converging_factor = 0.00000001
    if num_of_iterations > max_num_of_iterations :
        return True

    for i in range(len(new)):
        for j in range(len(new[0])):
            if math.fabs(new[i][j]- old[i][j]) > converging_factor:
                return False
    return True


def nCr(n,r):
    try:
        if (n-r < 0) :
            return 1
        f = math.factorial
        return f(n) / f(r) / f(n-r)
    except:
        print("value error " + str(n) + "  " + str(r))
        raise


def factorial(n):
    if n < 0 :
        return 1
    f = math.factorial
    return f(n)


