from numpy.lib.type_check import imag
import cv2
import numpy as np


def video_to_images(video_dir, output_dir, frames_per_output_file=64):
    vidcap = cv2.VideoCapture(video_dir)
    success, image = vidcap.read()

    frame_count = 0
    batch_count = 0

    batch_array = []
    image_tensor = _handle_image(image)
    batch_array.append(image_tensor)

    while success:

        success, image = vidcap.read()
        image_tensor = _handle_image(image)
        if not len(image_tensor.shape) > 2:
            success = True
            print("Err")
            continue

        batch_array.append(image_tensor)

        if len(batch_array) == frames_per_output_file:

            batch_tensor = np.concatenate(batch_array)

            np.savez_compressed(
                "%svideo_out_%u" % (output_dir, batch_count), batch_tensor
            )

            batch_count += 1
            batch_tensor = []
            batch_array = []

        frame_count += 1

    batch_tensor = np.concatenate(batch_array)
    np.savez_compressed("%svideo_out_%u" % (output_dir, batch_count), batch_tensor)

    batch_count += 1

    print("Total frames: %s, total batches: %s" % (frame_count, batch_count))


def _handle_image(image):
    image_tensor = np.array(image)
    image_tensor = np.reshape(image_tensor, [1, *image_tensor.shape])
    return image_tensor
