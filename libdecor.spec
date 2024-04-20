%define major 0
%define libname %mklibname decor %{major}
%define devname %mklibname decor -d

Name:           libdecor
Version:        0.2.2
Release:        1
Summary:        Wayland client side decoration library
Group:          System/Libraries 
License:        MIT
URL:            https://gitlab.gnome.org/jadahl/libdecor
Source0:         https://gitlab.freedesktop.org/libdecor/libdecor/-/archive/%{version}/libdecor-%{version}.tar.bz2

BuildRequires:  meson
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(xkbcommon)
 
%description
Libdecor provides a small helper library for providing client side decoration to Wayland clients.

%package -n %{libname}
Summary:	Library for Libdecor provides a small helper library for providing client side decoration to Wayland clients.
Group:		System/Libraries

%description -n	%{libname}
This package contains the library needed to run programs dynamically
linked with %{name}.

 
%package -n %{devname}
Summary:        Development files for %{name}
Requires:       %{libname}%{?_isa} = %{version}-%{release}
 
%description -n %{devname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.
 
%prep
%autosetup -p1
 
%build
%meson -Ddemo=false
%meson_build
 
%install
%meson_install
 
%files -n %{libname}
%{_libdir}/libdecor-%{major}.so.%{major}*
%dir %{_libdir}/libdecor/
%dir %{_libdir}/libdecor/plugins-1
%{_libdir}/libdecor/plugins-1/libdecor-cairo.so
%{_libdir}/libdecor/plugins-1/libdecor-gtk.so
 
%files -n %{devname}
%license LICENSE
%doc README.md
%{_includedir}/libdecor-%{major}/
%{_libdir}/libdecor-%{major}.so
%{_libdir}/pkgconfig/libdecor-%{major}.pc
