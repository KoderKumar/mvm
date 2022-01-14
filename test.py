from moviepy.editor import *
  
# loading video gfg
clip = VideoFileClip("1.gif")
  
  
# getting only first 5 seconds
clip = clip.subclip(0, 7)
  
# looping video 3 times
clip.ipython_display(loop = 3)