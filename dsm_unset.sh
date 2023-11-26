## source this bash script to unset all DSM env vars based on $DSM_DIRS
i=0
for x in $DSM_DIRS
do
    r=`expr $i % 2`
    #echo $r
    if [ $r == 0 ]
    then
        eval xx='$'_$x
	#echo unset _$x
	eval unset _$x
    fi
    #echo $i $x
    i=`expr $i + 1`
done
DSM_DIRS=""
