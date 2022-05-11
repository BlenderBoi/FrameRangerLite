
import bpy

def RemapKeyframe(old, new, subframe):

    rate = old/new

    for action in bpy.data.actions:

        for fc in action.fcurves:
            for kf in fc.keyframe_points:

                if subframe:
                    kf.co.x = int(kf.co.x / rate)
                    kf.handle_left[0] = int(kf.handle_left[0] / rate)
                    kf.handle_right[0] = int(kf.handle_right [0] / rate)
                else:
                    kf.co.x = kf.co.x / rate
                    kf.handle_left[0] = kf.handle_left[0] / rate
                    kf.handle_right[0] = kf.handle_right [0] / rate

def RemapTimelineMarker(old, new, subframe):

    rate = old/new

    for scene in bpy.data.scenes:
        for tm in scene.timeline_markers:
            if subframe:
                tm.frame = int(tm.frame / rate)
            else:
                tm.frame = int(tm.frame / rate)

def RemapPoseMarker(old, new, subframe):
    
    rate = old/new

    for action in bpy.data.actions:
    
        for pm in action.pose_markers:
            if subframe:
                pm.frame = int(pm.frame / rate)
            else:
                pm.frame = int(pm.frame / rate)





def RemapFrameRange(context, old, new, subframe):

    rate = old/new
    if subframe:
        context.scene.frame_end = int(context.scene.frame_end / rate)
        context.scene.frame_start = int(context.scene.frame_start / rate)
    else:
        context.scene.frame_end =int(context.scene.frame_end / rate)
        context.scene.frame_start = int(context.scene.frame_start / rate)


def Nudge_Keyframe():

    for action in bpy.data.actions:

        for fc in action.fcurves:
            for kf in fc.keyframe_points:

                    kf.co.x = int(kf.co.x)
                    kf.handle_left[0] = int(kf.handle_left[0])
                    kf.handle_right[0] = int(kf.handle_right [0])


def Nudge_TimelineMarker():

    for scene in bpy.data.scenes:
        for tm in scene.timeline_markers:

            tm.frame = int(tm.frame)




