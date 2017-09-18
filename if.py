#!/usr/bin/env python3

age = input("Enter your age: ")
age = int(age)
have_own_car = input("Do you can own your own car (y/n):")

if (age > 21) and (have_own_car == "y"):
    print("You are over 21 years old and own your own car")

if (age > 21) and (have_own_car == "n"):
    print("You are over 21 years old and you donot own your own car")

if (age == 21) and (have_own_car == "y"):
    print("You are 21 years old and own your own car")

if (age == 21) and (have_own_car == "n"):
    print("You are over 21 years old and you do not own your own car")

if (age < 21) and (have_own_car == "y"):
    print("You are younger than 21 and own your own car")

if (age > 21) and (have_own_car == "n"):
    print("You are younger than 21 and you do not own your own car")