x = input()
a = int(x[0])
b = int(x[1])
c = int(x[2])
d = int(x[3])
a_new = (a + 7) % 10
b_new = (b + 7) % 10
c_new = (c + 7) % 10
d_new = (d + 7) % 10
a_final = c_new
b_final = d_new
c_final = a_new
d_final = b_new
result = a_final * 1000 + b_final * 100 + c_final * 10 + d_final
print(result)