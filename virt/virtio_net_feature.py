#!/usr/bin/env python3
import sys
# features extract from cmd 'grep "define.*VIRTIO.*_F_" include/uapi/linux/virtio_*.h' in kernel source
virtio_net_features = {
"VIRTIO_NET_F_CSUM": 0 ,
"VIRTIO_NET_F_GUEST_CSUM": 1 ,
"VIRTIO_NET_F_CTRL_GUEST_OFFLOADS": 2 ,
"VIRTIO_NET_F_MTU": 3 ,
"VIRTIO_NET_F_MAC": 5 ,
"VIRTIO_NET_F_GUEST_TSO4": 7 ,
"VIRTIO_NET_F_GUEST_TSO6": 8 ,
"VIRTIO_NET_F_GUEST_ECN": 9 ,
"VIRTIO_NET_F_GUEST_UFO": 10 ,
"VIRTIO_NET_F_HOST_TSO4": 11 ,
"VIRTIO_NET_F_HOST_TSO6": 12 ,
"VIRTIO_NET_F_HOST_ECN": 13 ,
"VIRTIO_NET_F_HOST_UFO": 14 ,
"VIRTIO_NET_F_MRG_RXBUF": 15 ,
"VIRTIO_NET_F_STATUS": 16 ,
"VIRTIO_NET_F_CTRL_VQ": 17 ,
"VIRTIO_NET_F_CTRL_RX": 18 ,
"VIRTIO_NET_F_CTRL_VLAN": 19 ,
"VIRTIO_NET_F_CTRL_RX_EXTRA": 20 ,
"VIRTIO_NET_F_GUEST_ANNOUNCE": 21 ,
"VIRTIO_NET_F_MQ": 22 ,
"VIRTIO_NET_F_CTRL_MAC_ADDR": 23 ,
"VIRTIO_NET_F_NOTF_COAL": 53 ,
"VIRTIO_NET_F_GUEST_USO4": 54 ,
"VIRTIO_NET_F_GUEST_USO6": 55 ,
"VIRTIO_NET_F_HOST_USO": 56 ,
"VIRTIO_NET_F_HASH_REPORT": 57 ,
"VIRTIO_NET_F_GUEST_HDRLEN": 59 ,
"VIRTIO_NET_F_RSS": 60 ,
"VIRTIO_NET_F_RSC_EXT": 61 ,
"VIRTIO_NET_F_STANDBY": 62 ,
"VIRTIO_NET_F_SPEED_DUPLEX": 63 ,
"VIRTIO_NET_F_GSO": 6 ,
"VIRTIO_NET_HDR_F_NEEDS_CSUM": 1 ,
"VIRTIO_NET_HDR_F_DATA_VALID": 2 ,
"VIRTIO_NET_HDR_F_RSC_INFO": 4 
}

virtio_ring_features = {
"VIRTIO_RING_F_INDIRECT_DESC": 28 ,
"VIRTIO_RING_F_EVENT_IDX": 29
}

virtio_config_features = {
"VIRTIO_F_NOTIFY_ON_EMPTY": 24 ,
"VIRTIO_F_ANY_LAYOUT": 27 ,
"VIRTIO_F_VERSION_1": 32 ,
"VIRTIO_F_ACCESS_PLATFORM": 33 ,
"VIRTIO_F_IOMMU_PLATFORM": 33,
"VIRTIO_F_RING_PACKED": 34 ,
"VIRTIO_F_IN_ORDER": 35 ,
"VIRTIO_F_ORDER_PLATFORM": 36 ,
"VIRTIO_F_SR_IOV": 37 ,
"VIRTIO_F_NOTIFICATION_DATA": 38 ,
"VIRTIO_F_RING_RESET": 40
}

if len(sys.argv) < 2:
    print("usage: %s interface_name" % sys.argv[0])
    print("eg:\n %s eth0" % sys.argv[0])
    sys.exit(1)

intf = sys.argv[1]

feature_file = "/sys/class/net/%s/device/features" % intf
features_bits = open(feature_file).read().strip()

all_features = {}
all_features.update(virtio_net_features)
all_features.update(virtio_ring_features)
all_features.update(virtio_config_features)

print("feature bits: %s" % features_bits)
print("feature\tstatus")
for feature,idx in all_features.items():
    print("%s\t%s" % (feature, features_bits[idx]))

