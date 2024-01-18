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
# from mpl_toolkits.mplot3d import Axes3D 
from matplotlib import cm # all the colormaps...


def vis_rgb_cube(I, numpoints=5000, fixaxis=True):
    '''
    vis_rgb_cube(I, numPoints=5000): Display RGB color cube for the image I
    '''
    assert len(I.shape)==3 and I.shape[-1]==3, \
           f'visRGB Error: I.shape should be 3-channel, got {I.shape}.'
    
    if I.dtype == 'uint8':
        assert I.min() >= 0 and I.max() <= 255, \
            f'visRGB Error: integer I should be in [0,255], got {(I.min(), I.max())}.'
            
    
    colr_func = lambda X: X/255
    if np.max(I) <= 1.0:
        colr_func = lambda X: X # colors must be in [0,1]

    fig = plt.figure(figsize=(4,4))
    ax = fig.add_subplot(111, projection='3d')

    # X is the N*M x 3 version of the image.
    X = np.stack([I[...,i].ravel() for i in range(3)]).T

    # https://numpy.org/doc/stable/reference/random/generated/numpy.random.choice.html
    randomInds = np.random.choice(np.arange(X.shape[0]), numpoints, replace=False)

    # Now plot those pixels in the 3d space.
    ax.scatter(X[randomInds,0], X[randomInds,1], X[randomInds,2], c=colr_func(X[randomInds, :]))
    if I.dtype == 'uint8' and fixaxis:
        ax.set_xlim3d(0, 255)
        ax.set_ylim3d(0, 255)
        ax.set_zlim3d(0, 255)

    # Label the axes.
    ax.set_xlabel('Red')
    ax.set_ylabel('Green')
    ax.set_zlabel('Blue');
    plt.tight_layout()
    
    
def vis_hsv_cube(I, numpoints = 5000):
    '''
    vis_hsv_cube(I, numPoints=5000): Display HSV color cylinder for the image I.
    Hue can be seen as P(phi), and Saturation as R(radius, ro) in polar coordinates. 
    Value is the Z. Easy, if you remember how to convert p,r to x,y.
    https://matplotlib.org/3.1.0/gallery/mplot3d/surface3d_radial.html
    '''
    
    Ihsv = color.rgb2hsv(I)
    
    P = 2*np.pi*Ihsv[...,0].ravel()
    R = Ihsv[...,1].ravel()
    Z = Ihsv[...,2].ravel()
    
    # Now transform P,R into X,Y for Euclidean scatter.
    X, Y = R*np.cos(P), R*np.sin(P)
    
    # Still need the RGBs for scatter colors
    # X is the N*M x 3 version of the image.
    Xrgb = np.stack([I[...,i].ravel() for i in range(3)]).T
    
    # Pick a random subset of the pixels to plot. Otherwise, pretty chaotic and slow.
    # https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.choice.html
    randomInds = np.random.choice(X.shape[0], numpoints, replace=False)

    # A function to normalize the color for the purpose of 
    # coloring scatter points.
    colr_func = lambda X: X/255
    if np.max(I) <= 1.0:
        colr_func = lambda X: X # colors must be in [0,1]
    
    fig = plt.figure(figsize=(4,4))
    ax = fig.add_subplot(111, projection='3d')
    
#     # point colors
#     point_colors = Xrgb[randomInds, :]
#     if point_colors.max() > 1:
#         point_colors = point_colors-point_colors.min()
#         point_colors = point_colors/point_colors.max()

    # Now plot those pixels in the 3d space.
    # depthshade defaults to True. I leave it there cause
    # the colors get all messed up if you put False though.
    ax.scatter(X[randomInds], Y[randomInds], Z[randomInds], 
               c=colr_func(Xrgb[randomInds, :]), depthshade=True)

    #Label the axes.
    ax.set_xlabel('H and S')
    ax.set_ylabel('H and S')
    ax.set_zlabel('Value')
    
    
def vis_lab_cube(I, numpoints = 5000):
    '''
    vis_lab_cube(I, numPoints=5000): Display L*a*b* color space for the image I.
    '''
    
    Ilab = color.rgb2lab(I)

    # for scattering
    Xlab = np.stack([Ilab[...,i].ravel() for i in range(3)]).T
#     Xlab = np.concatenate([np.expand_dims(Ichan, axis = 1) for Ichan in
#                            [Ilab[...,0].ravel(), Ilab[...,1].ravel(), Ilab[...,2].ravel()]], axis = 1)
    
    # Still need the RGBs for scatter colors
    # X is the N*M x 3 version of the image.
    Xrgb = np.stack([I[...,i].ravel() for i in range(3)]).T
# Old way of doing it. I'm much smarter now...
#     Xrgb = np.concatenate([np.expand_dims(Ichan, axis = 1) for Ichan in
#                            [I[...,0].ravel(), I[...,1].ravel(), I[...,2].ravel()]], axis = 1)
    
    # Pick a random subset of the pixels to plot. Otherwise, pretty chaotic and slow.
    # https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.choice.html
    randomInds = np.random.choice(np.arange(Xlab.shape[0]), numpoints, replace=False)

    # A function to normalize the color for the purpose of 
    # coloring scatter points.
    colr_func = lambda X: X/255
    if np.max(I) <= 1.0:
        colr_func = lambda X: X # colors must be in [0,1]
    
    
    fig = plt.figure(figsize=(4,4))
    ax = fig.add_subplot(111, projection='3d')


    #Now plot those pixels in the 3d space.
    ax.scatter(Xlab[randomInds,1], Xlab[randomInds,2], Xlab[randomInds,0], 
               c=colr_func(Xrgb[randomInds, :]), depthshade=True)

    #Label the axes.
    ax.set_xlabel('green->red')
    ax.set_ylabel('blue->yellow')
    ax.set_zlabel('Lightness')
    
    
def vis_ybr_cube(I, numpoints = 5000):
    '''
    vis_lab_cube(I, numPoints=5000): Display L*a*b* color space for the image I.
    '''
    
    Iybr = color.rgb2ycbcr(I)

    # for scattering
    Xybr = np.stack([Iybr[...,i].ravel() for i in range(3)]).T
    
    # Still need the RGBs for scatter colors
    # X is the N*M x 3 version of the image.
    Xrgb = np.stack([I[...,i].ravel() for i in range(3)]).T
    
    # Pick a random subset of the pixels to plot. Otherwise, pretty chaotic and slow.
    # https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.choice.html
    randomInds = np.random.choice(np.arange(Xybr.shape[0]), numpoints, replace=False)

    # A function to normalize the color for the purpose of 
    # coloring scatter points.
    colr_func = lambda X: X/255
    if np.max(I) <= 1.0:
        colr_func = lambda X: X # colors must be in [0,1]
    
    fig = plt.figure(figsize=(4,4))
    ax = fig.add_subplot(111, projection='3d')
    

    #Now plot those pixels in the 3d space.
    ax.scatter(Xybr[randomInds,0], Xybr[randomInds,1], Xybr[randomInds,2], 
               c=colr_func(Xrgb[randomInds, :]), depthshade=True)

    #Label the axes.
    ax.set_xlabel('Lightness (Y)')
    ax.set_ylabel('yellow->blue (Cb)')
    ax.set_zlabel('cyan->red (Cr)')
    

def vis_image(I, figsize=(4,3), title='Image', show_ticks = True, **kwargs):
    '''
    vis_image(I, figsize=(4,3), title='Image', show_ticks = True, **kwargs): 
    plot an image. Very simple, but save a little typing.
    '''
    f, ax = plt.subplots(1,1, figsize=figsize)
    ax.imshow(I, **kwargs)
    ax.set_title(title)
    
    if not show_ticks:
        ax.get_xaxis().set_visible(False);
        ax.get_yaxis().set_visible(False);
    
    plt.tight_layout()

    
def vis_hists(I, bins = 256):
    '''
    vis_hists(I): plot the image and its three-channel histograms together.
    '''
#     assert len(I.shape)==3 and I.shape[-1]==3, \
#            f'vis_hists Error: I.shape should be 3-channel, got {I.shape}.'
    
    _, allbins = np.histogram(I.ravel(), bins=bins)
    
    f, axarr = plt.subplots(1,2, figsize=(9, 3))

    axarr[0].imshow(I, cmap=[None, 'gray'][len(I.shape)==2]) #https://matplotlib.org/api/_as_gen/matplotlib.pyplot.imshow.html
    axarr[0].set_title('Image')

    if len(I.shape) == 2:
        axarr[1].hist(I.ravel(), allbins, alpha = .8, label = 'gray', color = 'k');
    else:
        axarr[1].hist(I[...,0].ravel(), allbins, alpha = .6, label = 'red', color = 'r');
        axarr[1].hist(I[...,1].ravel(), allbins, alpha = .6, label = 'green', color = 'g');
        axarr[1].hist(I[...,2].ravel(), allbins, alpha = .6, label = 'blue', color = 'b');
    axarr[1].legend(loc = 'upper right');
    plt.tight_layout()
    
    
def vis_pair(I, J, figsize = (8,3), shared = True, 
             first_title = 'Original', second_title = 'New',
             show_ticks = True, **kwargs):
    '''
    vis_pair(I, J, figsize = (8,3), shared = True, first_title = 'Original', second_title = 'New'):
    produce a plot of images I and J together. By default takes care of sharing axes to provide
    a little 1x2 plot without all the coding.
    '''
    f, ax = plt.subplots(1,2, figsize=figsize, sharex = shared, sharey = shared)
    ax[0].imshow(I, **kwargs)
    ax[0].set_title(first_title)
    ax[1].imshow(J, **kwargs)
    ax[1].set_title(second_title)
    
    if not show_ticks:
        [a.axes.get_xaxis().set_visible(False) for a in ax];
        [a.axes.get_yaxis().set_visible(False) for a in ax];
    
    plt.tight_layout()
    
def vis_triple(I, J, K, figsize = (8,3), shared = True, 
               first_title = 'Original', second_title = 'New',
               third_title = 'Newer',
               show_ticks = True, **kwargs):
    '''
    vis_pair(I, J, figsize = (8,3), shared = True, first_title = 'Original', second_title = 'New'):
    produce a plot of images I and J together. By default takes care of sharing axes to provide
    a little 1x2 plot without all the coding.
    '''
    f, ax = plt.subplots(1,3, figsize=figsize, sharex = shared, sharey = shared)
    ax[0].imshow(I, **kwargs)
    ax[0].set_title(first_title)
    ax[1].imshow(J, **kwargs)
    ax[1].set_title(second_title)
    ax[2].imshow(K, **kwargs)
    ax[2].set_title(third_title)
    
    if not show_ticks:
        [a.axes.get_xaxis().set_visible(False) for a in ax];
        [a.axes.get_yaxis().set_visible(False) for a in ax];

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


# Thanks: https://matplotlib.org/3.1.0/gallery/mplot3d/surface3d.html
def vis_surface(Z):
    '''
    vis_surface(Z): Simple function to visualize an image as a surface.
    '''
    fig = plt.figure(figsize=(4,4))
    # ax = fig.gca(projection='3d')
    ax = fig.add_subplot(111, projection='3d')

    # Make data.
    X = np.arange(Z.shape[1])
    Y = np.arange(Z.shape[0])
    X, Y = np.meshgrid(X, Y)

    # Plot the surface.
    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                           linewidth=0, antialiased=False)

    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()
