Currency = ["Dollar", "Euro", "Pound","Turkish Lira", "Yuan"] # Currency list
ValueToRub = [80.70, 94.16, 108.86, 1.97, 11.26] #Value to Rubble
RubleValue = float(input("Введите сумму :")) # Input Rubble value
RubleToCurrency = input("Введите валюту :") #Input Name of Currency
index = Currency.index(RubleToCurrency)
rate = ValueToRub[index]
if RubleToCurrency in Currency: # Check by list of currencies
    print(rate * RubleValue)

#In this small program im working with *lists, *Inputs, *Functions, *and Index method
#I absolutely understand that this program can be made simpler using dictionaries.
#But specifically here I wanted to work with lists, so don't judge strictly :)