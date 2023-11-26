## source this bash script to set all DSM env vars based on $DSM_DIRS
i=0
for x in $DSM_DIRS
do
    r=`expr $i % 2`
    if [ $r == 0 ]
    then
	k=$x
    else
	#echo export _$k=$x
	eval export _$k=$x
    fi
    i=`expr $i + 1`
done

