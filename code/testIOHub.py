from psychopy import visual
from psychopy.iohub import launchHubServer, EventConstants

io = launchHubServer()
keyboard = io.devices.keyboard # in OSX 1.8 'Mountain Lion' and later, ioHub requires 'assisted devices' to be turned on for keyboard (doesn't work yet, mouse is fine)
mouse = io.devices.mouse
display = io.devices.display

# We can use display to find info for the Window creation, like the resolution
# (which means PsychoPy won't warn you that the fullscreen does not match your requested size)
displayRes=display.getPixelResolution()

# ioHub currently supports the use of a single full-screen PsychoPy Window
win=visual.Window(displayRes,
                        units='pix',
                        fullscr=True, allowGUI=False,
                        screen=0
                        )
stim = visual.GratingStim(win, mask = 'gauss', sf = 6)

for frameN in range(1200):
    # Get the current mouse position
    # posDelta is the change in position *since the last call*
    position, posDelta = mouse.getPositionAndDelta()
    dX, dY=posDelta
    # Get the current state of each of the Mouse Buttons
    left_button, middle_button, right_button = mouse.getCurrentButtonStates()
    # Change stimulus position depending on mouse position
    stim.setPos(position)
    
    stim.setOri(frameN*2)
    stim.draw()
    win.flip()
    
    # Can get keyboard events if we wish
    keys = keyboard.getEvents()
    for thisKey in keys:
        print thisKey

