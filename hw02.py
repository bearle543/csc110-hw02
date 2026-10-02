# ------------------------------------------------------
#        Name: Brioni Earle
#       Peers: None
#  References: None
# ------------------------------------------------------

# Task 1.1:
#  Complete the function "read_two_ints" below:

def read_two_ints():
    
    # ADD a Docstring for this function
    
    """Asks for and returns two integers, x and y"""
    
    # the return shown below is a placeholder to make sure this runs
    # TODO: complete the function instead of the line shown below
    
    x = int(input("give me x: "))
    y = int(input("give me y: "))
    print(x, y)
    return x, y
    
# Task 2.1:
#  Complete the function "compute_multadd" below:

def compute_multadd(a, b):
    
    # ADD a Docstring for this function
    
    """Calculates the product and sum of two input integers"""
    
    # the pass shown below is a placeholder to make sure this runs
    # TODO: complete the function instead of the line shown below
    
    mult_result = (a*b)
    print("mult result:", mult_result)
    add_result = (a+b)
    print("add result:", add_result)
    return mult_result/add_result

# Task 3.1:
#  Complete the function "print_fancy" below:

def print_fancy(a, b, xy_multadd):
    
    # ADD a Docstring for this function
    
    """Prints integers and solutions"""
    
    # the pass shown below is a placeholder to make sure this runs
    # TODO: complete the function instead of the line shown below
    
    print("****************")
    print("RESULTS: ")
    print("first number: ",a)
    print("second number: ",b)
    print("multadd result: ",xy_multadd)
    print("================")

def main ():
    # ADD a Docstring for this function
    
    """Prints function final output"""
    
    # Task 1.2:
    #  Add one line below to call read_two_ints (note that it returns two values)    
    #  the call should provide no arguments
    #  store the returned values into two variables: x and y

    x, y = read_two_ints()

    # Task 2.2:
    #  Add one line below to call multadd (note that it returns one value)
    #  the call should provide the arguments x, and y you obtained above;
    #  store the returned value in a variable called xy_multadd

    xy_multadd = compute_multadd(x, y)

    # Task 3.2:
    #  Complete The line below to call print_fancy
    #  the call should provide the arguments x, y, and xy_multadd you obtained above;

    print_fancy(x, y, xy_multadd)


    # Do not modify this final print statement
    print("The End")

# Do not modify these two lines
if __name__ == "__main__":
    main()
