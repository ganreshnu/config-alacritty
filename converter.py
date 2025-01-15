#!/bin/env python
import sys, json

if len(sys.argv) == 1:
    print("nothing to convert!")
    exit(1)

filename = sys.argv[1]
with open(filename, 'r') as file:
    data = json.load(file)

colors = ["black", "red", "green", "yellow", "blue", "magenta", "cyan", "white"]

print("[colors.normal]")
for x in range(0, 8):
    print(f"{colors[x]} = '{data["color"][x]}'")

print("[colors.bright]")
for x in range(8, 16):
    print(f"{colors[x-8]} = '{data["color"][x]}'")

print("[colors.primary]")
print(f"foreground = '{data["foreground"]}'")
print(f"background = '{data["background"]}'")
