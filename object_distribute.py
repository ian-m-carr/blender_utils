import bpy

from bpy.types import Operator
from bpy.props import BoolProperty

import os
from copy import copy
import mathutils
from functools import partial

def filtered_location(location: mathutils.Vector, in_x: bool, in_y: bool, in_z: bool) -> mathutils.Vector:
    x = location.x if in_x else 0
    y = location.y if in_y else 0
    z = location.z if in_z else 0

    return mathutils.Vector((x, y, z))


def filtered_distance_from_active(in_x: bool, in_y: bool, in_z: bool, obj) -> mathutils.Vector:
    return filtered_location(bpy.context.active_object.location, in_x, in_y, in_z) - filtered_location(obj.location, in_x, in_y, in_z)


def distribute_objects(self, in_x: bool, in_y: bool, in_z: bool):
    # obtain the set of selected objects
    selection = bpy.context.selected_objects

    if len(selection[:]) > 2:
        # now create the selection, other than the active object
        ordered_selection = []

        for obj in selection[:]:
            if obj != bpy.context.active_object:
                ordered_selection.append(obj)

        # curry the distance extraction with the axis selections
        sort_func = partial(filtered_distance_from_active, in_x, in_y, in_z)

        # now sort the selections, based on the (filtered) distance from the active object
        ordered_selection.sort(key=sort_func)

        # derive the distance between active and furthest object location
        total_dist = filtered_location(ordered_selection[-1].location, in_x, in_y, in_z) - filtered_location(bpy.context.active_object.location,
                                                                                                             in_x, in_y, in_z)

        # calculate the separation between items (total length divided by num item -1 (n fence panels need n+1 posts!)
        item_delta = total_dist / (len(selection[:]) - 1)

        # the position of the active element
        location = copy(bpy.context.active_object.location) + item_delta

        # iterate and move the objects (other than the active one) along the selected axes
        for obj in ordered_selection[:]:
            if in_x:
                obj.location.x = location.x
            if in_y:
                obj.location.y = location.y
            if in_z:
                obj.location.z = location.z

            location += item_delta

    else:
        self.report({'INFO'}, "Please select 2 or more objects to distribute")


class Distribute(Operator):
    bl_idname = "object.distribute"
    bl_label = "Distribute Objects"
    b_X: BoolProperty(name="distribute along global X")
    b_Y: BoolProperty(name="distribute along global Y")
    b_Z: BoolProperty(name="distribute along global Z")

    def execute(self, context):
        distribute_objects(self, self.b_X, self.b_Y, self.b_Z)
        return {'FINISHED'}

    def invoke(self, context, event):
        self.b_X = True
        self.b_Y = True
        self.b_Z = True
        return context.window_manager.invoke_props_dialog(self)


registry = [
    Distribute
]

def menu_draw(self: bpy.types.UIList, context: bpy.types.Context) -> None:
    self.layout.separator()
    self.layout.operator_context = "INVOKE_DEFAULT"
    self.layout.operator("object.distribute")

def register():
    bpy.types.VIEW3D_MT_object_context_menu.append(menu_draw)

def unregister():
    bpy.types.VIEW3D_MT_object_context_menu.remove(menu_draw)
