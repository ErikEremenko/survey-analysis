from sqlite3 import Row
import pandas as pd
filename = "(8) Politische Bildung.csv"
data = pd.read_csv(filename)

col = []

for i in range(8):
    col.append(str(i+3))
    
print(col)

df = pd.DataFrame(data, columns= col)

# for col in data.columns:
#     print(col)

print(df)

means = []

for i in range(8):
    means.append(df[str(i+3)].mean())
    
print(means)

Row_list= []

for index, rows in df.iterrows():
    
    #my_list = [rows.3, rows.4, rows.5, rows.6, rows.7, rows.8, rows.9, rows.10]
    
    Row_list.append(rows)
    
# print(Row_list[0][0])

#print(pd.DataFrame(data, Name = "20"))

#print(Row_list)

t = 0

# for row in Row_list:
#     print('row',t,":", row[t][:])
#     t += 1

print(df.columns())