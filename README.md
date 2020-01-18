# Solving SUDOKU with convolutions


The following will walk you through solving [sudoku game](https://en.wikipedia.org/wiki/Sudoku) automatically with a computer vision technique. The computer vision technique used here is a [convolution](https://en.wikipedia.org/wiki/Convolution). The idea is simple, for identifying numbers on greed, kernels of different numbers are convolved. After numbers on greed have been identified, we use `soduku.py` to solve the sudoku game. The notebook uses two sets of temples and two additional python scripts:

 - `axillary.py` 
 - `sudoku.py` - credits go to [Nesh Patel](https://medium.com/@neshpatel/solving-sudoku-part-i-7c4bb3097aa7)
 
### **Table of content**

1. [Import sudoku an image](#image)
2. [Import tamplet sets](#sets)
3. [Normalize the image](#normalize)
4. [Solve sudoku and visualize the results](#results)
    1. [Run the two sets of templets over the image and plot the result](#2sets)




***Side note:***

The proposed algorithm is not optimal. For some images of sudoku, the algorithm might not be able to identify numbers on the agreed. That depends on the rotation and the tilt of the sudoku greed on an image.
