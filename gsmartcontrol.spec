Name:		gsmartcontrol
Version:	0.8.3
Release:	%mkrel 1
License:	GPLv2, GPLv3
Url:		http://gsmartcontrol.berlios.de
Group:		System/Kernel and hardware
Source:		gsmartcontrol-%{version}.tar.bz2
SOURCE1:	gsmartcontrol_root.sh.in
BuildRoot:	%{_tmppath}/%{name}-%{version}-build
Summary:	GSmartControl - Hard Disk Health Inspection Tool
Requires: smartmontools, gtkmm2.4 >= 2.12.0
BuildRequires: pcre-devel, gtkmm2.4-devel >= 2.12.0, desktop-file-utils


%description
GSmartControl is a graphical user interface for smartctl, which is a tool for
querying and controlling SMART (Self-Monitoring, Analysis, and Reporting
Technology) data in hard disk drives. It allows you to inspect the drive's
SMART data to determine its health, as well as run various tests on it.

%prep
%setup -q
cp %SOURCE1 data/

%build
%configure2_5x
%make

%install
rm -fr %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%doc %{_datadir}/doc/gsmartcontrol
%defattr(-,root,root)
%attr(0755,root,root) %{_bindir}/*
%{_datadir}/gsmartcontrol
%{_datadir}/applications/*.desktop
%{_datadir}/icons/*
%{_datadir}/pixmaps/*
