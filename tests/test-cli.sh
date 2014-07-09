#!/bin/bash

TEST1=`decipher -U dataapi -P dataapi pull -s 'kbdemo/data' -f csv -S qualified -F 'q1=2,q2r2=1' -c q1,q2r2 | md5sum | cut -c 1-32`
if [[ $TEST1 != "724ef1b137cc8d3f68d9c173c9acd9cb" ]]
then
    echo "TEST1 failed"
    echo "GOT \"${TEST1}\""
    exit 1
fi

TEST2=`decipher -U dataapi -P dataapi pull -s 'kbdemo/data' -f csv -S qualified -t '2010-03-01T00:00:00' | md5sum | cut -c 1-32`
if [[ $TEST2 != "1b0337266657593841bb6c62c99e7e2c" ]]
then
    echo "TEST2 failed"
    echo "GOT \"${TEST2}\""
    exit 1
fi

TEST3=`decipher -U dataapi -P dataapi pull -s 'kbdemo/data' -f csv -S qualified -T '2007-03-01T00:00:00' | md5sum | cut -c 1-32`
if [[ $TEST3 != "1b0337266657593841bb6c62c99e7e2c" ]]
then
    echo "TEST3 failed"
    echo "GOT \"${TEST3}\""
    exit 1
fi
