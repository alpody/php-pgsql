Name:		php-pgsql-alpody
Version:	0.0.3        
Release:        1%{?dist}
Summary:	Postgresql 10 extension for php 7.1.11        

License:	GPL        
URL:		http://www.example.com/%{name}	            
Source0:	php-pgsql-alpody-%{version}.tar.gz        
Source1:	php-7.1.11.tar.bz2

BuildRequires:	bash  
Requires:	bash       

%description
Postgresql 10 extension pgsql.so and pdo_pgsql for php 7.1.11

%prep
%setup -q -b 1

%build
cd %{_builddir}/php-7.1.11/ext/pgsql/
phpize
./configure --with-pgsql=/usr/pgsql-10/
make 

cd %{_builddir}/php-7.1.11/ext/pdo_pgsql/
phpize
./configure --with-pdo_pgsql=/usr/pgsql-10/
make 

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/etc/php.d 
mkdir -p %{buildroot}/usr/lib64/php/modules/
install -m 0644 *.ini %{buildroot}/etc/php.d/
install -m 0644 %{_builddir}/php-7.1.11/ext/pdo_pgsql/modules/*.so  %{buildroot}/usr/lib64/php/modules/
install -m 0644 %{_builddir}/php-7.1.11/ext/pgsql/modules/*.so  %{buildroot}/usr/lib64/php/modules/

%files
/etc/php.d/20-pgsql.ini
/etc/php.d/30-pdo_pgsql.ini
/usr/lib64/php/modules/pdo_pgsql.so
/usr/lib64/php/modules/pgsql.so
%changelog
* Fri Nov 3 2017 Alexey Podyapolsky <alpody@yandex.ru> - 0.0.3-1
- Add php sources. Extension compiling  
* Fri Nov 3 2017 Alexey Podyapolsky <alpody@yandex.ru> - 0.0.2-1
- Package with static embeded php extensions
* Fri Nov 3 2017 Alexey Podyapolsky <alpody@yandex.ru> - 0.0.1-1
- First rpm package
