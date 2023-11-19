### Purpose
on AMD cpu, sysconf may return large L3 cache on vm, which may cause larger memory footprint
for application written in dotnet etc.

hook into glibc to solve this

### Usage
#### 1. build the so
```
make
```

### 2. run your program with LD_PRELOAD env
```
LD_PRELOAD=$PWD/hook_l3.so /path/to/your/app
```

