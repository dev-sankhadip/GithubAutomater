#!/usr/bin/env python3

import click
import os


@click.group()
def main():
    pass


@main.command()
@click.option('--msg', prompt="Commit message", required=True, type=str)
def push(msg):
    curDir = os.getcwd()
    files = os.listdir(curDir)
    if '.git' in files:
        print('already exists')
        os.system('git init')
        os.system('git add .')
        os.system(f'git commit -m "{msg}"')
        os.system('git push origin master')
    else:
        origin = input('Type github remote origin: ')
        print(origin)
        os.system('git init')
        os.system('git add .')
        os.system(f'git commit -m "{msg}"')
        os.system(f'git remote add origin {origin}')
        os.system('git push origin master')


if __name__=="__main__":
    main()