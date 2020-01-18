#!/usr/bin/env python
# coding: utf-8

# # 2-1 Intro Python Practice
# ## Sequence: String
# 
# <font> <b>Student will be able to</b></font>  
# - Work with String Characters
# - Slice strings into substrings
# - Iterate through String Characters
# - Use String ~~Tricks~~ Methods

# #  
# <font> <b>Task 1</b></font>
# ##  Access String Characters 
# ### `working_string[index]`
# 

# In[2]:


# [ ] access and print the second character from planet_name: "u"
planet_name = "Jupiter"

for letter in planet_name[1]:
    print(letter)


# In[3]:


# [ ] access and print the first character from planet_name: "J"
planet_name = "Jupiter"

print(planet_name[0])


# In[4]:


# [ ] access and print the first and last characters from planet_name
planet_name = "Jupiter"

print(planet_name[0])
print(planet_name[-1])


# In[5]:


# [ ] using a negative index access and print the first character from planet_name: "J"
planet_name = "Jupiter"

print(planet_name[-7])


# In[1]:


print("Hello")


# #  
# <font> <b>Task 2</b></font>
# ## slice
# ### `working_string[start:stop]`
# ### `working_string[start:stop:step]`

# In[6]:


# [ ] print planet_name sliced into the first 3 characters and remaining characters
planet_name = "Neptune"


print(planet_name[:3])
print(planet_name[3:])


# In[7]:


# [ ] print 1st char and then every 3rd char of wise_words
# use string slice with a step
wise_words = 'Play it who opens'

print(wise_words[0::3])


# In[8]:


# [ ] print planet_name in reverse
print(planet_name[::-1])


# #  
# <font> <b>Task 3</b></font>
# 
# ## iterate a String
# ### `for letter in sentence:`

# In[9]:


# [ ] Get user input for 1 fav_food
# [ ] iterate through letters in fav_food 
#    - print each letter on a new line


fav_food = input("Enter your favourite food: ")

print("\n")
for letter in fav_food:
    print(letter)
    
print("\n", "OK, now I know your favourite food! It's a {}".format(fav_food))



# In[10]:


# [ ] iterate work_tip string concatenate each letter to variable: new_string 
# [ ] concatenate the letter or a "-" instead of a space " "
# tip: concatenate string example: word = word + "a"
work_tip = "Good code is commented code"

new_string = ""

# Task 1
for letter in work_tip:
    new_string += letter

print(new_string)


# In[ ]:


# [ ] Print the first 4 letters of name on new line

name = "Hiroto"
print("\n", name[:4])
In [ ]:


# In[1]:




# [ ] Print every other letter from 2nd to last letter of name 
name = "Hiroto"
print(name[1:])


# #  
# <font> <b>Task 4</b></font>
# 
# ## Program: Mystery Name
# - get user input for first_name
# - create an empty string variable: new_name
# - iterate through letters in first_name Backwards 
#   - add each letter to new_name as you iterate
#   - Replace the letter if "e", "t" or "a" with "?" *(hint: if, elif, elif, else)*
# - print new_name  
# 
# **example: "Alton" = "no?l?"**

# In[2]:


# [ ] Create Mystery Name

first_name = input("Enter your First Name: ")
# print('Fine, your First Name is \"{}\"'.format(first_name))
print("Nice to meet you {}".format(first_name))


# #  
# <font> <b>Task 4</b></font>
# ## `len(), .find(), .count()`   
# 
# ```  
# - len(working_string)
# - .find("i")
# - .find("i",start)
# - .find("i", start, end)
# - .count("i")
# - .count("i", start)
# - .count("i", start, end)
# ```   

# In[3]:


# [ ] find and display the length of the string: topic
topic = "len() returns the length of a string"

print(len(topic))


# In[4]:


# [ ] use len() to find and display the mid_pt (middle) index (+/- 1) of the string: topic
# note: index values are whole numbers
topic = "len() can take a sequence, like a string, as an argument"

length = len(topic)
print(length)

if length%2 == 0:
    mid_pt = int(length / 2)
else:
    mid_pt = int(length/2 + 1)

print(mid_pt)


# In[5]:


# [ ] print index where first instance of the word  "code" starts using .find()
work_tip = "Good code is commented code"

work_tip = "Good code is commented code"
print(work_tip.find("code"))


# In[6]:


# [ ] search for "code" in code_tip using .find() 
# [ ] search substring with substring index start= 13,end = last char 
# [ ] save result in variable: code_index
# [ ] display index of where "code" is found, or print "not found" if code_index == -1
work_tip = "Good code is commented code"

print("First occurrence at index {}".format(work_tip.find("code")))
print("Another string has been found at index {}".format(work_tip.find("code",13)))
code_index = work_tip.find("code",13)

if code_index == -1:
    print("not found")
else:
    print(code_index)


# #  
# <font> <b>Task 5</b></font>

# In[7]:


# [ ] find and report (print) number of w's, o's + use of word "code"
work_tip = "Good code is commented code"

w_count = 0    # number of w's
o_count = 0    # number of o's
word_count = 0 # number of word occurrencies
word_index = 0 # current word position

for letter in work_tip:
    if letter == "w":
        w_count += 1
    elif letter == "o":
        o_count += 1

start_index = 0


while word_index >= 0 and word_index <= len(work_tip):
    word_index = work_tip.find("code", start_index)
       
    if word_index != -1:
        word_count += 1
    start_index = word_index + 1
    
print('"w" found: {}'.format(w_count))
print('"o" found: {}'.format(o_count))
print('A word "code" has been found {} times'.format(word_count))
        


# In[8]:


# [ ]  count times letter "i" appears in code_tip string
# [ ] find and display the index of all the letter i's in code_tip
# Remember: if .find("i") has No Match, -1 is returned
code_tip = "code a conditional decision like you would say it"
print ("code_tip:" , code_tip)

letter_count = 0
letter_index = 0

"""
for letter in code_tip:
    if letter == "i":
        letter_count += 1
"""     

while letter_index >= 0 and letter_index <= len(code_tip):
    letter_index = code_tip.find("i", start_index)
    
    if letter_index != -1:
        letter_count += 1
        print('Letter "i" found at index: {}'.format(letter_index))
    start_index = letter_index + 1

print("\n", 'Total letters "i" found: {}'.format(letter_count))


# #  
# <font> <b>Task 6</b></font>
# 
# ## Program: Words after "G"/"g"
# Create a program inputs a phrase (like a famous quotation) and prints all of the words that start with h-z
# 
# Sample input:  
# `enter a 1 sentence quote, non-alpha separate words:` **`Wheresoever you go, go with all your heart`**  
# 
# Sample output:
# ```
# WHERESOEVER
# YOU
# WITH
# YOUR
# HEART
# ```
# - split the words by building a placeholder variable: **`word`**  
#   - loop each character in the input string  
#   - check if character is a letter  
#   - add a letter to **`word`** each loop until a non-alpha char is encountered  
# 
# - **if** character is alpha 
#   - add character to **`word`**    
#   - non-alpha detected (space, punctuation, digit,...) defines the end of a word and goes to **`else`**    
# - **`else`**  
#   - check **`if`** word is greater than "g" alphabetically
#       - print word 
#       - set word = empty string
#   - or **else** 
#     - set word = empty string and build the next word  
# 
# Hint: use `.lower()`

# In[10]:


# [] create words after "G"
# sample quote "Wheresoever you go, go with all your heart" ~ Confucius (551 BC - 479 BC)
quote = input("Enter your sentence: ") + " "

word = ""
for character in quote:
    if character.isalpha():
        word += character.capitalize()
    else:
        if word != "":
            if word[0].lower() >= "h":
                print(word)
                word = ""
            else:
                word = ""


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977)   [Privacy &amp; cookies](https://go.microsoft.com/fwlink/?LinkId=521839)   © 2017 Microsoft
