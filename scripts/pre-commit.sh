#!/bin/bash

# Clean *.pyc files
for i in $(find . -name '*.pyc'); do rm -f $i; done

BRANCH=$(git branch | grep '*' | cut -d' ' -f2)

production_checks(){

    # First the pylint rate
    tput bold
    tput setaf 4
    echo
    echo "Pylint is rating your code"
    pylint app | grep rated
    echo
    tput sgr0

    # Should pass pep8
    PEP=$(pep8 --ignore=E501,E221,E202,E251,W391,W291,E701,W293 --repeat gae app scripts | wc -l);
    if [ $PEP -gt 0 ];
    then
	pep8 --ignore=E501,E221,E202,E251,W391,W291,E701,W293 --repeat gae app scripts
	echo "$(tput bold) $(tput setaf 1) Commit failed. Check the PEP8 results and try again $(tput sgr0)"
	exit 1
    else
	echo "PEP8 tests ... $(tput setaf 2)passed$(tput sgr0)"
    fi

    # Should pass pyflakes
    echo "$(tput setaf 1)"

    #exclude __init__.py's from pyflakes so we can import w/o using on modules
    files=$(find gae app scripts -name "*.py" -not -name "__init__.py")
    if pyflakes $files;
    then
	echo "$(tput sgr0)"
	echo "Pyflakes tests ... $(tput setaf 2)passed$(tput sgr0)";
    else
	echo "$(tput sgr0)"
	echo "Pyflakes tests ... $(tput setaf 1)FAILED$(tput sgr0) Check pyflakes results and try again"
	echo
	echo
	exit 1
    fi
}

production_checks;
