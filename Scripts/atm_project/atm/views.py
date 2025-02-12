from django.shortcuts import render, redirect
from django.contrib import messages

user_pin = 1234
user_balance = 40000

def login(request):
    return render(request, 'atm/login.html')

def authenticate(request):
    global user_pin
    if request.method == 'POST':
        input_pin = int(request.POST.get('pin'))
        if input_pin == user_pin:
            request.session['authenticated'] = True
            request.session['balance'] = user_balance
            return redirect('main_menu')
        else:
            messages.error(request, 'Authentication Failed. Please try again.')
            return redirect('login')  # Fixed here

def main_menu(request):
    if not request.session.get('authenticated'):
        return redirect('login')  # Fixed here
    return render(request, 'atm/main_menu.html', {
        'balance': request.session.get('balance', user_balance)
    })

def logout_view(request):
    request.session.flush()
    messages.success(request, 'You have been logged out.')
    return redirect('login')  # Fixed here

def withdraw(request):
    global user_balance
    if request.method == 'POST':
        withdraw_amount = int(request.POST.get('amount'))
        if withdraw_amount > user_balance:
            messages.error(request, f'Cannot withdraw Rs. {withdraw_amount}. Please enter a lower amount.')
        else:
            user_balance -= withdraw_amount
            request.session['balance'] = user_balance
            messages.success(request, f'Amount withdrawn: Rs. {withdraw_amount}. Remaining balance: Rs. {user_balance}.')
    return redirect('main_menu')

def deposit(request):
    global user_balance
    if request.method == 'POST':
        deposit_amount = int(request.POST.get('amount'))
        user_balance += deposit_amount
        request.session['balance'] = user_balance
        messages.success(request, f'Amount deposited: Rs. {deposit_amount}. Total balance: Rs. {user_balance}.')
    return redirect('main_menu')

def change_pin(request):
    global user_pin
    if request.method == 'POST':
        new_pin = int(request.POST.get('new_pin'))
        user_pin = new_pin
        messages.success(request, 'PIN changed successfully!')
    return redirect('main_menu')

