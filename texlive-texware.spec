# revision 23089
# category TLCore
# catalog-ctan /systems/knuth/dist/texware
# catalog-date 2011-03-22 20:58:47 +0100
# catalog-license knuth
# catalog-version undef
Name:		texlive-texware
Version:	20110322
Release:	1
Summary:	Utility programs for use with TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/systems/knuth/dist/texware
License:	KNUTH
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texware.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texware.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Requires:	texlive-texware.bin
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
