#!/bin/bash
##----------------------------------------------------------------------------##
##       █      █                                                             ##
##       ████████                                                             ##
##     ██        ██     File    : compilecocos.sh                             ##
##    ███  █  █  ███    Project : Cocos2d_Compile_Helpers                     ##
##    █ █        █ █    Author  : N2OMatt                                     ##
##     ████████████     Date    : Mon Aug 15 13:32:01 2016 UTC                ##
##   █              █                                                         ##
##  █     █    █     █  Copyright (c) 2016                                    ##
##  █     █    █     █  AmazingCow - www.AmazingCow.com                       ##
##   █              █                                                         ##
##     ████████████     This File / Project is PROPRIETARY                    ##
##                                                                            ##
##                          Enjoy :)                                          ##
##----------------------------------------------------------------------------##

MODE=$1
PLATFORM=$2;
COCOS=cocos-console

################################################################################
## Android                                                                    ##
################################################################################
if [ "$PLATFORM" == "android" ]; then
    ## Clean
    if [ "$MODE" == "clean" ]; then
        echo "Cleaning Android.";
        ./clean_android.sh
    ## Compile
    else
        $COCOS $MODE --android-studio                          \
                     --target android-19                       \
                     --ap android-19                           \
                     --ndk-mode debug                          \
                     --ndk-toolchain arm-linux-androideabi-4.9 \
                     --platform android                        \
                     --app-abi armeabi
    fi;

################################################################################
## Linux                                                                      ##
################################################################################
else
    ## Cleen
    if [ "$MODE" == "clean" ]; then
        echo "Cleaning Linux.";
        ./clean_linux.sh
    else
        echo "Compiling for linux";
        $COCOS $MODE -p linux
    fi;
fi;
