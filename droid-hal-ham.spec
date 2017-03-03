# These and other macros are documented in dhd/droid-hal-device.inc
%define device ham
%define vendor zuk
%define vendor_pretty ZUK
%define device_pretty Z1
%define installable_zip 1
%define enable_kernel_update 1
%define straggler_files \
/selinux_version\
/service_contexts\
%{nil}
%include rpm/dhd/droid-hal-device.inc
