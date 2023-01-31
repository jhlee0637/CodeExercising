'''
There are two assembly lines.
Each assemply line has six stations.
Each 12 stations have their own consuming time.
Also, each line has enter and exit belt, which also needs time to pass.
When you pass the one station, you have two options: 1) stay in the same assembly line and go to the next station
                                                     2) cross to another assembly line through the belt and go to the next station of the line
                                                        (when you cross, it needs another additional time)

'''
class AssemblyLines:
   timeStation = [[7, 9, 3, 4, 8, 4],
                  [8, 5, 6, 4, 5, 7]]
   timeBelt = [[2, 2, 3, 1, 3, 4, 3],
               [4, 2, 1, 2, 2, 1, 2]]
   intCount = 0

   def Scheduling(self, idxLine, idxStation):
      print("Calculate scheduling: line, station: ", idxLine, idxStation, "(", self.intCount, "recursion calls )")
      self.intCount = self.intCount + 1

      #escape when it's not for the recursion
      if idxStation == 0: 
         if idxLine == 1:
            return self.timeBelt[0][0] + self.timeStation[0][0]
         elif idxLine == 2:
            return self.timeBelt[1][0] + self.timeStation[1][0]

      #recursion
      if idxLine == 1:  
         costLine1 = self.Scheduling(1, idxStation-1) + self.timeStation[0][idxStation]
         costLine2 = self.Scheduling(2, idxStation-1) + self.timeStation[0][idxStation] + self.timeBelt[1][idxStation]
      if idxLine == 2:
         costLine1 = self.Scheduling(1, idxStation-1) + self.timeStation[1][idxStation] + self.timeBelt[0][idxStation]
         costLine2 = self.Scheduling(2, idxStation-1) + self.timeStation[1][idxStation]

      if costLine1 > costLine2:
         return costLine2
      else:
         return costLine1
      
   def startScheduling(self):
      numStation = len(self.timeStation[0])
      costLine1 = self.Scheduling(1, numStation - 1) + self.timeBelt[0][numStation]
      costLine2 = self.Scheduling(2, numStation - 1) + self.timeBelt[1][numStation]
      if costLine1 > costLine2:
         return costLine2
      else:
         return costLine1


lines = AssemblyLines()
time = lines.startScheduling() # 125 times calling
print("Fastest production time:", time) #38