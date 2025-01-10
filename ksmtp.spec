#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v21
# autospec commit: f4a13a5
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : ksmtp
Version  : 24.12.1
Release  : 78
URL      : https://download.kde.org/stable/release-service/24.12.1/src/ksmtp-24.12.1.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.12.1/src/ksmtp-24.12.1.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.12.1/src/ksmtp-24.12.1.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 LGPL-2.0 LGPL-2.1
Requires: ksmtp-data = %{version}-%{release}
Requires: ksmtp-lib = %{version}-%{release}
Requires: ksmtp-license = %{version}-%{release}
Requires: ksmtp-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : cyrus-sasl-dev
BuildRequires : extra-cmake-modules
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
SPDX-License-Identifier: CC0-1.0

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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n ksmtp-24.12.1
cd %{_builddir}/ksmtp-24.12.1
pushd ..
cp -a ksmtp-24.12.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1736488331
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1736488331
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ksmtp
cp %{_builddir}/ksmtp-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/ksmtp/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/ksmtp-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/ksmtp/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/ksmtp-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/ksmtp/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/ksmtp-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/ksmtp/6f1f675aa5f6a2bbaa573b8343044b166be28399 || :
cp %{_builddir}/ksmtp-%{version}/metainfo.yaml.license %{buildroot}/usr/share/package-licenses/ksmtp/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
cp %{_builddir}/ksmtp-%{version}/readme-build-ftime.txt.license %{buildroot}/usr/share/package-licenses/ksmtp/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang libksmtp6
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories6/ksmtp.categories

%files dev
%defattr(-,root,root,-)
/usr/include/KPim6/KSMTP/KSMTP/Job
/usr/include/KPim6/KSMTP/KSMTP/LoginJob
/usr/include/KPim6/KSMTP/KSMTP/SendJob
/usr/include/KPim6/KSMTP/KSMTP/Session
/usr/include/KPim6/KSMTP/KSMTP/SessionUiProxy
/usr/include/KPim6/KSMTP/ksmtp/job.h
/usr/include/KPim6/KSMTP/ksmtp/ksmtp_export.h
/usr/include/KPim6/KSMTP/ksmtp/loginjob.h
/usr/include/KPim6/KSMTP/ksmtp/sendjob.h
/usr/include/KPim6/KSMTP/ksmtp/session.h
/usr/include/KPim6/KSMTP/ksmtp/sessionuiproxy.h
/usr/include/KPim6/KSMTP/ksmtp_version.h
/usr/lib64/cmake/KPim6SMTP/KPim6SMTPConfig.cmake
/usr/lib64/cmake/KPim6SMTP/KPim6SMTPConfigVersion.cmake
/usr/lib64/cmake/KPim6SMTP/KPim6SMTPTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KPim6SMTP/KPim6SMTPTargets.cmake
/usr/lib64/libKPim6SMTP.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKPim6SMTP.so.6.3.1
/usr/lib64/libKPim6SMTP.so.6
/usr/lib64/libKPim6SMTP.so.6.3.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ksmtp/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/ksmtp/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/ksmtp/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/ksmtp/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/ksmtp/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c

%files locales -f libksmtp6.lang
%defattr(-,root,root,-)

