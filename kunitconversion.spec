#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kunitconversion
Version  : 5.50.0
Release  : 3
URL      : https://download.kde.org/stable/frameworks/5.50/kunitconversion-5.50.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.50/kunitconversion-5.50.0.tar.xz
Source99 : https://download.kde.org/stable/frameworks/5.50/kunitconversion-5.50.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: kunitconversion-lib
Requires: kunitconversion-license
Requires: kunitconversion-locales
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : qtbase-dev qtbase-extras mesa-dev

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
Requires: kunitconversion-lib
Provides: kunitconversion-devel

%description dev
dev components for the kunitconversion package.


%package lib
Summary: lib components for the kunitconversion package.
Group: Libraries
Requires: kunitconversion-license

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
%setup -q -n kunitconversion-5.50.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1536424923
mkdir clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1536424923
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/kunitconversion
cp COPYING.LIB %{buildroot}/usr/share/doc/kunitconversion/COPYING.LIB
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
/usr/lib64/libKF5UnitConversion.so.5.50.0

%files license
%defattr(-,root,root,-)
/usr/share/doc/kunitconversion/COPYING.LIB

%files locales -f kunitconversion5.lang
%defattr(-,root,root,-)

