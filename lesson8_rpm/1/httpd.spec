%define contentdir %{_datadir}/httpd
%define docroot /var/www
%define mmn 20120211
%define mmnisa %{mmn}%{__isa_name}%{__isa_bits}

%if 0%{?rhel} >= 7
%define vstring %(source /etc/os-release; echo ${REDHAT_SUPPORT_PRODUCT})
%else
%define vstring centos
%endif

%global mpm prefork

%define aprver 1.6.3
%define apuver 1.6.1
%define aprlibver 1
%define apulibver 1

%global rpmrel 3

Summary: Apache HTTP Server
Name: httpd
Version: 2.4.34
Release: %{rpmrel}%{?dist}
URL: https://httpd.apache.org/
Source0: https://www.apache.org/dist/httpd/httpd-%{version}.tar.bz2
Source1: https://www.apache.org/dist/apr/apr-%{aprver}.tar.bz2
Source2: https://www.apache.org/dist/apr/apr-util-%{apuver}.tar.bz2
Source8: index.html
Source9: server-status.conf
Source10: httpd.sysconf

# CentOS 7
Source11: httpd.tmpfiles
Source12: httpd.service
Source13: action-graceful.sh
Source14: action-configtest.sh

Source15: httpd.init

Source16: httpd.conf
Source23: 00-ssl.conf
Source24: 05-ssl.conf

# CentOS 7
Source25: 10-listen443.conf
Source26: httpd.socket
Source29: httpd.logrotate

# Documentation
Source30: README.confd
Source31: README.confmod

# CentOS 7
Source32: httpd.service.xml
Source40: htcacheclean.service
Source41: htcacheclean.sysconf
Source44: httpd@.service

# build/scripts patches
Patch1: httpd-2.4.1-apctl.patch
Patch2: httpd-2.4.9-apxs.patch
Patch3: httpd-2.4.1-deplibs.patch

# CentOS 7
Patch6: httpd-2.4.3-apctl-systemd.patch
# Needed for socket activation and mod_systemd patch
Patch19: httpd-2.4.25-detect-systemd.patch

# Features/functional changes
Patch21: httpd-2.4.33-mddefault.patch
Patch23: httpd-2.4.33-export.patch
Patch24: httpd-2.4.1-corelimit.patch
Patch25: httpd-2.4.25-selinux.patch
Patch26: httpd-2.4.4-r1337344+.patch
Patch27: httpd-2.4.2-icons.patch

# CentOS 7
Patch29: httpd-2.4.33-systemd.patch

Patch30: httpd-2.4.4-cachehardmax.patch
Patch31: httpd-2.4.33-sslmultiproxy.patch

# CentOS 7
Patch34: httpd-2.4.17-socket-activation.patch

Patch35: httpd-2.4.33-sslciphdefault.patch
Patch36: httpd-2.4.33-r1830819+.patch

# ulimit to apachectl
Patch41: httpd-2.4.27-apct2.patch
# compile apache statically with apr and apr-util
Patch42: httpd-2.4.27-static.patch
# compile apache with bundled APR and APR-Util
Patch43: httpd-2.4.27-apr.patch
# Set POSIX Semaphores as default
Patch44: httpd-2.4.27-sem.patch

# Bug fixes
# https://bugzilla.redhat.com/show_bug.cgi?id=1397243
Patch58: httpd-2.4.34-r1738878.patch
Patch59: httpd-2.4.34-r1555631.patch

# Security fixes

License: ASL 2.0
Group: System Environment/Daemons
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: autoconf, perl, perl-generators, pkgconfig, findutils, xmlto
BuildRequires: zlib-devel, libselinux-devel
BuildRequires: pcre-devel >= 5.0
BuildRequires: gcc

%if 0%{?rhel} >= 7
BuildRequires: systemd-devel
%endif

Requires: /etc/mime.types, redhat-logos
Provides: webserver
Provides: httpd-mmn = %{mmn}, httpd-mmn = %{mmnisa}
Requires: httpd-tools = %{version}-%{release}
Requires: httpd-filesystem = %{version}-%{release}
Requires(pre): httpd-filesystem

%if 0%{?rhel} >= 7
Requires(preun): systemd-units
Requires(postun): systemd-units
Requires(post): systemd-units
%endif

%description
The Apache HTTP Server is a powerful, efficient, and extensible
web server.

%package apr
Group: System Environment/Libraries
Summary: Apache Portable Runtime library
BuildRequires: libtool >= 1.4
Requires: httpd = %{version}-%{release}
Conflicts: apr, apr-devel

%description apr
The mission of the Apache Portable Runtime (APR) is to provide a
free library of C data structures and routines, forming a system
portability layer to as many operating systems as possible,
including Unices, MS Win32, BeOS and OS/2.

%package apr-util
Group: System Environment/Libraries
Summary: Apache Portable Runtime Utility library
BuildRequires: expat-devel
Requires: httpd = %{version}-%{release}
Requires: httpd-apr = %{version}-%{release}
Conflicts: apr-util, apr-util-devel

%description apr-util
The mission of the Apache Portable Runtime (APR) is to provide a
free library of C data structures and routines.  This library
contains additional utility interfaces for APR; including support
for XML, LDAP, database interfaces, URI parsing and more.

%package devel
Group: Development/Libraries
Summary: Development interfaces for the Apache HTTP Server
Requires: pkgconfig
Requires: httpd = %{version}-%{release}
Requires: httpd-apr = %{version}-%{release}
Requires: httpd-apr-util = %{version}-%{release}
BuildConflicts: apr-devel
BuildConflicts: apr-util-devel

%description devel
The httpd-devel package contains the APXS binary and other files
that you need to build Dynamic Shared Objects (DSOs) for the
Apache HTTP Server.

If you are installing the Apache HTTP Server and you want to be
able to compile or develop additional modules for Apache, you need
to install this package.

%package filesystem
Group: System Environment/Daemons
Summary: The basic directory layout for the Apache HTTP Server
BuildArch: noarch
Requires(pre): /usr/sbin/useradd

%description filesystem
The httpd-filesystem package contains the basic directory layout
for the Apache HTTP Server including the correct permissions
for the directories.

%package tools
Group: System Environment/Daemons
Summary: Tools for use with the Apache HTTP Server

%description tools
The httpd-tools package contains tools which can be used with
the Apache HTTP Server.

%package -n mod_ssl
Group: System Environment/Daemons
Summary: SSL/TLS module for the Apache HTTP Server
Epoch: 1
BuildRequires: openssl-devel
Requires(pre): httpd-filesystem
Requires: httpd = 0:%{version}-%{release}, httpd-mmn = %{mmnisa}

%description -n mod_ssl
The mod_ssl module provides strong cryptography for the Apache Web
server via the Secure Sockets Layer (SSL) and Transport Layer
Security (TLS) protocols.

%prep
%setup -q
%setup -q -T -D -a 1
%setup -q -T -D -a 2

# Make sure you have APR and APR-Util already installed on your system. If you
# don't, or prefer to not use the system-provided versions, download the latest
# versions of both APR and APR-Util from Apache APR, unpack them into
# /httpd_source_tree_root/srclib/apr and /httpd_source_tree_root/srclib/apr-util
# (be sure the directory names do not have version numbers; for example, the APR
# distribution must be under /httpd_source_tree_root/srclib/apr/) and use
# ./configure's --with-included-apr option.
mv apr-%{aprver} srclib/apr
mv apr-util-%{apuver} srclib/apr-util

%patch1 -p1 -b .apctl
%patch2 -p1 -b .apxs
%patch3 -p1 -b .deplibs

%if 0%{?rhel} >= 7
%patch6 -p1 -b .apctlsystemd
%patch19 -p1 -b .detectsystemd
%endif

%patch21 -p1 -b .mddefault
%patch23 -p1 -b .export
%patch24 -p1 -b .corelimit
%patch25 -p1 -b .selinux
#%patch26 -p1 -b .r1337344+
%patch27 -p1 -b .icons

%if 0%{?rhel} >= 7
%patch29 -p1 -b .systemd
%endif

%patch30 -p1 -b .cachehardmax
#%patch31 -p1 -b .sslmultiproxy

%if 0%{?rhel} >= 7
%patch34 -p1 -b .socketactivation
%endif

%patch35 -p1 -b .sslciphdefault
%patch36 -p1 -b .r1830819+

%patch41 -p1 -b .apct2
%patch42 -p1 -b .static
%patch43 -p1 -b .apr
%patch44 -p1 -b .sem

%patch58 -p1 -b .r1738878
%patch59 -p1 -b .r1555631

# Patch in the vendor string
sed -i '/^#define PLATFORM/s/Unix/%{vstring}/' os/unix/os.h

cp -p $RPM_SOURCE_DIR/server-status.conf server-status.conf

# Safety check: prevent build if defined MMN does not equal upstream MMN.
vmmn=`echo MODULE_MAGIC_NUMBER_MAJOR | cpp -include include/ap_mmn.h | sed -n '/^2/p'`
if test "x${vmmn}" != "x%{mmn}"; then
   : Error: Upstream MMN is now ${vmmn}, packaged MMN is %{mmn}
   : Update the mmn macro and rebuild.
   exit 1
fi

%if 0%{?rhel} >= 7
sed 's/@MPM@/%{mpm}/' < $RPM_SOURCE_DIR/httpd.service.xml \
    > httpd.service.xml

xmlto man ./httpd.service.xml
%endif

: Building with MMN %{mmn}, MMN-ISA %{mmnisa} and vendor string '%{vstring}'

%build
# reconfigure to enable wired minds module
./buildconf

# regenerate configure scripts
autoheader && autoconf || exit 1

# Before configure; fix location of build dir in generated apxs
%{__perl} -pi -e "s:\@exp_installbuilddir\@:%{_libdir}/httpd/build:g" \
        support/apxs.in

# -fPIC required for compilling APR and APR-Util and linking them with PIE httpd
# and tools (--enable-pie)
# https://lists.debian.org/debian-devel/2016/05/msg00309.html
export CFLAGS="$RPM_OPT_FLAGS -fPIC"
export LDFLAGS="-Wl,-z,relro,-z,now"

# httpd-2.4.25-selinux.patch adds -lselinux flag into HTTPD_LIBS which not in
# use by autotools
export LIBS="-lselinux"

# Hard-code path to links to avoid unnecessary builddep
export LYNX_PATH=/usr/bin/links

# Build the daemon
./configure \
    --prefix=%{_sysconfdir}/httpd \
    --exec-prefix=%{_prefix} \
    --bindir=%{_bindir} \
    --sbindir=%{_sbindir} \
    --mandir=%{_mandir} \
    --libdir=%{_libdir} \
    --sysconfdir=%{_sysconfdir}/httpd/conf \
    --includedir=%{_includedir}/httpd \
    --libexecdir=%{_libdir}/httpd/modules \
    --datadir=%{contentdir} \
    --enable-layout=Fedora \
    --with-installbuilddir=%{_libdir}/httpd/build \
    --with-mpm=%{mpm} \
    --with-pcre \
    --enable-pie \
    --with-included-apr \
    --enable-modules=none \
    --enable-mods-static=few \
    --enable-include \
    --enable-deflate \
    --enable-expires \
    --enable-proxy \
        --enable-proxy-ftp=no \
        --enable-proxy-fcgi=no \
        --enable-proxy-scgi=no \
        --enable-proxy-fdpass=no \
        --enable-proxy-ajp=no \
        --enable-proxy-balancer=no \
        --enable-proxy-express=no \
        --enable-proxy-uwsgi=no \
    --enable-asis \
    --enable-cgi \
    --enable-vhost-alias \
    --enable-negotiation \
    --enable-actions \
    --enable-speling \
    --enable-userdir \
    --enable-rewrite \
    --enable-substitute \
    --enable-remoteip \
    --enable-socache-shmcb \
    --enable-ssl=shared \
    --disable-reqtimeout \
    --disable-status

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

%if 0%{?rhel} >= 7
# Install systemd service files (CentOS 7)
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
for s in httpd.service htcacheclean.service httpd.socket httpd@.service; do
  install -p -m 644 $RPM_SOURCE_DIR/${s} \
                    $RPM_BUILD_ROOT%{_unitdir}/${s}
done
%else
# install SYSV init stuff
mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d
install -m 755 %{SOURCE15} \
        $RPM_BUILD_ROOT/etc/rc.d/init.d/httpd
%endif

# install conf file/directory
mkdir $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d \
    $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.modules.d
install -m 644 $RPM_SOURCE_DIR/README.confd \
    $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d/README
install -m 644 $RPM_SOURCE_DIR/README.confmod \
    $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.modules.d/README
for f in \
    00-ssl.conf; do
    install -m 644 -p $RPM_SOURCE_DIR/$f \
        $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.modules.d/$f
done

%if 0%{?rhel} >= 7
# install systemd override drop directory
# Web application packages can drop snippets into this location if
# they need ExecStart[pre|post].
mkdir $RPM_BUILD_ROOT%{_unitdir}/httpd.service.d
mkdir $RPM_BUILD_ROOT%{_unitdir}/httpd.socket.d
install -m 644 -p $RPM_SOURCE_DIR/10-listen443.conf \
    $RPM_BUILD_ROOT%{_unitdir}/httpd.socket.d/10-listen443.conf
%endif

for f in \
    05-ssl.conf; do
    install -m 644 -p $RPM_SOURCE_DIR/$f \
        $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d/$f
done

# Split-out extra config shipped as default in conf.d:
# we have single httpd.conf with all standard settings inside
#for f in autoindex; do
#  install -m 644 docs/conf/extra/httpd-${f}.conf \
#        $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d/${f}.conf
#done

rm $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf/*.conf
install -m 644 -p $RPM_SOURCE_DIR/httpd.conf \
   $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf/httpd.conf

mkdir $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
install -m 644 -p $RPM_SOURCE_DIR/httpd.sysconf \
   $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/httpd
install -m 644 -p $RPM_SOURCE_DIR/htcacheclean.sysconf \
   $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/htcacheclean

%if 0%{?rhel} >= 7
# tmpfiles.d configuration (CentOS 7)
mkdir -p $RPM_BUILD_ROOT%{_prefix}/lib/tmpfiles.d
install -m 644 -p $RPM_SOURCE_DIR/httpd.tmpfiles \
    $RPM_BUILD_ROOT%{_prefix}/lib/tmpfiles.d/httpd.conf
%endif

# Other directories
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/dav \
         $RPM_BUILD_ROOT%{_localstatedir}/lib/httpd
%if 0%{?rhel} >= 7
mkdir -p $RPM_BUILD_ROOT/run/httpd/htcacheclean
%else
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/run/httpd/htcacheclean
%endif

# Substitute in defaults which are usually done (badly) by "make install"
sed -i \
   "s,@@ServerRoot@@/var,%{_localstatedir}/lib/dav,;
    s,@@ServerRoot@@/user.passwd,/etc/httpd/conf/user.passwd,;
    s,@@ServerRoot@@/docs,%{docroot},;
    s,@@ServerRoot@@,%{docroot},;
    s,@@Port@@,80,;" \
    docs/conf/extra/*.conf

# Create cache directory
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/cache/httpd \
         $RPM_BUILD_ROOT%{_localstatedir}/cache/httpd/proxy \
         $RPM_BUILD_ROOT%{_localstatedir}/cache/httpd/ssl

mkdir -p $RPM_BUILD_ROOT/%{_libexecdir}

# Make the MMN accessible to module packages
echo %{mmnisa} > $RPM_BUILD_ROOT%{_includedir}/httpd/.mmn
cat > macros.httpd <<EOF
%%_httpd_mmn %{mmnisa}
%%_httpd_apxs %%{_bindir}/apxs
%%_httpd_modconfdir %%{_sysconfdir}/httpd/conf.modules.d
%%_httpd_confdir %%{_sysconfdir}/httpd/conf.d
%%_httpd_contentdir %{contentdir}
%%_httpd_moddir %%{_libdir}/httpd/modules
EOF

%if 0%{?rhel} >= 7
mkdir -p $RPM_BUILD_ROOT%{_rpmconfigdir}/macros.d
install -m 644 -D macros.httpd \
           $RPM_BUILD_ROOT%{_rpmconfigdir}/macros.d/macros.httpd
%else
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/rpm
install -m 644 -c macros.httpd \
           $RPM_BUILD_ROOT%{_sysconfdir}/rpm/macros.httpd
%endif


# Handle contentdir
mkdir $RPM_BUILD_ROOT%{contentdir}/noindex \
      $RPM_BUILD_ROOT%{contentdir}/server-status
install -m 644 -p $RPM_SOURCE_DIR/index.html \
        $RPM_BUILD_ROOT%{contentdir}/noindex/index.html
install -m 644 -p docs/server-status/* \
        $RPM_BUILD_ROOT%{contentdir}/server-status
rm -rf $RPM_BUILD_ROOT%{contentdir}/htdocs

# remove manual sources
find $RPM_BUILD_ROOT%{contentdir}/manual \( \
    -name \*.xml -o -name \*.xml.* -o -name \*.ent -o -name \*.xsl -o -name \*.dtd \
    \) -print0 | xargs -0 rm -f

# Strip the manual down just to English and replace the typemaps with flat files:
set +x
for f in `find $RPM_BUILD_ROOT%{contentdir}/manual -name \*.html -type f`; do
   if test -f ${f}.en; then
      cp ${f}.en ${f}
      rm ${f}.*
   fi
done
set -x

# Clean Document Root
rm -rf $RPM_BUILD_ROOT%{docroot}/html/*.html \
      $RPM_BUILD_ROOT%{docroot}/cgi-bin/*

# Symlink for the powered-by-$DISTRO image:
ln -s ../../pixmaps/poweredby.png \
        $RPM_BUILD_ROOT%{contentdir}/icons/poweredby.png

# symlinks for /etc/httpd
ln -s ../..%{_localstatedir}/log/httpd $RPM_BUILD_ROOT/etc/httpd/logs
ln -s ../..%{_localstatedir}/lib/httpd $RPM_BUILD_ROOT/etc/httpd/state
%if 0%{?rhel} >= 7
ln -s /run/httpd $RPM_BUILD_ROOT/etc/httpd/run
%else
ln -s %{_localstatedir}/run/httpd $RPM_BUILD_ROOT/etc/httpd/run
%endif
ln -s ../..%{_libdir}/httpd/modules $RPM_BUILD_ROOT/etc/httpd/modules

%if 0%{?rhel} >= 7
# Install action scripts
mkdir -p $RPM_BUILD_ROOT%{_libexecdir}/initscripts/legacy-actions/httpd
for f in graceful configtest; do
    install -p -m 755 $RPM_SOURCE_DIR/action-${f}.sh \
        $RPM_BUILD_ROOT%{_libexecdir}/initscripts/legacy-actions/httpd/${f}
done
%endif

# Install logrotate config
mkdir -p $RPM_BUILD_ROOT/etc/logrotate.d
install -m 644 -p $RPM_SOURCE_DIR/httpd.logrotate \
        $RPM_BUILD_ROOT/etc/logrotate.d/httpd

%if 0%{?rhel} >= 7
# Install systemd service man pages (CentOS 7)
install -m 644 -p httpd.service.8 httpd.socket.8 httpd@.service.8 \
    $RPM_BUILD_ROOT%{_mandir}/man8
%endif

# fix man page paths
sed -e "s|/usr/local/apache2/conf/httpd.conf|/etc/httpd/conf/httpd.conf|" \
    -e "s|/usr/local/apache2/conf/mime.types|/etc/mime.types|" \
    -e "s|/usr/local/apache2/conf/magic|/etc/httpd/conf/magic|" \
    -e "s|/usr/local/apache2/logs/error_log|/var/log/httpd/error_log|" \
    -e "s|/usr/local/apache2/logs/access_log|/var/log/httpd/access_log|" \
    -e "s|/usr/local/apache2/logs/httpd.pid|/run/httpd/httpd.pid|" \
    -e "s|/usr/local/apache2|/etc/httpd|" < docs/man/httpd.8 \
  > $RPM_BUILD_ROOT%{_mandir}/man8/httpd.8
# Make ap_config_layout.h libdir-agnostic
sed -i '/.*DEFAULT_..._LIBEXECDIR/d;/DEFAULT_..._INSTALLBUILDDIR/d' \
    $RPM_BUILD_ROOT%{_includedir}/httpd/ap_config_layout.h

# Fix path to instdso in special.mk
sed -i '/instdso/s,top_srcdir,top_builddir,' \
    $RPM_BUILD_ROOT%{_libdir}/httpd/build/special.mk

# Remove unpackaged files
rm -vf \
      $RPM_BUILD_ROOT%{_libdir}/*.exp \
      $RPM_BUILD_ROOT/etc/httpd/conf/mime.types \
      $RPM_BUILD_ROOT%{_libdir}/httpd/modules/*.exp \
      $RPM_BUILD_ROOT%{_libdir}/httpd/build/config.nice \
      $RPM_BUILD_ROOT%{_bindir}/{ap?-config,dbmmanage} \
      $RPM_BUILD_ROOT%{_sbindir}/{checkgid,envvars*} \
      $RPM_BUILD_ROOT%{contentdir}/htdocs/* \
      $RPM_BUILD_ROOT%{_mandir}/man1/dbmmanage.* \
      $RPM_BUILD_ROOT%{contentdir}/cgi-bin/*

rm -rf $RPM_BUILD_ROOT/etc/httpd/conf/{original,extra}

%pre filesystem
#getent group apache >/dev/null || groupadd -g 48 -r apache
#getent passwd apache >/dev/null || \
#  useradd -r -u 48 -g apache -s /sbin/nologin \
#    -d %{contentdir} -c "Apache" apache
getent group nogroup >/dev/null || groupadd -o -g 65534 nogroup
pkill -u nobody && usermod -u 65534 -o nobody || \
    usermod -u 65534 -o nobody
exit 0

%post
%if 0%{?rhel} >= 7
%systemd_post httpd.service htcacheclean.service httpd.socket
%else
/sbin/chkconfig --add httpd
%endif

%preun
%if 0%{?rhel} >= 7
%systemd_preun httpd.service htcacheclean.service httpd.socket
%else
if [ $1 = 0 ]; then
        /sbin/service httpd stop > /dev/null 2>&1
        /sbin/chkconfig --del httpd
fi
%endif

%postun
%if 0%{?rhel} >= 7
%systemd_postun
%endif

# Trigger for conversion from SysV, per guidelines at:
# https://fedoraproject.org/wiki/Packaging:ScriptletSnippets#Systemd
%triggerun -- httpd < 2.2.21-5
# Save the current service runlevel info
# User must manually run systemd-sysv-convert --apply httpd
# to migrate them to systemd targets
%if 0%{?rhel} >= 7
/usr/bin/systemd-sysv-convert --save httpd.service >/dev/null 2>&1 ||:

# Run these because the SysV package being removed won't do them
/sbin/chkconfig --del httpd >/dev/null 2>&1 || :
%endif

# disabled while SysV not configured
%posttrans
%if 0%{?rhel} >= 7
test -f /etc/sysconfig/httpd-disable-posttrans || \
    /bin/systemctl try-restart --no-block httpd.service htcacheclean.service >/dev/null 2>&1 || :
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)

%doc ABOUT_APACHE README CHANGES LICENSE VERSIONING NOTICE
%doc docs/conf/extra/*.conf
%doc server-status.conf

%{_sysconfdir}/httpd/modules
%{_sysconfdir}/httpd/logs
%{_sysconfdir}/httpd/state
%{_sysconfdir}/httpd/run
%dir %{_sysconfdir}/httpd/conf
%config(noreplace) %{_sysconfdir}/httpd/conf/httpd.conf
%config(noreplace) %{_sysconfdir}/httpd/conf/magic
%config(noreplace) %{_sysconfdir}/logrotate.d/httpd

%dir %{_sysconfdir}/httpd/conf.modules.d
%{_sysconfdir}/httpd/conf.modules.d/README

%config(noreplace) %{_sysconfdir}/sysconfig/htcacheclean
%config(noreplace) %{_sysconfdir}/sysconfig/httpd

%if 0%{?rhel} >= 7
%{_prefix}/lib/tmpfiles.d/httpd.conf
%dir %{_libexecdir}/initscripts/legacy-actions/httpd
%{_libexecdir}/initscripts/legacy-actions/httpd/*
%endif

%{_sbindir}/ht*
%{_sbindir}/fcgistarter
%{_sbindir}/apachectl
%{_sbindir}/rotatelogs

%dir %{_libdir}/httpd
%dir %{_libdir}/httpd/modules

%dir %{contentdir}/error
%dir %{contentdir}/error/include
%dir %{contentdir}/noindex
%dir %{contentdir}/server-status
%{contentdir}/icons/*
%{contentdir}/error/README
%{contentdir}/error/*.var
%{contentdir}/error/include/*.html
%{contentdir}/noindex/index.html
%{contentdir}/server-status/*
%if 0%{?rhel} >= 7
%attr(0710,root,apache) %dir /run/httpd
%attr(0700,apache,apache) %dir /run/httpd/htcacheclean
%else
%attr(0710,root,apache) %dir %{_localstatedir}/run/httpd
%attr(0700,apache,apache) %dir %{_localstatedir}/run/httpd/htcacheclean
%endif
%attr(0700,root,root) %dir %{_localstatedir}/log/httpd
%attr(0700,apache,apache) %dir %{_localstatedir}/lib/dav
%attr(0700,apache,apache) %dir %{_localstatedir}/lib/httpd
%attr(0700,apache,apache) %dir %{_localstatedir}/cache/httpd
%attr(0700,apache,apache) %dir %{_localstatedir}/cache/httpd/proxy
%{_mandir}/man8/*

%if 0%{?rhel} >= 7
%{_unitdir}/httpd.service
%{_unitdir}/httpd@.service
%{_unitdir}/htcacheclean.service
%{_unitdir}/*.socket
%else
%{_sysconfdir}/rc.d/init.d/httpd
%endif
# skip manual packaging (Mon Aug 21 2017 - aursu)
%exclude %{contentdir}/manual

%files filesystem
%dir %{_sysconfdir}/httpd
%dir %{_sysconfdir}/httpd/conf.d
%{_sysconfdir}/httpd/conf.d/README
%dir %{docroot}
%dir %{docroot}/cgi-bin
%dir %{docroot}/html
%dir %{contentdir}
%dir %{contentdir}/icons
%if 0%{?rhel} >= 7
%attr(755,root,root) %dir %{_unitdir}/httpd.service.d
%attr(755,root,root) %dir %{_unitdir}/httpd.socket.d
%endif

%files tools
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/man1/*
%doc LICENSE NOTICE
%exclude %{_bindir}/apxs
%exclude %{_mandir}/man1/apxs.1*

%files apr
%defattr(-,root,root,-)
%{_libdir}/libapr-%{aprlibver}.so.*
%{_bindir}/apr-%{aprlibver}-config
%{_libdir}/libapr-%{aprlibver}.*a
%{_libdir}/libapr-%{aprlibver}.so
%{_libdir}/pkgconfig/apr-%{aprlibver}.pc
%dir %{_libdir}/apr-%{aprlibver}
%dir %{_libdir}/apr-%{aprlibver}/build
%{_libdir}/apr-%{aprlibver}/build/*
%dir %{_includedir}/apr-%{aprlibver}
%{_includedir}/apr-%{aprlibver}/*.h

%files apr-util
%defattr(-,root,root,-)
%{_libdir}/libaprutil-%{apulibver}.so.*
%{_bindir}/apu-%{apulibver}-config
%{_libdir}/libaprutil-%{apulibver}.*a
%{_libdir}/libaprutil-%{apulibver}.so
%{_libdir}/pkgconfig/apr-util-%{apulibver}.pc

%files -n mod_ssl
%defattr(-,root,root)
%{_libdir}/httpd/modules/mod_ssl.so
%config(noreplace) %{_sysconfdir}/httpd/conf.modules.d/00-ssl.conf
%config(noreplace) %{_sysconfdir}/httpd/conf.d/05-ssl.conf
%attr(0700,apache,root) %dir %{_localstatedir}/cache/httpd/ssl
%if 0%{?rhel} >= 7
%{_unitdir}/httpd.socket.d/10-listen443.conf
%endif

%files devel
%defattr(-,root,root)
%{_includedir}/httpd
%{_bindir}/apxs
%{_mandir}/man1/apxs.1*
%dir %{_libdir}/httpd/build
%{_libdir}/httpd/build/*.mk
%{_libdir}/httpd/build/*.sh
%if 0%{?rhel} >= 7
%{_rpmconfigdir}/macros.d/macros.httpd
%else
%{_sysconfdir}/rpm/macros.httpd
%endif

%changelog
* Fri Jul 20 2018 Joe Orton <jorton@redhat.com> - 2.4.34-3
- mod_ssl: fix OCSP regression (upstream r1555631)

* Wed Jul 18 2018 Joe Orton <jorton@redhat.com> - 2.4.34-1
- update to 2.4.34 (#1601160)

* Mon Jul 16 2018 Joe Orton <jorton@redhat.com> - 2.4.33-10
- don't block on service try-restart in posttrans scriptlet
- add Lua-based /server-status example page to docs

* Tue Jul 10 2018 Alexander Ursu <alexander.ursu@gmail.com> - 2.4.33-5
- add httpd@.service; update httpd.service(8) and add new stub
- mod_md: change hard-coded default MdStoreDir to state/md (#1563846)
- updated APR and Apr-Util libraries

* Mon May 28 2018 Alexander Ursu <alexander.ursu@gmail.com> - 2.4.33-1
- mod_ssl: drop implicit 'SSLEngine on' for vhost w/o certs (#1564537)

* Fri Jan 05 2018 Alexander Ursu <alexander.ursu@gmail.com> - 2.4.29-3
- fixed pid file location for CentOS 6
- fixed default httpd.conf

* Tue Oct 31 2017 Alexander Ursu <alexander.ursu@gmail.com> - 2.4.29-2
- fixed rebuild script call

* Wed Oct 25 2017 Luboš Uhliarik <luhliari@redhat.com> - 2.4.29-1
- new version 2.4.29

* Mon Oct  9 2017 Joe Orton <jorton@redhat.com> - 2.4.27-7
- move httpd.service.d, httpd.socket.d dirs to -filesystem
- add new content-length filter (upstream PR 61222)
- update mod_systemd (r1802251)

* Fri Sep 22 2017 Joe Orton <jorton@redhat.com> - 2.4.27-13
- drop Requires(post) for mod_ssl

* Tue Sep 12 2017 Alexander Ursu <alexander.ursu@gmail.com> - 2.4.27-2
- disabled proxy balancer and protocols SCGI, AJP and FTP

* Mon Sep 11 2017 Alexander Ursu <alexander.ursu@gmail.com> - 2.4.27-1
- configured according to Apache 2.2 configuration

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.27-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

