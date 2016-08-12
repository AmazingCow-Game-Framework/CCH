#!/usr/bin/python

import os;

def add_android_definitions(target_file):
    definitions = ["MONSTERFRAMEWORK_DEBUG",
                   "SQLITE_THREADSAFE=0",
                   "SQLITE_OMIT_LOAD_EXTENSION"];

def add_linux_definitions(target_file):
    definitions = ["MONSTERFRAMEWORK_DEBUG",
                   "SQLITE_THREADSAFE=0",
                   "SQLITE_OMIT_LOAD_EXTENSION"];

    for curr_def in definitions:
        write_line(target_file, "    ADD_DEFINITIONS(-D{0})\n".format(curr_def));

def add_include_directories(target_file):
    definitions = [
        "Classes/CoreMemory/include",
        "Classes/CoreMemory/lib/CoreCoord/include",
        "Classes/CoreMemory/lib/CoreRandom/include",
        "Classes/MonsterFramework",
        "Classes/",
    ];

    for curr_def in definitions:
        write_line(target_file, "    {0}\n".format(curr_def));

def add_game_sources(target_file):
    os.system("rm -rf game_sources.temp");
    os.system("find Classes -iname \"*.cpp\" >> game_sources.temp");
    os.system("find Classes -iname \"*.c\" >> game_sources.temp");
    for line in open("game_sources.temp").readlines():
        write_line(target_file, "    {0}".format(line));
    os.system("rm -rf game_sources.temp");


def write_line(target_file, line):
    target_file.write(line);


def main():
    original_file = open("CMakeLists_Original.txt").readlines();
    target_file   = open("CMakeLists.txt", "w");

    for line in original_file:
        if("__UPDATE_CMAKE_ADD_DEFINITIONS_ANDROID__" in line):
            add_android_definitions(target_file);

        elif("__UPDATE_CMAKE_ADD_DEFINITIONS_LINUX__" in line):
            add_linux_definitions(target_file);

        elif("__UPDATE_CMAKE_INCLUDE_DIRECTORIES__" in line):
            add_include_directories(target_file);

        elif("__UPDATE_CMAKE_GAME_SOURCES__" in line):
            add_game_sources(target_file);

        else:
            write_line(target_file, line);

    target_file.close();

main();
