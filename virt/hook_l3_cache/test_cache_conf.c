#include <unistd.h>
#include <stdio.h>

int main() {
        printf("_SC_LEVEL1_DCACHE_SIZE:%d\n",sysconf(_SC_LEVEL1_DCACHE_SIZE));
        printf("_SC_LEVEL2_CACHE_SIZE:%d\n",sysconf(_SC_LEVEL2_CACHE_SIZE));
        printf("_SC_LEVEL3_CACHE_SIZE:%d\n",sysconf(_SC_LEVEL3_CACHE_SIZE));
        printf("_SC_LEVEL4_CACHE_SIZE:%d\n",sysconf(_SC_LEVEL4_CACHE_SIZE));
}
