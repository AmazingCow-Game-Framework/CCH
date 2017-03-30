#!/bin/bash
##----------------------------------------------------------------------------##
##               █      █                                                     ##
##               ████████                                                     ##
##             ██        ██                                                   ##
##            ███  █  █  ███        compilecocos.sh                           ##
##            █ █        █ █        CCH                                       ##
##             ████████████                                                   ##
##           █              █       Copyright (c) 2016, 2017                  ##
##          █     █    █     █      AmazingCow - www.AmazingCow.com           ##
##          █     █    █     █                                                ##
##           █              █       N2OMatt - n2omatt@amazingcow.com          ##
##             ████████████         www.amazingcow.com/n2omatt                ##
##                                                                            ##
##                  This software is licensed as GPLv3                        ##
##                 CHECK THE COPYING FILE TO MORE DETAILS                     ##
##                                                                            ##
##    Permission is granted to anyone to use this software for any purpose,   ##
##   including commercial applications, and to alter it and redistribute it   ##
##               freely, subject to the following restrictions:               ##
##                                                                            ##
##     0. You **CANNOT** change the type of the license.                      ##
##     1. The origin of this software must not be misrepresented;             ##
##        you must not claim that you wrote the original software.            ##
##     2. If you use this software in a product, an acknowledgment in the     ##
##        product IS HIGHLY APPRECIATED, both in source and binary forms.     ##
##        (See opensource.AmazingCow.com/acknowledgment.html for details).    ##
##        If you will not acknowledge, just send us a email. We'll be         ##
##        *VERY* happy to see our work being used by other people. :)         ##
##        The email is: acknowledgment_opensource@AmazingCow.com              ##
##     3. Altered source versions must be plainly marked as such,             ##
##        and must not be misrepresented as being the original software.      ##
##     4. This notice may not be removed or altered from any source           ##
##        distribution.                                                       ##
##     5. Most important, you must have fun. ;)                               ##
##                                                                            ##
##      Visit opensource.amazingcow.com for more open-source projects.        ##
##                                                                            ##
##                                  Enjoy :)                                  ##
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
