
# coding: utf-8

# # Hello World!

# ## This is my first Notebook in Python

# Notebook documents (or “notebooks”) are documents which contains both, computer code (e.g. Python code) and rich text elements (paragraph, images, equations, figures, links, etc...). Notebook documents are both human-readable documents containing the analysis description and the results (figures, tables, etc..) as well as executable documents which can be run to perform data analysis.

# In this Paragraph we are going to use an image. The Markdown for enter an image is **\!\[ \]( )** So let's use it to show an image: 
# ![IBM LOGO](https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/IBM_logo.svg/250px-IBM_logo.svg.png)
# 

# In this URL you can find a good **Markdown Cheatsheet**: https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet

# Ok, previous cells are just *Markdown cells*. 

# The next cell is a *code cell*. And I'm going to use it as a calculator:

# In[21]:

(323 * 234) + (1423 / 3)


# Now I'm going to use the **print** & **if/else** functions from Pyhton:

# In[22]:

# Hi! I'm am a comment on the code. 
# If you write '#' and text, this text will be interpreted as a comment

# First we define the 'age' variable
age = 29

# Now we are going to use if/else functions 
# to evaluate if the 'age' variable is greater than 18
if age > 18:
    print 'Congratulations! You can drive a car in Spain.'
else:
    print 'You can not drive a car in Spain :('


# ![Fibonacci](https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Fibonacci2.jpg/150px-Fibonacci2.jpg)
# ![Fib](https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Fibonacci_spiral_34.svg/280px-Fibonacci_spiral_34.svg.png)
# Ok, let's do something more complex. We can calculate the Fibonacci numbers. In the Fibonacci sequence of numbers, each number is the sum of the previous two numbers. We will use a loop (**while** function) and create a custom function for that called **fib()**. How to do it?

# In[55]:

def fib(n):
    a, b = 0,1
    while a < n:
        print a
        a, b = b, a+b
    print
    
# Call to the fib() function with a number    
fib(100)


# ## Now we are going to do something more cool. A graph.

# In[12]:

# First we must import a graph library called matplotlib
get_ipython().magic(u'matplotlib inline')
import pylab as plt
import seaborn


# In[13]:

# Now we give some set the figure size
plt.rc('figure', figsize=(10, 5))


# In[20]:

# Generating some ramdom values using the normal distribution and standard deviation
samples_1 = np.random.normal(loc=1, scale=.5, size=10000)
samples_2 = np.random.standard_t(df=10, size=10000)
bins = np.linspace(-4, 4, 60)

# Set an alpha and use the same bins since we are plotting two hists
plt.hist(samples_1, bins=bins, alpha=0.5, label='Samples 1 - Normal')
plt.hist(samples_2, bins=bins, alpha=0.5, label='Samples 2 - Standard')
plt.legend(loc='upper left');
plt.show()


