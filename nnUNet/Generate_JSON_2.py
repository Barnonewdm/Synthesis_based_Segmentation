# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 13:49:23 2021

@author: dongming.wei@sjtu.edu.cn
"""
import glob
import os
import sys

def generate_json(imagesTr, imagesTs, training_str, testing_str):
    for filename in glob.glob(imagesTr+'/*'):
        training_str = training_str + "{\"image\":\"" + filename + "\",\"label\":\"./labelsTr/" + os.path.basename(filename) + "\"}," 
    
    for filename in glob.glob(imagesTs + '/*'):
        testing_str = testing_str + "\"" + filename + "\","
    
    return training_str, testing_str
    
if __name__ == '__main__':
    training_str = "\"training\":["
    testing_str = "\"test\":["
    
    training_str, testing_str = generate_json(imagesTr=sys.argv[1], imagesTs=sys.argv[2],
                                 training_str=training_str, testing_str=testing_str)
    training_str += "]"
    testing_str += "]"
    print(training_str)
    print(testing_str)