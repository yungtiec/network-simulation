"""
Router Exercise Topology

https://github.com/mininet/openflow-tutorial/wiki/Router-Exercise

   host1(h1) -- switch(s1) -- host3(h3)
                   |
                 host2(h2)

$ sudo mn --custom ~/mininet/mytopo1.py --topo mytopo --mac --controller=remote,ip=127.0.0.1

"""

from mininet.topo import Topo

class MyTopo( Topo ):

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        host1 = self.addHost( 'h1', ip="10.0.1.100/24", defaultRoute = "via 10.0.1.1" )
        host2 = self.addHost( 'h2', ip="10.0.2.100/24", defaultRoute = "via 10.0.2.1" )
        host3 = self.addHost( 'h3', ip="10.0.3.100/24", defaultRoute = "via 10.0.3.1" )

        # Add hosts and switches
        switch1 = self.addSwitch( 's1' )

        # Add links
        self.addLink( 'h1', 's1')
        self.addLink( 'h2', 's1')
        self.addLink( 'h3', 's1')


topos = { 'mytopo': ( lambda: MyTopo() ) }