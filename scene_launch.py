# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\KeyLab_mk3\scene_launch.py
# Bytecode version: 3.11a7e (3495)
# Source timestamp: 2024-09-26 15:27:47 UTC (1727364467)
import sys

from ableton.v3.control_surface import Component
from ableton.v3.control_surface.controls import ButtonControl
from ableton.v3.control_surface.display import Renderable
from .settings import *
scroll_count = 0
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
        #global scroll_count
        #if self.is_arranger_visible():
        #    scroll_count += 1
        #    if scroll_count % 3 != 0:
        #        self.focus_anything_but_arranger()
        #    else:
        #        self.application.view.focus_view("Arranger")
        #        scroll_count = 0
        #return
        if self.is_arranger_visible():
            self.focus_anything_but_arranger()

    def focus_anything_but_arranger(self):
        for view in self.application.view.available_main_views():
            if view != 'Arranger' and view != 'Session':
                if self.application.view.is_view_visible(view):
                    self.application.view.focus_view(view)
                    return

        if self.application.view.is_view_visible('Detail'):
            self.application.view.focus_view(self.visible_detail_view())
        elif SHOW_VIEW_ON_SCROLL:
            self.application.view.show_view(SHOW_VIEW_ON_SCROLL)


    def visible_detail_view(self):
        if self.application.view.is_view_visible('Detail/DeviceChain'):
            return "Detail/DeviceChain"
        elif self.application.view.is_view_visible('Detail/Clip'):
            return "Detail/Clip"


    def is_arranger_visible(self):
        return self.application.view.is_view_visible('Arranger')