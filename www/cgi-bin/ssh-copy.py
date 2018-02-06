#!/usr/bin/python

cat ~/.ssh/id_rsa.pub | pssh -h /etc/ansible/hosts  -A -I -i '                                         \
      umask 077;                              \
      mkdir -p ~/.ssh;                        \
      afile=~/.ssh/authorized_keys;           \
      cat - >> $afile;                        \
      sort -u $afile -o $afile                \
    '

