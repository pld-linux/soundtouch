Summary:	SoundTouch - sound processing library
Summary(pl):	SoundTouch - biblioteka do przetwarzania d¼wiêku
Name:		soundtouch
Version:	1.1.1
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://www.sunpoint.net/~oparviai/soundtouch/%{name}_v%{version}.zip
# Source0-md5:	c154b7d3b9c3145297ee359b6d14e3d3
URL:		http://www.sunpoint.net/~oparviai/soundtouch/soundstretch.html
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.4d
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
Requires:	%{name} = %{version}
Requires:	libstdc++-devel

%description devel
Header files for SoundTouch library.

%description devel -l pl
Pliki nag³ówkowe biblioteki SoundTouch.

%package static
Summary:	Static SoundTouch library
Summary(pl):	Statyczna biblioteka SoundTouch
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static SoundTouch library.

%description static -l pl
Statyczna biblioteka SoundTouch.

%package soundstretch
Summary:	SoundStretch - sound processing application
Summary(pl):	SoundStretch - aplikacja do przetwarzania d¼wiêku
Group:		Applications/Sound
URL:		http://www.sunpoint.net/~oparviai/soundtouch/soundstretch.html
Requires:	%{name} = %{version}

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
%setup -q -n SoundTouch

%build
# try to abuse makefiles :)
%{__make} -C source/SoundTouch -f makefile.gcc \
	CC="libtool --mode=compile --tag=CXX %{__cxx}" \
	FLAGS="-I../../include %{rpmcflags}" \
	LINK=/bin/true

libtool --mode=link %{__cxx} %{rpmldflags} -o libSoundTouch.la \
	source/SoundTouch/*.lo -rpath %{_libdir}

%{__make} -C source/example/SoundStretch -f makefile.gcc \
	main.o RunParameters.o WavFile.o BPMDetect.o PeakFinder.o \
	CC="%{__cxx}" \
	FLAGS="-I../../../include %{rpmcflags}"

libtool --mode=link %{__cxx} %{rpmldflags} -o soundstretch \
	source/example/SoundStretch/*.o libSoundTouch.la

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_bindir},%{_includedir}/SoundTouch}

libtool --mode=install install libSoundTouch.la $RPM_BUILD_ROOT%{_libdir}
libtool --mode=install install soundstretch $RPM_BUILD_ROOT%{_bindir}
install include/*.h $RPM_BUILD_ROOT%{_includedir}/SoundTouch

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.TXT
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/SoundTouch

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files soundstretch
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/soundstretch
