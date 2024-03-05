
import pandas
import datetime

# Reading csv file into the dataframe 

df = pandas.read_csv("DataCleaning.csv",skiprows=1)
print("****"*20)
print()
print("--"*10,"Data Frame","--"*10)
print(df)
print("****"*20)

# Droping Rows with NaN(Not a numerical ) values 
print("--"*10,"Drop NaN","--"*10)
print()
df_without_nan = df.copy().dropna()
print(df_without_nan)
print("****"*20)

# Replacing specific  columns every value 

print("--"*10,"Replace specific column values into default","--"*10)
print()
pulse_default_value = 110
df_without_nan['Pulse'] = pulse_default_value
print(df_without_nan)
print("****"*20)

# Replacing the NaN values in columns 

print("--"*10,"Replace NaN","--"*10)
date_string = "2023-12-23"
date = datetime.datetime.strptime(date_string, "%Y-%m-%d")
df_with_replaced_nan = df.copy()
df_with_replaced_nan['Date'] = df_with_replaced_nan['Date'].fillna(pandas.to_datetime(date))
print(df_with_replaced_nan)
print("****"*20)

# Replacing column missing with mean value 

print("--"*10,"Replace column with mean value","--"*10)
print() 
mean_value = df['Calories'].mean()
df_with_replaced_nan['Calories'] = df_with_replaced_nan['Calories'].fillna(mean_value)
print(df_with_replaced_nan)
print("****"*20)

#Cleaning wrong data 

print("--"*10,"Cleaning wrong data","--"*10)
print() 
df_with_replaced_nan["Date"] = pandas.to_datetime(df_with_replaced_nan["Date"],errors="coerce")
print(df_with_replaced_nan)
print("****"*20) 

# Cleaning Unidentified datetime

print("--"*10,"Cleaning Unidentified datetime","--"*10)
print()
df_with_replaced_nan = df_with_replaced_nan.dropna(subset=["Date"])
print(df_with_replaced_nan)
print("****"*20)


# Cleaning Outliers

print("--"*10,"Cleaning Outliers","--"*10)
print()
for i in df_with_replaced_nan.index:
    if df_with_replaced_nan.loc[i,"Duration"] > 120:
        df_with_replaced_nan.loc[i,"Duration"] = 80 
print(df_with_replaced_nan)
print("****"*20) 

# Cleaning Duplicates 

print("--"*10,"Cleaning Duplicates","--"*10) 
print() 

df_with_replaced_nan = df_with_replaced_nan.drop_duplicates() 
print(df_with_replaced_nan) 

print("****"*20) 

