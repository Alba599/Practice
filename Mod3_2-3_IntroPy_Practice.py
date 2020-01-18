#!/usr/bin/env python
# coding: utf-8

# # 2-3 Intro Python Practice  
# ## power iteration of sequences
# 
# <font> <b>Student will be able to</b></font>  
# - Iterate through Lists using **`for`** and **`in`**
# - Use **`for` *`count`* `in range()`** in looping operations  
# - Use list methods **`.extend()`, `+, .reverse(), .sort()`**  
# - convert between lists and strings using  **`.split()`** and **`.join()`**
# - cast strings to lists **/** direct multiple print outputs to a single line.  ** `print("hi", end='')`**

# #  
# <font> <b>Task 1</b></font>
# ##  list iteration: `for in`
# ### `for item in list:`

# In[6]:


# [ ] print out the "physical states of matter" (matter_states) in 4 sentences using list iteration
# each sentence should be of the format: "Solid - is state of matter #1" 
matter_states = ['solid', 'liquid', 'gas', 'plasma']

for words in range(len(matter_states)):
    print(matter_states[words], "- is state of matter #" + str(words + 1))



# In[ ]:


7+7


# In[8]:


# [ ] iterate the list (birds) to see any bird names start with "c" and remove that item from the list
# print the birds list before and after removals
birds = ["turkey", "hawk", "chicken", "dove", "crow"]

for words in birds:
    if words[0] == "c":
        birds.remove(words)

print(birds)


# In[10]:


# the team makes 1pt, 2pt or 3pt baskets
# [ ] print the occurace of each type of basket(1pt, 2pt, 3pt) & total points using the list baskets
baskets = [2,2,2,1,2,1,3,3,1,2,2,2,2,1,3]

scores = range(1,4)
for score in scores:
    print(str(score) + "'s:", baskets.count(score))

total = 0
for score in baskets:
    total += score
print("total:", total)


# #  
# <font> <b>Task 2</b></font>
# ##  iteration with `range(start)` &amp; `range(start,stop)`
# 

# In[11]:


# [ ] using range() print "hello" 4 times

for word in range(0, 4):
    print("hello")
hello


# In[14]:


# [ ] find spell_list length
# [ ] use range() to iterate each half of spell_list  
# [ ] label & print the first and second halves
spell_list = ["Tuesday", "Wednesday", "February", "November", "Annual", "Calendar", "Solstice"]

length = len(spell_list)
half = int(length / 2)
print("first")
for word in range(0, half):
    print(spell_list[word])
print("second")
for word in range(half, l):
    print(spell_list[word])


# In[13]:


# [ ] build a list of numbers from 20 to 29: twenties 
# append each number to twenties list using range(start,stop) iteration
# [ ] print twenties
twenties = []

for num in range(20, 30):
    twenties.append(num)
print(twenties)


# In[15]:


# [ ] iterate through the numbers populated in the list twenties and add each number to a variable: total
# [ ] print total
total = 0

for num in twenties:
    total += num
print(total)


# In[16]:


# check your answer above using range(start,stop)
# [ ] iterate each number from 20 to 29 using range()
# [ ] add each number to a variable (total) to calculate the sum
# should match earlier task 
total = 0

for num in range(20, 30):
    total += num
print(total)


# #  
# <font> <b>Task 3</b></font>
# ##  iteration with `range(start:stop:skip)`
# 

# In[17]:


# [ ] create a list of odd numbers (odd_nums) from 1 to 25 using range(start,stop,skip)
# [ ] print odd_nums
# hint: odd numbers are 2 digits apart
odd_nums = []
for num in range(1, 26, 2):
    odd_nums.append(num)
    
print(odd_nums)


# In[18]:


# [ ] create a Decending list of odd numbers (odd_nums) from 25 to 1 using range(start,stop,skip)
# [ ] print odd_nums,  output should resemble [25, 23, ...]

for num in range(25, 0 ,-1):
    odd_nums.append(num)
print(odd_nums)


# In[22]:


# the list, elements, contains the names of the first 20 elements in atomic number order
# [ ] print the even number elements "2 - Helium, 4 - Beryllium,.." in the list with the atomic number
elements = ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine',  'Neon', 'Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon',  'Potassium', 'Calcium']

for word in range(1, len(elements)+1, 2):
    print(word +1, "-", elements[word])


# In[24]:


# [ ] the list, elements_40, contains the names of the first 40 elements in atomic number order
# [ ] print the odd number elements "1 - Hydrogen, 3 - Lithium,.." in the list with the atomic number elements_40
elements_40 = ['Hydrogen',  'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine',  'Neon', 'Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine',  'Argon', 'Potassium', 'Calcium', 'Scandium', 'Titanium', 'Vanadium', 'Chromium', 'Manganese',  'Iron', 'Cobalt', 'Nickel', 'Copper', 'Zinc', 'Gallium', 'Germanium', 'Arsenic', 'Selenium',  'Bromine', 'Krypton', 'Rubidium', 'Strontium', 'Yttrium', 'Zirconium']

for word in range(0, len(elements_40), 2):
    print(word + 1, "-", elements_40[word])


# In[ ]:





# #  
# <font> <b>Task 4</b></font>
# ## combine lists with `+` and `.extend()`

# In[25]:


# [ ] print the combined lists (numbers_1 & numbers_2) using "+" operator
numbers_1 = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]

# pythonic casting of a range into a list
numbers_2 = list(range(30,50,2))

print("numbers_1:",numbers_1)
print("numbers_2",numbers_2)

print("combined", numbers_1 + numbers_2)


# In[26]:


# [ ] print the combined element lists (first_row & second_row) using ".extend()" method
first_row = ['Hydrogen', 'Helium']
second_row = ['Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon']

print("1st Row:", first_row)
print("2nd Row:", second_row)

first_row.extend(second_row)
print("combined", first_row)


# ## Project: Combine 3 element rows
# Choose to use **"+" or ".extend()" **to build output similar to   
# 
# ```
# The 1st three rows of the Period Table of Elements contain:
# ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon', 'Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon']
# 
# The row breakdown is
# Row 1: Hydrogen, Helium
# Row 2: Lithium, Beryllium, Boron, Carbon, Nitrogen, Oxygen, Fluorine, Neon
# Row 3: Sodium, Magnesium, Aluminum, Silicon, Phosphorus, Sulfur, Chlorine, Argon
# ```

# In[27]:


# [ ] create the program: combined 3 element rows 

elem_1 = ['Hydrogen', 'Helium'] 
elem_2 = ['Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon']
elem_3 = ['Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon']
print("combined", elem_1 + elem_2 + elem_3)


# In[29]:


# [ ] .extend() jack_jill with "next_line" string - print the result
jack_jill = ['Jack', 'and', 'Jill', 'went', 'up', 'the', 'hill']
next_line = ['To', 'fetch', 'a', 'pail', 'of', 'water']

jack_jill.extend(next_line)
print(jack_jill)


# #  
# <font> <b>Task 5</b></font>
# ## .reverse() : reverse a list in place

# In[30]:


# [ ] use .reverse() to print elements starting with "Calcium", "Chlorine",... in reverse order
elements = ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine',  'Neon', 'Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon',  'Potassium', 'Calcium']

elements.reverse()

print(elements)


# In[31]:


# [ ] reverse order of the list... Then print only words that are 8 characters or longer from the now reversed order
spell_list = ["Tuesday", "Wednesday", "February", "November", "Annual", "Calendar", "Solstice"]


spell_list.reverse()

for spell in spell_list:
    if len(spell) >= 8:
        print(spell)


# #  
# <font> <b>Task 6</b></font>
# ## .sort() and sorted()

# In[32]:


# [ ] sort the list element, so names are in alphabetical order and print elements
elements = ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine',  'Neon', 'Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon',  'Potassium', 'Calcium']
elements.sort()

print(elements)


# In[37]:


# [ ] print the list, numbers, sorted and then below print the original numbers list 
numbers = [2,2,2,1,2,1,3,3,1,2,2,2,2,1,3]

print(sorted(numbers))
print(numbers)


# #  
# <font> <b>Task 7</b></font>
# ## Converting a string to a list with `.split()`

# In[38]:


# [ ] split the string, daily_fact, into a list of word strings: fact_words
# [ ] print each string in fact_words in upper case on its own line
daily_fact = "Did you know that there are 1.4 billion students in the world?"

fact_words = daily_fact.split()

for word in fact_words:
    print(word.upper())


# In[39]:


# [ ] convert the string, code_tip, into a list made from splitting on the letter "o"


code_tip = "Python uses spaces for indentation"
no_o_code_tip = code_tip.split('o')

print(no_o_code_tip)


# In[40]:


# [ ] split poem on "b" to create a list: poem_words
# [ ] print poem_words by iterating the list
poem = "The bright brain, has bran!"

poem_words = poem.split('b')

for word in poem_words:
    print(word)


# #  
# <font> <b>Task 8</b></font>
# ## `.join()`
# ### build a string from a list

# In[41]:


# [ ] print a comma separated string output from the list of Halogen elements using ".join()"

halogens = ['Chlorine', 'Florine', 'Bromine', 'Iodine']

str_halogens = ', '.join(halogens)
print(str_halogens)


# In[42]:


# [ ] split the sentence, code_tip, into a words list
# [ ] print the joined words in the list with no spaces in-between
# [ ] Bonus: capitalize each word in the list before .join()
code_tip ="Read code aloud or explain the code step by step to a peer"

code_tip_list = code_tip.split()

code_string = ''.join(code_tip_list)

print(code_string)


# #  
# <font> <b>Task 9</b></font>  
# ## `list(string)` &amp; `print("hello",end=' ')`
# 
# - **Cast a string to a list** 
# - **print to the same line**   

# In[43]:


# [ ] cast the long_word into individual letters list 
# [ ] print each letter on a line
long_word = 'decelerating'

word_list = list(long_word)
for letter in word_list:
    print(letter)


# In[44]:


# [ ] use use end= in print to output each string in questions with a "?" and on new lines
questions = ["What's the closest planet to the Sun", "How deep do Dolphins swim", "What time is it"]


for quest in questions:
    print(quest, end = '?\n')


# In[45]:


# [ ] print each item in foot bones 
#    - capitalized, both words if two word name
#    - separated by a comma and space
#    - and keeping on a single print line
foot_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform", 
            "intermediate cuneiform", "medial cuneiform"]

for bones in foot_bones:
    print(bones.title(), end=', ')


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977)   [Privacy &amp; cookies](https://go.microsoft.com/fwlink/?LinkId=521839)   © 2017 Microsoft
