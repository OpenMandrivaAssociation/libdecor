Name:           libdecor
Version:        0.1.0
Release:        2%{?dist}
Summary:        Wayland client side decoration library
 
License:        MIT
URL:            https://gitlab.gnome.org/jadahl/libdecor
Source:         %{url}/uploads/81adf91d27620e20bcc5f6b9b312d768/libdecor-0.1.0.tar.xz
 
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(xkbcommon)
 
%description
Libdecor provides a small helper library for providing client side decoration
to Wayland clients.
 
%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
 
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.
 
 
%prep
%autosetup -p1
 
 
%build
%meson -Ddemo=false
%meson_build
 
%install
%meson_install
 
%files
%license LICENSE
%doc README.md
%{_libdir}/libdecor-0.so.0*
%dir %{_libdir}/libdecor/
%dir %{_libdir}/libdecor/plugins-1
%{_libdir}/libdecor/plugins-1/libdecor-cairo.so
 
%files devel
%{_includedir}/libdecor-0/
%{_libdir}/libdecor-0.so
%{_libdir}/pkgconfig/libdecor-0.pc
