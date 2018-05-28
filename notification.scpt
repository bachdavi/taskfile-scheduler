#!/usr/bin/osascript

on run argv
    display dialog "These are the tasks you did not finish today:\n " & item 1 of argv buttons {"Ok"} default button 1
end
