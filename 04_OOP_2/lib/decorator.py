# 1. ✅ First Class Functions
# "[We can] assign them to variables, store them in data structures, pass them as arguments
# to other functions, and even return them as values from other functions."
# See more => http://bit.ly/3YQh8KR

    # Create functions to be used as callbacks 

    # Create a higher-order function that will take a callback as an argument

def walk(pet):
    print(f'{pet} has been walked!')

def feed(pet):
    print(f'{pet} has been fed!')

# def execute_task(func):
#     return func("Rose")

# execute_task(walk)

# 2. ✅ Create a higher-order function that returns a function

def execute_task():
    def feed(pet="Rose"):
        print(f'{pet} has been fed')
    # def walk(pet="Boogie"):
    #     print(f'{pet} has been walked!')
    return feed

execute_task()

execute_task()("Bart")

# 3. ✅ Decorator

def coupon_calculator(func):
    def report_price():
        print(f'Initial Price = $35.00')
        final_price = func(35.00)
        print(f'Newly Discounted Price = ${final_price}')
    return report_price

# def calculate_price(price):
#     return '{:.2f}'.format(round(price/2, 2))

# coupon_calculator(calculate_price)()
# # OR
# report = coupon_calculator(calculate_price)
# report()

@coupon_calculator
def calculate_price(price):
    return '{:.2f}'.format(round(price/2, 2))
calculate_price()






# Create a function that:
    # - takes a function as an argument
    # - has an inner function defined 
    # - returns the inner function

# Tools:

    # .format()
    # https://www.geeksforgeeks.org/python-string-format-method/

    # .round()
    # https://www.geeksforgeeks.org/round-function-python/

# Try using a decorator with / without pie syntax '@'

# Without pie syntax 

# With pie syntax