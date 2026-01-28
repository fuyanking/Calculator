# This code should run in Python 3.11
# This code implements a calculator to evaluate a basic math expression

# This function calculates the temp result of two numbers with the operator op
def operator(op, num1, num2):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        return num1 / num2
    else:
        return None     # otherwise, return None

#This function compares the priority between two operators op1 and op2
def is_prior(op1, op2):
    tier1 = {"(", ")"}      # represents the highest priority
    tier2 = {"*", "/"}      # represents the middle priority
    tier3 = {"+", "-"}      # represents the lowest priority
    # If the priority of op1 is higher than op2's or op2 is in the highest priority "()", return True.
    # Otherwise, return False
    if op1 in tier2 and op2 in tier3 or op2 in tier1:
        return True
    else:
        return False

# This function calculates and returns the temporary result
def pop_and_calculate(num_stack, op_stack):
    #pop the first top number in num_stack as the number following an operator
    #pop the second top number in num_stack as the number before an operator
    #THE ORDER MATTERS, especially for subtraction and division!
    num2 = num_stack.pop()
    num1 = num_stack.pop()
    #pop the top operator in op_stack as op_top
    op_top = op_stack.pop()
    # calculate the temp result and push it into num_stack
    result = operator(op_top, num1, num2)
    num_stack.append(result)
    return result

# This function accepts users' input expression and two lists as parameters
# return the final result
def calc_expression(expression, num_stack, op_stack):
    # use num_str to store the string of a multi-digit number
    # and initialize it as an empty string
    num_str = ""
    for i in range(len(expression)):
        if expression[i].isdigit():
            # when i-th character is a digit
            # merge consecutive digits into a multi-digit number string
            num_str += expression[i]
            # if we reach the end of the expression or next character is not a digit
            # convert num_str into an integer and push it into num_stack
            if i == len(expression) - 1 or not expression[i + 1].isdigit():
                num_stack.append(int(num_str))
                # reset num_str as an empty string, get ready for another number
                num_str = ""
        else:
            op = expression[i]
            # if we reach "(" push it into op_stack
            if op == "(":
                op_stack.append(op)
            # if we reach ")", use pop_and_calculate function
            # to calculate the temp result and push it into num_stack
            elif op == ")":
                pop_and_calculate(num_stack, op_stack)
                # pop the "(" out of op_stack
                op_stack.pop()
            # if the operator is not "(" nor ")"
            else:
                if len(op_stack) > 0:
                    # peek the top of op_stack as op_top
                    op_top = op_stack[-1]
                    # if op_top is prior to the current operator
                    # use pop_and_calculate function to calculate temp result
                    if not is_prior(op, op_top):
                        pop_and_calculate(num_stack, op_stack)
                # push current operator into op_stack
                op_stack.append(op)
    # after traversing the expression
    # usually some operators and numbers remain in the stacks
    # use while loop to clear all elements in two stacks and calculate final result
    while len(op_stack) > 0:
        pop_and_calculate(num_stack, op_stack)
    return num_stack.pop()

# The main function controls the main process of code and interacts with users
def main():
    # the flag_continue denotes whether the program will continue calculation
    # True for continuing, False for stop
    flag_continue = True
    # use while loop to repeat the main body, until the flag is False
    while flag_continue:
        # initialize two lists to simulate a stack's LIFO property
        # list.append() for push, list[-1] for peek, list.pop() for pop
        # num_stack stores numbers in the expression
        # op_stack stores operators in the expression
        num_stack = []
        op_stack = []
        # prompt users to input a math expression
        expression = input(str("Enter an expression: "))
        # call the function to calculate the result
        result = calc_expression(expression, num_stack, op_stack)
        # display the final result
        print("The result is:")
        print(result)
        # prompt users to decide whether to continue calculation
        continue_input = input(str("Calculate another expression? (y/n): "))
        # 'y' for continuing, keep the flag True
        if continue_input == 'y':
            flag_continue = True
        # 'n' for stop, set the flag False, break the while loop
        elif continue_input == 'n':
            flag_continue = False
        # otherwise, prompt users and break the loop
        else:
            print('Invalid input, program exits!')
            break
    # end prompt, program terminates
    print("Thank you for using the calculator!")

# entrance of the python code
if __name__ == "__main__":
    main()

