#!/usr/bin/env python
# coding: utf-8

# In[1]:


def primeRangeSum(num1, num2):
    total = 0
    if num2>num1:
        for i in range(num1, num2+1):
            if isprime(i):
                total = total + i
        return total
    else:
        for i in range(num2, num1+1):
            if isprime(i):
                total = total + i
        return total
def isprime(num):
    temp = 0
    if num == 1:
        return True
    else:
        for i in range(2, num):
            if num % i == 0: #yes
                temp += 1
        if temp > 0:
            return False
        else:
            return True
print(primeRangeSum(10, 20))
print(primeRangeSum(20, 10))
print(primeRangeSum(20, 29))
print(primeRangeSum(50, 41))


# In[2]:


def is_prime(n):
    #Anything that is less than 2 is not prime
    #A prime num is a num that is only divisible by itself
    
    if n < 2:
        return False
    # check each number from 2 to n to see if any number is divisible by n
    
    for i in range(2, n):
        #check to see if n % i == 0
        #one example 15 -> False
        
        if n % i == 0:
            return False
    # Num is prime
    return True


# In[3]:


print(is_prime(2))
print(is_prime(4))
print(is_prime(101))
print(is_prime(-1))


# In[10]:


def prime_range_sum(num1, num2):
    # result variable to store additions of prime numbers
    result = 0
    
    # check to see if num1 is less than num2
    if num1 > num2:
        temp = num2
        num2 = num1
        
        num1 = temp
    
    # loop from num1 to num2 (inclusive) and check each number to see if prime
    # if prime, then I want to add the number to my result
    for i in range(num1, (num2 + 1)):
        # pass in i into my is_prime function
            if (is_prime(i)):
                result += i
    
    return result


# In[12]:


print(prime_range_sum(10,20))
print(prime_range_sum(50,41))


# In[ ]:




