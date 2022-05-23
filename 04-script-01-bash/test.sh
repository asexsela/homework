#!/usr/bin/env bash

# a=1
# b=2
# c=a+b
# d=$a+$b
# e=$(($a+$b))

# echo $a
# echo $b
# echo $c
# echo $d
# echo $e

# while (( 1 == 1 ))
# do
#     curl http://localhost:9200
#     if (($? != 0))
#     then
#         date >> curl.log
#     else exit
#     fi
#     sleep 5
# done

hosts=(127.0.0.1 173.194.222.113 87.250.250.242)
timeout=5

# for i in {1..5}
# do
#     echo "--------------------" >> hosts.log

#     for h in ${hosts[@]}
#     do
# 	curl -Is --connect-timeout $timeout $h:80 >/dev/null
#         echo "  " $h check=$? >> hosts.log
#     done
# done

res=0

while (($res == 0))
do
    for h in ${hosts[@]}
    do
        curl -Is --connect-timeout $timeout $h:9200 >/dev/null
        res=$?
        
        if (($res != 0))
        then
            echo "    ERROR on " $h check=$res >>error.log
            exit
        fi
    done
done