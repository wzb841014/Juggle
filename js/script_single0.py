# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



#%%

#%%
def pv_f(c,r,n):
    pv = 0
    for i in range(1,n+1):
        pv=pv + c/(1+r)**i
    return pv

def fv_f(c,r,n):
    fv = 0
    for i in range(n):
        fv=fv + c*(1+r)**i
    return fv


def fv_inc_f(c,r,g,n):
    fv = 0
    for i in range(n):
        fv = fv + c*(1+r)**(n-i)*(1+g)**i
    return fv


def fv_current_assets(profit_rate, age,retire_age,cash, financial_assets, properties, annual_income, increase_rate_income):
    if age <= 45:
        increase_year = 45 - age
        fv_income = fv_inc_f(annual_income, profit_rate, increase_rate_income, increase_year) * (1 + profit_rate)**(retire_age - 45) + fv_f(annual_income*(1+increase_rate_income)**increase_year,profit_rate,retire_age-45)
    if age > 45:
        fv_income = fv_f(annual_income,profit_rate,retire_age-age)
    return financial_assets*(1+profit_rate)**(retire_age - age)+ fv_income

def fv_liabilities(profit_rate, age, retire_age, annual_expense, dream_age_1, dream_expense_1, dream_age_2, dream_expense_2, dream_age_3, dream_expense_3,borrow_rate, liabilities):
    pv_expense = fv_f(annual_expense, profit_rate, retire_age - age) + pv_f(annual_expense, profit_rate, 100 - retire_age)
    if dream_age_1 >= retire_age:
        pv_dream_1 = dream_expense_1/(1 + profit_rate)**(dream_age_1 - retire_age)
    else:
        pv_dream_1 = dream_expense_1 * (1 + profit_rate)**(retire_age - dream_age_1)
    if dream_age_2 >= retire_age:
        pv_dream_2 = dream_expense_2/(1 + profit_rate)**(dream_age_2 - retire_age)
    else:
        pv_dream_2 = dream_expense_2 * (1 + profit_rate)**(retire_age - dream_age_2)
    if dream_age_3 >= retire_age:
        pv_dream_3 = dream_expense_3/(1 + profit_rate)**(dream_age_3 - retire_age)
    else:
        pv_dream_3 = dream_expense_3 * (1 + profit_rate)**(retire_age - dream_age_3)
    return pv_expense + pv_dream_1 + pv_dream_2 + pv_dream_3 + liabilities * (1 + borrow_rate)**(retire_age - age)


def func(i):
    return fv_current_assets(i, age,retire_age,cash, financial_assets, properties, annual_income, increase_rate_income) - fv_liabilities(i, age, retire_age, annual_expense, dream_age_1, dream_expense_1, dream_age_2, dream_expense_2, dream_age_3, dream_expense_3, borrow_rate, liabilities)

def to_result():
    return fsolve(func,0)

def fsolve(func, a):
    delta = 0.00001
    while(abs(func(a)) >= 100):
        y = func(a + delta) - func(a)
        if y > 0:
            if func(a) > 0:
                a = a - delta
            else:
                a = a + delta
        else:
            if func(a) > 0:
                a = a + delta
            else:
                a = a - delta
        if abs(func(a)) <= 10000:
            delta = 0.0000001
        print(func(a))
    return a


def print_out():
    cash = document.getElementById("cash").value
    financial_assets = document.getElementById("financial_assets").value
    properties = document.getElementById("property").value
    annual_income = document.getElementById("annual_income").value
    increase_rate_income =   document.getElementById("increase_rate_income").value
    age = document.getElementById("age").value
    retire_age = document.getElementById("retire_age").value
    annual_expense = document.getElementById("annual_expense").value
    dream_age_1 = document.getElementById("dream_age_1").value
    dream_expense_1 = document.getElementById("dream_expense_1").value
    dream_age_2 = document.getElementById("dream_age_2").value
    dream_expense_2 = document.getElementById("dream_expense_2").value
    dream_age_3 = document.getElementById("dream_age_3").value
    dream_expense_3 = document.getElementById("dream_expense_3").value
    liabilities = document.getElementById("liability").value
    borrow_rate = document.getElementById("borrow_rate").value
    message = "<h2>Return is " + to_result() + "!</h2>";
    document.getElementById("content").innerHTML = message;      
    


