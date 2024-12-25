# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\KeyLab_mk3\scene_launch.py
# Bytecode version: 3.11a7e (3495)
# Source timestamp: 2024-09-26 15:27:47 UTC (1727364467)

from ableton.v3.control_surface import Component
from ableton.v3.control_surface.controls import ButtonControl
from ableton.v3.control_surface.display import Renderable

class SceneLaunchComponent(Component, Renderable):
    pass
    launch_button = ButtonControl()

    def __init__(self, *a, **k):
        super().__init__(*a, name='Scene_Launch', **k)
        self.song.view.add_selected_track_listener(
            self.__on_selected_track_changed)

    @launch_button.released_immediately
    def launch_button(self, _):
        self.song.view.selected_scene.fire()

    @launch_button.pressed_delayed
    def launch_button(self, _):
        self.song.stop_all_clips()
        self.song.back_to_arranger = not self.song.back_to_arranger

    def __on_selected_track_changed(self):
        self.focus_visible_detail_view(show_if_hidden=True)

    def focus_visible_detail_view(self,show_if_hidden=False):
        if self.application.view.is_view_visible('Detail'):
            self.application.view.focus_view(self.visible_detail_viw())
        elif show_if_hidden:
            self.application.view.show_view('Detail')
            self.application.view.focus_view(self.visible_detail_viw())

    def visible_detail_viw(self):
        if self.application.view.is_view_visible('Detail/DeviceChain'):
            return "Detail/DeviceChain"
        elif self.application.view.is_view_visible('Detail/Clip'):
            return "Detail/Clip"
