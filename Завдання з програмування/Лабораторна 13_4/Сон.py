hours_of_sleep = int(input("Скільки годин Ви сьогодні спали вчора?"))
ate_food = input("Ви їли що-небуть  після сну? (так/ні)")
if hours_of_sleep < 8:
    print("Ви ще досить сонні.")
elif hours_of_sleep > 8 and ate_food == "ні":
    print("Ви голодні.")
elif hours_of_sleep > 8 and ate_food == "так":
    print("Ви щасливі.")
else:
    print("Введіть конкретну інформцію")
    
