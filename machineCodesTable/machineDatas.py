# There are machine codes and daily production amounts of each machine for one week in "file.txt" file 
# This program gets datas from the file and creates a blank table from two dimentional list
# and it fills the table according to datas from file and calculates daily, weekly and monhtly production
# amounts of each machine and prints table to the console
# Theese datas tested according to 5 machine's datas.
# It can be added optionally a display function for writing datas more well and in easy understandable form.

table = []

MACHINE_NUM = 5
DATA_NUM_FOR_ONE_MACHINE = 8

# Create the outline of the table for fill then
for row in range(MACHINE_NUM + 1):
    data_for_one_machine = [0] * (DATA_NUM_FOR_ONE_MACHINE + 1)
    table.append(data_for_one_machine)

#gets datas and fills the table for each machine 
def getDatasAndFillTheTable():
    with open("file.txt","r") as dataFile:
        line = dataFile.readline().strip()
        while line != "":
            machineCode = int(line)
            for machineIndex in range(MACHINE_NUM):
                table[machineIndex][0] = machineCode
                machineCode += 1
                for machineDataIndex in range(1,DATA_NUM_FOR_ONE_MACHINE):
                    line = dataFile.readline().strip()
                    table[machineIndex][machineDataIndex] = line
                line = dataFile.readline().strip()
            line = dataFile.readline().strip()

# gets datas from table and calculates weekly and totals of each machine and fills the table 
def calculateRowSumAndFillTable():
    for machine in table:
        rowSum = 0
        for machineDataIndex in range(1,len(machine)-1):
            rowSum += int(machine[machineDataIndex])
            table[table.index(machine)][8] = rowSum

# gets datas from table and calculates daily and monhtly total production amount of each machine and fills the table
def calculateColumnSumAndFillTable():
    for machineDataIndex in range(1,DATA_NUM_FOR_ONE_MACHINE+1):
        columnSum = 0
        for machineIndex in range(len(table)-1):
            columnSum += int(table[machineIndex][machineDataIndex])
            table[5][machineDataIndex] = columnSum

# main order for work
getDatasAndFillTheTable()
calculateRowSumAndFillTable()
calculateColumnSumAndFillTable()

# prints the table for checking
for machineData in table:
    print(machineData)