Name:		texlive-lsc
Version:	15878
Release:	2
Summary:	Typesetting Live Sequence Charts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/lsc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lsc.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lsc.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package is similar to the msc package in that it provides
macros for typesetting a variant of sequence diagrams, in this
case the Live Sequence Charts of Damm and Harel. The package
supports the full LSC language of the original LSC paper, the
Klose-extensions for formal verification and some of the Harel-
extensions for the Play-In/Play-Out approach (cf. the manual).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bib/lsc/lsc.bib
%{_texmfdistdir}/tex/latex/lsc/lsc.sty
%doc %{_texmfdistdir}/doc/latex/lsc/README
%doc %{_texmfdistdir}/doc/latex/lsc/lsc.pdf
%doc %{_texmfdistdir}/doc/latex/lsc/lsc.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}
