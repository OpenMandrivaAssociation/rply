%define major	1
%define libname	%mklibname %{name} %{major}
%define develname	%mklibname -d %{name}

Name:		rply
Version:	1.1.1
Release:	5
Summary:	A library to read and write PLY files
Group:		Development/Other
License:	MIT
URL:		http://www.tecgraf.puc-rio.br/~diego/professional/rply/
Source0:	http://www.tecgraf.puc-rio.br/~diego/professional/rply/%{name}-%{version}.tar.gz
Source1:	rply_CMakeLists.txt
Source2:	RPLYConfig.cmake.in
Source3:	rply_cmake_export_cmakelists.txt
BuildRequires:	cmake >= 2.6.0

%description
RPly is a library that lets applications read and write PLY files.
The PLY file format is widely used to store geometric information, such as 3D
models, but is general enough to be useful for other purposes.

RPly is easy to use, well documented, small, free, open-source, ANSI C, 
efficient, and well tested. The highlights are:

* A callback mechanism that makes PLY file input straightforward;
* Support for the full range of numeric formats;
* Binary (big and little endian) and text modes are fully supported;
* Input and output are buffered for efficiency;
* Available under the MIT license for added freedom. 

%package -n %{libname}
Summary:	A library to read and write PLY files
Group:		System/Libraries

%description -n %{libname}
RPly is a library that lets applications read and write PLY files.
The PLY file format is widely used to store geometric information, such as 3D
models, but is general enough to be useful for other purposes.

%package -n %{develname}
Summary:	Development files and headers for %{name}
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
Rply Library Header Files and Link Libraries.

%prep
%setup -q

iconv -f ISO8859-1 -t UTF-8 LICENSE > LICENSE.utf8
mv -f LICENSE.utf8 LICENSE

# Add CMakeLists.txt file
cp %{SOURCE1} CMakeLists.txt

# Add CMake detection modules
mkdir -p CMake/export
mkdir -p CMake/Modules

cp %{SOURCE2} CMake/Modules/
cp %{SOURCE3} CMake/export/CMakeLists.txt

%build
%cmake \
	-DCMAKE_BUILD_TYPE:STRING="Release"\
	-DCMAKE_VERBOSE_MAKEFILE=ON

%make

%install
%makeinstall_std -C build

%files
%doc LICENSE
%doc manual/*
%{_bindir}/*

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}*

%files -n %{develname}
%{_includedir}/%{name}/*
%{_libdir}/lib%{name}.so
%{_datadir}/%{name}/



%changelog
* Tue Mar 13 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.1.1-1
+ Revision: 784764
- imported package rply

