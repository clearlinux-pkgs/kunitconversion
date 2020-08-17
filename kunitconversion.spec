#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kunitconversion
Version  : 5.73.0
Release  : 31
URL      : https://download.kde.org/stable/frameworks/5.73/kunitconversion-5.73.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.73/kunitconversion-5.73.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.73/kunitconversion-5.73.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: kunitconversion-lib = %{version}-%{release}
Requires: kunitconversion-license = %{version}-%{release}
Requires: kunitconversion-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : ki18n-dev
BuildRequires : qtbase-dev mesa-dev

%description
# KUnitConversion
Converting physical units
## Introduction
KUnitConversion provides functions to convert values in different physical
units. It supports converting different prefixes (e.g. kilo, mega, giga) as
well as converting between different unit systems (e.g. liters, gallons). The
following areas are supported:

%package dev
Summary: dev components for the kunitconversion package.
Group: Development
Requires: kunitconversion-lib = %{version}-%{release}
Provides: kunitconversion-devel = %{version}-%{release}
Requires: kunitconversion = %{version}-%{release}

%description dev
dev components for the kunitconversion package.


%package lib
Summary: lib components for the kunitconversion package.
Group: Libraries
Requires: kunitconversion-license = %{version}-%{release}

%description lib
lib components for the kunitconversion package.


%package license
Summary: license components for the kunitconversion package.
Group: Default

%description license
license components for the kunitconversion package.


%package locales
Summary: locales components for the kunitconversion package.
Group: Default

%description locales
locales components for the kunitconversion package.


%prep
%setup -q -n kunitconversion-5.73.0
cd %{_builddir}/kunitconversion-5.73.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1597703596
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1597703596
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kunitconversion
cp %{_builddir}/kunitconversion-5.73.0/COPYING.LIB %{buildroot}/usr/share/package-licenses/kunitconversion/9a1929f4700d2407c70b507b3b2aaf6226a9543c
pushd clr-build
%make_install
popd
%find_lang kunitconversion5

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KUnitConversion/KUnitConversion/Converter
/usr/include/KF5/KUnitConversion/KUnitConversion/Unit
/usr/include/KF5/KUnitConversion/KUnitConversion/UnitCategory
/usr/include/KF5/KUnitConversion/KUnitConversion/Value
/usr/include/KF5/KUnitConversion/kunitconversion/converter.h
/usr/include/KF5/KUnitConversion/kunitconversion/kunitconversion_export.h
/usr/include/KF5/KUnitConversion/kunitconversion/unit.h
/usr/include/KF5/KUnitConversion/kunitconversion/unitcategory.h
/usr/include/KF5/KUnitConversion/kunitconversion/value.h
/usr/include/KF5/kunitconversion_version.h
/usr/lib64/cmake/KF5UnitConversion/KF5UnitConversionConfig.cmake
/usr/lib64/cmake/KF5UnitConversion/KF5UnitConversionConfigVersion.cmake
/usr/lib64/cmake/KF5UnitConversion/KF5UnitConversionTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5UnitConversion/KF5UnitConversionTargets.cmake
/usr/lib64/libKF5UnitConversion.so
/usr/lib64/qt5/mkspecs/modules/qt_KUnitConversion.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5UnitConversion.so.5
/usr/lib64/libKF5UnitConversion.so.5.73.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kunitconversion/9a1929f4700d2407c70b507b3b2aaf6226a9543c

%files locales -f kunitconversion5.lang
%defattr(-,root,root,-)

