#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kunitconversion
Version  : 5.52.0
Release  : 7
URL      : https://download.kde.org/stable/frameworks/5.52/kunitconversion-5.52.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.52/kunitconversion-5.52.0.tar.xz
Source99 : https://download.kde.org/stable/frameworks/5.52/kunitconversion-5.52.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: kunitconversion-lib = %{version}-%{release}
Requires: kunitconversion-license = %{version}-%{release}
Requires: kunitconversion-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : qtbase-dev mesa-dev

%description
# KUnitConversion
Converting physical units
## Introduction
KUnitConversion provides functions to convert values in different physical
units. It supports converting different prefixes (e.g. kilo, mega, giga) as
well as converting between different unit systems (e.g. liters, gallons). The
following areas are supported:

%package abi
Summary: abi components for the kunitconversion package.
Group: Default

%description abi
abi components for the kunitconversion package.


%package dev
Summary: dev components for the kunitconversion package.
Group: Development
Requires: kunitconversion-lib = %{version}-%{release}
Provides: kunitconversion-devel = %{version}-%{release}

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
%setup -q -n kunitconversion-5.52.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1541872366
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1541872366
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kunitconversion
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/kunitconversion/COPYING.LIB
pushd clr-build
%make_install
popd
%find_lang kunitconversion5

%files
%defattr(-,root,root,-)

%files abi
%defattr(-,root,root,-)
/usr/share/abi/libKF5UnitConversion.so.5.52.0.abi

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
/usr/lib64/libKF5UnitConversion.so.5.52.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kunitconversion/COPYING.LIB

%files locales -f kunitconversion5.lang
%defattr(-,root,root,-)

