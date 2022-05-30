from FileManager import ReadAndParse 
from NodeTrees import CreateTree
class main():

                   
         
    Path=('OutdoorGame')
    Data=ReadAndParse(Path)
    print("+============FileMenager==============")
    
    i=1

    for set in Data.listofAttributes:
    
            print()
            print("Attribute",end=" ")
            print(i,end="")
            print(":")

            j=1
            for value in set:
                        print(j,end=".")
                        print(value,end=" ")
                        j+=1
            i+=1

    print("")
    print("Determinants:")
    print()
    for value in Data.Determinants:
    
        print(value,end=" | ")

    Result = CreateTree(Data)
    print (Result.NodeTrees)
        