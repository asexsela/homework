FROM centos:7

RUN curl -SL https://artifacts.opensearch.org/releases/bundle/opensearch/2.x/opensearch-2.x.repo -o /etc/yum.repos.d/opensearch-2.x.repo

RUN yum clean all

RUN yum install -y opensearch vim openssl

CMD ["/usr/sbin/init"]