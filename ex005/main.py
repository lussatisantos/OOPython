class A:
    vc = 123

a1 = A()
a2 = A()

a1.vc =321

print(a1.vc)
print(a2.vc)
print(A.vc)