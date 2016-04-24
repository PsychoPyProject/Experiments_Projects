#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.82.01), 2015_07_16_2020
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""
from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

chunk = 5 #a number of loop 13 trial*chunk 
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'Exp1 Vib Ev'  # from the Builder filename that created this script
expInfo = {u'participant': u'', u'vibrator_name': u'001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
#filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])
filename = _thisDir + os.sep + 'data/%s_%s_%s_%s' %(expInfo['participant'], expInfo['vibrator_name'], expName, expInfo['date'])

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
win = visual.Window(size=(1280, 1024), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
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
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
explanation_2 = visual.TextStim(win=win, ori=0, name='explanation_2',
    text=u'Please wear vibration on your light index finger \n\nNext:Press 5',    font='Arial',
    units='cm', pos=[0, 0], height=1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0)
text_6 = visual.TextStim(win=win, ori=0, name='text_6',
    text='default text',    font='Arial',
    units='cm', pos=[0, 5], height=1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0)

# Initialize components for Routine "explanation_3"
explanation_3Clock = core.Clock()
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text=u'The standerd vibration will be played.\n If you can remember this vibration, please go next.\nPlay standard vibration : Press 8\nNext :Press 5\n',    font='Arial',
    units='cm', pos=[0, -2], height=1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
sample_standard_stim = sound.Sound('standard.wav', secs=-1)
sample_standard_stim.setVolume(0.3)

# Initialize components for Routine "stim_trial"
stim_trialClock = core.Clock()
volume_value = [0]
for num in range(40):
    volume_value.append(0.025 * num)

volume = 0
stim_sound = sound.Sound('A', secs=-1)
stim_sound.setVolume(0.1)
standard_sound = sound.Sound('standard.wav', secs=-1)
standard_sound.setVolume(0.3)
text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text=u'Stimulate vibration will be played again: Press →\nStandard vibration will be played again: Press ←\nComplete: Press[Enter]\n',    font='Arial',
    units='cm', pos=[0, -8], height=0.9, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-3.0)
text_8 = visual.TextStim(win=win, ori=0, name='text_8',
    text=u'Stimulate vibration will be played.\n',    font='Arial',
    units='cm', pos=[0, 4], height=1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-9.0)
text_5 = visual.TextStim(win=win, ori=0, name='text_5',
    text=u'Please adjust the volume of the stimulate vibration and\nmake it as same as standard vibration.\nup:press↑\ndown:press↓',    font='Arial',
    units='cm', pos=[0, 0], height=1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-10.0)

# Initialize components for Routine "thanks"
thanksClock = core.Clock()
text = visual.TextStim(win=win, ori=0, name='text',
    text=u'Thank you for your participation.\n\n',    font='Arial',
    units='cm', pos=[0, 0], height=1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "introduction"-------
t = 0
introductionClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
confirm_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
confirm_2.status = NOT_STARTED
text_6.setText(expInfo['vibrator_name'])
# keep track of which components have finished
introductionComponents = []
introductionComponents.append(ISI)
introductionComponents.append(confirm_2)
introductionComponents.append(explanation_2)
introductionComponents.append(text_6)
for thisComponent in introductionComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "introduction"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = introductionClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *confirm_2* updates
    if t >= 0.0 and confirm_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        confirm_2.tStart = t  # underestimates by a little under one frame
        confirm_2.frameNStart = frameN  # exact frame index
        confirm_2.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if confirm_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['5'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # *explanation_2* updates
    if t >= 0.0 and explanation_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        explanation_2.tStart = t  # underestimates by a little under one frame
        explanation_2.frameNStart = frameN  # exact frame index
        explanation_2.setAutoDraw(True)
    
    # *text_6* updates
    if t >= 0.0 and text_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_6.tStart = t  # underestimates by a little under one frame
        text_6.frameNStart = frameN  # exact frame index
        text_6.setAutoDraw(True)
    # *ISI* period
    if t >= 0.0 and ISI.status == NOT_STARTED:
        # keep track of start time/frame for later
        ISI.tStart = t  # underestimates by a little under one frame
        ISI.frameNStart = frameN  # exact frame index
        ISI.start(0.5)
    elif ISI.status == STARTED: #one frame should pass before updating params and completing
        ISI.complete() #finish the static period
    
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
# the Routine "introduction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=chunk, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('exam1_setwave.xlsx'),
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
    
    #------Prepare to start Routine "explanation_3"-------
    t = 0
    explanation_3Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_2.status = NOT_STARTED
    # keep track of which components have finished
    explanation_3Components = []
    explanation_3Components.append(text_2)
    explanation_3Components.append(key_resp_2)
    explanation_3Components.append(sample_standard_stim)
    for thisComponent in explanation_3Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "explanation_3"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = explanation_3Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_2* updates
        if t >= 0.0 and text_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_2.tStart = t  # underestimates by a little under one frame
            text_2.frameNStart = frameN  # exact frame index
            text_2.setAutoDraw(True)
        
        # *key_resp_2* updates
        if t >= 0.0 and key_resp_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_2.tStart = t  # underestimates by a little under one frame
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if key_resp_2.status == STARTED:
            theseKeys = event.getKeys(keyList=['5'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        if key_resp_2.status == STARTED:
            theseKeys = event.getKeys(keyList=['8'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                standard_sound.stop()
                stim_sound.stop()
                standard_sound.tStart = t
                standard_sound.frameNStart = frameN
                standard_sound.play()
        # start/stop sample_standard_stim
        if t >= 1.5 and sample_standard_stim.status == NOT_STARTED:
            # keep track of start time/frame for later
            sample_standard_stim.tStart = t  # underestimates by a little under one frame
            sample_standard_stim.frameNStart = frameN  # exact frame index
            sample_standard_stim.play()  # start the sound (it finishes automatically)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in explanation_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "explanation_3"-------
    for thisComponent in explanation_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sample_standard_stim.stop() #ensure sound has stopped at end of routine
    # the Routine "explanation_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "stim_trial"-------
    t = 0
    stim_trialClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    volume = randint(15, 25)
    initial_volume = volume
    stim_sound.setSound(exp_filename)
    stim_sound.setVolume(volume_value[volume])
    up_dB = event.BuilderKeyResponse()  # create an object of type KeyResponse
    up_dB.status = NOT_STARTED
    down_dB = event.BuilderKeyResponse()  # create an object of type KeyResponse
    down_dB.status = NOT_STARTED
    play_standard = event.BuilderKeyResponse()  # create an object of type KeyResponse
    play_standard.status = NOT_STARTED
    deside_stim = event.BuilderKeyResponse()  # create an object of type KeyResponse
    deside_stim.status = NOT_STARTED
    confirm_stim = event.BuilderKeyResponse()  # create an object of type KeyResponse
    confirm_stim.status = NOT_STARTED
    # keep track of which components have finished
    stim_trialComponents = []
    stim_trialComponents.append(stim_sound)
    stim_trialComponents.append(standard_sound)
    stim_trialComponents.append(text_3)
    stim_trialComponents.append(up_dB)
    stim_trialComponents.append(down_dB)
    stim_trialComponents.append(play_standard)
    stim_trialComponents.append(deside_stim)
    stim_trialComponents.append(confirm_stim)
    stim_trialComponents.append(text_8)
    stim_trialComponents.append(text_5)
    for thisComponent in stim_trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "stim_trial"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = stim_trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # start/stop stim_sound
        if t >= 1.5 and stim_sound.status == NOT_STARTED:
            # keep track of start time/frame for later
            stim_sound.tStart = t  # underestimates by a little under one frame
            stim_sound.frameNStart = frameN  # exact frame index
            stim_sound.play()  # start the sound (it finishes automatically)
        # start/stop standard_sound
        if () and standard_sound.status == NOT_STARTED:
            # keep track of start time/frame for later
            standard_sound.tStart = t  # underestimates by a little under one frame
            standard_sound.frameNStart = frameN  # exact frame index
            standard_sound.play()  # start the sound (it finishes automatically)
        
        # *text_3* updates
        if t >= 0.0 and text_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_3.tStart = t  # underestimates by a little under one frame
            text_3.frameNStart = frameN  # exact frame index
            text_3.setAutoDraw(True)
        
        # *up_dB* updates
        if t >= 0.0 and up_dB.status == NOT_STARTED:
            # keep track of start time/frame for later
            up_dB.tStart = t  # underestimates by a little under one frame
            up_dB.frameNStart = frameN  # exact frame index
            up_dB.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if up_dB.status == STARTED:
            theseKeys = event.getKeys(keyList=['up'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:
                standard_sound.stop()
                #stim_sound.stop()
                if volume < len(volume_value)-1:
                    volume = volume + 1
                    stim_sound.setVolume(volume_value[volume])
                if stim_sound.status == FINISHED:
                    #stim_sound.tStart = t
                    #stim_sound.ftameNStart = frameN
                    stim_sound.play()
        
        # *down_dB* updates
        if t >= 0.0 and down_dB.status == NOT_STARTED:
            # keep track of start time/frame for later
            down_dB.tStart = t  # underestimates by a little under one frame
            down_dB.frameNStart = frameN  # exact frame index
            down_dB.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if down_dB.status == STARTED:
            theseKeys = event.getKeys(keyList=['down'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:
                standard_sound.stop()
                #stim_sound.stop()
                if volume > 0:
                    volume = volume - 1
                    stim_sound.setVolume(volume_value[volume])
                    print volume
                if stim_sound.status == FINISHED:
                    #stim_sound.tStart = t
                    #stim_sound.ftameNStart = frameN
                    stim_sound.play()
        
        # *play_standard* updates
        if t >= 0.0 and play_standard.status == NOT_STARTED:
            # keep track of start time/frame for later
            play_standard.tStart = t  # underestimates by a little under one frame
            play_standard.frameNStart = frameN  # exact frame index
            play_standard.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if play_standard.status == STARTED:
            theseKeys = event.getKeys(keyList=['left'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:
                standard_sound.stop()
                stim_sound.stop()
                standard_sound.tStart = t
                standard_sound.frameNStart = frameN
                standard_sound.play()
        
        # *deside_stim* updates
        if t >= 0.0 and deside_stim.status == NOT_STARTED:
            # keep track of start time/frame for later
            deside_stim.tStart = t  # underestimates by a little under one frame
            deside_stim.frameNStart = frameN  # exact frame index
            deside_stim.status = STARTED
            # keyboard checking is just starting
            deside_stim.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if deside_stim.status == STARTED:
            theseKeys = event.getKeys(keyList=['return'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                deside_stim.keys = theseKeys[-1]  # just the last key pressed
                deside_stim.rt = deside_stim.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # *confirm_stim* updates
        if t >= 0.0 and confirm_stim.status == NOT_STARTED:
            # keep track of start time/frame for later
            confirm_stim.tStart = t  # underestimates by a little under one frame
            confirm_stim.frameNStart = frameN  # exact frame index
            confirm_stim.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if confirm_stim.status == STARTED:
            theseKeys = event.getKeys(keyList=['right'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:
                standard_sound.stop()
                stim_sound.stop()
                stim_sound.tStart = t
                stim_sound.ftameNStart = frameN
                stim_sound.play()
        
        # *text_8* updates
        if t >= 0.0 and text_8.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_8.tStart = t  # underestimates by a little under one frame
            text_8.frameNStart = frameN  # exact frame index
            text_8.setAutoDraw(True)
        
        # *text_5* updates
        if t >= 0.0 and text_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_5.tStart = t  # underestimates by a little under one frame
            text_5.frameNStart = frameN  # exact frame index
            text_5.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stim_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "stim_trial"-------
    for thisComponent in stim_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('initial_volume', volume_value[initial_volume])
    trials.addData('decided_volume', volume_value[volume])
    stim_sound.stop() #ensure sound has stopped at end of routine
    standard_sound.stop() #ensure sound has stopped at end of routine
    # check responses
    if deside_stim.keys in ['', [], None]:  # No response was made
       deside_stim.keys=None
    # store data for trials (TrialHandler)
    trials.addData('decide_stim.keys',deside_stim.keys)
    if deside_stim.keys != None:  # we had a response
        trials.addData('decide_stim.rt', deside_stim.rt)
    # the Routine "stim_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


#------Prepare to start Routine "thanks"-------
t = 0
thanksClock.reset()  # clock 
frameN = -1
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
thanksComponents = []
thanksComponents.append(text)
for thisComponent in thanksComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "thanks"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = thanksClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t  # underestimates by a little under one frame
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    if text.status == STARTED and t >= (0.0 + (5.0-win.monitorFramePeriod*0.75)): #most of one frame period left
        text.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "thanks"-------
for thisComponent in thanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

win.close()
core.quit()
