FROM centos:7

# YUM requires root 
USER 0

#2019/10/15:Python�p�Ƀ��|�W�g���ǉ�
RUN yum -y install https://centos7.iuscommunity.org/ius-release.rpm
    yum -y install python36u.x86_64 python36u-libs.x86_64 python36u-devel.x86_64 python36u-pip.noarch && \
    yum -y install httpd && \
    rm -rf /var/cache/yum


#�ȉ����X�̋L�q
#    yum -y install yum-utils && \
#    yum -y install gettext  && \
#    yum -y install hostname && \
#    yum -y install nss_wrapper && \
#    yum -y install bind-utils &&\
#    yum -y install httpd24 &&\ 
#    yum -y install httpd24-mod_ssl &&\ 
#    yum -y install httpd24-mod_auth_mellon &&\ 
#    yum -y install httpd &&\ 
#    yum -y install perl && \
#    yum -y install which && \
#    yum -y install unzip && \
#    yum -y install net-tools && \
#    yum -y install perl-DBI && \
#    rm -rf /var/cache/yum
#    /usr/libexec/httpd-prepare && rpm-file-permissions

RUN chmod 777 /run/httpd
RUN chmod 777 /var/log/httpd
ADD httpd.conf /etc/httpd/conf/httpd.conf
ADD index.html /var/www/html/index.html
ADD index.cgi /var/www/cgi-bin/index.cgi
RUN chmod 766 /var/www/html/index.html
RUN chmod 755 /var/www/cgi-bin/index.cgi


# CGI scripts go to /opt/rh/httpd24/root/var/www/cgi-bin/
#ADD share/cgi-bin ${HTTPD_DATA_ORIG_PATH}/cgi-bin/

# Static files go to /opt/rh/httpd24/root/var/www/html
#ADD share/html ${HTTPD_DATA_ORIG_PATH}/html

CMD /usr/sbin/httpd -k start && tail -f /dev/null
