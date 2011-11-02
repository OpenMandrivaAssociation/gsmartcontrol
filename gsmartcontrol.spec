Name:		gsmartcontrol
Version:	0.8.6
Release:	%mkrel 1
License:	GPLv2, GPLv3
Url:		http://gsmartcontrol.berlios.de
Group:		System/Kernel and hardware
Source:		http://download.berlios.de/%{name}/%{name}-%{version}.tar.bz2
Patch0:		gsmartcontrol-0.8.6-glib2.31.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-build
Summary:	GSmartControl - Hard Disk Health Inspection Tool
Requires:	gtkmm2.4 >= 2.12.0
Requires:	smartmontools
Requires:	usermode-consoleonly
BuildRequires:	pcre-devel
BuildRequires:	gtkmm2.4-devel >= 2.12.0


%description
GSmartControl is a graphical user interface for smartctl, which is a tool for
querying and controlling SMART (Self-Monitoring, Analysis, and Reporting
Technology) data in hard disk drives. It allows you to inspect the drive's
SMART data to determine its health, as well as run various tests on it.

%prep
%setup -q
%if %{mdvver} > 201100
#GLib API changed in 2.31 so use patch
%patch0 -p1 -b .glib2.31
%endif
sed -i -e "s/Exec=.*gsmartcontrol-root\"/Exec=gsmartcontrol/" data/gsmartcontrol.desktop.in

%build
%configure2_5x
%make

%install
rm -fr %buildroot
%makeinstall_std

mkdir %{buildroot}%{_sbindir}
mv %{buildroot}%{_bindir}/%{name} %{buildroot}%{_sbindir}/%{name}
ln -s %{_bindir}/consolehelper %{buildroot}%{_bindir}/%{name}

%clean
rm -rf %buildroot

%files
%doc %{_datadir}/doc/%{name}
%defattr(-,root,root)
%attr(0755,root,root) %{_bindir}/*
%attr(0755,root,root) %{_sbindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/*
%{_datadir}/pixmaps/*
%{_mandir}/man1/%{name}-root.1*
%{_mandir}/man1/%{name}.1*
