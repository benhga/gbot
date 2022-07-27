import pandas as pd


demos = pd.read_csv("./demographics/ww_test_csv.csv")
nums = demos['Phone number 1']
nums2 = demos['Phone number 2']
num = "+27822205729"

num = num.replace('+27', '0')

# num = num[:3] + ' ' + num[3:6] + " " +
print(num)

