from demo import load_checkpoints
from skimage import img_as_ubyte
from demo import make_animation
import imageio
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from skimage.transform import resize
from IPython.display import HTML
import warnings
import os
warnings.filterwarnings("ignore")

# source_image = imageio.imread('/content/gdrive/My Drive/first-order-motion-model/02.png')
# source_image = resize(source_image, (256, 256))[..., :3]

driving_video = imageio.mimread(HERE_IS_PATH_TO_MIMICING_VIDEO, memtest=False)
# Resize image and video to 256x256

driving_video = [resize(frame, (256, 256))[..., :3] for frame in driving_video]


def ourDisplay(videos):
    fig = plt.figure(figsize=(10, 10))
    ax = plt.axes([0.0, 0.0, 1.0, 1.0])

    ims = []
    for i in range(len(videos[0])):
        cols = []

        size = int(len(videos)**0.5)

        frames = [video[i] for video in videos]
        size = int(len(frames)**0.5)
        aframes = [np.concatenate(
            frames[i * size:(i + 1) * size], axis=0) for i in range(size)]
        im = plt.imshow(np.concatenate(aframes, axis=1), animated=True)
        plt.axis('off')
        ims.append([im])

    ani = animation.ArtistAnimation(fig, ims, interval=50, repeat_delay=1000)
    plt.close()
    return ani


def displaySolo(video):
    videos = [video]
    # fig = plt.figure(figsize=(2.56, 2.56))
    fig = plt.figure(figsize=(5, 5))
    ax = plt.axes([0.0, 0.0, 1.0, 1.0])

    ims = []
    for i in range(len(videos[0])):
        cols = []

        # size = int(len(videos)**0.5)
        size = int(1)

        frames = [video[i] for video in videos]
        size = int(len(frames)**0.5)
        aframes = [np.concatenate(
            frames[i * size:(i + 1) * size], axis=0) for i in range(size)]
        im = plt.imshow(np.concatenate(aframes, axis=1), animated=True)
        plt.axis('off')
        ims.append([im])

    ani = animation.ArtistAnimation(
        fig, ims, interval=29.97, repeat_delay=1000)
    plt.close()
    return ani


generator, kp_detector = load_checkpoints(config_path='config/vox-256.yaml',
                                          checkpoint_path='vox-cpk.pth.tar')


directory = 'outs/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Set up formatting for the movie files
Writer = animation.writers['ffmpeg']
writer = Writer(fps=29.97, metadata=dict(artist='Me'), bitrate=1800)
outputs = []
for i in range(46, 48):
    gett = imageio.imread(f"all-the-faces/faces/{i}.png")
    gett = resize(gett, (256, 256))[..., :3]
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # outputs.append(make_animation(gett, driving_video,
    #                               generator, kp_detector, relative=True))

    solovid = make_animation(
        gett, driving_video, generator, kp_detector, relative=True)
    print(f"{i} is Done!!")

    # # # # # # # # # # # # # # # # # # # # # # # # # #
    # im_ani = ourDisplay(outputs)
    im_ani = displaySolo(solovid)
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    print(f"SAVING VIDEO NO {i}")
    im_ani.save(f'outs/{i}out.mp4', writer=writer)
    print(f"{i} SAVED")
