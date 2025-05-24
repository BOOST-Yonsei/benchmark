# 연세대학교 CAS4101 컴퓨터종합설계 webOS 부팅 최적화

## Kernel binary optimized for boot time

- WebOS v2.28
- Built with LD v2.43
- Kernel images included in the repository for reference
	- `./kernel_original` = kernel compiled from upstream source
	- `./kernel_optimized` = kernel compiled after optimizations applied

## Boot time measurement

- Tested on RaspberryPi 4 Model B
- Kernel argument += quiet
- Connected via USB UART serial console
- Power fully disconnected between each trial
- Raspberry Pi cooled with an external fan at all times during the test

## Notable improvements

- File size reduction
	- Compressed binary (`Image`) : 28M -> 24M
	- Uncompressed binary (`vmlinux`) : 36M -> 34M
- Kernel boot time improvements
	- E(t) : 7.373s -> 7.317s
	- Does not factor speed gains from smaller binary size
		- Current measured data set is not sufficient to assert statistical significance
