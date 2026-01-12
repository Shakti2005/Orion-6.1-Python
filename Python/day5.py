# Property of String and It's Inbuilt Methods
# s1 = "Hello Everyone"
# s2 = 'This is first line'
# s3 = '''This is first line
# This is second line'''
# s4 = """This is first line
# This is second line"""
# print(s1)
# print(s2)
# print(s3)
# print(s4)
# print(s1[2])
# print(s1[-2])
# print(s1[2:9])
# print(s1[2:])
# print(s1[:9])
# print(s1[:])
# print(s1[2:9:2])
# print(s2[:-2])
# print(len(s1))

# String Concatenation
# s1 = "Hello"
# s2 = "Everyone"
# print(s1 + " " + s2)

# String Inbuilt Methods
s = 'This is first line'
# s1 = s.lower()
# print(s1)
# print(s.upper())
# print(s.capitalize())
# print(s.title())
# print(s.swapcase())
# print(s.split())
# print(s.split("i"))
# print(s.split("z"))
# s1 = s.split()
# s2 = " ".join(s1)
# print(s1)
# print(s2)
# print(s.replace("is", "a"))
# print(s)
# print(s.strip())
# print(s.lstrip())
# print(s.rstrip())
# print(s.find('i'))
# print(s.rfind('i'))
# print(s.rfind('is'))
# print(s.find('is'))
# print(s.index('z'))
# print(s.count('is'))
# print(s.isalnum())
# print(s.isalpha())
# print(s.isdigit())
# print(s.isdecimal())
# print(s.islower())
# print(s.isupper())
# print(s.isspace())
# print(s.startswith('Thus'))
# print(s.endswith('ee'))

s3 = "Stress"
s4 = "Streß"

print(s3.lower() == s4.lower())
print(s3.casefold() == s4.casefold())