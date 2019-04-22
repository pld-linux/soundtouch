#
# Conditional build:
%bcond_without	openmp		# OpenMP support
%bcond_without	static_libs	# static library
#
Summary:	SoundTouch - sound processing library
Summary(pl.UTF-8):	SoundTouch - biblioteka do przetwarzania dźwięku
Name:		soundtouch
Version:	2.1.2
Release:	1
License:	LGPL v2.1+
Group:		Libraries
#Source0Download: https://gitlab.com/soundtouch/soundtouch/tags
Source0:	https://gitlab.com/soundtouch/soundtouch/-/archive/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	c86cbd3ac6978aa4111302c085641f78
URL:		http://www.surina.net/soundtouch/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
%ifarch %{ix86} %{x8664} x32
# <cpuid.h>
BuildRequires:	gcc >= 6:4.3
%endif
%{?with_openmp:BuildRequires:	libgomp-devel}
BuildRequires:	libstdc++-devel >= 6:4.3
BuildRequires:	libtool >= 2:1.5
BuildRequires:	pkgconfig
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# gcc runs out of regs in mmx_gcc.cpp
%define		specflags_ia32	-fomit-frame-pointer

%description
SoundTouch is a library for changing tempo, pitch and playback rate of
digital sound.

%description -l pl.UTF-8
SountTouch jest biblioteką do zmiany tempa, wysokości i częstotliwości
odtwarzania dźwięku cyfrowego.

%package devel
Summary:	Header files for SoundTouch library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki SoundTouch
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for SoundTouch library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki SoundTouch.

%package static
Summary:	Static SoundTouch library
Summary(pl.UTF-8):	Statyczna biblioteka SoundTouch
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static SoundTouch library.

%description static -l pl.UTF-8
Statyczna biblioteka SoundTouch.

%package soundstretch
Summary:	SoundStretch - sound processing application
Summary(pl.UTF-8):	SoundStretch - aplikacja do przetwarzania dźwięku
Group:		Applications/Sound
URL:		http://www.surina.net/soundtouch/soundstretch.html
Requires:	%{name} = %{version}-%{release}

%description soundstretch
SoundStretch is a command-line application for changing tempo, pitch
and playback rates of WAV sound files. This program also demonstrates
how the "SoundTouch" library can be used to process sound in own
programs.

%description soundstretch -l pl.UTF-8
SoundStretch to działająca z linii poleceń aplikacja do zmiany tempa,
wysokości i częstotliwości odtwarzania plików dźwiękowych WAV. Ten
program ma także być przykładem, jak można wykorzystywać bibliotekę
SoundTouch do przetwarzania dźwięku we własnych programach.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?with_openmp:--enable-openmp} \
	--disable-silent-rules \
	%{?with_static_libs:--enable-static}

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
%attr(755,root,root) %{_libdir}/libSoundTouch.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libSoundTouch.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libSoundTouch.so
%{_libdir}/libSoundTouch.la
%{_includedir}/soundtouch
%{_aclocaldir}/soundtouch.m4
%{_pkgconfigdir}/soundtouch.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libSoundTouch.a
%endif

%files soundstretch
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/soundstretch
