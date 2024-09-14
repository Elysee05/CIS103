def main():...
num = 1
while num <= 10:
    if num == 7:
        break
    if num == 5:
        num += 1
        continue
    print(num)
    num += 1

print()
print()
if __name__=="__main__":
    main()