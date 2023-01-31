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
   
   #setting up a memoization table
   timeScheduling = [list(range(6)), list(range(6))] #consider it as an empty list
   stationTracing = [list(range(6)), list(range(6))] 

   def startSchedulingDP(self):
      #table initiation
      numStation = len(self.timeStation[0])
      self.timeScheduling[0][0] = self.timeStation[0][0] + self.timeBelt[0][0] 
      self.timeScheduling[1][0] = self.timeStation[1][0] + self.timeBelt[1][0] #Scheduling becomes [[9, _, _, _, _, _], [12, _, _, _, _, _]]

      #dynamic programming
      for itr in range(1, numStation):
         if self.timeScheduling[0][itr-1] > self.timeScheduling[1][itr-1] + self.timeBelt[1][itr]:
            self.timeScheduling[0][itr] = self.timeScheduling[0][itr] + self.timeScheduling[1][itr-1] + self.timeBelt[1][itr]
            self.stationTracing[0][itr] = 1
         else:
            self.timeScheduling[0][itr] = self.timeStation[0][itr] +  self.timeScheduling[0][itr-1]
            self.stationTracing[0][itr] = 0

         if self.timeScheduling[1][itr-1] > self.timeScheduling[0][itr-1] + self.timeBelt[0][itr]:
            self.timeScheduling[1][itr] = self.timeStation[1][itr] + self.timeScheduling[0][itr-1] + self.timeBelt[0][itr]
            self.stationTracing[1][itr] = 0
         else:
            self.timeScheduling[1][itr] = self.timeStation[1][itr] + self.timeScheduling[1][itr-1]
            self.stationTracing[1][itr] = 1
      
      #caculate the time cost overall
      costLine1 = self.timeScheduling[0][numStation-1] + self.timeBelt[0][numStation] #adding last belt's time
      costLine2 = self.timeScheduling[1][numStation-1] + self.timeBelt[1][numStation] #adding last belt's time
      
      #compare between two paths
      if costLine1 > costLine2:
         return costLine2, 1
      else:
         return costLine1, 0

   def printTracing(self, lineTracing):
      numStation = len(self.timeStation[0])
      print("Line: ", lineTracing,", Station:", numStation)
      for itr in range(numStation-1, 0, -1):
         lineTracing = self.stationTracing[lineTracing][itr]
         print("Line:", lineTracing, ", Station:", itr)


lines = AssemblyLines()
time, lineTracing = lines.startSchedulingDP() # 6 times calling
print("Fastest produiction time:", time) #38
lines.printTracing(lineTracing)