#!/bin/sh

# Define your function here
Hello () {
   echo "Hello World"
}

# Invoke your function
Hello

# Define your function here
Hello_args () {
   echo "Hello World $1 $2"
}

# Invoke your function
Hello_args Zara Ali

# Define your function here
Hello_return () {
   echo "Hello World $1 $2"
   return 10
}

# Invoke your function
Hello_return Zara Ali

# Capture value returnd by last command
ret=$?

echo "Return value is $ret"

