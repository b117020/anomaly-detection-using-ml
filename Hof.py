import numpy as np
import math
import cv2
import glob
import pdb

import matplotlib.pyplot as plt
def get_flow_to_hist(vid_name):
    """ from image name to hist wrapper """
    flow_name = '{}1.jpg'.format(vid_name)
    img = cv2.imread(flow_name)
    hist, bin_edges = flow_to_hist(img)

    return hist, bin_edges


def flow_to_hist(img):
    """ Feed not normalized flow [0 ~ 255] (h, w, 3), convert to normalized arr [0 ~ 1], return hist and bin_edges """
    flow_arr = convert_flowimg(img)
    hist, bin_edges = gradient_histogram(flow_arr)

    return hist, bin_edges


def checker():
    """ Debug """
    FLOW_DIR = './ZzBVziOgi8g_4/'

    # right to left
    hist, bin_edges = get_flow_to_hist(FLOW_DIR)
    print("right to left - img 11")
    show_result(hist, bin_edges)
    print

    

    #            y,  x
    arctan_test( 0,  0)
    arctan_test( 1,  0)
    arctan_test(-1,  0)
    arctan_test( 0,  1)
    arctan_test( 0, -1)


def arctan_test(x, y):
    """ tester to check arctan function """
    print ("arctan2(y={}, x={}) is : {}.".format(y, x, np.arctan2(y,x)))


def show_result(hists, bin_edges):
    """ check results """
    for b_edge in bin_edges/math.pi*180:
        print ('{0:.2f}\t'.format(round(b_edge))),
    print
    for hist in hists:
        print ('{0:.2f}\t'.format(hist)),
    print
    plt.figure(figsize=[10, 8])

    plt.bar(bin_edges[:-1], hists, width=0.5, color='#0504aa', alpha=0.7)
    plt.xlim(min(bin_edges), max(bin_edges))
    plt.grid(axis='y', alpha=0.75)
    plt.xlabel('Value', fontsize=15)
    plt.ylabel('Frequency', fontsize=15)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.ylabel('Frequency', fontsize=15)
    plt.title('Normal Distribution Histogram', fontsize=15)
    plt.show()


def gradient_histogram(flow_img, binsize=12):
    """ calculate histogram """
    assert len(flow_img.shape) == 3, "Wrong flow image."

    # NOTE the frame is in RGB, while cv2 is in BGR, so do REMEMBER to reverse it.
    img_mag, img_v, img_u = np.split(flow_img, 3, 2)

    # NOTE the role reversal: the "y-coordinate" is the first function parameter, the "x-coordinate" is the second.
    # NOTE that we use same axis configure as image axis(x is larger to the right, y is larger to the bottom),
    # so add a minus sign before img_v, to make the two axis align.
    orientation = np.arctan2(-img_v, img_u)

    # Original result not applicable
    # Directly use full 360 degree
    new_orient = orientation

    # Prune zero motion
    _mag_greater_zero = img_mag > 0.0
    pruned_orient = new_orient[_mag_greater_zero]

    # Histogram of optical flow
    hofbins = np.arange(-math.pi, math.pi+1e-6, 2*math.pi/binsize)
    hist, bin_edges = np.histogram(pruned_orient.flatten(), bins= hofbins) #, density=True)

    # Normalize
    hist = hist.astype(np.float32) / (np.sum(_mag_greater_zero) + 1e-6)


    return hist, bin_edges


def flow_orientation(orientation):
    """ Currently not use anymore """
    # Boolean map
    _greater_pi = orientation > math.pi/2
    _less_minuspi = orientation < -math.pi/2
    _remaining_part = ~(_greater_pi & _less_minuspi)

    # orientation map
    greater_pi = orientation*_greater_pi
    less_minuspi = orientation*_less_minuspi
    remaining_part = orientation*_remaining_part
    pi_map = math.pi * np.ones(orientation.shape)

    # converted orientation map
    convert_greater_pi = pi_map*_greater_pi - greater_pi
    convert_less_minuspi = -pi_map*_less_minuspi - less_minuspi

    new_orient = remaining_part + convert_greater_pi + convert_less_minuspi

    return new_orient


def convert_flowimg(img):
    """ Convert flow image to numpy arr """
    flow_img = np.array(img, dtype=np.float32)
    flow_mag = flow_img - 128.0
    flow_mag = flow_mag / 128.0

    return flow_mag


if __name__ == '__main__':
    checker()
    print (flow_to_hist(cv2.imread('C:\\Users\\DELL\\PycharmProjects\\anomaly_detection\\Deep360Pilot-optical-flow-master\\hist_of_opt_flow\\ZzBVziOgi8g_4\\1_1.jpg')))


