on run argv
    tell application "Terminal" to set current settings of tab (item 1 of argv as number) of front window to first settings set whose name is (item 2 of argv)
end run
