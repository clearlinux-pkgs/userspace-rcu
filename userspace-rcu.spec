#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x17280A9781186ACF (mathieu.desnoyers@efficios.com)
#
Name     : userspace-rcu
Version  : 0.10.1
Release  : 3
URL      : https://www.lttng.org/files/urcu/userspace-rcu-0.10.1.tar.bz2
Source0  : https://www.lttng.org/files/urcu/userspace-rcu-0.10.1.tar.bz2
Source99 : https://www.lttng.org/files/urcu/userspace-rcu-0.10.1.tar.bz2.asc
Summary  : A userspace RCU (read-copy-update) library, bulletproof version
Group    : Development/Tools
License  : LGPL-2.1
Requires: userspace-rcu-lib
Requires: userspace-rcu-doc

%description
Userspace RCU Implementation
============================
by Mathieu Desnoyers and Paul E. McKenney

%package dev
Summary: dev components for the userspace-rcu package.
Group: Development
Requires: userspace-rcu-lib
Provides: userspace-rcu-devel

%description dev
dev components for the userspace-rcu package.


%package doc
Summary: doc components for the userspace-rcu package.
Group: Documentation

%description doc
doc components for the userspace-rcu package.


%package lib
Summary: lib components for the userspace-rcu package.
Group: Libraries

%description lib
lib components for the userspace-rcu package.


%prep
%setup -q -n userspace-rcu-0.10.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1516760583
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1516760583
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/include/urcu/arch.h
/usr/include/urcu/arch/generic.h
/usr/include/urcu/cds.h
/usr/include/urcu/compiler.h
/usr/include/urcu/config.h
/usr/include/urcu/debug.h
/usr/include/urcu/futex.h
/usr/include/urcu/hlist.h
/usr/include/urcu/lfstack.h
/usr/include/urcu/list.h
/usr/include/urcu/map/urcu-bp.h
/usr/include/urcu/map/urcu-qsbr.h
/usr/include/urcu/map/urcu.h
/usr/include/urcu/rcuhlist.h
/usr/include/urcu/rculfhash.h
/usr/include/urcu/rculfqueue.h
/usr/include/urcu/rculfstack.h
/usr/include/urcu/rculist.h
/usr/include/urcu/ref.h
/usr/include/urcu/static/lfstack.h
/usr/include/urcu/static/rculfqueue.h
/usr/include/urcu/static/rculfstack.h
/usr/include/urcu/static/urcu-bp.h
/usr/include/urcu/static/urcu-pointer.h
/usr/include/urcu/static/urcu-qsbr.h
/usr/include/urcu/static/urcu.h
/usr/include/urcu/static/wfcqueue.h
/usr/include/urcu/static/wfqueue.h
/usr/include/urcu/static/wfstack.h
/usr/include/urcu/syscall-compat.h
/usr/include/urcu/system.h
/usr/include/urcu/tls-compat.h
/usr/include/urcu/uatomic.h
/usr/include/urcu/uatomic/generic.h
/usr/include/urcu/uatomic_arch.h
/usr/include/urcu/urcu-futex.h
/usr/include/urcu/urcu_ref.h
/usr/include/urcu/wfcqueue.h
/usr/include/urcu/wfqueue.h
/usr/include/urcu/wfstack.h
/usr/lib64/liburcu-bp.so
/usr/lib64/liburcu-cds.so
/usr/lib64/liburcu-common.so
/usr/lib64/liburcu-mb.so
/usr/lib64/liburcu-qsbr.so
/usr/lib64/liburcu-signal.so
/usr/lib64/liburcu.so
/usr/lib64/pkgconfig/liburcu-bp.pc
/usr/lib64/pkgconfig/liburcu-cds.pc
/usr/lib64/pkgconfig/liburcu-mb.pc
/usr/lib64/pkgconfig/liburcu-qsbr.pc
/usr/lib64/pkgconfig/liburcu-signal.pc
/usr/lib64/pkgconfig/liburcu.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/userspace\-rcu/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/liburcu-bp.so.6
/usr/lib64/liburcu-bp.so.6.0.0
/usr/lib64/liburcu-cds.so.6
/usr/lib64/liburcu-cds.so.6.0.0
/usr/lib64/liburcu-common.so.6
/usr/lib64/liburcu-common.so.6.0.0
/usr/lib64/liburcu-mb.so.6
/usr/lib64/liburcu-mb.so.6.0.0
/usr/lib64/liburcu-qsbr.so.6
/usr/lib64/liburcu-qsbr.so.6.0.0
/usr/lib64/liburcu-signal.so.6
/usr/lib64/liburcu-signal.so.6.0.0
/usr/lib64/liburcu.so.6
/usr/lib64/liburcu.so.6.0.0
