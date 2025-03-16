import unittest
from is_even import is_even

# בדיקת מספרים זוגיים - צריכים להחזיר True
print("Testing even numbers...")
assert is_even(2) == True, "2 should be even"
assert is_even(4) == True, "4 should be even"
assert is_even(100) == True, "100 should be even"
assert is_even(0) == True, "0 should be even"

# בדיקת מספרים אי-זוגיים - צריכים להחזיר False
print("Testing odd numbers...")
assert is_even(1) == False, "1 should be odd"
assert is_even(3) == False, "3 should be odd"
assert is_even(99) == False, "99 should be odd"

# בדיקת מספרים שליליים
print("Testing negative numbers...")
assert is_even(-2) == True, "-2 should be even"
assert is_even(-4) == True, "-4 should be even"
assert is_even(-1) == False, "-1 should be odd"
assert is_even(-3) == False, "-3 should be odd"

print("All tests passed successfully!")