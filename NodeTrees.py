

class CreateTree():
    def __init__(self,Data):
        self.NodeTrees=self.NodeTrees(Data)

    def NodeTrees(self,Data):
        Hashmap=self.CreatHashMap(Data)
        Columnindex=-1

        for Header in Hashmap:
            Columnindex+=1
            print(Header)
            for AttributeList in Hashmap[Header]:
                print(AttributeList)
                for Attribute in AttributeList:
                    print(Attribute)
                    for value in AttributeList[Attribute]:
                        print(value)
                        for determinant in Data.Determinants:    
                            print(determinant)
                            if value == determinant :
                                Tmp={determinant:self.CalculateDeterminantApperance(Columnindex,Attribute,determinant,Data)}
                                print(AttributeList)
                                AttributeList.update(Tmp)
                                print(Hashmap[Header])
                                print("Updated")
                                print(Attribute)
                                print(AttributeList[Attribute])
                    print(Hashmap[Header])


        return Hashmap

    def CalculateDeterminantApperance(self,ColumnIndex,Attribute,Determinant,Data):
        Apperance=0
        for i in range(0,len(Data.Parsed)):
                if (Data.Parsed[i][ColumnIndex]==Attribute and Data.Parsed[i][len(Data.Parsed[0])-1]==Determinant):
                    Apperance+=1
    
        Probability=Apperance
        return Apperance 

        





    def CreatHashMap(self,Data):
        i=0 
        j=0
        HeaderHashMap={}
        determinantHashMap={}
        for determinant in Data.Determinants: 
            tmphash={determinant:0}
            determinantHashMap.update(tmphash)
        for i in range(0,len(Data.Headers)-1): 
            TMPList=[]
            TMPHASH={}
            for Attribute in Data.listofAttributes[i]:
                tmp={Attribute:determinantHashMap}
                TMPList.append(tmp)
            TMPHASH={Data.Headers[i]:TMPList}
            HeaderHashMap.update(TMPHASH)
        return HeaderHashMap

