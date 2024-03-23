while True:
    boys_and_girls = int(input("Answer: "))
    if boys_and_girls > 14 and boys_and_girls < 115:
        break
answer = boys_and_girls - 15
girls = int(answer % 10)
boys = int((answer - girls) / 10)
if (boys == 1 and girls != 1):
    print(f"You have 1 boy and {girls} girls")
elif (girls == 1 and boys != 1):
    print(f"You have {boys} boys and 1 girl")
elif (girls == 1 and boys == 1):
    print("You have 1 boy and 1 girl")
else:
    print(f"You have {boys} boys and {girls} girls")
