'''
Image Processing Visualization Utilities
stough, 202-

Includes RGB color cube and three-channel histogramming.
Also a lab_uniform, which normalizes the perceived intensity of
custom colormaps.
'''

import matplotlib.pyplot as plt
import numpy as np
import skimage.color as color


def vis_rgb_cube(I, numPoints=5000):
    '''
    vis_rgb_cube(I, numPoints=5000): Display RGB color cube for the image I
    '''
    assert len(I.shape)==3 and I.shape[-1]==3, \
           f'visRGB Error: I.shape should be 3-channel, got {I.shape}.'
    
    if I.dtype == 'float':
        assert I.min() >= 0 and I.max() <= 1.0, \
            f'visRGB Error: float I should be in [0,1], got {(I.min(), I.max())}.'
    else:
        assert I.min() >= 0 and I.max() <= 255, \
            f'visRGB Error: integer I should be in [0,255], got {(I.min(), I.max())}.'
            
    
    colr_func = lambda X: X/255
    if np.max(I) <= 1.0:
        colr_func = lambda X: X # colors must be in [0,1]
    
    
    NUMPOINTS = 5000

    fig = plt.figure(figsize=(4,4))
    ax = fig.add_subplot(111, projection='3d')

    # X is the N*M x 3 version of the image.
    X = np.stack([I[...,i].ravel() for i in range(3)]).T

    # https://numpy.org/doc/stable/reference/random/generated/numpy.random.choice.html
    randomInds = np.random.choice(np.arange(X.shape[0]), NUMPOINTS, replace=False)

    # Now plot those pixels in the 3d space.
    ax.scatter(X[randomInds,0], X[randomInds,1], X[randomInds,2], c=colr_func(X[randomInds, :]))

    # Label the axes.
    ax.set_xlabel('Red')
    ax.set_ylabel('Green')
    ax.set_zlabel('Blue');
    plt.tight_layout()
    
    
def vis_hists(I):
    '''
    vis_hists(I): plot the image and its three-channel histograms together.
    '''
    assert len(I.shape)==3 and I.shape[-1]==3, \
           f'vis_hists Error: I.shape should be 3-channel, got {I.shape}.'
    
    _, allbins = np.histogram(I.ravel(), bins=256)
    
    f, axarr = plt.subplots(1,2, figsize=(9, 3))

    axarr[0].imshow(I) #https://matplotlib.org/api/_as_gen/matplotlib.pyplot.imshow.html
    axarr[0].set_title('Image')

    axarr[1].hist(I[...,0].ravel(), allbins, alpha = .6, label = 'red', color = 'r');
    axarr[1].hist(I[...,1].ravel(), allbins, alpha = .6, label = 'green', color = 'g');
    axarr[1].hist(I[...,2].ravel(), allbins, alpha = .6, label = 'blue', color = 'b');
    axarr[1].legend(loc = 'upper right');
    plt.tight_layout()
    
    
def lab_uniform(lyst):
    '''
    lab_uniform(lyst): intensity-normalize custom colormap list. return the normalized list.
    I want to be careful about my colormaps being uniform in perceived intensity: L*a*b* is the way to go.
    '''
    clyst = np.array(lyst, ndmin=3)
    clyst_lab = color.rgb2lab(clyst)
    # Give every one the average luminance.
    clyst_lab[...,0] = np.mean(clyst_lab[...,0].ravel())
    return color.lab2rgb(clyst_lab).squeeze()