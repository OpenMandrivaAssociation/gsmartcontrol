Name:		gsmartcontrol
Version:	0.8.1
Release:	%mkrel 1
License:	GPLv2+
Url:		http://gsmartcontrol.berlios.de
Group:		System/Kernel and hardware
Source:		gsmartcontrol-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-build
Summary:	GSmartControl - Hard Disk Health Inspection Tool
Patch0:		gsmartcontrol-script.patch
Patch1:		gsmartcontrol-menu.patch

# Dependencies for various distributions. The actual deps are:
# smartmontools, pcre, (gtkmm2 >= 2.12 || (gtkmm2 >= 2.6.0 && libglademm >= 2.4.0))
# (with the respective -devel packages of the libraries for build requirements).
# For non-specified distributions we don't specify any dependencies to avoid errors.


Requires: smartmontools, libpcre0, libgtkmm2.4_1 >= 2.12.0
BuildRequires: gcc-c++, gcc-cpp, pcre-devel, gtkmm2.4-devel >= 2.12.0


%description
GSmartControl is a graphical user interface for smartctl, which is a tool for
querying and controlling SMART (Self-Monitoring, Analysis, and Reporting
Technology) data in hard disk drives. It allows you to inspect the drive's
SMART data to determine its health, as well as run various tests on it.

%prep

%setup -q
%patch0 -p0
%patch1 -p0
%configure
# Don't use configure parameters - let rpm set them.
# --prefix=/usr --enable-default-gcc-options --enable-gcc-optimize


%build
%make

%install
# %makeinstall
make DESTDIR=%buildroot install
rm %buildroot/%{_datadir}/applications/gsmartcontrol_gnome.desktop
rm %buildroot/%{_datadir}/applications/gsmartcontrol_other.desktop
mv %buildroot/%{_datadir}/applications/gsmartcontrol_kde.desktop %buildroot/%{_datadir}/applications/gsmartcontrol.desktop

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="System" \
  --add-category="X-MandrivaLinux-System-Configuration-Hardware;Settings;HardwareSettings" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

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


