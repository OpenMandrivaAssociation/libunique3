%define url_ver %(echo %{version}|cut -d. -f1,2)

%define	oname	libunique
%define	api	3.0
%define	major	0
%define	libname	%mklibname unique %{api} %{major}
%define	girname	%mklibname unique-gir %{api}
%define	devname	%mklibname unique -d %{api}

Summary: 	Library for creating single instance applications
Name: 		libunique3
Version: 	3.0.2
Release:	5
License: 	LGPLv2+
Group: 		System/Libraries
Url: 		http://live.gnome.org/LibUnique
Source0: 	http://ftp.gnome.org/pub/GNOME/sources/libunique/%{url_ver}/%{oname}-%{version}.tar.xz
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gdk-3.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk-doc)
BuildRequires:	pkgconfig(x11)

%description
Unique is a library for creating single instance applications.

%package -n	%{libname}
Group:		System/Libraries
Summary:	Library for creating single instance applications

%description -n	%{libname}
Unique is a library for creating single instance applications.

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries
Conflicts:	%{libname} < 3.0.2-5

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n	%{devname}
Group:		Development/C
Summary:	Header files for development with %{oname}
Provides:	unique%{api}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n	%{devname}
Unique is a library for creating single instance applications.

%prep
%setup -qn %{oname}-%{version}

%build
%configure2_5x
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libunique-%{api}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/Unique-%{api}.typelib

%files -n %{devname}
%doc AUTHORS
%{_libdir}/libunique-%{api}.so
%{_libdir}/pkgconfig/unique-%{api}.pc
%{_includedir}/unique-%{api}
%{_datadir}/gir-1.0/Unique-%{api}.gir
%{_datadir}/gtk-doc/html/unique-3.0

