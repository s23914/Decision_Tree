
class ReadAndParse():
        

    
    def __init__(self,PATH):
        File_ = open(PATH)
        self.Headers=self.CutHeaders(File_.readline())
        self.Parsed=self.Parse(File_)
        self.listofAttributes=self.GetAttributes()
        self.Determinants=self.GetDeterminants()
        File_.close()

    def CutHeaders(self,line):
        Headers = []
        
        for header in line.split(','):
            Headers.append(header)
        return Headers




    def Parse(self,File):   
        Rows=File.readlines()
        print(Rows)
        Parsedlist=[]
        for line in Rows:
            SplittedLine=line.split(',')
            RowList=[]
            for value in SplittedLine:
                value=value.strip()
                RowList.append(value)
            Parsedlist.append(RowList)
        return Parsedlist


    def GetAttributes(self):
        TMPlist=[]
        for i in range(len(self.Parsed[0])-1):
            Attributes=[]
            for j in range(0,len(self.Parsed)):
                    Attributes.append(self.Parsed[j][i])
                    
            
            j=0
            AttributesSet=set(Attributes)
            TMPlist.append(AttributesSet)
        return TMPlist

    def GetDeterminants(self):
        TMPlist=[]
        for j in range(0,len(self.Parsed)):
                    TMPlist.append(self.Parsed[j][len(self.Parsed[0])-1])
        DeterminantSet=set(TMPlist)
        return DeterminantSet