def correlacao(x, y):
    average_x = sum(x) / len(x)
    average_y = sum(y) / len(y)
    sum_of_pow_difference_between_eachx_and_average_x = 0
    sum_of_pow_difference_between_eachy_and_average_y = 0
    sum_of_product_of_difference_between_x_and_average_x_and_between_y_and_average_y = 0
    for point in range(len(x)):
        difference_between_x_and_average_x = x[point] - average_x
        difference_between_y_and_average_y = y[point] - average_y

        sum_of_pow_difference_between_eachx_and_average_x += pow(difference_between_x_and_average_x)
        sum_of_pow_difference_between_eachy_and_average_y += pow(difference_between_y_and_average_y)

        sum_of_product_of_difference_between_x_and_average_x_and_between_y_and_average_y += difference_between_x_and_average_x * difference_between_y_and_average_y
    
    return sum_of_product_of_difference_between_x_and_average_x_and_between_y_and_average_y / sqrt(sum_of_pow_difference_between_eachx_and_average_x * sum_of_pow_difference_between_eachy_and_average_y)

def sqrt(number):
    return number ** 0.5

def pow(number):
    return number ** 2

def regressao(x, y):
    average_x = sum(x) / len(x)
    average_y = sum(y) / len(y)
    sum_of_product_of_difference_between_x_and_average_x_and_between_y_and_average_y = 0
    sum_of_product_of_difference_between_x_and_average_x = 0
    for point in range(len(x)):
        difference_between_x_and_average_x = x[point] - average_x
        difference_between_y_and_average_y = y[point] - average_y

        sum_of_product_of_difference_between_x_and_average_x += pow(difference_between_x_and_average_x)
        sum_of_product_of_difference_between_x_and_average_x_and_between_y_and_average_y += difference_between_x_and_average_x * difference_between_y_and_average_y

    bone = sum_of_product_of_difference_between_x_and_average_x_and_between_y_and_average_y / sum_of_product_of_difference_between_x_and_average_x

    bzero = average_y - (bone * average_x)

    return bone, bzero