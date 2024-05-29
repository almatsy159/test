#!/bin/bash


nb_term_zero= ls /dev/pts/
echo $nb_term_zero
actual_dir= pwd
echo $actual_dir
qterminal --workdir $actual_dir
nb_term_un= ls /dev/pts/
echo $nb_term_un
