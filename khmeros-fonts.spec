%global fontname khmeros
%global archivename All_KhmerOS_%{version}

%global fontconf 65-0-%{fontname}

%global common_desc \
The Khmer OS fonts include Khmer and Latin alphabets, and they have equivalent \
sizes for Khmer and English alphabets, so that when texts mix both it is not \
necessary to have different point sizes for the text in each language. \
\
They were created by Danh Hong of the Cambodian Open Institute.


Name:           %{fontname}-fonts
Version:        5.0
Release:        16%{?dist}
Summary:        Khmer font set created by Danh Hong of the Cambodian Open Institute

Group:          User Interface/X
License:        LGPLv2+
URL:            http://www.khmeros.info/drupal/?q=en/download/fonts
Source0:        http://downloads.sourceforge.net/khmer/%{archivename}.zip
Source1:        65-0-khmeros-battambang.conf
Source2:        65-0-khmeros-bokor.conf
Source3:        65-0-khmeros-handwritten.conf
Source4:        65-0-khmeros-base.conf
Source5:        65-0-khmeros-metal-chrieng.conf
Source6:        65-0-khmeros-muol.conf
Source7:        65-0-khmeros-siemreap.conf
Source8:        License.txt

BuildArch:      noarch
BuildRequires:  fontpackages-devel

%description
%common_desc


%package common
Summary:        Common files of %{name}
Group:          User Interface/X
Requires:       fontpackages-filesystem

%description common
%common_desc

This package consists of files used by other %{name} packages.


%package -n %{fontname}-base-fonts
Summary:        Base KhmerOS font
Group:          User Interface/X
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-base-fonts
%common_desc

Base KhmerOS fonts.

%_font_pkg -n base -f 65-0-khmeros-base.conf KhmerOS.ttf KhmerOS_content.ttf KhmerOS_sys.ttf

%package -n %{fontname}-battambang-fonts
Summary:        Battambang font
Group:          User Interface/X
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-battambang-fonts
%common_desc

Battambang font.

%_font_pkg -n battambang -f 65-0-khmeros-battambang.conf KhmerOS_battambang.ttf

%package -n %{fontname}-bokor-fonts
Summary:        Bokor font
Group:          User Interface/X
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-bokor-fonts
%common_desc

Bokor font.

%_font_pkg -n bokor -f 65-0-khmeros-bokor.conf KhmerOS_bokor.ttf

%package -n %{fontname}-handwritten-fonts
Summary:        Freehand and fasthand fonts
Group:          User Interface/X
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-handwritten-fonts
%common_desc

Freehand and fasthand - handwritten fonts.

%_font_pkg -n handwritten -f 65-0-khmeros-handwritten.conf KhmerOS_freehand.ttf KhmerOS_fasthand.ttf

%package -n %{fontname}-metal-chrieng-fonts
Summary:        Metal Chrieng font
Group:          User Interface/X
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-metal-chrieng-fonts
%common_desc

Metal Chrieng font.

%_font_pkg -n metal-chrieng -f 65-0-khmeros-metal-chrieng.conf  KhmerOS_metalchrieng.ttf

%package -n %{fontname}-muol-fonts
Summary:        Muol fonts - normal, light and Pali
Group:          User Interface/X
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-muol-fonts
%common_desc

Muol fonts - normal, light and Pali.

%_font_pkg -n muol -f 65-0-khmeros-muol.conf KhmerOS_muol.ttf KhmerOS_muollight.ttf KhmerOS_muolpali.ttf

%package -n %{fontname}-siemreap-fonts
Summary:        Siemreap font
Group:          User Interface/X
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-siemreap-fonts
%common_desc

Siemreap font.

%_font_pkg -n siemreap -f 65-0-khmeros-siemreap.conf KhmerOS_siemreap.ttf


%prep
%setup -q -n %{archivename}
install -p %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} .
install -p %{SOURCE5} %{SOURCE6} %{SOURCE7} %{SOURCE8} .


%build
#nothing

%install
# get rid of the white space (' ')
mv 'KhmerOS .ttf' KhmerOS.ttf

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

for conffile in *.conf ; do
install -m 0644 -p $conffile %{buildroot}%{_fontconfig_templatedir}/${conffile}
ln -s %{_fontconfig_templatedir}/$conffile \
      %{buildroot}%{_fontconfig_confdir}/$conffile
done

%files common
%defattr(0644,root,root,0755)
%doc License.txt


%changelog
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 27 2012 Jon Ciesla <limburgher@gmail.com> - 5.0-15
- Remove old obsoletes, BZ 880479.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jul 05 2012 Parag <pnemade AT redhat.com> - 5.0-13
- Resolves:rh#837520 - Malformed fontconfig config file

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 12 2010 Parag <pnemade AT redhat.com> - 5.0-10
- Added License.txt in -common 

* Thu May 20 2010 Parag <pnemade AT redhat.com> - 5.0-9
- Resolves:rh#586253 - No fontconfig config files provided

* Tue Feb 16 2010 Parag <pnemade AT redhat.com> - 5.0-8
- drop -common owning %%{_fontdir}
      
* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 25 2009 Michal Nowak <mnowak@redhat.com> - 5.0-5
- provide Obsoletes and dependency on -common pkg

* Fri Jan 23 2009 Michal Nowak <mnowak@redhat.com> - 5.0-4
- changes to comply with F11 font rules

* Tue Jul 8 2008 Michal Nowak <mnowak@redhat.com> - 5.0-3
- reshaping to multiple subpackages based on font type/purpose
- license uncertainity is solved; licence field is set according
  to information from .ttf files read via gnome-font-viewer

* Mon Jul 7 2008 Michal Nowak <mnowak@redhat.com> - 5.0-2
- removing Fedora specific license
- refactoring summary and description texts (Nicolas Mailhot)

* Fri Jul 4 2008 Michal Nowak <mnowak@redhat.com> - 5.0-1
- initial release

