FROM centos:7

MAINTAINER Blasto "pwentrys@gmail.com"

RUN yum -y -q install https://centos7.iuscommunity.org/ius-release.rpm && yum -q update
RUN yum -y -q install epel-release && yum -q clean all
RUN yum -y -q install python36u python36u-libs python36u-devel python36u-pip && yum -q clean all

# We copy just the requirements.txt first to leverage Docker cache
COPY . /app

WORKDIR /app

RUN pip3.6 install -r requirements.txt

ENTRYPOINT [ "python3.6" ]

CMD [ "run.py" ]
