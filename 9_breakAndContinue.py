# THEORY

# break -> loop ko chodkar nikal jao
# continue -> iteration ko chodkar nikal jao

for i in range(10):
    print("12 * ",i+1," = ",12*(i+1))

    if(i==5):
        break
        
print("loop ko chodkar nikal gya😁")

print("\n\n")

for i in range(10):
    if(i==7):
        print("skip the",i,"th iteration😁")
        continue
    print("12 * ",i+1," = ",12*(i+1))

