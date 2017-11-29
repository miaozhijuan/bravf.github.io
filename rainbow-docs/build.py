#!/usr/bin/python
#coding:utf-8
import os,sys,time,json

#fepack 集成
with open('fepack.json') as f:
    fedogConfig = json.loads(f.read())

#前端项目名
project = fedogConfig['release']['project']

def exeCmd(cmd):
    print '------------------------------------------------------'
    print cmd
    os.system(cmd)

def releaseWww():
    currPath = os.getcwd()

    #进行打包编译
    cmd = 'fepack release www'
    exeCmd(cmd)

    os.chdir('../bravf.github.io/')
    exeCmd('git add .')
    exeCmd('git commit -m "auto commit" *')
    exeCmd('git push')

def main():
    releaseWww()

if __name__ == "__main__":
    main()
