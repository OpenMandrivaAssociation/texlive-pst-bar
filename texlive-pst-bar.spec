Name:		texlive-pst-bar
Version:	64331
Release:	2
Summary:	Produces bar charts using pstricks
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-bar
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-bar.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-bar.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/dvips/pst-bar
%{_texmfdistdir}/tex/generic/pst-bar
%{_texmfdistdir}/tex/latex/pst-bar
%doc %{_texmfdistdir}/doc/generic/pst-bar

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc %{buildroot}%{_texmfdistdir}
