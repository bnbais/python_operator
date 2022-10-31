'''Problem Statement:
Pooja would like to withdraw X $US from an ATM. The cash machine will only accept the transaction 
if X is a multiple of 5, and Pooja's account balance has enough cash to perform 
the withdrawal transaction (including bank charges). For each successful withdrawal the bank charges 0.50 $US.
Calculate Pooja's account balance after an attempted transaction.

Input
Positive integer 0 < X <= 2000 - the amount of cash which Pooja wishes to withdraw.

Nonnegative number 0<= Y <= 2000 with two digits of precision - Pooja's initial account balance.

Output
Output the account balance after the attempted transaction, given as a number with two digits of precision. If there is not enough money in the account to complete the transaction, output the current bank balance.

Example - Successful Transaction
Input:
30 120.00

Output:
89.50
'''
'''withdraw_money,balance_money=map(str,input().split())
withdraw_money=int(withdraw_money)
balance_money=float(balance_money)


if withdraw_money%5==0 and withdraw_money+0.50<=balance_money:
    print(f'{0:.2f}'.format(balance_money-withdraw_money-0.50))
else:
    print(f'{0:.2f}'.format(balance_money))
'''


x,y=input().split()
if int(x)%5==0 and int(x)+0.50<=float(y):
    print(float(float(y)-int(x)-0.50))
else:
    print(float(y))


