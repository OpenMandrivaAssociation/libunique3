%define major 		0
%define api 3.0
%define oname libunique
%define libname		%mklibname unique %api %major
%define develname	%mklibname unique -d %api

Summary: 	Library for creating single instance applications
Name: 		libunique3
Version: 	2.90.1
Release:	%mkrel 2
URL: 		http://live.gnome.org/LibUnique
License: 	LGPLv2+
Group: 		System/Libraries
Source0: 	http://ftp.gnome.org/pub/GNOME/sources/%oname/%{oname}-%{version}.tar.bz2
Buildroot: 	%{_tmppath}/%{oname}-%{version}-%{release}-buildroot
BuildRequires:	dbus-glib-devel >= 0.70
BuildRequires:	gtk+3-devel
#gw: the gir stuff in 2.90.1 still needs this:
BuildRequires:	gtk+2-devel
BuildRequires:	glib2-devel >= 2.12.0
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk-doc

%description
Unique is a library for creating single instance applications.

%package -n	%{libname}
Group:		System/Libraries
Summary:	Library for creating single instance applications
Conflicts: gir-repository < 0.6.5-3

%description -n %{libname}
Unique is a library for creating single instance applications.

%package -n %{develname}
Group:		Development/C
Summary:	Header files for development with %oname
Provides:	unique-%api-devel = %version-%release
Requires:	%{libname} = %{version}
Conflicts: gir-repository < 0.6.5-3

%description -n %{develname}
Unique is a library for creating single instance applications.

%prep
%setup -q -n %oname-%version

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}

%makeinstall_std

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libunique-%api.so.%{major}*
%_libdir/girepository-1.0/Unique-%{api}.typelib

%files -n %{develname}
%doc AUTHORS
%docdir %{_datadir}/gtk-doc/html/unique
%doc %{_datadir}/gtk-doc/html/unique/*
%defattr(-,root,root)
%{_libdir}/libunique-%api.so
%{_libdir}/libunique-%api.*a
%{_libdir}/pkgconfig/unique-%api.pc
%{_includedir}/unique-%api
%_datadir/gir-1.0/Unique-%api.gir
