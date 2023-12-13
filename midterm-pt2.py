import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import requests as rq

def main():
    data_url = "https://raw.githubusercontent.com/mdogy/dataForEng1999/master/ckd.csv"

    #2.1
    pp_df = pd.read_csv(data_url)
    pp_df.head()
    pp_df.info()
    pp_df.describe()

    #2.2
    pp_df.dropna(inplace=True)
    pp_df['Class'].nunique()

    class0 = pp_df['Blood Pressure'][pp_df['Class'] == 0]
    class1 = pp_df['Blood Pressure'][pp_df['Class'] == 1]

    class0_count = len(class0)
    class1_count = len(class1)
    print(class0_count, class1_count)

    class0_mean =  class0.mean()
    class1_mean =  class1.mean()
    print(f"class0_mean: {class0_mean}, class1_mean: {class1_mean}")

    emp_diff_mean = class1_mean - class0_mean
    print(f"emp_diff_mean: {emp_diff_mean}")

    fig, ax = plt.subplots()
    ax.bar([0,1],[class0_mean, class1_mean])
    ax.set_xticks([0,1])
    ax.set_xticklabels(['class0','class1'])
    ax.set_ylabel("Blood Pressure")
    ax.set_title('Mean Blood Pressure by Class')

    fig.savefig("barplot.png")

    #2.3
    class0_class1 = pp_df[['Blood Pressure', 'Class']]
    class0_class1.head()

    diff_means = []
    for i in range (10000):
        blood_pressures = class0_class1.sample(n=class0_count + class1_count,replace = True)
        class0_mean = blood_pressures['Blood Pressure'][:class0_count].mean()
        class1_mean = blood_pressures['Blood Pressure'][class0_count:].mean()
        diff = class0_mean - class1_mean
        diff_means.append(diff)
    print(f"length of diff_means: {len(diff_means)}")

    df_dm = pd.DataFrame({"diff_means":diff_means})
    
    fig, ax = plt.subplots()
    ax.hist(df_dm['diff_means'], bins = 30)
    ax.set_xlabel("Difference of Simulated Means")
    ax.scatter([emp_diff_mean],[10], c='r',s=30)
    fig.savefig("histplot.png")

    larger_than_emp = df_dm[df_dm['diff_means'] > emp_diff_mean]
    p_value = (len(larger_than_emp)+1)/len(df_dm)
    print(f"p-value = {p_value}")






if __name__ == "__main__":
    main()