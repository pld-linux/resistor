# TODO: optflags
Summary:	Resistor color bands/values converter
Summary(pl):	Konwerter kolorowych pasków/warto¶ci oporników
Name:		resistor
Version:	1.0
Release:	0.1
Epoch:		0
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/resistor/%{name}.src.tar.gz
# Source0-md5:	fc681b4843eb9c58e7976d0b3473a2a5
URL:		http://resistor.sourceforge.net/
BuildRequires:	qmake
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A simple GUI application that converts resistor color bands to
resistor values and vice-versa. The code is C++ using the QT widget
set.

%description -l pl
Prosta aplikacja z GUI pozwalaj±ca na konwersjê kolorów pasków na
opornikach na warto¶ci (i odwrotnie). Zaimplementowana jest w C++, z
u¿yciem QT.

%prep
%setup -q -n %{name}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%attr(754,root,root) /etc/rc.d/init.d/%{name}
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}
