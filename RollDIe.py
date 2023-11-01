import pandas as pd
def is_there_another_event(current_event):
    return current_event != [6] * len(current_event)
def get_next_event(current_event):
    next_event = current_event
    if current_event[-1] < 6:
        next_event[-1] += 1
    else:
        negative_index = -1
        while current_event[negative_index] == 6:
            next_event[negative_index] = 1
            negative_index -= 1
        next_event[negative_index] += 1
    return next_event
def rolldie(n):
    try:
        n = int(n)
    except ValueError:
        print("Please input an integer")
        return
    if not (1 <= n <= 3):
        print("Please input an integer between 1 and 3")
        return
    roll_labels = ['X'] * n
    int_labels = range(1,n+1)
    column_names = []
    for i in range(0,n):
        column_names.append(roll_labels[i]+str(int_labels[i]))
    df = pd.DataFrame(columns=column_names)
    count = 0
    current_event = [1] * n
    while is_there_another_event(current_event):
        df.loc[count] = current_event
        count += 1
        current_event = get_next_event(current_event)
    df.loc[count] = [6] * n
    return df
input_number = int(input('Please input number of times to roll die:'))
print(rolldie(input_number))