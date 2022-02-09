#-a array 	Store the words in an indexed array named array. Numbering of array elements starts at zero.
#-d delim 	Set the delimiter character to delim. This character signals the end of the line. If -d is not used, the default line delimiter is a newline.
#-e 	Get a line of input from an interactive shell. The user manually inputs characters until the line delimiter is reached.
#-i text 	When used in conjunction with -e (and only if -s is not used), text is inserted as the initial text of the input line. The user is permitted to edit text on the input line.
#-n nchars 	Stop reading after an integer number nchars characters are read, if the line delimiter has not been reached.
#-N nchars 	Ignore the line delimiter. Stop reading only after nchars characters are read, EOF is reached, or read times out (see -t).
#-p prompt 	Print the string prompt, without a newline, before beginning to read.
#-r 	Use "raw input". Specifically, this option causes read to interpret backslashes literally, rather than interpreting them as escape characters.
#-s 	Do not echo keystrokes when read is taking input from the terminal.
#-t timeout 	Time out, and return failure, if a complete line of input is not read within timeout seconds. If the timeout value is zero, read will not read any data, but returns success if input was available to read. If timeout is not specified, the value of the shell variable TMOUT is used instead, if it exists. The value of timeout are fractional numbers, e.g., 3.5.
#-u fd 	Read from the file descriptor fd instead of standard input. The file descriptor should be a small integer. For information about opening a custom file descriptor, see opening file descriptors in bash.
