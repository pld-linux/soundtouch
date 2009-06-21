#
# TODO:
# - fix x86_64 build
#
Summary:	SoundTouch - sound processing library
Summary(pl.UTF-8):	SoundTouch - biblioteka do przetwarzania dźwięku
Name:		soundtouch
Version:	1.4.0
Release:	2
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://www.surina.net/soundtouch/%{name}-%{version}.tar.gz
# Source0-md5:	fc4bb10401624899efe4fb554d4fd3ed
Patch0:		%{name}-nosse.patch
URL:		http://www.surina.net/soundtouch/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
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
URL:		http://sky.prohosting.com/oparviai/soundtouch/soundstretch.html
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
%setup -q -n %{name}
%patch0 -p1

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
%attr(755,root,root) %{_libdir}/libSoundTouch.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libSoundTouch.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libSoundTouch.so
%{_libdir}/libSoundTouch.la
%{_includedir}/soundtouch
%{_aclocaldir}/soundtouch.m4
%{_pkgconfigdir}/soundtouch-1.4.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libSoundTouch.a

%files soundstretch
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/soundstretch
