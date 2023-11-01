import pandas as pd
def cointoss(n):
    try:
        n = int(n)
    except ValueError:
        print("Please input an integer")
        return
    if not (1 <= n <= 3):
        print("Please input an integer between 1 and 3")
        return
    toss_labels = ['toss'] * n
    int_labels = range(1,n+1)
    column_names = []
    for i in range(0,n):
        column_names.append(toss_labels[i]+str(int_labels[i]))
    df = pd.DataFrame(columns=column_names)
    for i in range(0,2**n):
        int_to_binary = bin(i)[2:].zfill(n)
        new_row = []
        for j in range(0,n):
            if int_to_binary[j] == '0':
                new_row.append('T')
            else:
                new_row.append('H')
        df.loc[i] = new_row
    return df
input_number = int(input('Please input number of time to toss coin:'))
print(cointoss(input_number))