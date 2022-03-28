setwd(".../Project/R/Workspace/Task1")
library("EBImage"  , lib.loc="~/R/win-library/3.2")

# Image
img <- readImage(".../Project/Beispielbilder/drmtri.jpg")
display(img, title='Image')

# Grayscaled
img_gray<-channel(img,"gray")

# FFT
img_ff <- fft(img_gray) #fftw2d


# FFT SHIFT
fftshift <- function(img_ff, dim = -1) {

  rows <- dim(img_ff)[1]    
  cols <- dim(img_ff)[2]    

  swap_up_down <- function(img_ff) {
    rows_half <- ceiling(rows/2)
    return(rbind(img_ff[((rows_half+1):rows), (1:cols)], img_ff[(1:rows_half), (1:cols)]))
  }

  swap_left_right <- function(img_ff) {
    cols_half <- ceiling(cols/2)
    return(cbind(img_ff[1:rows, ((cols_half+1):cols)], img_ff[1:rows, 1:cols_half]))
  }

  if (dim == -1) {
    img_ff <- swap_up_down(img_ff)
    return(swap_left_right(img_ff))
  }
  else if (dim == 1) {
    return(swap_up_down(img_ff))
  }
  else if (dim == 2) {
    return(swap_left_right(img_ff))
  }
  else {
    stop("Invalid dimension parameter")
  }
}

ifftshift <- function(img_ff, dim = -1) {

  rows <- dim(img_ff)[1]    
  cols <- dim(img_ff)[2]    

  swap_up_down <- function(img_ff) {
    rows_half <- floor(rows/2)
    return(rbind(img_ff[((rows_half+1):rows), (1:cols)], img_ff[(1:rows_half), (1:cols)]))
  }

  swap_left_right <- function(img_ff) {
    cols_half <- floor(cols/2)
    return(cbind(img_ff[1:rows, ((cols_half+1):cols)], img_ff[1:rows, 1:cols_half]))
  }

  if (dim == -1) {
    img_ff <- swap_left_right(img_ff)
    return(swap_up_down(img_ff))
  }
  else if (dim == 1) {
    return(swap_up_down(img_ff))
  }
  else if (dim == 2) {
    return(swap_left_right(img_ff))
  }
  else {
    stop("Invalid dimension parameter")
  }
}

# FFT SHIFT

# Magnitude and Phase
magntd <- sqrt(Re(img_ff)^2+Im(img_ff)^2)
phase  <- atan(Im(img_ff)/Re(img_ff))

img_fftsh <- fftshift(magntd)

display(log(img_fftsh),title="FFT")
