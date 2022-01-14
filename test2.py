from moviepy.editor import VideoFileClip, concatenate_videoclips, CompositeVideoClip

clip1=VideoFileClip('lines.mp4')
clip2=VideoFileClip('lines.mp4')
clip3=VideoFileClip('lines.mp4')
clip4=VideoFileClip('lines.mp4')
clip5=VideoFileClip('lines.mp4')
clip6=VideoFileClip('lines.mp4')
# clip7=VideoFileClip('l.mp4')
# clip8=VideoFileClip('l.mp4')
# clip9=VideoFileClip('l.mp4')
# clip10=VideoFileClip('l.mp4')
# clip11=VideoFileClip('l.mp4')
# clip12=VideoFileClip('l.mp4')

final_clip = concatenate_videoclips([clip1, clip2, clip3, clip4, clip5, clip6])

final_clip.write_videofile("finall.mp4")