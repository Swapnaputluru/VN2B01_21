import pandas

print("version of pandas", pandas.__version__)

data = {
    "name": ["swapna", "dattu", "manu", "krish"],
    "job" : ["Software", "bank job", "Assistant Engineer", "CA"]
}
print("=========By using Series=========")
s = pandas.Series([2, 4, 6, 8, 10])
print(s)
print("==========by using index==============")
print("Value of index 2 is :", s[2])
a = pandas.DataFrame(data)
print(a)
print("------------Another example------------")
df = pandas.DataFrame({'Names':["Sony", "Sunny", "Syam", "Somu","saru"], 'Maths':[84,94,89,83,86],'English':[86,97,96,72,83]});
print(df)

print("==========First 2 rows==============")
print(df.head(2))

print("==========Last 2 rows==============")
print(df.tail(3))

print("==========Number of rows and columns==============")
print(df.shape)

print("==========Index, Datatype and Memory information==============")
print(df.info())


