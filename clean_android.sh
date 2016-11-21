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
## Assets
rm -rf proj.android-studio/app/assets
## Build
rm -rf proj.android-studio/build
rm -rf proj.android-studio/app/build
rm -rf proj.android-studio/app/libs
rm -rf proj.android-studio/app/obj
## Res
rm -rf proj.android-studio/app/res/mipmap-hdpi/
rm -rf proj.android-studio/app/res/mipmap-mdpi/
rm -rf proj.android-studio/app/res/mipmap-xhdpi/
rm -rf proj.android-studio/app/res/mipmap-xxhdpi/
rm -rf proj.android-studio/app/res/mipmap-xxxhdpi/
