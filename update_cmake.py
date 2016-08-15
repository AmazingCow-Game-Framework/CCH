#!/usr/bin/python
##----------------------------------------------------------------------------##
##       █      █                                                             ##
##       ████████                                                             ##
##     ██        ██     File    : update_cmake.py                             ##
##    ███  █  █  ███    Project : Cocos2d_Compile_Helpers                     ##
##    █ █        █ █    Author  : N2OMatt                                     ##
##     ████████████     Date    : Mon Aug 15 13:31:20 2016 UTC                ##
##   █              █                                                         ##
##  █     █    █     █  Copyright (c) 2016                                    ##
##  █     █    █     █  AmazingCow - www.AmazingCow.com                       ##
##   █              █                                                         ##
##     ████████████     This File / Project is PROPRIETARY                    ##
##                                                                            ##
##                          Enjoy :)                                          ##
##----------------------------------------------------------------------------##


################################################################################
## Imports                                                                    ##
################################################################################
import os;
import sys;
import getopt;


################################################################################
## Constants                                                                  ##
################################################################################
kORIGINAL_FILE = os.path.join(os.path.split(__file__)[0],"CMakeLists_Original.txt");
kTARGET_FILE   = "CMakeLists.txt";



################################################################################
## Functions                                                                  ##
################################################################################
def add_definitions(target_file, lines):
    kDEFINITION_FORMAT = "    ADD_DEFINITIONS(-D{0})\n";

    clean_lines = [];
    for line in lines:
        if(line == "\n" or line.startswith("--")):
            continue;
        clean_lines.append(line);

    lines = clean_lines;

    for line in lines:
        line = line.replace("\n", "");
        write_line(target_file, kDEFINITION_FORMAT.format(line));


def add_include_directories(target_file, lines):
    kINCLUDE_FORMAT = "    {0}\n";

    clean_lines = [];
    for line in lines:
        if(line == "\n" or line.startswith("--")):
            continue;
        clean_lines.append(line);

    lines = clean_lines;

    for line in lines:
        line = line.replace("\n", "");
        write_line(target_file, kINCLUDE_FORMAT.format(line));


def add_game_sources(target_file, lines):
    kSOURCE_FORMAT = "    {0}\n";

    for line in lines:
        line = line.replace("\n", "");
        write_line(target_file, kSOURCE_FORMAT.format(line));


################################################################################
## Helpers Functions                                                          ##
################################################################################
def write_line(target_file, line):
    target_file.write(line);

def canonize(path):
    return os.path.abspath(os.path.expanduser(path));


################################################################################
## Script Initialization                                                      ##
################################################################################
def main():
    working_dir           = None;
    game_sources_def_path = None;
    include_dirs_def_path = None;
    android_defs_path     = None;
    linux_defs_path       = None;

    ## COWTODO: Clean up the parsing stuff.
    ## Parse the command line options.
    options = getopt.gnu_getopt(
        sys.argv[1:],
        "",
        ["working-dir=",
         "game-sources=",
         "include-dirs=",
         "android-defs=",
         "linux-defs="]
    );

    for key, value in options[0]:
        key = key.lstrip("-");
        if(key == "working-dir"):
            working_dir = canonize(value);
        elif(key == "game-sources"):
            game_sources_def_path = canonize(value);
        elif(key == "include-dirs"):
            include_dirs_def_path = canonize(value);
        elif(key == "android-defs"):
            android_defs_path = canonize(value);
        elif(key == "linux-defs"):
            linux_defs_path = canonize(value);

    if(working_dir           is None or \
       game_sources_def_path is None or \
       include_dirs_def_path is None or \
       android_defs_path     is None or \
       linux_defs_path       is None):
        print "Missing parameters..."
        exit(1);



    original_file_path = kORIGINAL_FILE;
    target_file_path   = canonize(os.path.join(working_dir, kTARGET_FILE));

    print "Update the CMakeLists.txt";
    print "-----------";
    print "CWD:        %s" %(os.getcwd());
    print "Working dir %s" %(working_dir);
    print "-----------";
    print "Original File: %s" %(original_file_path);
    print "Target File  : %s" %(target_file_path);
    print "-----------";
    print "Game Sources Def:        %s" %(game_sources_def_path);
    print "Include Directories Def: %s" %(include_dirs_def_path);
    print "-----------";
    print "Android Def: %s" %(android_defs_path);
    print "Linux   Def: %s" %(linux_defs_path);
    print "-----------";
    print "Running..."


    ## Read the contents of the files.
    original_file_lines     = open(original_file_path).readlines();
    include_dir_file_lines  = open(include_dirs_def_path).readlines();
    game_sources_file_lines = open(game_sources_def_path).readlines();
    android_def_file_lines  = open(android_defs_path).readlines();
    linux_def_file_lines    = open(linux_defs_path).readlines();

    ## Open the target file for writting..
    target_file = open(target_file_path, "w");

    for line in original_file_lines:
        if("__UPDATE_CMAKE_ADD_DEFINITIONS_ANDROID__" in line):
            add_definitions(target_file, android_def_file_lines);

        elif("__UPDATE_CMAKE_ADD_DEFINITIONS_LINUX__" in line):
            add_definitions(target_file, linux_def_file_lines);

        elif("__UPDATE_CMAKE_INCLUDE_DIRECTORIES__" in line):
            add_include_directories(target_file, include_dir_file_lines);

        elif("__UPDATE_CMAKE_GAME_SOURCES__" in line):
            add_game_sources(target_file, game_sources_file_lines);

        else:
            write_line(target_file, line);

    target_file.close();

main();
