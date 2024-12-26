# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\KeyLab_mk3\colors.py
# Bytecode version: 3.11a7e (3495)
# Source timestamp: 2024-09-26 15:27:47 UTC (1727364467)

from ableton.v3.control_surface import BasicColors
from ableton.v3.control_surface.elements import FallbackColor, create_rgb_color
from ableton.v3.live import liveobj_color_to_midi_rgb_values


def create_blinking_color(r, g, b):
    return create_rgb_color((r, g, b, 2))

def create_color(r, g, b):
    return create_rgb_color((r, g, b, 0))

def create_dynamic_color_bright(x):
    return create_color(*liveobj_color_to_midi_rgb_values(x))

def create_dynamic_color_dark(x):
    color = liveobj_color_to_midi_rgb_values(x)
    return create_color(*(int(c / 8) for c in color))

class Rgb:
    #####TAKEN FROM ESSENTIAL#####
    #TODO FIX
    RED_BLINK = create_blinking_color(127, 0, 0)
    GREEN_HALF_BLINK = create_blinking_color(0, 32, 0)
    GREEN_BLINK = create_blinking_color(0, 127, 0)
    BLUE = create_color(0, 0, 127)
    BLUE_HALF = create_color(0, 0, 32)
    BLUE_THIRD = create_color(0, 0, 16)
    OCEAN = create_color(20, 80, 127)
    OCEAN_HALF = create_color(10, 40, 64)
    AMBER = create_color(127, 50, 0)
    AMBER_HALF = create_color(20, 5, 0)
    YELLOW_LOW = create_color(8, 6, 0)
    PURPLE = create_color(64, 0, 127)
    PURPLE_HALF = create_color(16, 0, 32)
    PURPLE_HALF_BLINK = create_blinking_color(16, 0, 32)


    #####ACTUALL#####
    OFF = FallbackColor(create_color(0, 0, 0), BasicColors.OFF)
    WHITE_HALF = create_color(64, 64, 64)
    WHITE = FallbackColor(create_color(127, 127, 127), BasicColors.ON)
    RED = create_color(127, 0, 0)
    RED_HALF = create_color(64, 0, 0)
    RED_LOW = create_color(32, 0, 0)
    GREEN = create_color(0, 127, 0)
    GREEN_HALF = create_color(0, 64, 0)
    YELLOW = create_color(127, 72, 0)
    YELLOW_HALF = create_color(64, 48, 0)

class Skin:

    class DefaultButton:
        On = Rgb.WHITE
        Off = Rgb.OFF
        Disabled = Rgb.OFF

    class Transport:
        PlayOn = Rgb.GREEN
        PlayOff = Rgb.GREEN_HALF
        StopOn = Rgb.WHITE
        StopOff = Rgb.WHITE_HALF
        LoopOn = Rgb.YELLOW
        LoopOff = Rgb.YELLOW_HALF
        MetronomeOn = Rgb.WHITE
        MetronomeOff = Rgb.WHITE_HALF
        TapTempoPressed = Rgb.WHITE
        TapTempo = Rgb.WHITE_HALF
        SeekPressed = Rgb.WHITE
        Seek = Rgb.WHITE_HALF
        CanCaptureMidi = Rgb.WHITE

    class Recording:
        ArrangementRecordOn = Rgb.RED
        ArrangementRecordOff = Rgb.RED_HALF
        SessionRecordOn = Rgb.RED
        SessionRecordOff = Rgb.RED_HALF

    class UndoRedo:
        UndoPressed = Rgb.WHITE
        Undo = Rgb.WHITE_HALF
        RedoPressed = Rgb.WHITE
        Redo = Rgb.WHITE_HALF

    class ClipActions:
        Quantize = Rgb.WHITE_HALF
        QuantizePressed = Rgb.WHITE

    class Session:
        Slot = Rgb.OFF
        SlotRecordButton = Rgb.RED_LOW
        NoSlot = Rgb.OFF
        ClipStopped = lambda x: create_color(*liveobj_color_to_midi_rgb_values(x))
        ClipTriggeredPlay = Rgb.GREEN_HALF
        ClipPlaying = Rgb.GREEN
        ClipTriggeredRecord = Rgb.RED_HALF
        ClipRecording = Rgb.RED

    class Mixer:
        pass
        #ArmOn = Rgb.RED
        #ArmOff = Rgb.RED_LOW
        #NoTrack = Rgb.OFF
        #TrackSelected = Rgb.WHITE
        #SoloOn = Rgb.BLUE
        #SoloOff = Rgb.BLUE_THIRD
        #MuteOn = Rgb.YELLOW
        #MuteOff = Rgb.YELLOW_LOW
        Selected = create_dynamic_color_bright
        NotSelected = create_dynamic_color_dark
        #SoloButton = Rgb.BLUE
        #MuteButton = Rgb.YELLOW

    class PadControlModes:
        Mixer_Mute = Rgb.YELLOW
        Mixer_Solo = Rgb.BLUE
        Mixer_Arm = Rgb.RED

        class Mixer:
            ArmOn = Rgb.RED
            ArmOff = Rgb.RED_LOW
            NoTrack = Rgb.OFF
            TrackSelected = Rgb.WHITE
            SoloOn = Rgb.BLUE
            SoloOff = Rgb.BLUE_THIRD
            MuteOn = Rgb.YELLOW
            MuteOff = Rgb.YELLOW_LOW