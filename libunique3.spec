%define	major	0
%define	api	3.0
%define	oname	libunique
%define	libname	%mklibname unique %{api} %{major}
%define	devname	%mklibname unique -d %{api}

Summary: 	Library for creating single instance applications
Name: 		libunique3
Version: 	3.0.2
Release:	4
URL: 		http://live.gnome.org/LibUnique
License: 	LGPLv2+
Group: 		System/Libraries
Source0: 	http://ftp.gnome.org/pub/GNOME/sources/%{oname}/%{oname}-%{version}.tar.xz
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gdk-3.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk-doc)

%description
Unique is a library for creating single instance applications.

%package -n	%{libname}
Group:		System/Libraries
Summary:	Library for creating single instance applications
Conflicts:	gir-repository < 0.6.5-3

%description -n	%{libname}
Unique is a library for creating single instance applications.

%package -n	%{devname}
Group:		Development/C
Summary:	Header files for development with %{oname}
Provides:	unique-%{api}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}
Conflicts:	gir-repository < 0.6.5-3

%description -n	%{devname}
Unique is a library for creating single instance applications.

%prep
%setup -q -n %{oname}-%{version}

%build
%configure2_5x
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libunique-%api.so.%{major}*
%{_libdir}/girepository-1.0/Unique-%{api}.typelib

%files -n %{devname}
%doc AUTHORS
%{_libdir}/libunique-%api.so
%{_libdir}/pkgconfig/unique-%api.pc
%{_includedir}/unique-%api
%{_datadir}/gir-1.0/Unique-%api.gir
%{_datadir}/gtk-doc/html/unique-3.0


%changelog
* Tue Jun 14 2011 Götz Waschk <waschk@mandriva.org> 3.0.2-1mdv2011.0
+ Revision: 685151
- new version
- xz tarball

* Tue Apr 05 2011 Funda Wang <fwang@mandriva.org> 3.0.0-1
+ Revision: 650483
- update file list
- update file list
- update to new version 3.0.0

* Wed Mar 23 2011 Funda Wang <fwang@mandriva.org> 2.91.4-1
+ Revision: 647740
- new version 2.91.4

* Thu Sep 16 2010 Götz Waschk <waschk@mandriva.org> 2.90.1-2mdv2011.0
+ Revision: 578932
- rebuild for new g-i

* Fri Jul 30 2010 Götz Waschk <waschk@mandriva.org> 2.90.1-1mdv2011.0
+ Revision: 563642
- gtk+3 version
- gtk+3 version

* Fri Jul 30 2010 Funda Wang <fwang@mandriva.org> 1.1.6-2mdv2011.0
+ Revision: 563406
- rebuild for new gobject-introspection

  + Götz Waschk <waschk@mandriva.org>
    - add conflict with older gir-repository (bug #55583)

* Thu Nov 12 2009 Götz Waschk <waschk@mandriva.org> 1.1.6-1mdv2010.1
+ Revision: 465324
- update to new version 1.1.6

* Thu Nov 12 2009 Götz Waschk <waschk@mandriva.org> 1.1.4-1mdv2010.1
+ Revision: 465206
- update build deps
- new version
- add gobject introspection support

* Tue Aug 25 2009 Götz Waschk <waschk@mandriva.org> 1.1.2-1mdv2010.0
+ Revision: 420755
- update to new version 1.1.2

* Sun Mar 22 2009 Götz Waschk <waschk@mandriva.org> 1.0.8-1mdv2009.1
+ Revision: 360241
- new version
- fix source URL
- spec file fixes
- rename from unique

* Mon Feb 02 2009 Funda Wang <fwang@mandriva.org> 1.0.6-1mdv2009.1
+ Revision: 336473
- New version 1.0.6

* Mon Nov 24 2008 Götz Waschk <waschk@mandriva.org> 1.0.4-1mdv2009.1
+ Revision: 306202
- new version
- drop patch

* Sat Sep 06 2008 Adam Williamson <awilliamson@mandriva.org> 1.0.0-1mdv2009.0
+ Revision: 281896
- buildrequires gtk-doc, it seems
- %%{buildroot} not $RPM_BUILD_ROOT
- need to do autoreconf after patching configure.ac
- add underlink.patch (fixes an underlinking problem)
- new release 1.0.0

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Sep 07 2007 Adam Williamson <awilliamson@mandriva.org> 0.9.3-1mdv2008.0
+ Revision: 81367
- add glib and gtk+ buildrequires
- Import unique

