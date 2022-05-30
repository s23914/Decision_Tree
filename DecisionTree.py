

class CreateTree():
    def __init__(self,Data):
        self.DecisionTrees=self.DecisionTrees(Data)

    def DecisionTrees(self,Data):
        Hashmap=self.CreatHashMap(Data)
        Columnindex=-1
        j=0
        print(Hashmap)
        for attributelist in Data.listofAttributes:
            Columnindex+=1
            for attribute in attributelist:
                for determinant in Data.Determinants:
                    Tmp={determinant:self.CalculateDeterminantApperance(Columnindex,attribute,determinant,Data)}
                    for Header in Hashmap:
                        for AttributeList in Hashmap[Header]:
                            # print(AttributeList)
                            for value in AttributeList:
                                if AttributeList[value] == determinant:
                                    value.update(Tmp)
                                    print("Updated")

        print(Hashmap)


                
            


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
        YesHash={"Yes":0}
        NoHash={"No":0}
        YesNoList=[]
        YesNoList.append(YesHash)
        YesNoList.append(NoHash)
        for i in range(0,len(Data.Headers)-1): 
            TMPList=[]
            TMPHASH={}
            for Attribute in Data.listofAttributes[i]:
                tmp={Attribute:YesNoList}
                TMPList.append(tmp)
            TMPHASH={Data.Headers[i]:TMPList}
            HeaderHashMap.update(TMPHASH)
        return HeaderHashMap

