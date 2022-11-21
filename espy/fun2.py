def sum_list(the_list):
    total = 0
    for element in the_list:
            total += element
    return total

def sum_csv(the_file):
    values = []
    open(the_file, 'r') as my_file:
        for line in my_file:
            elements = line.split(',')
            date  = elements[0]
            value = elements[1]
            values.append(float(value))
    file.close()
    return sum_list(values)