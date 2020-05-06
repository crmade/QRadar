#!/bin/bash
Email="<EMAILS>"
CLIENT="<CLIENT NAME"
PARTITION="<PARTITION>"
ALERT=70
USED=`df -h |grep $PARTITION | awk '{print $5}' |cut -d'%' -f1`
FLAG=/root/scripts/.disk.flag
if [ ! -f "$FLAG" ]
then
    if [ $USED -ge $ALERT ]
    then
#        echo "Entro"
        touch /root/scripts/.disk.flag
        mail -s "$CLIENT Alert: Almost out of disk space. Current usage is at $USED on $PARTITION" $Email <<< "<MESSAGE>"
    fi
fi
