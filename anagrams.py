#wapp to check if 2 strings are anagrams

def my_sort(s):
	return "".join(sorted(s))

s1=input("enter string 1: ")
s2=input("enter string 2: ")
if my_sort(s1)==my_sort(s2):
	print("input strings are anagrams")
else:
	print("strings are not anagrams")