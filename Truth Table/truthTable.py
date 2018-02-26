
testList = [(1, 0, 1, 1), (1, 1, 1, 1)]

def convertToSOP(tableData):
   pass

def convertFromSOP(listOfTubles):
   for tup in listOfTubles:
       for value in tup:
           if value[0] == "!":
               newTuple.ap

def generateTableData(listOfTubles):
   tableData = []
   if listOfTubles[0][0] == str:
      listOfTubles = convertFromSOP(listOfTubles)
   for i in range(2**(len(listOfTubles[0]))):
      tableData.append(format(i, '0%db' % len(listOfTubles[0])))
      tableData[i] += '0'
   for tup in listOfTubles:
      binary = ''
      for i in tup:
         binary += str(i)
      ind = int(binary, 2)
      tableData[ind] = tableData[ind][:-1]
      tableData[ind] += '1'
   return tableData

def printTable(tableData):
   # Header
   letters = ['A', 'B', 'C', 'D', 'E', 'F']
   count = 0
   for data in range(len(tableData[0])-1):
      print('%4s' % letters[count], end='')
      count+=1
   print(" |OUT")
   print(" " + "----"*(len(tableData[0])))

   # Body
   for entry in tableData:
      for data in entry[:len(entry)-1]:
         print('%4s' % data, end='')
      print(" |", entry[-1])

printTable(generateTableData(testList))
