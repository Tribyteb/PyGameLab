PlayStatus= True

FPChar=input("1. oyuncuyu temsil etmek için bir karakter giriniz:")
SpChar=input("2. oyuncuyu temsil etmek için bir karakter giriniz:")
Empty =" "
Size = int(input("Please enter the size of the table grid(4-8):"))

Alfabeth=["A","B","C","D","E","F","G","H"]

GameStatus= True
global ActivePlayer, WaitinPlayer


ActivePlayer = FPChar
WaitinPlayer = SpChar
# Başlangıç durumu için kurulum
Row = []
Table = []
for row in range(Size):
    for elem in range(Size):
        if row==0 : Row.append(FPChar)
        elif row==Size-1 :  Row.append(SpChar)
        else: Row.append(Empty)
    Table.append(Row)
    Row=[]

def Plot(Table):
    i=0
    print("    A   B   C   D   E   F   G   H  ")
    print("  ---------------------------------")
    for r in Table:
       print (i,end = " | ")
       for c in r:
          print(c,end = " | ")
       print( i )
       print("  ---------------------------------")
       i=i+1
    print("    A   B   C   D   E   F   G   H  ")

def checkMovementStatus(Table, Movement):
    Status = True
    
    if Table[int(Movement[0])][Alfabeth.index(Movement[1])] != ActivePlayer : 
        print("Oyuncu sadece kendi taşını haraket ettirebilir!!!")
        Status= False
    if Movement[0] != Movement[3] and Movement[1] != Movement[4] : 
        print("Oyun kuralları gereği oyuncu taşını çapraz haraket ettiremez!!!")
        Status=False
    
    # yatayda haraket ediyorsa yolunda engel varmı diye kontrol ediyor.
    if Movement[0]==Movement[3]:
        i=0
        for x in range(Alfabeth.index(Movement[1]),Alfabeth.index(Movement[4])):
            if Table[int(Movement[0])][x] != Empty and i>0 :
             print("Haraket yolu açık değil. Önünde başka taş olduğundan haraket imkansız.")
             Status=False
            i=i+1

    # Düşeyde haraketine engel varmı diye bakıyor.
    if Movement[1]==Movement[4]:
        i=0
        for x in range(int(Movement[0]),int(Movement[3])):
            if Table[x][Alfabeth.index(Movement[1])] != Empty and i>0 :
             print("Haraket yolu açık değil. Önünde başka taş olduğundan haraket imkansız.")
             Status=False
            i=i+1
    return Status

def RunEliminationRules():
    # Ara taşları elemek için kural
    if int(Movement[3])+2 < Size and Table[int(Movement[3])+2][Alfabeth.index(Movement[4])]== ActivePlayer:
        if Table[int(Movement[3])+1][Alfabeth.index(Movement[4])] == WaitinPlayer:
            Table[int(Movement[3])+1][Alfabeth.index(Movement[4])] = Empty
            print(int(Movement[3])+1,Movement[4]," konumundaki taş kilitlendi ve dışarı çıkarıldı.")

    if int(Movement[3])-2 >= 0 and Table[int(Movement[3])-2][Alfabeth.index(Movement[4])]== ActivePlayer:
        if Table[int(Movement[3])-1][Alfabeth.index(Movement[4])] == WaitinPlayer:
            Table[int(Movement[3])-1][Alfabeth.index(Movement[4])] = Empty
            print(int(Movement[3])-1,Movement[4]," konumundaki taş kilitlendi ve dışarı çıkarıldı.")
    
    if Alfabeth.index(Movement[4])+2 < Size and Table[int(Movement[3])][Alfabeth.index(Movement[4])+2]== ActivePlayer:
        if Table[int(Movement[3])][Alfabeth.index(Movement[4])+1] == WaitinPlayer:
            Table[int(Movement[3])][Alfabeth.index(Movement[4])+1] = Empty
            print(int(Movement[3]),Alfabeth[Alfabeth.index(Movement[4])+1]," konumundaki taş kilitlendi ve dışarı çıkarıldı.")

    if Alfabeth.index(Movement[4])-2 >=0 and Table[int(Movement[3])][Alfabeth.index(Movement[4])-2]== ActivePlayer:
        if Table[int(Movement[3])][Alfabeth.index(Movement[4])-1] == WaitinPlayer:
            Table[int(Movement[3])][Alfabeth.index(Movement[4])-1] = Empty
            print(int(Movement[3]),Alfabeth[Alfabeth.index(Movement[4])-1]," konumundaki taş kilitlendi ve dışarı çıkarıldı.")

    # Köşe taşları elemek için kural
    if Table[1][0]== ActivePlayer and Table[0][1]== ActivePlayer:
        if Table[0][0] == WaitinPlayer:
            Table[0][0] = Empty
            print(0,Alfabeth[0]," konumundaki taş kilitlendi ve dışarı çıkarıldı.")

    if Table[1][Size -1]== ActivePlayer and Table[0][Size - 2]== ActivePlayer:
        if Table[0][Size - 1] == WaitinPlayer:
            Table[0][Size - 1] = Empty
            print(0,Alfabeth[Size - 1]," konumundaki taş kilitlendi ve dışarı çıkarıldı.")

    if Table[Size - 2][0]== ActivePlayer and Table[Size - 1][ 1]== ActivePlayer:
        if Table[Size - 1][0] == WaitinPlayer:
            Table[Size - 1][0] = Empty
            print(Size - 1,Alfabeth[0]," konumundaki taş kilitlendi ve dışarı çıkarıldı.")

    if Table[Size - 2 ][Size - 1]== ActivePlayer and Table[Size - 1][Size - 2]== ActivePlayer:
        if Table[Size - 1][Size - 1] == WaitinPlayer:
            Table[Size - 1][Size - 1] = Empty
            print(Size - 1,Alfabeth[Size - 1]," konumundaki taş kilitlendi ve dışarı çıkarıldı.")

def Move(Movement):
    Table[int(Movement[3])][Alfabeth.index(Movement[4])] = Table[int(Movement[0])][Alfabeth.index(Movement[1])]
    Table[int(Movement[0])][Alfabeth.index(Movement[1])] = Empty


while GameStatus: 
        
    Plot(Table)
    
    Movement = input("Oyuncu, "+ ActivePlayer +", lütfen hareket ettirmek istediğiniz kendi taşınızın konumunu ve hedefkonumu giriniz:")
   
    Status=checkMovementStatus(Table, Movement)

    # Eğer haraketin yapılmasına bir engel yoksa Status True oluyor
    if Status == True :
        # Taşı haraket ettiren kod
        Move(Movement)

        RunEliminationRules()

        # Bütün işlemlerden sonra aktif ve bekleyen otuncuyu swich ediyor oyun sırası diğer oyuncuya geçiyor.
        Temporary=ActivePlayer
        ActivePlayer=WaitinPlayer
        WaitinPlayer=Temporary

print("Oyun Bitti")