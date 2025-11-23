FROM alpine:3.22.2

RUN apk update && \
	apk add texlive texlive-full && \
	apk add imagemagick && \
	apk add make

WORKDIR /root/diagrams

VOLUME ["/root/diagrams"]

CMD ["/bin/sh"]
