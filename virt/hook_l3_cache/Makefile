ALL: hook_l3.so test_cache_conf

hook_l3.so : hook_l3.c
	gcc -std=c99 -Wall -shared -g -fPIC -Wl,--no-as-needed -ldl -o $@ $<

clean:
	rm test_cache_conf hook_l3.so
