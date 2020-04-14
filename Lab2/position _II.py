#!/usr/bin/python

'Setting position of the nodes'

from mininet.log import setLogLevel, info
from mn_wifi.cli import CLI_wifi
from mn_wifi.net import Mininet_wifi


def topology():

    net = Mininet_wifi()

    info("*** Creating nodes\n")
    net.addStation('sta1', mac='00:00:00:00:00:02', ip='10.0.0.1/8',
                   position='30,60,0')
    net.addStation('sta2', mac='00:00:00:00:00:03', ip='10.0.0.2/8',
                   position='70,30,0')
    ap1 = net.addAccessPoint('ap1', ssid='new-ssid', mode='g', channel='1',
                             failMode="standalone", position='50,50,0')
    h1 = net.addHost('h1', ip='10.0.0.3/8', position='10,30,0')

    net.setPropagationModel(model="logDistance", exp=4.5)

    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    info("*** Creating links\n")
    net.addLink(ap1, h1)

    net.plotGraph(max_x=100, max_y=100, max_z=100)

    info("*** Starting network\n")
    net.build()
    ap1.start([])

    info("*** Running CLI\n")
    CLI_wifi(net)

    info("*** Stopping network\n")
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    topology()
