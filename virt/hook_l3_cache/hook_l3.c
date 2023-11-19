#define _GNU_SOURCE
#include <dlfcn.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

typedef long (*glibc_sysconf)(int name);

static glibc_sysconf _orig_sysconf;

static long orig_sysconf(int name)
{
    if (!_orig_sysconf) {
        _orig_sysconf = (glibc_sysconf)dlsym(RTLD_NEXT, "sysconf");
    }

    return _orig_sysconf(name);
}


long sysconf(int name)
{
	if(name != _SC_LEVEL3_CACHE_SIZE) {
		return orig_sysconf(name);
	}
	return 0;
}
