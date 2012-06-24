Summary:	SoundTouch - sound processing library
Summary(pl):	SoundTouch - biblioteka do przetwarzania d�wi�ku
Name:		soundtouch
Version:	1.3.0
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://sky.prohosting.com/oparviai/soundtouch/%{name}_v%{version}.zip
# Source0-md5:	5c2d3f54320e5197885b3462f5f35a15
Patch0:		%{name}-am18.patch
Patch1:		%{name}-optflags.patch
Patch2:		%{name}-link.patch
URL:		http://sky.prohosting.com/oparviai/soundtouch/
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
SountTouch jest bibliotek� do zmiany tempa, wysoko�ci i cz�stotliwo�ci
odtwarzania d�wi�ku cyfrowego.

%package devel
Summary:	Header files for SoundTouch library
Summary(pl):	Pliki nag��wkowe biblioteki SoundTouch
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for SoundTouch library.

%description devel -l pl
Pliki nag��wkowe biblioteki SoundTouch.

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
Summary(pl):	SoundStretch - aplikacja do przetwarzania d�wi�ku
Group:		Applications/Sound
URL:		http://sky.prohosting.com/oparviai/soundtouch/soundstretch.html
Requires:	%{name} = %{version}-%{release}

%description soundstretch
SoundStretch is a command-line application for changing tempo, pitch
and playback rates of WAV sound files. This program also demonstrates
how the "SoundTouch" library can be used to process sound in own
programs.

%description soundstretch -l pl
SoundStretch to dzia�aj�ca z linii polece� aplikacja do zmiany tempa,
wysoko�ci i cz�stotliwo�ci odtwarzania plik�w d�wi�kowych WAV. Ten
program ma tak�e by� przyk�adem, jak mo�na wykorzystywa� bibliotek�
SoundTouch do przetwarzania d�wi�ku we w�asnych programach.

%prep
%setup -q -n SoundTouch-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

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

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files soundstretch
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/soundstretch
