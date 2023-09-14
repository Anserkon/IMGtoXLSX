# IMGtoXLSX
Useless but fun code, that allows you to create excel table from any picture

The image must be in the same folder with the executable file, otherwise you need to specify the full path

The input looks like this: example.jpg

The code itself scales the image so as to remove the distortion associated with the visual length of the lines, and also reduces it for performance. at your own risk, you can comment out line 17 "resize", but I warned you.

There is an unfinished part in the code where grayscale is provided using ASCII characters, but I didn't like how it looks
