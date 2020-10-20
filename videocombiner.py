import numpy as np
from moviepy.editor import VideoFileClip, clips_array, vfx


def arrange(array, x, y):
    return [array[i * x:(i + 1) * x] for i in range(y)]


clips = []
for clp in range(STARTVIDEO, ENDVIDEO):
    clips.append(VideoFileClip(f"outs\{clp}out.mp4"))  # add 10px contour

#These must be adjusted    
x = 5
y = 3

final_clip = clips_array(arrange(clips, x, y))
final_clip.write_videofile("saveasname.mp4")
