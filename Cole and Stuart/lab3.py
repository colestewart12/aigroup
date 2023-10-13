"""
 Name: Cole Stewart, Jonah Mulcrone and Stuart Gavidia
 Assignment: Lab 3 - Process dataset
 Course: CS 330
 Semester: Fall 2023
 Instructor: Dr. Cao
 Date: 10/11/2023
 Sources consulted: any books, individuals, etc. consulted

 Known Bugs: description of known bugs and other program imperfections

 Creativity: anything extra that you added to the lab

 Instructions: instructions to user on how to execute your program

"""
import csv
import sys
import argparse
import math
import random


def splitData(data, trainData, testData, ratio):
    """
    Input: data Output: trainData, used for training your machine learning model testData, used to evaluate the
    performance of your machine learning model ratio, decide the percentage of training data on the whole dataset.
    Example: You have a training data with 10000 data record, ratio is 0.7, so you will split the whole dataset and
    store the first 7000 of them in trainData, and the rest 3000 in testData Instruction: There is no grading script
    for this function, because different group may select different dataset depending on their course project,
    but generally you should make sure that you code can divide the dataset correctly, since you may use it for the
    course project
    """
    length = 0
    with open(data, "r") as file, open(trainData, "w") as train, open(testData, "w") as test:
        Lines = file.readlines()
        for line in Lines:
            length += 1
            # writing headers
            if length == 1:
                train.write(line)
                test.write(line)
                continue
            if not line:
                break
            if length < ratio * len(Lines):
                train.write(line)
            else:
                test.write(line)


def splitDataRandom(data, trainData, testData, ratio):
    """
    Input: data Output: trainData, used for training your machine learning model testData, used to evaluate the
    performance of your machine learning model ratio, decide the percentage of training data on the whole dataset.
    Example: You have a training data with 10000 data record, ratio is 0.7, so you will split the whole dataset and
    store 7000 of them in trainData, and 3000 in testData. Instruction: Almost same as splitData, the only difference
    is this function will randomly shuffle the input data, so you will randomly select data and store it in the
    trainData
    """
    length = 0
    with open(data, "r") as file, open(trainData, "w") as train, open(testData, "w") as test:
        Lines = file.readlines()
        for line in Lines:
            length += 1
            # Writing headers
            if length == 1:
                train.write(line)
                test.write(line)
                # Remove headers from data
                Lines.pop(0)
                # Randomize training data
                random.shuffle(Lines)
                continue
            if not line:
                break
            if length < ratio * len(Lines):
                train.write(line)
            else:
                test.write(line)


def main():
    """
    This function is the main function that will be executed when the script is run.
    """
    mode = "N"
    ratio = 0.7
    print("mode is " + mode + " ratio is " + str(ratio))
    if mode == "N":
        splitData("data.csv", "trainData.txt", "testData.txt", ratio)
    elif mode == "R":
        splitDataRandom("data.csv", "randomTrainData.txt", "randomTestData.txt", ratio)
    else:
        showHelper()


def showHelper():
    """
    Similar to Lab 2, please update the showHelper function to show users how to use your code
    """
    parser.print_help(sys.stderr)
    """
    In main you are going to want to change the mode you want between normal and random
    You will also want to update the ratio of data in each file
    """

    sys.exit(0)


if __name__ == "__main__":
    # ------------------------arguments------------------------------#
    # Shows help to the users                                        #
    # ---------------------------------------------------------------#
    parser = argparse.ArgumentParser()
    parser._optionals.title = "Arguments"
    parser.add_argument('--mode', dest='mode',
                        default='',  # default empty!
                        help='Mode: R for random splitting, and N for the normal splitting')
    main()
