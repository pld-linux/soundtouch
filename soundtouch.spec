Summary:	SoundTouch - sound processing library
Summary(pl):	SoundTouch - biblioteka do przetwarzania d¼wiêku
Name:		soundtouch
Version:	1.3.1
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://www.surina.net/soundtouch/%{name}-%{version}.tar.gz
# Source0-md5:	5e0185e81dbba2f2eed8581b7664ab04
Patch0:		%{name}-optflags.patch
Patch1:		%{name}-link.patch
URL:		http://www.surina.net/soundtouch/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# gcc runs out of regs in mmx_gcc.cpp
%define		specflags_ia32	-fomit-frame-pointer

%description
SoundTouch is a library for changing tempo, pitch and playback rate of
digital sound.

%description -l pl
SountTouch jest bibliotek± do zmiany tempa, wysoko¶ci i czêstotliwo¶ci
odtwarzania d¼wiêku cyfrowego.

%package devel
Summary:	Header files for SoundTouch library
Summary(pl):	Pliki nag³ówkowe biblioteki SoundTouch
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for SoundTouch library.

%description devel -l pl
Pliki nag³ówkowe biblioteki SoundTouch.

%package static
Summary:	Static SoundTouch library
Summary(pl):	Statyczna biblioteka SoundTouch
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static SoundTouch library.

%description static -l pl
Statyczna biblioteka SoundTouch.

%package soundstretch
Summary:	SoundStretch - sound processing application
Summary(pl):	SoundStretch - aplikacja do przetwarzania d¼wiêku
Group:		Applications/Sound
URL:		http://sky.prohosting.com/oparviai/soundtouch/soundstretch.html
Requires:	%{name} = %{version}-%{release}

%description soundstretch
SoundStretch is a command-line application for changing tempo, pitch
and playback rates of WAV sound files. This program also demonstrates
how the "SoundTouch" library can be used to process sound in own
programs.

%description soundstretch -l pl
SoundStretch to dzia³aj±ca z linii poleceñ aplikacja do zmiany tempa,
wysoko¶ci i czêstotliwo¶ci odtwarzania plików d¼wiêkowych WAV. Ten
program ma tak¿e byæ przyk³adem, jak mo¿na wykorzystywaæ bibliotekê
SoundTouch do przetwarzania d¼wiêku we w³asnych programach.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

# kill DOS eols
%{__perl} -pi -e 's/\r$//' soundtouch.m4

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-shared

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.html
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/soundtouch
%{_aclocaldir}/soundtouch.m4
%{_pkgconfigdir}/soundtouch-1.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files soundstretch
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/soundstretch
