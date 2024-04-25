import statistics



def display_main_menu(): 
    print("display_main_menu")
    print("Enter some numbers separated by commas")

def calc_average(values_list): 
    print("calc_average")
    average = sum(values_list)/len(values_list)
    print(average)

def get_user_input():
    print("get user input")
    values = input("Enter values")
    splitText = values.split(",")
    values_list = []
    for x in splitText:
        values_list.append(float(x))
    print(values_list)
    return values_list
def find_min_max(values_list):
    print("find min and max")
    print("minimum is ",min(values_list))
    print("maximum is ",max(values_list))


    return list 
def sort_temperature(values_list): 
    print("sort temperature")
    print(sorted(values_list))
    return float 
def calc_median_temperature(values_list):
    print("calculate median temp")
    print(statistics.median(values_list))
    return float 
y=get_user_input() 
find_min_max(y)
calc_average(y)
sort_temperature(y)
calc_median_temperature(y)