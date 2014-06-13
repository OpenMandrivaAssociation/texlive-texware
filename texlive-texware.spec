# revision 29764
# category TLCore
# catalog-ctan /systems/knuth/dist/texware
# catalog-date 2012-06-27 22:19:02 +0200
# catalog-license knuth
# catalog-version undef
Name:		texlive-texware
Version:	20120627
Release:	6
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
%doc %{_texmfdistdir}/doc/man/man1/dvitype.man1.pdf
%doc %{_mandir}/man1/pooltype.1*
%doc %{_texmfdistdir}/doc/man/man1/pooltype.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
