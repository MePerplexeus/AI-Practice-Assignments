# M30299 – Programming <br>(Python Coursework: A Patchwork Sampler)

## Task:
Your task is to write a program to display and edit patchwork samples, an example of which is illustrated below. The actual patchworks your program will display will depend on your student number and on the user’s inputs.

![Patchwork Sample (2000902)](https://github.com/MePerplexeus/AI-Practice-Assignments/blob/master/2020_12_30_Patchwork_Sampler/PatchworkSample(2000902).jpg?raw=true)

A patchwork sample is made upof patches of two different designs and two or three different colours. Patchworks are square and can be of two different sizes: 5×5 patches or 7×7 patches. Each patch in the patchwork features a regular geometric design made up of lines, circles, rectangles and/or polygons and has dimensions of 100 × 100 pixels. The two patch designs and the layout and colouring of patches are not necessarily as given in the sample above. They are determined by the ﬁnal three digits of your student number, and are displayed inthe tables on the ﬁnal two pages. The layout and colouring of the patch designs is given by the antepenultimate digit of your student number. The two patch designs are given by the penultimate and ﬁnal digits of your student number. For example, if your student number is 2000902 (antepenultimate digit 9, penultimate digit 0 and ﬁnal digit 2), the patch designs and patch arrangement for a 5×5 patchwork with colours blue, green and red are those illustrated on page 1. 

It’s important that your program draws the patch designs accurately, and that it draws the correct designs, layout and colouring – you will receive no credit for drawing the wrong patch designs or patch arrangement. Your program should draw the patches using the facilities provided in the graphics module (Line, Circle etc.), and must not use images. The designs are intended to test algorithm development skills (e.g. they should involve the use of one or more for loops). For some of the designs, it will be useful to remember that shapes drawn later appear on top of those drawn earlier. You should not use parts of the Python language which we haven’t covered in this part of the module; for example, do not use exception handling and do not deﬁne your own classes.

## Main program requirements
Your program should begin by prompting the user, using a text (shell)-based interface, to enter: 
- the patchwork size (i.e. the common width & height in terms of patches); 
- three colours (your program should make sure the user gives atleast two different colours, so if colour 1 and colour 2 are the same, then your program needs to make sure colour 3 is different). 

The program’s user interface should be easy to use, helpful and robust; e.g., on entering invalid data, the user should be given appropriate feedback and re-prompted until the entered data is valid. (Valid sizes are 5 and 7, and valid colours are red, green, blue, magenta, orange and cyan.) Once these details have been entered, the patchwork sample should be drawn in a graphics window of the appropriate size. For example, if the user enters size 5, and colours blue, then green and ﬁnally red, then (in the case that your student number ends in 902) the patchwork shown on page 1 should be drawn in a graphics window of width 500 pixels and height 500 pixels.

#### Rest of the details can be found in the [M30299 – Programming (Python Coursework: A Patchwork Sampler) PDF](https://github.com/MePerplexeus/AI-Practice-Assignments/blob/master/2020_12_30_Patchwork_Sampler/pro.pdf)
