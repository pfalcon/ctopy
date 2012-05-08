Name: ctopy
Version: 1.1
Release: 1
URL: http://www.catb.org/~esr/ctopy/
Source0: %{name}-%{version}.tar.gz
License: BSD
Group: Development
Summary: a quick and dirty (but nevertheless effective) C to Python translator
BuildRoot: %{_tmppath}/%{name}-root
BuildArch: noarch

%description
ctopy automates the parts of translating C source code to Python
source code that are difficult for a human but easy for a
machine. This allows a human programmer to concentrate on the
nontrivial parts of the translation.

%prep 
%setup -q

%build
make %{?_smp_mflags} ctopy.1

%install
[ "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf "$RPM_BUILD_ROOT"
mkdir -p "$RPM_BUILD_ROOT"%{_bindir}
mkdir -p "$RPM_BUILD_ROOT"%{_mandir}/man1/
cp ctopy "$RPM_BUILD_ROOT"%{_bindir}
cp ctopy.1 "$RPM_BUILD_ROOT"%{_mandir}/man1/

%clean
[ "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf "$RPM_BUILD_ROOT"

%files
%doc README COPYING
%defattr(-,root,root,-)
%{_mandir}/man1/ctopy.1*
%{_bindir}/ctopy

%changelog
* Tue Oct 18 2010 Eric S. Raymond <esr@snark.thyrsus.com> - 1.1-1
- Add a regression test.

* Wed Oct 18 2006 Eric S. Raymond <esr@snark.thyrsus.com> - 1.0-1
- Initial build.


