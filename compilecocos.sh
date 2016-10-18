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


################################################################################
## "Constants"                                                                ##
################################################################################
## Gets the current script directory
## Taken from:
##      http://stackoverflow.com/questions/242538/unix-shell-script-find-out-which-directory-the-script-file-resides
SCRIPT=$(readlink -f "$0")
SCRIPTPATH=$(dirname "$SCRIPT")

COCOS=cocos-console


################################################################################
## VARS                                                                       ##
################################################################################
MODE=$1
PLATFORM=$2;
BUILD_MODE=$3
ARCH=$4


################################################################################
## Android                                                                    ##
################################################################################
if [ "$PLATFORM" == "android" ]; then
    ## Clean
    if [ "$MODE" == "clean" ]; then
        echo "Cleaning Android.";
        "$SCRIPTPATH"/clean_android.sh

    ## Compile
    else
        ## Mode was not specified.
        if [ -z "$BUILD_MODE" ]; then
            BUILD_MODE="debug";
            echo "BUILD_MODE was not specified - Setting to $BUILD_MODE";
        fi;

        ## Architeture was not specified.
        if [ -z "$ARCH" ]; then
            ARCH="armeabi";
            echo "ARCH was not specified - Setting to $ARCH";
        fi;

        $COCOS $MODE --android-studio       \
                     --platform android     \
                     --ndk-mode $BUILD_MODE \
                     --app-abi  $ARCH
                     # --target android-19                       \
                     # --ap android-19                           \
                     # --ndk-toolchain arm-linux-androideabi-4.9 \
    fi;

################################################################################
## Linux                                                                      ##
################################################################################
else
    ## Cleen
    if [ "$MODE" == "clean" ]; then
        echo "Cleaning Linux.";
        "$SCRIPTPATH"/clean_linux.sh
    else
        echo "Compiling for linux";
        $COCOS $MODE -p linux
    fi;
fi;
