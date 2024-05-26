import numpy as np
import collections
import cv2 as cv
from moving_average_filter import moving_average_filter
from file_io import file_io

# FriendlyName: Game Capture HD60 Pro
# InstanceId: PCI\VEN_12AB&DEV_0380&SUBSYS_00061CFA&REV_00\6&287A4141&0&0038000A
# 0 is elgato, 1 is webcam
cap = cv.VideoCapture(0) # cv.VideoCapture(1)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

print("getBackendName:" + cap.getBackendName())
# frame_shape = (1080, 1920, 3)
frame_shape = (1080, 1920)
n_frames = 1
filt = moving_average_filter(n_frames, frame_shape)
dumper = file_io('./data/dump.json')
dump_frame_counter = 0
dump_frames_max = 1
has_dumped_yet = False
dump_frames = [] # collections.deque(np.array([]))
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?) Exiting ...")
        break
    # Our operations on the frame come here
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    filt.add_sample(gray_frame)

    subsection = filt.average[636:972 , 412:1486]

    if dump_frame_counter < dump_frames_max:
        dump_frame_counter += 1
        dump_frames.append(subsection)

    if not has_dumped_yet and dump_frame_counter == dump_frames_max:
        has_dumped_yet = True
#         dumper.write(subsection.tolist())
        dumper.write(dump_frames)
#         dumper.write(filt.average.tolist()) ####

#     filt.add_sample(frame)

#     cv.imshow("frame", filt.sum/len(filt.buffer))

#     print(type(filt.average[0][0][0]))

#     # vertical slices
#     filt.average[:, 412] = 255
#     filt.average[:, 1486] = 255
#
#     # horizontal slices
#     filt.average[636, :] = 255
#     filt.average[972, :] = 255


    # Display the resulting frame
    cv.imshow("frame", subsection) #########

#     cv.imshow("frame", frame)
    if cv.waitKey(1) == ord("q"):
        break

# When everything is done, release the capture
cap.release()
cv.destroyAllWindows()
