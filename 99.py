print("九九乘法表")
for i in range(1, 10):
    for j in range(1, i+1):
        add_sum = i*j
        print(f"{i}x{j}={add_sum} \t", end='')
    print()

# row = 1
# while row <= 9:
#     col = 1
#     while col <= row:
#         print("%d * %d =" % (col,row),(col * row),end="\t")
#         col += 1
#     print()
#     row += 1

