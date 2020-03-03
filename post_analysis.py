import os
import numpy as np
from PIL import Image
from PIL.Image import FLIP_LEFT_RIGHT

import matplotlib.pyplot as plt
from skimage import data, color
from skimage.transform import rescale, resize, downscale_local_mean

import torch
import torchvision.transforms as transforms
from torchvision.utils import save_image

from scipy import fftpack
import scipy as sp

def spectrum1(h, dt=1):
    """
    First cut at spectral estimation: very crude.
    
    Returns frequencies, power spectrum, and
    power spectral density.
    Only positive frequencies between (and not including)
    zero and the Nyquist are output.
    """
    nt = len(h)
    npositive = nt//2
    pslice = slice(1, npositive)
    freqs = np.fft.fftfreq(nt, d=dt)[pslice] 
    ft = np.fft.fft(h)[pslice]
    psraw = np.abs(ft) ** 2
    # Double to account for the energy in the negative frequencies.
    psraw *= 2
    # Normalization for Power Spectrum
    psraw /= nt**2
    # Convert PS to Power Spectral Density
    psdraw = psraw * dt * nt  # nt * dt is record length
    return freqs, psraw, psdraw
    
    

name = './images/2300.png'
img = Image.open(name)
arr = np.array(img)


img = arr.transpose(-1, 0, 1) # we have to change the dimensions from height x width x channel (WHC) to channel x height x width (CWH)
#print(img)
print(img.shape)
#img = torch.from_numpy(np.asarray(img)) # create the image tensor
#print(img)
#print(img.shape)

# Select Subsection of image
img_subselect = img[:,2:102,2:102]
print(img_subselect.shape)
# Analysis of Image

# Sub-selection of image
img_subsub = img_subselect[:,1:26,0:100]
print(img_subsub.shape)
# Histogram Analysis

_ = plt.hist(img_subsub[0,:,:].flatten())  # arguments are passed to np.histogram
plt.title("Histogram for red channel")
plt.savefig('hist_red.png')
plt.clf()

_ = plt.hist(img_subsub[1,:,:].flatten())  # arguments are passed to np.histogram
plt.title("Histogram for green channel")
plt.savefig('hist_green.png')
plt.clf()

_ = plt.hist(img_subsub[2,:,:].flatten())  # arguments are passed to np.histogram
plt.title("Histogram for blue channel")
plt.savefig('hist_blue.png')
plt.clf()

# Signal Analysis
red = img_subsub[0,:,:]
green = img_subsub[1,:,:]
blue = img_subsub[2,:,:]

red_rows = 0
green_rows = 0
blue_rows = 0

# Selecting Rows
row = np.arange(img_subsub.shape[2])
for x in range(img_subsub.shape[1]):    
    # Signal Analysis
    red_rows += img_subselect[0,x,:]
    green_rows += img_subselect[1,x,:]
    blue_rows += img_subselect[2,x,:]
#print(red_rows.shape)
#print(row)
plt.plot(row, red_rows, color='red', linestyle='dashed',linewidth=2)
plt.savefig('time_series_red.png')
plt.clf()
plot2 = plt.plot(row, green_rows, color='green', linestyle='dashed',linewidth=2)
plt.savefig('time_series_green.png')
plt.clf()
plot3 = plt.plot(row, blue_rows, color='blue', linestyle='dashed',linewidth=2)    
plt.savefig('time_series_blue.png')  
plt.clf()     

# Frequency Analysis
dt = 0.001
freqs1, ps1, psd1 = spectrum1(red_rows, dt=dt)

fig, axs = plt.subplots(ncols=1, sharex=True)
axs.loglog(freqs1, ps1, 'r', alpha=0.5)
axs.set_title('Power Spectrum')
axs.axis('tight', which='x');

fig.savefig('freq_red.png')
plt.clf()     

freqs2, ps2, psd2 = spectrum1(green_rows, dt=dt)

fig, axs = plt.subplots(ncols=1, sharex=True)
axs.loglog(freqs2, ps2, 'g', alpha=0.5)
axs.set_title('Power Spectrum')
axs.axis('tight', which='x');

fig.savefig('freq_green.png')
plt.clf()     

freqs3, ps3, psd3 = spectrum1(blue_rows, dt=dt)

fig, axs = plt.subplots(ncols=1, sharex=True)
axs.loglog(freqs3, ps3, 'b', alpha=0.5)
axs.set_title('Power Spectrum')
axs.axis('tight', which='x');

fig.savefig('freq_blue.png')
plt.clf()     


#img = np.asarray(img).transpose(1, 2, 0) # we have to change the dimensions from width x height x channel (WHC) to channel x width x height (CWH)
#im = transforms.ToPILImage()(img_subselect).convert("RGB")
#im.save("images/trial.png")
