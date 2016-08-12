#!/usr/bin/python

import os;


def add_include_directories(target_file):
    definitions = [
        "Classes/CoreMemory/include",
        "Classes/CoreMemory/lib/CoreCoord/include",
        "Classes/CoreMemory/lib/CoreRandom/include",
        "Classes/MonsterFramework",
        # "Classes/",
    ];

    for i in xrange(len(definitions)):
        curr_def = definitions[i];
        write_line(target_file, "    $(LOCAL_PATH)/../../../{0} \\\n".format(curr_def));

    curr_def = definitions[-1];
    write_line(target_file, "    $(LOCAL_PATH)/../../../{0} \n".format(curr_def));


def add_game_sources(target_file):
    os.system("rm -rf game_sources.temp");
    os.system("find Classes -iname \"*.cpp\" >> game_sources.temp");
    os.system("find Classes -iname \"*.c\" >> game_sources.temp");
    for line in open("game_sources.temp").readlines():
        line = line.replace("\n", "");
        write_line(target_file, "    ../../../{0} \\\n".format(line));
    os.system("rm -rf game_sources.temp");


def write_line(target_file, line):
    target_file.write(line);


def main():
    original_file = open("./proj.android-studio/app/jni/Android_Original.mk").readlines();
    target_file   = open("./proj.android-studio/app/jni/Android.mk", "w");

    for line in original_file:
        if("__UPDATE_CMAKE_INCLUDE_DIRECTORIES__" in line):
            add_include_directories(target_file);

        elif("__UPDATE_CMAKE_GAME_SOURCES__" in line):
            add_game_sources(target_file);

        else:
            write_line(target_file, line);

    target_file.close();

main();
