print_B=[[" "for i in range(5)]for j in range(5)]
print_H=[[" "for i in range(5)]for j in range(5)]
print_A=[[" "for i in range(5)]for j in range(5)]
print_R=[[" "for i in range(5)]for j in range(5)]
print_T=[[" "for i in range(5)]for j in range(5)]
# code for B
for i in range(5):
    for j in range(5):
        if(j==0 or i==0 and j!=4 or i==2 and j!=4 or i==4 and j!=4 or i==1 and j==4 or i==3 and j==4 ):
            print_B[i][j]="*"
# code for H
for i in range(5):
    for j in range(5):
        if(j==0 or j==4 or i==2 ):
            print_H[i][j]="*"
# for code A
for i in range(5):
    for j in range(5):
        if(j==0 and i!=0 or j==4 and i!=0 or i==0 and j!=0 and j!=4 or i==2):
            print_A[i][j]="*"
# for code R
for i in range(5):
    for j in range(5):
        if(j==0 or i==0 and j!=3 and j!=4 or i==2 and j!=3 and j!=4 or i==1 and j==3 or i==3 and j==1 or i==4 and j==2):
            print_R[i][j]="*"
# for code T
for i in range(5):
    for j in range(5):
        if(i==0 or j==2):
            print_T[i][j]="*"

for i in range(5):
    for j in range(5):
        print(print_B[i][j],end="")
    print(end="  ")
    for j in range(5):
        print(print_H[i][j],end="")
    print(end="    ")
    for j in range(5):
        print(print_A[i][j],end="")
    print(end="    ")
    for j in range(5):
        print(print_R[i][j],end="")
    print(end="    ")
    for j in range(5):
        print(print_A[i][j], end="")
    print(end="    ")
    for j in range(5):
        print(print_T[i][j], end="")
    print()
