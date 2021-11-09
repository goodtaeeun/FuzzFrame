#!/bin/bash

# Replay newly found crash inputs
rm /box/output/crashes/README.txt
CRASH_LIST=$(ls /box/output/crashes)

echo "Crash Replay log for ${1}" > /box/output/replay_log.txt

for crash in $CRASH_LIST; do
    DIFF_TIME=$(echo `stat -c%Y /box/output/crashes/${crash}` - `stat -c%Y /box` | bc)
    readarray -d , -t CRASH_ID <<<$crash

    echo -e "\nReplaying crash - ${CRASH_ID[0]} (found at ${DIFF_TIME} sec.):" >> /box/output/replay_log.txt
    cat /box/output/crashes/$crash | /box/$1 2>> /box/output/replay_log.txt
done

# Copy the output directory to the path visible by the host.
cp -r /box/output /output

# Notify that the whole fuzzing campaign has successfully finished.
echo "FINISHED" > /STATUS
