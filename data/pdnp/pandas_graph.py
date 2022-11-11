import pandas as pd

df = pd.DataFrame({'영어':[10, 30, 50, 30], '수학':[30,60,70,10]})

pd.plotting.andrews_curves(df, '영어')