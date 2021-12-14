from datetime import datetime
dateime_object = datetime.now()
print(dateime_object)


x = dateime_object.strftime("%m-%d-%y %T")
print(x)

x = dateime_object.strftime("%d%h%y%H%M")
print(x)