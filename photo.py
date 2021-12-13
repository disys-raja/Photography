photos={"candit":10,"downloaded":25,"instaimages":1,"screenshots":100}
photos["nature"]=10
photos["monuments"]=17
photos["animals"]=57       
photos["tourist"]=98
photos["bloom camera"]=14
print(photos)
if isinstance(photos,dict)==True:
    print("entry is correct")
else :
    raise TypeError("entered datatype is wrong")
for i in photos.items():
    print(i)
