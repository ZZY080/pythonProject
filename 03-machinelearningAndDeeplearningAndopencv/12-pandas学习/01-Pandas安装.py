import pandas as pd
mydata={
    "sites":["google","Runoob","wiki"],
    "number":[1,2,3]
}
myvar = pd.DataFrame(mydata)

print(myvar)