A=2
A=[2,14,7]
import copy
print(A)
print(A)
A=[2,14,7]
B=A B=A
print(A)
print(B)
print(B)
B=copy.copy(A)
A=5 A[0]=5
print(B)
print(B)
print(B)
A[0]=5
print("===")
print("===")
print(B)
