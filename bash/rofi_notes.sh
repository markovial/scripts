#!/bin/bash

# rofi script to quickly open my most used notes files

ROFI_THEME="~/.config/rofi/launchers/text/style_4"
ITEM_PATH="$HOME/Documents/notes/"

# i dont want to see the .txt extensions in the menu
SEARCHED_ITEM=$(ls $ITEM_PATH | sed -e 's/\.txt$//' | rofi -dmenu -i -p "" -theme $ROFI_THEME)

# if variable is empty exit script / do nothing
[[ -z $SEARCHED_ITEM ]] && exit

SEARCHED_ITEM="$SEARCHED_ITEM.txt"
alacritty -e nvim $ITEM_PATH$SEARCHED_ITEM

