l = [65, 756, 24, 455, 3]
# print(25 / 0)
# l[4] += l[1]
print(25 / 0)
print(f"NameError - {type(NameError)} - {issubclass(NameError, BaseException)}")
try:
    print(25 / 0)
except ZeroDivisionError:
    print("ZeroDivisionError")
except NameError:
    print("NameError")
