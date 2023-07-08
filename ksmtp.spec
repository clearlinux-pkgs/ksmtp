#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : ksmtp
Version  : 23.04.3
Release  : 56
URL      : https://download.kde.org/stable/release-service/23.04.3/src/ksmtp-23.04.3.tar.xz
Source0  : https://download.kde.org/stable/release-service/23.04.3/src/ksmtp-23.04.3.tar.xz
Source1  : https://download.kde.org/stable/release-service/23.04.3/src/ksmtp-23.04.3.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 LGPL-2.0 LGPL-2.1
Requires: ksmtp-data = %{version}-%{release}
Requires: ksmtp-lib = %{version}-%{release}
Requires: ksmtp-license = %{version}-%{release}
Requires: ksmtp-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules pkgconfig(libsasl2)
BuildRequires : extra-cmake-modules-data
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package data
Summary: data components for the ksmtp package.
Group: Data

%description data
data components for the ksmtp package.


%package dev
Summary: dev components for the ksmtp package.
Group: Development
Requires: ksmtp-lib = %{version}-%{release}
Requires: ksmtp-data = %{version}-%{release}
Provides: ksmtp-devel = %{version}-%{release}
Requires: ksmtp = %{version}-%{release}

%description dev
dev components for the ksmtp package.


%package lib
Summary: lib components for the ksmtp package.
Group: Libraries
Requires: ksmtp-data = %{version}-%{release}
Requires: ksmtp-license = %{version}-%{release}

%description lib
lib components for the ksmtp package.


%package license
Summary: license components for the ksmtp package.
Group: Default

%description license
license components for the ksmtp package.


%package locales
Summary: locales components for the ksmtp package.
Group: Default

%description locales
locales components for the ksmtp package.


%prep
%setup -q -n ksmtp-23.04.3
cd %{_builddir}/ksmtp-23.04.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1688842690
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1688842690
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ksmtp
cp %{_builddir}/ksmtp-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/ksmtp/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/ksmtp-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/ksmtp/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/ksmtp-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/ksmtp/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/ksmtp-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/ksmtp/6f1f675aa5f6a2bbaa573b8343044b166be28399 || :
cp %{_builddir}/ksmtp-%{version}/metainfo.yaml.license %{buildroot}/usr/share/package-licenses/ksmtp/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
%find_lang libksmtp5
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories5/ksmtp.categories

%files dev
%defattr(-,root,root,-)
/usr/include/KPim5/KSMTP/KSMTP/Job
/usr/include/KPim5/KSMTP/KSMTP/LoginJob
/usr/include/KPim5/KSMTP/KSMTP/SendJob
/usr/include/KPim5/KSMTP/KSMTP/Session
/usr/include/KPim5/KSMTP/KSMTP/SessionUiProxy
/usr/include/KPim5/KSMTP/ksmtp/job.h
/usr/include/KPim5/KSMTP/ksmtp/ksmtp_export.h
/usr/include/KPim5/KSMTP/ksmtp/loginjob.h
/usr/include/KPim5/KSMTP/ksmtp/sendjob.h
/usr/include/KPim5/KSMTP/ksmtp/session.h
/usr/include/KPim5/KSMTP/ksmtp/sessionuiproxy.h
/usr/include/KPim5/ksmtp_version.h
/usr/lib64/cmake/KPim5SMTP/KPim5SMTPConfig.cmake
/usr/lib64/cmake/KPim5SMTP/KPim5SMTPConfigVersion.cmake
/usr/lib64/cmake/KPim5SMTP/KPim5SMTPTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KPim5SMTP/KPim5SMTPTargets.cmake
/usr/lib64/cmake/KPimSMTP/KPim5SMTPTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KPimSMTP/KPim5SMTPTargets.cmake
/usr/lib64/cmake/KPimSMTP/KPimSMTPConfig.cmake
/usr/lib64/cmake/KPimSMTP/KPimSMTPConfigVersion.cmake
/usr/lib64/libKPim5SMTP.so
/usr/lib64/qt5/mkspecs/modules/qt_KSMTP.pri

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKPim5SMTP.so.5.23.3
/usr/lib64/libKPim5SMTP.so.5
/usr/lib64/libKPim5SMTP.so.5.23.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ksmtp/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/ksmtp/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/ksmtp/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/ksmtp/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/ksmtp/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c

%files locales -f libksmtp5.lang
%defattr(-,root,root,-)

