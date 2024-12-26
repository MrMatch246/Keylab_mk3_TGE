# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\KeyLab_mk3\mappings.py
# Bytecode version: 3.11a7e (3495)
# Source timestamp: 2024-09-26 15:27:47 UTC (1727364467)

from ableton.v3.control_surface.mode import ImmediateBehaviour
from ableton.v3.control_surface.mode.behaviour import ToggleBehaviour

from Keylab_mk3_TGE.settings import PAD_CONTROL_MODES_MIXER


def create_mappings(_):
    mappings = {}
    mappings['Transport'] = dict(play_button='play_button',
                                 stop_button='stop_button',
                                 metronome_button='metronome_button',
                                 loop_button='loop_button',
                                 tap_tempo_button='tap_button',
                                 rewind_button='rewind_button',
                                 fastforward_button='fastforward_button',
                                 capture_midi_button='save_button')

    mappings['View_Based_Recording'] = dict(record_button='record_button')

    mappings['Undo_Redo'] = dict(undo_button='undo_button',
                                 redo_button='redo_button')

    mappings['Clip_Actions'] = dict(quantize_button='quantize_button')

    mappings['View_Control'] = dict(scene_encoder='display_encoder_with_shift_context_button',
                                    track_encoder='display_encoder')

    mappings['Mixer'] = dict(target_track_mute_button='context_button_4',
                             target_track_solo_button='context_button_5',
                             target_track_arm_button='context_button_6',
                             shift_button='shift_context_button',
                             #prehear_volume_control='encoder_8_with_shift_context_button',
                             )



    mappings['Scene_Launch'] = dict(launch_button='context_button_7')

    mappings['Active_Parameter'] = dict(
        touch_controls='parameter_touch_elements')

    mappings['Mode_Buttons'] = dict(device_button='device_context_button',
                                    mixer_button='mixer_context_button',
                                    pad_button='pad_context_button')

    mappings['Continuous_Control_Modes'] = dict(
        device_button='device_context_button', mixer_button='mixer_context_button',
        device=dict(modes=[
            dict(component='Device', parameter_controls='continuous_controls'),
            dict(component='Device_Navigation',
                 scroll_encoder='display_encoder_with_device_context_button'),
            dict(component='Mixer',
                 target_track_volume_control='fader_8',
                 target_track_send_a_control='encoder_8',
                 )]),
        mixer=dict(component='Mixer', volume_controls='faders',
                   pan_controls='encoders',
                   track_bank_encoder='display_encoder_with_mixer_context_button',
                   master_track_volume_control='fader_8',
                   target_track_pan_control='encoder_8',
                   ),
        default_behaviour=ImmediateBehaviour())

    if PAD_CONTROL_MODES_MIXER:
        mappings['Pad_Control_Modes'] = dict(
            support_momentary_mode_cycling=False,
            cycle_mode_button="pad_context_button",
            default_behaviour=ToggleBehaviour(),
            Session_Mode=dict(component="Session",
                              clip_launch_buttons="pads"),
            Mixer_Mute=dict(component="Mixer",
                            track_select_buttons="pads_row_1",
                            mute_buttons="pads_row_2",
                            solo_buttons="pads_row_3"),
            Mixer_Solo=dict(component="Mixer",
                            track_select_buttons="pads_row_1",
                            solo_buttons="pads_row_2",
                            arm_buttons="pads_row_3"),
            Mixer_Arm=dict(component="Mixer",
                           track_select_buttons="pads_row_1",
                           mute_buttons="pads_row_2",
                           arm_buttons="pads_row_3"),
        )
    else:
        mappings['Session'] = dict(clip_launch_buttons='pads')

    return mappings
