#!/usr/bin/env pythone3
# created by: Andrei Chirilov
# created on: Spetember 2019
# This program calculates the circumference of a circle


import constants


def main():
    # this function calculated the circumference
    # input
    radius = int(input("Enter radius of the circle (mm): "))
    
    # process
    circumference = constants.TAU*radius

    # output
    print("")
    print("Circumference is {}mm2".format(circumference))
    
    
if __name__ == "__main__":
    main()
