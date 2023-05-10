import bpy
import importlib
from bpy.app.handlers import persistent
from bpy.types import Menu

from . import object_distribute

bl_info = {
    "name": "(IMC) Blender utils",
    "author": "Ian Carr",
    "description": "Blender Add-on  object and mesh tools. includes: Distribute objects uniformly",
    "blender": (3, 1, 0),
    "version": (0, 1, 0),
    "location": "View3D > Context Menu > Object/Edit Modes",
    "warning": "",
    "doc_url": "",
    "tracker_url": "",
    "category": "Object",
}

modules = [
 object_distribute
]

classes = [
]

def reload() -> None:
    global modules

    for m in modules:
        importlib.reload(m)


_need_reload = "prefs" in locals()
if _need_reload:
    reload()

# ----------------REGISTER--------------.


def register() -> None:
    if bpy.app.background:
        return
    for m in modules:
        if hasattr(m, 'registry'):
            for c in m.registry:
                bpy.utils.register_class(c)
        if hasattr(m, 'register'):
            m.register()

    for cls in classes:
        bpy.utils.register_class(cls)

def unregister() -> None:
    if bpy.app.background:
        return
    for m in modules:
        if hasattr(m, 'registry'):
            for c in m.registry:
                bpy.utils.unregister_class(c)
        if hasattr(m, 'unregister'):
            m.unregister()

    for cls in classes:
        bpy.utils. unregister_class(cls)