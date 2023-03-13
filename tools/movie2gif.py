from moviepy.editor import *
  
# loading video gfg
clip = VideoFileClip("media/input/chaplin.mp4")

# getting only first 3 seconds
clip1 = clip.subclip(0, 3).resize(1.0)

txt_clip = (TextClip("My Holidays 2013",fontsize=30,color='white')
             .set_position('top')
             .set_duration(6))

clip2 = clip.subclip(6, 9).resize(1.0)

video = concatenate_videoclips([clip1, clip2])
video_with_text = CompositeVideoClip([video, txt_clip]) # Overlay text on video

# saving video clip as gif
video_with_text.write_gif("media/output/chaplin.gif", fps=25, program='ffmpeg')
