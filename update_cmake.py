#!/usr/bin/python

import os;
import sys;

kORIGINAL_FILE = "CMakeLists_Original.txt";
kTARGET_FILE   = "CMakeLists.txt";


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


def write_line(target_file, line):
    target_file.write(line);

def canonize(path):
    return os.path.abspath(os.path.expanduser(path));


def main():
    working_dir           = canonize(sys.argv[1]);
    game_sources_def_path = canonize(sys.argv[2]);
    include_dirs_def_path = canonize(sys.argv[3]);
    android_defs_path     = canonize(sys.argv[4]);
    linux_defs_path       = canonize(sys.argv[5]);

    original_file_path = canonize(os.path.join(working_dir, kORIGINAL_FILE));
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
