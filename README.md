# AFLGOPT
Project to optimize the exploitation transition phase in AFLGo

## Build Docker
Simply run ``` ./build.sh ``` at the project home directory.

## Run fuzzer
First, launce a docker container by ``` ./launch.sh ```

Then, inside the docker, run fuzzer by the following command
```
/tool-script/run_ALFGo.sh cxxfilt-2016-4487 stdin 600
```
This means you will run AFLGo on a binary named cxxfilt-2016-4487, which takes inputs from stdin, for 600 seconds.

For other targets or other time limits, you may change the arguments.

Currently, the exploitation phase starts at the 3/4 point of the entire runtime.

See the script "run_ALFGo.sh" to modify it.

## Check results
After the fuzzing is done, you can check the results under ``` /box/output ```

There, you can check the crashing inputs, and the replays logs generated by them.


## System configuration for docker

To run AFL/AFLGo, you should first fix core dump name pattern.
```
$ echo core | sudo tee /proc/sys/kernel/core_pattern
```

If your system has `/sys/devices/system/cpu/cpu*/cpufreq` directory, AFL may
also complain about the CPU frequency scaling configuration. Check the current
configuration and remember it if you want to restore it later. Then, set it to
`performance`, as requested by AFL.
```
$ cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
powersave
powersave
powersave
powersave
$ echo performance | sudo tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
```

