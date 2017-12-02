import cv2

def countFramesInFile(path, override=False):
    # grab a pointer to the video file and initialize the total
    # number of frames read
    video = cv2.VideoCapture(path)
    total = 0

    # if the override flag is passed in, revert to the manual
    # method of counting frames
    if override:
        total = countFrameManual(video)

    # otherwise, let's try the fast way first
    else:
        # lets try to determine the number of frames in a video
        # via video properties; this method can be very buggy
        # and might throw an error based on your OpenCV version
        # or may fail entirely based on your which video codecs
        # you have installed
        try:
            # check if we are using OpenCV 3
            total = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

        # uh-oh, we got an error -- revert to counting manually
        except:
            total = countFrameManual(video)

    # release the video file pointer
    video.release()

    # return the total number of frames in the video
    return total

def countFramesManual(video):
    # initialize the total number of frames read
    total = 0

    # loop over the frames of the video
    while True:
        # grab the current frame
        (grabbed, frame) = video.read()
     
        # check to see if we have reached the end of the
        # video
        if not grabbed:
            break

        # increment the total number of frames read
        total += 1

    # return the total number of frames in the video file
    return total
