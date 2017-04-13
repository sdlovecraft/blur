from grid_tools import get_filenames
import matplotlib.pyplot as plt
from natsort import natsorted, ns
import numpy as np

output_filenames = get_filenames('./input')


def get_images(dir_name):
    filenames = get_filenames(dir_name)
    filenames = natsorted(filenames, alg=ns.IGNORECASE)
    imgs = [plt.imread(fname)[..., :3] for fname in filenames]
    return np.array(imgs)

def normalize(input_dir='./input', output_dir='./output'):
    input_imgs = get_images(input_dir)
    output_imgs = get_images(output_dir)

    filenames = get_filenames('./output')
    filenames = natsorted(filenames, alg=ns.IGNORECASE)

    for idx, (input_img, output_img) in enumerate(zip(input_imgs, output_imgs)):
        input_mean = input_img.mean()
        output_mean = output_img.mean()
        difference = input_mean - output_mean
        adjusted_output = output_img + difference
        adjusted_output = np.clip(adjusted_output, 0, 1)
        # plt.imsave(filenames[idx], adjusted_output)
        plt.imsave("processed/{}.jpg".format(idx), adjusted_output)

normalize()