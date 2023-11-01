import pandas as pd
def create_df(r):
    sample_labels = ['X'] * r
    int_labels = range(1,r+1)
    column_names = []
    for i in range(0,r):
        column_names.append(sample_labels[i]+str(int_labels[i]))
    df = pd.DataFrame(columns=column_names)
    return df

def generate_combinations(n,r):
    df = create_df(r)
    if r == 0:
        return df
    current_selection = [*range(1,r+1)]
    count = 0
    df.loc[count] = current_selection
    count+=1
    index = -1
    flag = False
    while current_selection != [*range(n-r+1,n+1)]:
        if current_selection[index]+1<=n+index+1:
            current_selection[index]+=1
            if flag:
                for i in range(index+1,0):
                    current_selection[i] = current_selection[i-1]+1
                df.loc[count] = current_selection
                count+=1
                flag=False
                index=-1
            else:
                df.loc[count]=current_selection
                count+=1
        else:
            index-=1
            flag=True
    return df


input_number_n = int(input('Please input number of distinct options (n):'))
input_number_r = int(input('Please input number of selections (r):'))
print(generate_combinations(input_number_n,input_number_r))