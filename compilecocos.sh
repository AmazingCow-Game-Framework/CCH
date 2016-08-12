#!/bin/bash

MODE=$1
PLATFORM=$2;
COCOS=/home/n2omatt/Documents/Packages/AndroidDev/cocos2d-x-3.12/tools/cocos2d-console/bin/cocos

./update_cmake.py
./update_androidmk.py

if [ "$PLATFORM" == "android" ]; then
    $COCOS $MODE --android-studio \
                --target android-24 \
                --ap android-24 \
                --ndk-mode debug \
                --ndk-toolchain arm-linux-androideabi-4.9  \
                --platform android \
                --app-abi armeabi
else
    echo "Compiling for linux";
    $COCOS compile -p linux
fi;
