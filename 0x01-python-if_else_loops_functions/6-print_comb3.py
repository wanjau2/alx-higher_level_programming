#!/usr/bin/python3
for i in range(10):
    for j in range(i+1, 10):
        print(f"{i}{j:02d}", end=', ' if i != 9 or j != 8 else '\n')
