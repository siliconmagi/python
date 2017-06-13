import pandas as pd

# read
# path = r'./'  # use your path
# allFiles = glob.glob(path + "/*.xlsx")
#  print(allFiles)

sd = pd.read_excel('./solidData.xlsx')
vd = pd.read_excel('./vendorDataTrim.xlsx')

print(sd)
print(vd)
