#!/bin/bash

if [ ! -f antlr4.jar ]; then
    echo "you need antlr4.jar and java to build parser code"
    exit 1
fi

java -jar antlr4.jar BoolExpr.g -o boolexpr -visitor  -Dlanguage=Python3
