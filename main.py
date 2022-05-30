from FileManager import ReadAndParse 
from DecisionTree import CreateTree
class main():

                   
         
    Path=('OutdoorGame')
    Data=ReadAndParse(Path)
    print(Data.Headers)
    print(Data.Parsed)
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
    for value in Data.Determinants:
    
        print(value,end=" | ")

    Result = CreateTree(Data)