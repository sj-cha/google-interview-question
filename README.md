# google-interview-question
I don't exactly know where I've seen it, but there was a puzzle that supposedly came from an interview at Google. It goes like this: 


```
In a country in which people only want boys, every family continues to have children until they get a boy. 

If they get a girl, they will have another child. If they get their first boy, they will stop. 

What is the proportion of boys to girls in the country?
```

I mean let's not even talk about the proportion. Are there more girls or boys? Just one boy will stop them from having another kid, so it's easy to conclude that there will be more girls than boys in this country.

But is your intuition right, though? Let's simulate this using Python.

# Method
```python
t = int(input("Number of trials : "))
valdata = []
ratiodata = []

for a in range(0, t):
    b = 0 
    g = 0
    for i in range(0,100):
        initial = g
        n = random.random()
        if n < 0.50: 
            b += 1
        while n >= 0.50:
            g += 1
            n = random.random()
            if n < 0.50:
                b += 1
                val = g-initial
                valdata.append(val)
    ratiodata.append(g/b)
```

Let's have 100 couples in each trial. They will make babies according to their preference for boy.

Also, let's assume that probability of having a boy or girl is 50%. 

You can choose how many times you want to repeat this baby-making process. I'm going to put 1000. 

# Result
Let's plot the girl to boy ratio for each trial using histogram. 

![histogram 1](https://raw.githubusercontent.com/sj-cha/google-interview-question/main/histogram%201.png)

The result is normally distributed with the mean of 1.00. This means the number of boys and girls are roughly the same regardless of their preference for boy, because the probability of getting a boy or girl is 50% no matter what.

Let's put it this way. If you start with 200 couples, there will be 100 boys and 100 girls after the first birth. Those 100 couples with a girl will have another child, giving birth to 50 boys and 50 girls. There will be equal number of boys and girls after every round of bith, and so on. 

![histogram 2](https://raw.githubusercontent.com/sj-cha/google-interview-question/main/histogram%202.png)

This plot shows a number of daughter before they get their first son. It is explicit that the graph follows the trend `y = (1/2)^x`.

Apparently, some couples had 18 girls before having their first boy. That's 1 in 262144. What a luck.  





