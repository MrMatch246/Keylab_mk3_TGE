#This file allows you to change some behavior of the Keylab mk3 script.



# IF you scroll through tracks but the arranger is focused, the window wont scroll
# The workaround is to focus another view.
# If no other view is available, you can have any of the above views shown.
# The default value is None which means nothing will happen.
# Available views are: 'Browser', 'Detail/DeviceChain', 'Detail/Clip' , 'Detail'
SHOW_VIEW_ON_SCROLL = None


# Pad Control Modes
# This is a completely WORK IN PROGRESS feature.
# It is not recommended to enable this unless you want to play around with it.
# Code wise, not actually playing around with it.
# it is supposed to allow you to switch between different modes for the pads.
# The the mode that i want, is a mode where the first row of pads is used to select tracks
# The second row is used to mute tracks and the third row is used to solo tracks.
# or something like that.
# currently there are a number of problems here:
# 1. armed tracks dont change light color unless you cycle through the modes
# 2. there is no good way to scroll through them without using a modifier key
# 3. i dont know how to follow the track selection, which would be very useful
# I dont know if i will ever finish this feature, but if you want to try it out, you can enable it here.
PAD_CONTROL_MODES_MIXER = False


#Sets the Speed of the Fast Forward and Rewind Buttons
REWIND_FORWARD_SPEED = 4

# Set this to True if you the Play button to pause/continue on press
# and start from song marker on longer press
ENABLE_PLAY_PAUSE_BUTTON = True


############## PYTHON BASED FEATURES ##############
# If you can run python3 scripts on your system set this to True
I_HAVE_PYTHON_3 = False

# If you are a Mac user
IS_MAC = False

# Port to use for the Python Bridge
PY_PORT = 49200

# Part + TAP Toggles the Wrench on the Plugin (currently has to be opened
# manually first and then closed with the button) The wrench has three modes
# black, grey and blue. The button toggles between grey and blue
#TODO: This feature is not yet implemented
PY_TOGGLE_WRENCH = True

# Save your Project! with the Tap + Save Button!!!
#TODO: This feature is not yet implemented
PY_SAVE_PROJECT = True

# Update the Filesystem/Places with the Tap + Update Button
# Set it to true and the path to a folder you want to update
# This is used for situations like a Google Drive folder in places that doesnt
# trigger an update when changes are synchronized.
# especially useful if you collaborate, and or drag and drop doesnt work due to
# Ableton running as Admin
#TODO: This feature is not yet implemented
PY_UPDATE_FILESYSTEM = False
PY_UPDATE_FILESYSTEM_PATH = None

# If you want to Loop the selected area with the SHIFT + Loop Button
#TODO: This feature is not yet implemented
PY_ENABLE_LOOP_SELECTION = True


# Set this to false if you don't want the encoder to jump to the first bank
# after the last bank (only for the device parameter bank)
#TODO: This feature is not yet implemented
ENABLE_ROUNDTRIP_BANKING_PARAM = True


#TODO: This feature is not yet implemented
# DOCUMENTATION
ENCODER_TRACK_BANK_TRACKS_PER_CLICK = 1

# Set this to false if you don't want the encoder to jump to the first Tracks
# Page after the last bank
#TODO: This feature is not yet implemented
ENABLE_ROUNDTRIP_BANKING_TRACK = False



#Set this to True if you want the encoder to scroll in the opposite direction
#for the Pads
#TODO: This feature is not yet implemented
ENCODER_TRACK_DIRECTION_INVERTED = False


### DO NOT CHANGE ANYTHING BELOW THIS LINE ###
if not I_HAVE_PYTHON_3:
    PY_TOGGLE_WRENCH = False
    PY_SAVE_PROJECT = False
    PY_UPDATE_FILESYSTEM = False

if not PY_UPDATE_FILESYSTEM_PATH:
    PY_UPDATE_FILESYSTEM = False
