%define		_state		stable
%define		orgname		bovo
%define		qtver		4.8.0

Summary:	bovo
Name:		kde4-bovo
Version:	4.12.0
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	cfa48bda5e7be690d00356c850e19d7d
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	phonon-devel >= 4.3.80
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kde4-libkdegames-devel >= %{version}
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
Obsoletes:	kde4-kdegames-bovo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
bovo.

%description-l pl.UTF-8
bovo.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT/var/games
touch $RPM_BUILD_ROOT/var/games/kbounce.scores
# remove locolor icons
rm -rf $RPM_BUILD_ROOT%{_iconsdir}/locolor

%find_lang bovo	--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post			-p /sbin/ldconfig
%postun			-p /sbin/ldconfig

%files -f bovo.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/bovo
%{_desktopdir}/kde4/bovo.desktop
%{_datadir}/apps/bovo
%{_iconsdir}/hicolor/*x*/apps/bovo.png
%{_iconsdir}/hicolor/scalable/apps/bovo.svgz
