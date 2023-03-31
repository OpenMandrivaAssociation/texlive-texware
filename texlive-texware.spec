Name:		texlive-texware
Version:	62387
Release:	2
Summary:	Utility programs for use with TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/systems/knuth/dist/texware
License:	KNUTH
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texware.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texware.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
