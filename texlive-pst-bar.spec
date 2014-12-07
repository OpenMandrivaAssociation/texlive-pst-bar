# revision 18734
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-bar
# catalog-date 2009-03-12 20:12:20 +0100
# catalog-license lppl
# catalog-version 0.92
Name:		texlive-pst-bar
Version:	0.92
Release:	9
Summary:	Produces bar charts using pstricks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-bar
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-bar.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-bar.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-bar.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
pst-bar uses pstricks to draw bar charts from data stored in a
comma-delimited file. Several types of bar charts may be drawn,
and the drawing parameters are highly customizable. No external
packages are required except those that are part of the
standard pstricks distribution.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/pst-bar/pst-bar.pro
%{_texmfdistdir}/tex/generic/pst-bar/pst-bar.tex
%{_texmfdistdir}/tex/latex/pst-bar/pst-bar.sty
%doc %{_texmfdistdir}/doc/generic/pst-bar/README
%doc %{_texmfdistdir}/doc/generic/pst-bar/pst-bar-doc.bib
%doc %{_texmfdistdir}/doc/generic/pst-bar/pst-bar-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pst-bar/pst-bar-doc.tex
%doc %{_texmfdistdir}/doc/generic/pst-bar/pst-bar-docDE.pdf
%doc %{_texmfdistdir}/doc/generic/pst-bar/pst-bar-docDE.tex
#- source
%doc %{_texmfdistdir}/source/generic/pst-bar/Makefile

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.92-2
+ Revision: 755220
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.92-1
+ Revision: 719333
- texlive-pst-bar
- texlive-pst-bar
- texlive-pst-bar
- texlive-pst-bar
- texlive-pst-bar

