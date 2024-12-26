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