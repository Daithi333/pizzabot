#!/bin/bash

expected_arg_count=1

if [ $# -ne $expected_arg_count ]; then
  echo "$expected_arg_count arg expected containing grid size and delivery co-ordinates but found $#"
  read -n 1 -s -r -p "Press any key to continue"
  exit
fi

echo "$expected_arg_count Arg found: $*. Proceeding"
python -m pizzabot "$*"
read -n 1 -s -r -p "Press any key to continue.."
