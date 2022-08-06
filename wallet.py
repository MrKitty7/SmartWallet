import os
import sqlite3

print('---------------')
print('Smart Wallet')
print('Make your purchases smarter')
print('---------------')


print('1. List all Purchases')
print('2. Add a new Purchase')
print('3. Check your current balance')
print('4. Edit your current balance')
print('5. List Currencies')
print('6. Edit Currencies')

def list_purchases():
    pass

def add_purchase():
    pass

def check_balance():
    pass

def edit_balance():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    print('---------------')

    current_bal_hrk = cursor.execute('SELECT hrk FROM balance').fetchone()[0]
    current_bal_eur = cursor.execute('SELECT eur FROM balance').fetchone()[0]
    current_bal_usd = cursor.execute('SELECT usd FROM balance').fetchone()[0]
    current_bal_gbp = cursor.execute('SELECT gbp FROM balance').fetchone()[0]
    
    print('Your current balance is: ')
    print(f'HRK: {current_bal_hrk}')
    print(f'EUR: {current_bal_eur}')
    print(f'USD: {current_bal_usd}')
    print(f'GBP: {current_bal_gbp}')
    
    print('---------------')
    new_raw_bal = int(input('Enter your new balance. '))
    new_raw_bal_cur = input('Enter the currency your balance is in. ')

    currencies = ['HRK', 'EUR', 'USD', 'GBP']

    for currency in currencies:
        if currency.lower() == new_raw_bal_cur.lower():
            current_currency = currency
            currencies.remove(currency)

    hrk = cursor.execute('SELECT hrk FROM currencies').fetchone()[0]
    eur = cursor.execute('SELECT eur FROM currencies').fetchone()[0]
    usd = cursor.execute('SELECT usd FROM currencies').fetchone()[0]
    gbp = cursor.execute('SELECT gbp FROM currencies').fetchone()[0]



    for currency in currencies:
        pass


    connection.commit()
    connection.close()
    
def list_currencies():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    hrk = cursor.execute('SELECT hrk FROM currencies').fetchone()[0]
    eur = cursor.execute('SELECT eur FROM currencies').fetchone()[0]
    usd = cursor.execute('SELECT usd FROM currencies').fetchone()[0]
    gbp = cursor.execute('SELECT gbp FROM currencies').fetchone()[0]

    print(f'HRK: {hrk}, EUR: {eur}, USD: {usd}, GBP: {gbp}')

def edit_currencies():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    print('---------------')
    print(cursor.execute('SELECT hrk, eur, usd, gbp FROM currencies').fetchall())

    new_hrk = float(input('Enter the new value for HRK: '))
    new_eur = float(input('Enter the new value for EUR: '))
    new_usd = float(input('Enter the new value for USD: '))
    new_gbp = float(input('Enter the new value for GBP: '))

    new_currencies = [
        (new_hrk),
        (new_eur),
        (new_usd),
        (new_gbp)] 

    cursor.execute('INSERT INTO currencies VALUES (?,?,?,?)', new_currencies)

    print(cursor.execute('SELECT hrk, eur, usd, gbp FROM currencies').fetchall())

    connection.commit()

    connection.close()
choice = int(input())

if choice == 1:
    list_purchases()

if choice == 2:
    add_purchase()

if choice == 3:
    check_balance()

if choice == 4:
    edit_balance()

if choice == 5:
    list_currencies()

if choice == 6:
    edit_currencies()
