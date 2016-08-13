#!/usr/bin/python
import os;
import sys;

kORIGINAL_FILE = "proj.android-studio/app/jni/Android_Original.mk";
kTARGET_FILE   = "proj.android-studio/app/jni/Android.mk";


def add_include_directories(target_file, lines):
    kWRITE_FORMAT_WITH_ESCAPE    = "    $(LOCAL_PATH)/../../../{0} \\\n";
    kWRITE_FORMAT_WITH_NO_ESCAPE = "    $(LOCAL_PATH)/../../../{0} \n";

    write_lines(
        target_file,
        lines,
        kWRITE_FORMAT_WITH_ESCAPE,
        kWRITE_FORMAT_WITH_NO_ESCAPE
    );


def add_game_sources(target_file, lines):
    kWRITE_FORMAT_WITH_ESCAPE    = "    ../../../{0} \\\n";
    kWRITE_FORMAT_WITH_NO_ESCAPE = "    ../../../{0} \n";

    write_lines(
        target_file,
        lines,
        kWRITE_FORMAT_WITH_ESCAPE,
        kWRITE_FORMAT_WITH_NO_ESCAPE
    );


def write_lines(target_file, lines, espace_format, no_escape_format):
    clean_lines = [];
    for line in lines:
        if(line == "\n" or line.startswith("--")):
            continue;
        clean_lines.append(line);

    lines = clean_lines;

    ## We don't want the last line to be escaped
    ## so write all lines -1 with escape and
    ## let the last unescaped.
    for i in xrange(len(lines) -1):
        line = lines[i].replace("\n", "");
        write_line(target_file, espace_format.format(line));

    last_line = lines[-1];
    write_line(target_file, no_escape_format.format(last_line));

    ## Write a new line.
    write_line(target_file, "\n");


def write_line(target_file, line):
    target_file.write(line);


def canonize(path):
    return os.path.abspath(os.path.expanduser(path));

def main():
    working_dir           = canonize(sys.argv[1]);
    game_sources_def_path = canonize(sys.argv[2]);
    include_dirs_def_path = canonize(sys.argv[3]);

    original_file_path = canonize(os.path.join(working_dir, kORIGINAL_FILE));
    target_file_path   = canonize(os.path.join(working_dir, kTARGET_FILE));

    print "Update the Android.mk";
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
    print "Running..."

    ## Read the contents of the files.
    original_file_lines     = open(original_file_path).readlines();
    include_dir_file_lines  = open(include_dirs_def_path).readlines();
    game_sources_file_lines = open(game_sources_def_path).readlines();

    ## Open the target file for writting..
    target_file = open(target_file_path, "w");


    for line in original_file_lines:
        if("__UPDATE_CMAKE_INCLUDE_DIRECTORIES__" in line):
            add_include_directories(target_file, include_dir_file_lines);

        elif("__UPDATE_CMAKE_GAME_SOURCES__" in line):
            add_game_sources(target_file, game_sources_file_lines);

        else:
            write_line(target_file, line);

    target_file.close();

main();
