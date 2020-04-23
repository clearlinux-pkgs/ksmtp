#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : ksmtp
Version  : 20.04.0
Release  : 20
URL      : https://download.kde.org/stable/release-service/20.04.0/src/ksmtp-20.04.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/20.04.0/src/ksmtp-20.04.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/20.04.0/src/ksmtp-20.04.0.tar.xz.sig
Summary  : Job-based library to send email through an SMTP server
Group    : Development/Tools
License  : LGPL-2.1
Requires: ksmtp-data = %{version}-%{release}
Requires: ksmtp-lib = %{version}-%{release}
Requires: ksmtp-license = %{version}-%{release}
Requires: ksmtp-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules pkgconfig(libsasl2)

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
%setup -q -n ksmtp-20.04.0
cd %{_builddir}/ksmtp-20.04.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1587686000
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1587686000
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ksmtp
cp %{_builddir}/ksmtp-20.04.0/COPYING.LIB %{buildroot}/usr/share/package-licenses/ksmtp/9a1929f4700d2407c70b507b3b2aaf6226a9543c
pushd clr-build
%make_install
popd
%find_lang libksmtp5

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories5/ksmtp.categories

%files dev
%defattr(-,root,root,-)
/usr/include/KPim/KSMTP/KSMTP/Job
/usr/include/KPim/KSMTP/KSMTP/LoginJob
/usr/include/KPim/KSMTP/KSMTP/SendJob
/usr/include/KPim/KSMTP/KSMTP/Session
/usr/include/KPim/KSMTP/KSMTP/SessionUiProxy
/usr/include/KPim/KSMTP/ksmtp/job.h
/usr/include/KPim/KSMTP/ksmtp/ksmtp_export.h
/usr/include/KPim/KSMTP/ksmtp/loginjob.h
/usr/include/KPim/KSMTP/ksmtp/sendjob.h
/usr/include/KPim/KSMTP/ksmtp/session.h
/usr/include/KPim/KSMTP/ksmtp/sessionuiproxy.h
/usr/include/KPim/ksmtp_version.h
/usr/lib64/cmake/KPimSMTP/KPimSMTPConfig.cmake
/usr/lib64/cmake/KPimSMTP/KPimSMTPConfigVersion.cmake
/usr/lib64/cmake/KPimSMTP/KPimSMTPTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KPimSMTP/KPimSMTPTargets.cmake
/usr/lib64/libKPimSMTP.so
/usr/lib64/qt5/mkspecs/modules/qt_KSMTP.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKPimSMTP.so.5
/usr/lib64/libKPimSMTP.so.5.14.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ksmtp/9a1929f4700d2407c70b507b3b2aaf6226a9543c

%files locales -f libksmtp5.lang
%defattr(-,root,root,-)

