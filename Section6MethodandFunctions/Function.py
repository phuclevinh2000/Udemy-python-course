def name_of_function(num1, num2):
    return num1 + num2


result = name_of_function('1', '2')
print(result)

# function to check if a number is even or not


def even_check(number):
    return number % 2 == 0


print(even_check(20))

# function return true if any number is even inside a list

# return all the even number in a list


def even_list(num_list):
    even_numbers = []

    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            pass
    return even_numbers


result = even_list([5, 3, 5, 5, 23, 24, 26])
print(result)
