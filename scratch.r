setwd(".../Project/R/Workspace/Task1")
library("EBImage"  , lib.loc="~/R/win-library/3.2")
library("fftwtools", lib.loc="~/R/win-library/3.2")
library("fftw", lib.loc="~/R/win-library/3.2")

# Image Acquisition
img <- readImage(".../Project/Beispielbilder/drmcircle.jpg")
display(img, title='Image')

# Grayscaled
img_gray<-channel(img,"gray")

# FFT
img_ff <- fft(img_gray)    #fftw2d

magntd <- sqrt(Re(img_ff)^2+Im(img_ff)^2)
phase  <- atan(Im(img_ff)/Re(img_ff))

plot(log(magntd),main="FFT")
