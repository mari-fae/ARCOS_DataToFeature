##---------------------------------------------------------------------
## ImportARGOS.py
##
## Description: Read in ARGOS formatted tracking data and create a line
##    feature class from the [filtered] tracking points
##
## Usage: ImportArgos <ARGOS folder> <Output feature class> 
##
## Created: Fall 2018
## Author: alison.petro@duke.edu (for ENV859)
##---------------------------------------------------------------------

# Import modules
import sys, os, arcpy

# Set input variables (Hard-wired...i.e. not relative paths)
inputFile = '../Data/ARGOSData/1997dg.txt'
outputFC = '../Scratch/ARGOStrack.shp'

## Construct a while loop to iterate through all lines in the datafile
# Open the ARGOS data file for reading
inputFileObj = open(inputFile,'r')

# get the first line of data so we can use while loo
lineString = inputFileObj.readline()
while lineString:
    #get the next line
    lineString = inputFileObj.readline()

    # Set code to run only if the line contains the string "Date: "
    if ("Date :" in lineString):
        #print(lineString)

        #split the line into a list (called lineData in lab doc)
        lineList = lineString.split() # no argument = split by space
        # print (lineList)

        #extract attributes from datum header line
        tagID = lineList[0]

        #get the next line
        line2String = inputFileObj.readline()

        line2Data = line2String.split()

        #print (line2Data)

        #get attributes from 2nd line
        obsLat = line2Data[2]
        obsLon = line2Data[5]

        print (tagID, obsLat, obsLon)
        #break

    #move to the next line so the while loop progresses
    lineString = inputFileObj.readline()

#close the file object
inputFileObj.close()