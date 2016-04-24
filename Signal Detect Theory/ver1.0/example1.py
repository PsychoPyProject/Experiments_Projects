#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.83.01), March 27, 2016, at 23:17
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import locale_setup, visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'example1'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1280, 720), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "introduction"
introductionClock = core.Clock()
Intro1 = visual.TextStim(win=win, ori=0, name='Intro1',
    text='Now, experiment will begin.',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "explanation2"
explanation2Clock = core.Clock()
text1_2 = visual.TextStim(win=win, ori=0, name='text1_2',
    text='This is a standard vibration.',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
text2_2 = visual.TextStim(win=win, ori=0, name='text2_2',
    text=u'This is a stimulate vibration.',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-1.0)
standard_vib_2 = sound.Sound('SIN80_20.wav', secs=-1)
standard_vib_2.setVolume(0.5)
stim_vib_2 = sound.Sound(u'SIN250_20.wav', secs=-1)
stim_vib_2.setVolume(0.5)

# Initialize components for Routine "explanation"
explanationClock = core.Clock()

text1 = visual.TextStim(win=win, ori=0, name='text1',
    text=u'This is a standard vibration.',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-1.0)
text2 = visual.TextStim(win=win, ori=0, name='text2',
    text=u'This is a stimulate vibration.',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-2.0)
text_4 = visual.TextStim(win=win, ori=0, name='text_4',
    text=u"\nPress 'y':provide stimulate vibration.\nPress 'i':provede standard vibration.\nPress 'space', if you can remenber both type of vibration. ",    font=u'Arial',
    pos=[0, -0.5], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-3.0)
standard_vib = sound.Sound(u'SIN80_20.wav', secs=-1)
standard_vib.setVolume(0.5)
stim_vib = sound.Sound(u'SIN250_20.wav', secs=-1)
stim_vib.setVolume(0.5)

# Initialize components for Routine "bef_trial"
bef_trialClock = core.Clock()
text = visual.TextStim(win=win, ori=0, name='text',
    text="Trial will start soon.\nDuring trial, \nif you can feel stimulate vibration, press 'y'key.\nif you can feel standard vibtation, press 'i'key.",    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text=" \nif you can feel stimulate vibration, press 'y'key.\nif you can feel standard vibtation, press 'i'key.",    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
stimlus = sound.Sound('A', secs=-1)
stimlus.setVolume(1.0)

# Initialize components for Routine "end"
endClock = core.Clock()
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text='Thank you very much for your participation.',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "introduction"-------
t = 0
introductionClock.reset()  # clock 
frameN = -1
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
introductionComponents = []
introductionComponents.append(Intro1)
for thisComponent in introductionComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "introduction"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = introductionClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Intro1* updates
    if t >= 0.0 and Intro1.status == NOT_STARTED:
        # keep track of start time/frame for later
        Intro1.tStart = t  # underestimates by a little under one frame
        Intro1.frameNStart = frameN  # exact frame index
        Intro1.setAutoDraw(True)
    if Intro1.status == STARTED and t >= (2.0-win.monitorFramePeriod*0.75): #most of one frame period left
        Intro1.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introductionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "introduction"-------
for thisComponent in introductionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "explanation2"-------
t = 0
explanation2Clock.reset()  # clock 
frameN = -1
routineTimer.add(6.000000)
# update component parameters for each repeat
key_resp_4 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_4.status = NOT_STARTED
# keep track of which components have finished
explanation2Components = []
explanation2Components.append(text1_2)
explanation2Components.append(text2_2)
explanation2Components.append(standard_vib_2)
explanation2Components.append(stim_vib_2)
explanation2Components.append(key_resp_4)
for thisComponent in explanation2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "explanation2"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = explanation2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text1_2* updates
    if t >= 0.0 and text1_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text1_2.tStart = t  # underestimates by a little under one frame
        text1_2.frameNStart = frameN  # exact frame index
        text1_2.setAutoDraw(True)
    if text1_2.status == STARTED and t >= (0.0 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
        text1_2.setAutoDraw(False)
    
    # *text2_2* updates
    if t >= 3.0 and text2_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text2_2.tStart = t  # underestimates by a little under one frame
        text2_2.frameNStart = frameN  # exact frame index
        text2_2.setAutoDraw(True)
    if text2_2.status == STARTED and t >= (6.0-win.monitorFramePeriod*0.75): #most of one frame period left
        text2_2.setAutoDraw(False)
    # start/stop standard_vib_2
    if t >= 0.0 and standard_vib_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        standard_vib_2.tStart = t  # underestimates by a little under one frame
        standard_vib_2.frameNStart = frameN  # exact frame index
        standard_vib_2.play()  # start the sound (it finishes automatically)
    if standard_vib_2.status == STARTED and t >= (0.0 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
        standard_vib_2.stop()  # stop the sound (if longer than duration)
    # start/stop stim_vib_2
    if t >= 3.0 and stim_vib_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        stim_vib_2.tStart = t  # underestimates by a little under one frame
        stim_vib_2.frameNStart = frameN  # exact frame index
        stim_vib_2.play()  # start the sound (it finishes automatically)
    if stim_vib_2.status == STARTED and t >= (3.0 + (3.0-win.monitorFramePeriod*0.75)): #most of one frame period left
        stim_vib_2.stop()  # stop the sound (if longer than duration)
    
    # *key_resp_4* updates
    if t >= 4.0 and key_resp_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_4.tStart = t  # underestimates by a little under one frame
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.status = STARTED
        # keyboard checking is just starting
    if key_resp_4.status == STARTED and t >= (6.0-win.monitorFramePeriod*0.75): #most of one frame period left
        key_resp_4.status = STOPPED
    if key_resp_4.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in explanation2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "explanation2"-------
for thisComponent in explanation2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
standard_vib_2.stop() #ensure sound has stopped at end of routine
stim_vib_2.stop() #ensure sound has stopped at end of routine

#------Prepare to start Routine "explanation"-------
t = 0
explanationClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
Flag = 0
key_resp_5 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_5.status = NOT_STARTED
# keep track of which components have finished
explanationComponents = []
explanationComponents.append(text1)
explanationComponents.append(text2)
explanationComponents.append(text_4)
explanationComponents.append(standard_vib)
explanationComponents.append(stim_vib)
explanationComponents.append(key_resp_5)
for thisComponent in explanationComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "explanation"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = explanationClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    if 'i' in theseKeys:
        Flag = 1
        if stim_vib_2.status == STARTED:#most of one frame period left
            stim_vib_2.stop()  # stop the sound (if longer than duration)
    elif 'y' in theseKeys:
        Flag = 2
        if standard_vib_2.status == STARTED:#most of one frame period left
            standard_vib_2.stop()  # stop the sound (if longer than duration)
    elif 'space' in theseKeys:
        continueRoutine = False
    
    # *text1* updates
    if (Flag == 1) and text1.status == NOT_STARTED:
        # keep track of start time/frame for later
        text1.tStart = t  # underestimates by a little under one frame
        text1.frameNStart = frameN  # exact frame index
        text1.setAutoDraw(True)
    if text1.status == STARTED and (Flag == 2):
        text1.setAutoDraw(False)
    
    # *text2* updates
    if t >= Flag == 2 and text2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text2.tStart = t  # underestimates by a little under one frame
        text2.frameNStart = frameN  # exact frame index
        text2.setAutoDraw(True)
    if text2.status == STARTED and (Flag == 1):
        text2.setAutoDraw(False)
    
    # *text_4* updates
    if t >= 0.0 and text_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_4.tStart = t  # underestimates by a little under one frame
        text_4.frameNStart = frameN  # exact frame index
        text_4.setAutoDraw(True)
    # start/stop standard_vib
    if (Flag == 1) and standard_vib.status == NOT_STARTED:
        # keep track of start time/frame for later
        standard_vib.tStart = t  # underestimates by a little under one frame
        standard_vib.frameNStart = frameN  # exact frame index
        standard_vib.play()  # start the sound (it finishes automatically)
    # start/stop stim_vib
    if (Flag == 2) and stim_vib.status == NOT_STARTED:
        # keep track of start time/frame for later
        stim_vib.tStart = t  # underestimates by a little under one frame
        stim_vib.frameNStart = frameN  # exact frame index
        stim_vib.play()  # start the sound (it finishes automatically)
    
    # *key_resp_5* updates
    if t >= 0.0 and key_resp_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_5.tStart = t  # underestimates by a little under one frame
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        key_resp_5.clock.reset()  # now t=0
    if key_resp_5.status == STARTED:
        theseKeys = event.getKeys(keyList=['y', 'i', 'space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_5.keys = theseKeys[-1]  # just the last key pressed
            key_resp_5.rt = key_resp_5.clock.getTime()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in explanationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "explanation"-------
for thisComponent in explanationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

standard_vib.stop() #ensure sound has stopped at end of routine
stim_vib.stop() #ensure sound has stopped at end of routine
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
   key_resp_5.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.nextEntry()
# the Routine "explanation" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "bef_trial"-------
t = 0
bef_trialClock.reset()  # clock 
frameN = -1
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
bef_trialComponents = []
bef_trialComponents.append(text)
for thisComponent in bef_trialComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "bef_trial"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = bef_trialClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t  # underestimates by a little under one frame
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    if text.status == STARTED and t >= (5.0-win.monitorFramePeriod*0.75): #most of one frame period left
        text.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in bef_trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "bef_trial"-------
for thisComponent in bef_trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stimulation2.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    stimlus.setSound(frequency_1, secs=-1)
    stimlus.setVolume(volume_1)
    key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_2.status = NOT_STARTED
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(text_3)
    trialComponents.append(stimlus)
    trialComponents.append(key_resp_2)
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if t >= 0.0 and text_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_3.tStart = t  # underestimates by a little under one frame
            text_3.frameNStart = frameN  # exact frame index
            text_3.setAutoDraw(True)
        # start/stop stimlus
        if t >= Timing and stimlus.status == NOT_STARTED:
            # keep track of start time/frame for later
            stimlus.tStart = t  # underestimates by a little under one frame
            stimlus.frameNStart = frameN  # exact frame index
            stimlus.play()  # start the sound (it finishes automatically)
        
        # *key_resp_2* updates
        if t >= Timing and key_resp_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_2.tStart = t  # underestimates by a little under one frame
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        if key_resp_2.status == STARTED:
            theseKeys = event.getKeys(keyList=['y', 'i'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_2.keys = theseKeys[-1]  # just the last key pressed
                key_resp_2.rt = key_resp_2.clock.getTime()
                # was this 'correct'?
                if (key_resp_2.keys == str(ans_key)) or (key_resp_2.keys == ans_key):
                    key_resp_2.corr = 1
                else:
                    key_resp_2.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    stimlus.stop() #ensure sound has stopped at end of routine
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
       key_resp_2.keys=None
       # was no response the correct answer?!
       if str(ans_key).lower() == 'none': key_resp_2.corr = 1  # correct non-response
       else: key_resp_2.corr = 0  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('key_resp_2.keys',key_resp_2.keys)
    trials.addData('key_resp_2.corr', key_resp_2.corr)
    if key_resp_2.keys != None:  # we had a response
        trials.addData('key_resp_2.rt', key_resp_2.rt)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):  params = []
else:  params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
trials.saveAsText(filename + 'trials.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

#------Prepare to start Routine "end"-------
t = 0
endClock.reset()  # clock 
frameN = -1
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = []
endComponents.append(text_2)
for thisComponent in endComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "end"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t  # underestimates by a little under one frame
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    if text_2.status == STARTED and t >= (2.0-win.monitorFramePeriod*0.75): #most of one frame period left
        text_2.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

win.close()
core.quit()
