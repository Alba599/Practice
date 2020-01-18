#!/usr/bin/env python
# coding: utf-8

# # 2-2 Intro Python Practice
# ## Lists
# <font> <b>Student will be able to</b></font>  
# - Create Lists
# - Access items in a list
# - Add Items to the end of a list
# - Insert items into a list
# - Delete items from a list

# ## Create Lists

# In[1]:


# [ ] create and populate list called days_of_week then print it

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

print(days_of_week)


# In[2]:


# [ ] after days_of_week is run above, print the days in the list at odd indexes 1,3,5

print(days_of_week[1])
print(days_of_week[3])
print(days_of_week[5])


# ## Phone letters
# ![phone keys: number and letters](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/phone_letters.JPG)
# Create a list, **`phone_letters`**, where the index 0 - 9 contains the letters for keys 0 - 9.  
# 
# - 0 = ' ' (a space)
# - 1 = '' (empty)
# - 2 = 'ABC'
# - 3 = 'DEF'
# - etc...
# 

# In[3]:


# [ ] create and populate list called phone_letters then print it
phone_letters = [" ", "", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
print(phone_letters)


# ## Access Lists
# ### for the 2 cells below
# - Use days_of_week list created above
# - Run the cell above to make the list available

# In[4]:


# [ ] create a variable: day, assign day to "Tuesday" using days_of_week[]
# [ ] print day variable

day = days_of_week[1]

print(day)



# In[5]:


# PART 2
# [ ] assign day to days_of_week index = 5
# [ ] print day
day = days_of_week[5]
print(day)



# ## Append and Insert items into a list
# 
# ### Endsday, Midsday, Resterday
# #### for the exercises below
# - Use days_of_week list created above
# - Run the cell defining days_of_week above to make the list available

# In[6]:


# [ ] Make up a new day! - append an 8th day of the week to days_of_week 
# [ ] print days_of_week

days_of_week.append("Mars")

print(days_of_week)


# ### Question  
# - What happens if you keep running the cell above?  
# - How can you return to the initial state with the regular 7 days in days_of_week? 

# In[7]:


# [ ] Make up another new day - insert a new day into the middle of days_of_week between Wed - Thurs
# [ ] print days_of_week

days_of_week.insert(3, "Pluton")

print(days_of_week)



# In[8]:


# [ ]  Extend the weekend - insert a day between Fri & Sat in the days_of_week list
# [ ] print days_of_week

days_of_week.insert(6, "Merkur")
print(days_of_week)


# ## Delete from a list
# ### `del` &amp; `.pop()` some bad ideas
# #### exercises below assume days_of_week appended/inserted 3 extra days in previous exercises

# In[9]:


# [ ] print days_of_week 
# [ ] modified week is too long - pop() the last index of days_of_week & print .pop() value
# [ ] print days_of_week


days_of_week.pop()
print(days_of_week)


# In[10]:


# [ ] print days_of_week 
# [ ] delete (del) the new day added to the middle of the week 
# [ ] print days_of_week

del days_of_week[3]

print(days_of_week)


# In[ ]:


# [ ] print days_of_week 
# [ ] programmers choice - pop() any day in days_of week & print .pop() value
# [ ] print days_of_week

days_of_week.pop()

print(days_of_week)


# ## Program:  Letter to Number Function
# # TODO: insert video
# ### for the exercise below
# - Use phone_letters list created above
# - Run the cell above to make the list available 
# 
# #### recall unit 1 using **`in`** to search for a string in a string
# ```python
# if "e" in "open":
#     print("e found")
# else:
#    print("e not found")
# ```
# 
# ![phone keys: number and letters](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/phone_letters.JPG)
# 
# ### create funtion let_to_num()
# - let_to_num() takes input of a single letter, space or empty string stored in an argument variable: letter
#   - use `while key &lt; 10:` to try numbers 0 - 9 as index for `phone_letters` ("key" = phone dial pad key)
#   - check if `letter` variable is in the index of `phone_letters[key]` 
# ```python
# key = 0
# while key &lt; 10:
#     if # Create Code: determine if letter is **`in`** any of the phone_letters[key] where key is the index 0 -9:
#         return key
#     else:
#         key = key + 1
# return "Not Found"
# ```
# - return the number or "Not Found"
# - **call** let_to_num() to test the function so it prints the argument and return value with:
#   - space
#   - lowercase letter
#   - different letter, uppercase
#   - a number
#   
# **Bonus**: create a special case to check if empty string (`""`) was submitted   
# the problem is that an empty string will be found in all strings as  
# ```python
# if "" in "ABC": 
# ```  
# is True, and is true for any phone_letters, but should `return 1`

# In[ ]:


# [ ] create let_to_num()
phone_letters = [" ", "", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

def let_to_num(letter):
    if letter == "":
        return 1
    
    key = 0
    while key < 10:
        if letter in phone_letters:
            return key
    else:
        key = key + 1
    return "Not Found"

print(let_to_num("a"))
print(let_to_num(""))
print(let_to_num("ab"))



# In[ ]:





# ## Challenge: reverse a string 
# ### using 
# - while
# - .pop()
# - insert()  
# 
# **`pop()`** the **first item** in the list and 

# In[ ]:


# [ ] Challenge: write the code for "reverse a string"
word = "word"
reverse = []
print(word.split(","));
 


# In[ ]:





# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977)   [Privacy &amp; cookies](https://go.microsoft.com/fwlink/?LinkId=521839)   © 2017 Microsoft
