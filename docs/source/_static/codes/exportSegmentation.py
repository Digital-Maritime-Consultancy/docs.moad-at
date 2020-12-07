'''
Copyright (c) 2020 Jinki Jung (Digital Maritime Consultancy ApS)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

from skimage import io, segmentation, transform
import numpy as np
from os import listdir
from os.path import isfile, join
import os
import json
# main.py
import sys
def create_segment_file(input_folder, output_folder, given_width, given_height):
    file_list = [f for f in listdir(input_folder) if isfile(join(input_folder, f))]
    file_list = [k for k in file_list if '.jpg' in k or '.png' in k]
    count = 0
    for file_name in file_list:
        img = io.imread(input_folder + '/' + file_name)
        resized = transform.resize(img, (int(given_height), int(given_width)))
        seg = segmentation.slic(resized, n_segments=3000, compactness=20.0, enforce_connectivity=True, sigma=3, start_label=1)
        height, width, depth = resized.shape
        intermediate_file_name = output_folder + '/' + file_name + '_' + '_'.join(['raw', str(width), str(height)]) + '.json'
        output_file_name = output_folder + '/' + '_'.join(
            [file_name, str(width), str(height)]) + '.seg'
        np.savetxt(intermediate_file_name, seg, fmt="%s")
        convertFormat(intermediate_file_name, output_file_name)
        print (str(count+1) + '/' + str(len(file_list)) + '\t' +output_file_name + ' has exported.')
        count += 1

def convertFormat(inputFileName, outputFileName):
    f = open(inputFileName)
    d = dict()
    index = 0
    for line in f:
        for label in line.strip().split(' '):
            if not label in d:
                d[label] = str(index)
            else:
                d[label] += "," + str(index)
            index += 1
    of = open(outputFileName, 'w')
    of.write(json.dumps(d))
    of.close()
    f.close()
    os.remove(inputFileName)

def convert(imageFolderName, outputFolderName, width, height):
    if imageFolderName and outputFolderName and width and height:
        create_segment_file(imageFolderName, outputFolderName, width, height)

if __name__ == "__main__":
    imageFolderName = sys.argv[1]
    outputFolderName = sys.argv[2]
    width = sys.argv[3]
    height = sys.argv[4]
    convert(imageFolderName, outputFolderName, width, height)

# Example from source code: convert('./images', './', 1024, 768)
# Example from terminal: python exportSegmentation.py ./images ./ 1024 768