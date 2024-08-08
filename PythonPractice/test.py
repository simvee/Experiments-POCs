list_str = []

def return_gen_str(str_current, n):
    # adds a parenthesis to the left right and center of the current string
    print("n=", n)
    if n == 1:
        list_str.append(str_current)
        print(str_current)
        return None
    
    for ind in range(len(str_current)):
        
        next_str = str_current[:ind] + "()" + str_current[ind:]
        return_gen_str(next_str, n-1)

n = 5

if n!=0:
    initial_str = "()"
else:
    initial_str = ""

return_gen_str(initial_str, n)

list_str = list(set(list_str))

print(list_str)