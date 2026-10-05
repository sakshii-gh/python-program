# python-program
Q1:hello world..by your name?
ANS:print("Hello Sakshi")

Q2:create 2 variables cost_price,selling_price and calculate the profit or loss?
ANS:cp = 1000
    sp = 1200
    if sp > cp:
      profit = sp - cp
      print("Profit =", profit)
    elif cp > sp:
      loss = cp - sp
      print("Loss =", loss)
    else:
      print("No Profit No Loss")  

Q3:write a program to check whether a number is odd or even?
ANS:num = 10
   if num % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

Q4:write a program to check whether the age is valid and eligible for voting or not?
ANS:    age = 20
        if age >= 18:
          print("Age is valid and eligible for voting")
        else:
          print("Age is valid but not eligible for voting")


Q5:write a program to check whether word 1 and word2 is anagram or not?
ANS:word1 = "listen"
    word2 = "silent"
    if sorted(word1) == sorted(word2):
        print("Words are Anagrams")
    else:
        print("Words are Not Anagrams")
