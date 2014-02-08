# revision 26689
# category TLCore
# catalog-ctan /systems/knuth/dist/texware
# catalog-date 2011-03-22 20:58:47 +0100
# catalog-license knuth
# catalog-version undef
Name:		texlive-texware
Version:	20110322
Release:	4
Summary:	Utility programs for use with TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/systems/knuth/dist/texware
License:	KNUTH
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texware.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texware.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-texware.bin

%description
Basic utitility programs, comprising: - dvitype, which converts
a TeX output (DVI) file to a plain text file (see also the DVI
Text Language suite); - pooltype, which converts a TeX-suite
program's "pool" (string) file into human-readable form; and -
tftopl and pltotf, which convert TeX Font Metric (TFM) file to
human readable Property List (PL) files and vice versa.

#-----------------------------------------------------------------------
%files
%doc %{_mandir}/man1/dvitype.1*
%doc %{_texmfdir}/doc/man/man1/dvitype.man1.pdf
%doc %{_mandir}/man1/pooltype.1*
%doc %{_texmfdir}/doc/man/man1/pooltype.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1


%changelog
* Wed Aug 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 20110322-3
+ Revision: 812921
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20110322-2
+ Revision: 756793
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20110322-1
+ Revision: 719723
- texlive-texware
- texlive-texware
- texlive-texware

