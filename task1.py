#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pandas matplotlib')



# In[2]:


import pandas as pd
import matplotlib.pyplot as plt


# In[3]:


df = pd.read_csv(
    "C:/Users/BinduShree S/OneDrive/Desktop/population_project/API_SP.POP.TOTL_DS2_en_csv_v2_38144.csv",
    skiprows=4
)


# In[4]:


df.head()


# In[5]:


df.info()


# In[6]:


# Remove empty column
df = df.drop(columns=["Unnamed: 69"])


# In[7]:


year = "2022"

data_2022 = df[["Country Name", year]].dropna()
data_2022.head()


# In[8]:


top10 = data_2022.sort_values(by=year, ascending=False).head(10)

plt.figure()
plt.bar(top10["Country Name"], top10[year])
plt.xticks(rotation=75)
plt.xlabel("Country")
plt.ylabel("Population")
plt.title("Top 10 Population Distribution (2022)")
plt.show()


# In[9]:


plt.figure()
plt.hist(data_2022[year], bins=20)
plt.xlabel("Population")
plt.ylabel("Number of Countries")
plt.title("Population Distribution of Countries (2022)")
plt.show()


# In[10]:


india = df[df["Country Name"] == "India"]

years = india.columns[4:]
population = india.iloc[0, 4:]

plt.figure()
plt.plot(years, population)
plt.xticks(rotation=90)
plt.xlabel("Year")
plt.ylabel("Population")
plt.title("India Population Growth (1960–2024)")
plt.show()


# In[12]:


num = int(input("Enter number: "))
flag = True

for i in range(2, num):
    if num % i == 0:
        flag = False
        break

if flag:
    print("Prime number")
else:
    print("Not prime")


# In[15]:


num = int(input("Enter number: "))
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print("Reversed number:", rev)


# In[18]:


num = int(input("Enter number: "))
temp = num
rev = 0

while num > 0:
    rev = rev * 10 + num % 10
    num //= 10

if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")


# In[33]:


n = int(input("Enter n: "))
a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b



# In[34]:


nums = [10, 25, 7, 90, 45]
largest = nums[0]

for i in nums:
    if i > largest:
        largest = i

print("Largest:", largest)


# In[1]:


num = int(input("Enter the Number:"))
temp = num
reverse = 0
while num > 0:
    remainder = num % 10
    reverse = (reverse * 10) + remainder
    num = num // 10

print("The Given number is {} and Reverse is {}".format(temp, reverse))


# In[4]:


num1 = int(input("Enter First Number:"))
num2 = int(input("Enter Second Number:"))


def gcdFunction(num1, num2):
    if num1 > num2:
        small = num2
    else:
        small = num1
    for i in range(1, small+1):
        if (num1 % i == 0) and (num2 % i == 0):
            gcd = i
    print("GCD of two Number: {}".format(gcd))

gcdFunction(num1, num2)


# In[6]:


#take user input
String1 = input('Enter the String :')
#initialize string and save reverse of 1st string
String2 = String1[::-1]
#check if both matches
if String1 == String2:
    print('String is palindromic')
else:
    print('Strings is not palindromic')


# In[ ]:




