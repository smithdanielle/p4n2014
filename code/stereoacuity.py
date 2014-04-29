from psychopy import core, visual, gui, data, misc, event,logging
import copy, random, os, numpy

# set things that don't change throughout the experiment
win = visual.Window([800,800], fullscr=False, units='deg', 
    monitor='default', blendMode='add', useFBO=True)
globalClock = core.Clock()
respClock = core.Clock()

#logging stuff
logging.setDefaultClock(globalClock)
logging.console.setLevel(logging.WARNING)#set the console to receive warnings and errors

# initialise experiment information
info = {} # a dictionary
info['participant'] = ''
dlg = gui.DlgFromDict(info) # present dialog to collect info
if not dlg.OK:
    core.quit()
info['dateStr'] = data.getDateStr() #will create str of current date/time
info['refDisp'] = 0.16 # disparity of reference stays constant at 0.16 deg


#create the base filename for our data files
#fileName = "data/{participant}_{dateStr}".format(**info)
#dataFile = open(fileName+'.csv', 'w')#a simple text file with 'comma-separated-values'

#create the staircase handler
staircase = data.StairHandler(startVal = 0.3,
                          stepType = 'lin', stepSizes=[0.05,0.03,0.03,0.02,0.02,0.01,0.01],
                          nUp=1, nDown=1, minVal = 0, maxVal=0.3)  #will home in on the 50% threshold

# initialise stimuli
fixation = visual.Circle(win, size = 0.25,
    lineColor = 'white', fillColor = 'lightGrey')
    
rds=visual.DotStim(win, nDots=500, fieldSize=(4,4), fieldShape='sqr', dotLife= -1, speed = 0.0, dotSize=5)

target = copy.copy(rds)

reference = copy.copy(rds)

referenceLeft=copy.copy(reference)
referenceLeft.setColor([1.0,0,0])
referenceLeft.setFieldPos([-(info['refDisp'])/2,0])
referenceRight=copy.copy(reference)
referenceRight.setColor([0,0.6,0.6])
referenceRight.setFieldPos([(info['refDisp'])/2,0])

# display fixation cross
fixation.draw()
win.flip()
event.waitKeys()

for thisIncrement in staircase:
    # set location of the stimuli
    targetSide= random.choice([-1,1]) #will be either +1(right) or -1(left)
    referenceLeft.setFieldPos([-(info['refDisp'])/2,-5*targetSide])
    referenceRight.setFieldPos([(info['refDisp'])/2,-5*targetSide])
    refText=visual.TextStim(win, 'ref', pos=(8,-5*targetSide))
    
    # set disparity of target
    targetLeft=copy.copy(target)
    targetLeft.setColor([1.0,0,0])
    targetLeft.setFieldPos([-thisIncrement/2,5*targetSide])
    targetRight=copy.copy(target)
    targetRight.setColor([0,0.6,0.6])
    targetRight.setFieldPos([thisIncrement/2,5*targetSide])
    targetText=visual.TextStim(win, 'target', pos=(8,5*targetSide))
    
    # draw all stimuli
    referenceLeft.draw()
    referenceRight.draw()
    refText.draw()
    targetLeft.draw()
    targetRight.draw()
    targetText.draw()
    fixation.draw()
    
    # now show them
    win.flip()
    core.wait(2)
    
    # blank screen
    fixation.draw()
    win.flip()
    
    #get response
    thisResp=None
    while thisResp==None:
        allKeys=event.waitKeys()
        for thisKey in allKeys:
            if thisIncrement<(info['refDisp']):
                if thisKey=='up':
                    if targetSide==1: thisResp = 1#correct
                    else: thisResp = -1             #incorrect
                elif thisKey=='down':
                    if targetSide== -1: thisResp = 1#correct
                    else: thisResp = -1             #incorrect
            elif thisIncrement>(info['refDisp']):
                if thisKey=='up':
                    if targetSide==1: thisResp = 1#correct
                    else: thisResp = -1             #incorrect
                elif thisKey=='down':
                    if targetSide== -1: thisResp = 1#correct
                    else: thisResp = -1             #incorrect
            elif thisKey in ['q', 'escape']:
                core.quit() #abort experiment
                
    #add the data to the staircase so it can calculate the next level
    staircase.addData(thisResp)
#    dataFile.write('%i,%.3f,%i\n' %(targetSide, thisIncrement, thisResp))

#staircase has ended
#dataFile.close()

#give some output to user in the command line in the output window
print 'reversals:'
print staircase.reversalIntensities
print 'mean of final 6 reversals = %.3f' %(numpy.average(staircase.reversalIntensities[-6:]))


win.close()