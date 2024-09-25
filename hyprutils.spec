%define major 1
%define libname %mklibname hyprutils
%define devname %mklibname -d hyprutils

Name:           hyprutils
Version:        0.2.3
Release:        1
Summary:        Hyprland utilities library used across the ecosystem
Group:          System/Hyprland
License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hyprutils
Source:         https://github.com/hyprwm/hyprutils/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  pkgconfig(pixman-1)

%description
%{summary}.

%package -n %{libname}
Summary:        Shared library for %{name}
Provides:  %{name} = %{EVRD}

%description -n %{libname}
This package contains the shared library files.

%package -n %{devname}
Summary:        Development files for %{name}
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Development files for %{name}.

%prep
%autosetup -p1

%build
%cmake
%make_build

%install
%make_install -C build

%files -n %{libname}
%license LICENSE
%doc README.md
%{_libdir}/lib%{name}.so.%{version}
%{_libdir}/lib%{name}.so.%{major}

%files -n %{devname}
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
