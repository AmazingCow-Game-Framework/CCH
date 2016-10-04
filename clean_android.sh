#!/bin/bash
##----------------------------------------------------------------------------##
##       █      █                                                             ##
##       ████████                                                             ##
##     ██        ██     File    : clean_android.sh                            ##
##    ███  █  █  ███    Project : Cocos2d Compile Helpers                     ##
##    █ █        █ █    Author  : N2OMatt                                     ##
##     ████████████     Date    : Tue Oct  4 06:45:20 2016 UTC                ##
##   █              █                                                         ##
##  █     █    █     █  Copyright (c) 2016                                    ##
##  █     █    █     █  AmazingCow - www.AmazingCow.com                       ##
##   █              █                                                         ##
##     ████████████     This File / Project is PROPRIETARY                    ##
##                                                                            ##
##                          Enjoy :)                                          ##
##----------------------------------------------------------------------------##


## Clean everything about Android build.
rm -rf proj.android-studio/build
rm -rf proj.android-studio/app/assets
rm -rf proj.android-studio/app/build
rm -rf proj.android-studio/app/libs
rm -rf proj.android-studio/app/obj

