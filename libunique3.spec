%define major 		0
%define api 3.0
%define oname libunique
%define libname		%mklibname unique %{api} %{major}
%define develname	%mklibname unique -d %{api}
%define gi_name		%mklibname unique-gir %{api}

Summary: 	Library for creating single instance applications
Name: 		libunique3
Version: 	3.0.2
Release:	2
URL: 		http://live.gnome.org/LibUnique
License: 	LGPLv2+
Group: 		System/Libraries
Source0: 	http://ftp.gnome.org/pub/GNOME/sources/%{oname}/%{oname}-%{version}.tar.xz

BuildRequires:	pkgconfig(dbus-glib-1) >= 0.70
BuildRequires:	pkgconfig(gdk-3.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)

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
Summary:	Header files for development with %{oname}
Provides:	unique-%{api}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}%{release}
Conflicts: gir-repository < 0.6.5-3

%description -n %{develname}
Unique is a library for creating single instance applications.

%package -n %{gi_name}
Group:		System/Libraries
Summary:	GObject Introspection interface library for libunique
Requires:	%{libname} = %{version}-%{release}

%description -n %{gi_name}
GObject Introspection interface library for libunique.

%prep
%setup -qn %{oname}-%{version}

%build
%configure2_5x \
	--disable-static \
	--enable-introspection=yes

%make

%install
rm -rf %{buildroot}
%makeinstall_std

# remove unpackaged files
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files -n %{libname}
%{_libdir}/libunique-%{api}.so.%{major}*

%files -n %{gi_name}
%{_libdir}/girepository-1.0/Unique-%{api}.typelib

%files -n %{develname}
%doc AUTHORS
%{_libdir}/libunique-%{api}.so
%{_libdir}/pkgconfig/unique-%{api}.pc
%{_includedir}/unique-%{api}
%{_datadir}/gir-1.0/Unique-%{api}.gir
%{_datadir}/gtk-doc/html/unique-3.0

