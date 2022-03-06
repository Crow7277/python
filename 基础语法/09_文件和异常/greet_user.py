"""
crow7
2021年07月03日
"""
import json

filename = 'username.json'

with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Welcome back, " + username + '!')
