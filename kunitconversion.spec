#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kunitconversion
Version  : 5.103.0
Release  : 58
URL      : https://download.kde.org/stable/frameworks/5.103/kunitconversion-5.103.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.103/kunitconversion-5.103.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.103/kunitconversion-5.103.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC0-1.0 LGPL-2.0
Requires: kunitconversion-data = %{version}-%{release}
Requires: kunitconversion-lib = %{version}-%{release}
Requires: kunitconversion-license = %{version}-%{release}
Requires: kunitconversion-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : ki18n-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# KUnitConversion
Converting physical units
## Introduction
KUnitConversion provides functions to convert values in different physical
units. It supports converting different prefixes (e.g. kilo, mega, giga) as
well as converting between different unit systems (e.g. liters, gallons). The
following areas are supported:

%package data
Summary: data components for the kunitconversion package.
Group: Data

%description data
data components for the kunitconversion package.


%package dev
Summary: dev components for the kunitconversion package.
Group: Development
Requires: kunitconversion-lib = %{version}-%{release}
Requires: kunitconversion-data = %{version}-%{release}
Provides: kunitconversion-devel = %{version}-%{release}
Requires: kunitconversion = %{version}-%{release}

%description dev
dev components for the kunitconversion package.


%package lib
Summary: lib components for the kunitconversion package.
Group: Libraries
Requires: kunitconversion-data = %{version}-%{release}
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
%setup -q -n kunitconversion-5.103.0
cd %{_builddir}/kunitconversion-5.103.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1676312972
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1676312972
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kunitconversion
cp %{_builddir}/kunitconversion-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kunitconversion/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kunitconversion-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kunitconversion/20079e8f79713dce80ab09774505773c926afa2a || :
pushd clr-build
%make_install
popd
%find_lang kunitconversion5

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories5/kunitconversion.categories

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
/usr/include/KF5/KUnitConversion/kunitconversion_version.h
/usr/lib64/cmake/KF5UnitConversion/KF5UnitConversionConfig.cmake
/usr/lib64/cmake/KF5UnitConversion/KF5UnitConversionConfigVersion.cmake
/usr/lib64/cmake/KF5UnitConversion/KF5UnitConversionTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5UnitConversion/KF5UnitConversionTargets.cmake
/usr/lib64/libKF5UnitConversion.so
/usr/lib64/qt5/mkspecs/modules/qt_KUnitConversion.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5UnitConversion.so.5
/usr/lib64/libKF5UnitConversion.so.5.103.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kunitconversion/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kunitconversion/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0

%files locales -f kunitconversion5.lang
%defattr(-,root,root,-)

