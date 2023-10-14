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
import pandas as pd


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

def splitThree(data, trainData, testData, validationData, ratios):
    """
    Input: data Output: trainData, used for training your machine learning model testData, used to evaluate the
    performance of your machine learning model ratios,validationData, used for validating the results, ratios decide the percentage of trainingData:testData:validationData.
    Example: You have a training data with 10000 data record, ratio is 0.7, so you will split the whole dataset and
    store 7000 of them in trainData, and 3000 in testData. Instruction: Almost same as splitData, the only difference
    is this function will randomly shuffle the input data, so you will randomly select data and store it in the
    trainData
    """
    ratio1, ratio2, ratio3 = ratios

    with open(data, "r") as file:
        Lines = file.readlines()
        total_lines = len(Lines) - 1

        header_line = Lines[0]

        train_boundary = int(total_lines * ratio1)
        test_boundary = train_boundary + int(total_lines * ratio2)
        
        train_lines = Lines[1:train_boundary+1]
        test_lines = Lines[train_boundary+1:test_boundary+1]
        validation_lines = Lines[test_boundary+1:]

        with open(trainData, "w") as train:
            train.write(header_line)
            train.writelines(train_lines)
        with open(testData, "w") as test:
            test.write(header_line)
            test.writelines(test_lines)
        with open(validationData, "w") as validation:
            validation.write(header_line)
            validation.writelines(validation_lines)

def main(args):
    """
    This function is the main function that will be executed when the script is run.
    """
    #Extract arguments or use defaults
    mode = args.mode
    ratio = args.r
    ratios = args.ratios
    ratios = valid_ratios(ratios)
    team = args.team
    team = valid_team(team)

    if mode == "V":
        print("mode is " + mode + " ratios are " + str(ratios))
        splitThree("data.csv", "trainData.txt", "testData.txt", "validationData.txt", ratios)
    elif mode == "N":
        print("mode is " + mode + " ratio is " + str(ratio))
        splitData("data.csv", "trainData.txt", "testData.txt", ratio)
    elif mode == "R":
        print("mode is " + mode + " ratio is " + str(ratio))
        splitDataRandom("data.csv", "randomTrainData.txt", "randomTestData.txt", ratio)
    elif mode == "A":
        print("mode is " + mode + ": Game duration statistics for " + team + " in 2016.")
        analysis(team)
    else:
        showHelper()

def analysis(team):

    df = pd.read_csv('data.csv')
    mask = df['homeTeamName'] == str(team)
    filter = df[mask]

    average = filter['durationMinutes'].mean()
    minimum = filter['durationMinutes'].min()
    maximum = filter['durationMinutes'].max()

    print(f"Year: 2016")
    print(f"Average Game Duration in Minutes: {average}")
    print(f"Minimum Game Duration in Minutes: {minimum}")
    print(f"Maximum Game Duration in Minutes: {maximum}")
    

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

def valid_r(value):
    """
    Checks that the command line argument value is a numeric and is between 0 and 1, if none provided then provides a default of 0.7
    """
    if value in ['']:
        return 0.7
    try:
        value_float = float(value)
        if 0 < value_float < 1:
            return value_float
        else:
            raise argparse.ArgumentTypeError(f"Invalid value {value}. 'r' must be between 0 and 1 (exclusive).")
    except ValueError:
        raise argparse.ArgumentTypeError(f"Invalid value {value}. 'r' must be a decimal number between 0 and 1 (exclusive).")

def valid_mode(value):
    """
    Checks that the command line argument values falls into a list (N, R, V, or A), if none provided then provides a default of N
    """
    if value in ['']:
        return 'N'
    if value in ['N', 'R', 'V', 'A']:
        return value
    else:
        raise argparse.ArgumentTypeError(f"Invalid value {value}. 'mode' must be either 'N', 'R', 'V', or 'A'.")

def valid_ratios(ratios):
    if not 0.99 <= sum(ratios) <= 1.01: 
        raise argparse.ArgumentTypeError("The sum of the ratios must be 1.")

    return ratios

def valid_team(team):

    df = pd.read_csv("data.csv")
    mask = list(df['homeTeamName'].unique())

    if team in mask:
        return team
    else:
        raise argparse.ArgumentTypeError(f"Invalid team: {team}.")
    
if __name__ == "__main__":
    # ------------------------arguments------------------------------#
    # Shows help to the users                                        #
    # ---------------------------------------------------------------#
    parser = argparse.ArgumentParser()
    parser._optionals.title = "Arguments"
    parser.add_argument('--mode', dest='mode', type=valid_mode,
                        default='',  # default empty!
                        help='Mode: R for random splitting, N for the normal splitting, and V for a three datasets including Validation')
    parser.add_argument('--r', dest='r', type=valid_r,
                        default='',  # default empty!
                        help='Ratio: takes a numeric value r that is used to split the dataset that follows this rule: 0 < r < 1')
    parser.add_argument('--ratios', dest='ratios', type=float, nargs=3, default=[0.3, 0.3, 0.4],
                        help='Ratios: takes three numeric values that are used to split the training, testing, and validation datasets in the order training:testing:validation with the ratios needing to add to 1')
    parser.add_argument('--team', dest='team', type=str, default="Indians",
                        help='Enter team name to be passed into args for analysis method.')
    
    args = parser.parse_args()
    main(args)
