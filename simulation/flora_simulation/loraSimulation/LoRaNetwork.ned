package loraSimulation;

import inet.networklayer.configurator.ipv4.Ipv4NetworkConfigurator;
import flora.LoRaPhy.LoRaMedium;
import flora.LoraNode.LoRaNode;
import flora.LoraNode.LoRaGW;

network LoRaNetwork
{
    parameters:
        int numberOfNodes = 4;
        int numberOfGateways = 1;
        int networkSizeX = 500;
        int networkSizeY = 500;
        @display("bgb=562,417");
    submodules:
        loRaNodes[numberOfNodes]: LoRaNode {
            @display("p=250+50*i,200");
        }
        loRaGW[numberOfGateways]: LoRaGW {
            @display("p=200,100");
        }
        LoRaMedium: LoRaMedium {
            @display("p=309,102");
        }
}
