cp = 1000
sp = 1200
if sp > cp:
    profit = sp - cp
    print("Profit =", profit)
elif cp > sp:
    loss = cp - sp
    print("Loss =", loss)
else:
    print("No Profit No Loss")
