# -*- coding: utf-8 -*-

from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import MAIN_DISPATCHER, CONFIG_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_3
from ryu.lib import hub


class PortMonitor(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]

    def __init__(self, *args, **kwargs):
        super(PortMonitor, self).__init__(*args, **kwargs)

        self.port_status = {}  # {dpid: {port: state}}
        self.monitor_thread = hub.spawn(self._monitor)

    # -----------------------------
    # CLEAN STATUS DISPLAY LOOP
    # -----------------------------
    def _monitor(self):
        while True:
            print("\n" + "="*40)
            print("      PORT STATUS MONITOR")
            print("="*40)

            if not self.port_status:
                print("No switches connected yet.")
            else:
                for dpid in self.port_status:
                    print("\nSwitch ID:", dpid)
                    print("-"*30)
                    print("{:<10} {:<10}".format("PORT", "STATE"))

                    for port, state in sorted(self.port_status[dpid].items()):
                        print("{:<10} {:<10}".format(port, state))

            print("="*40 + "\n")

            hub.sleep(5)

    # -----------------------------
    # SWITCH CONNECT EVENT
    # -----------------------------
    @set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER)
    def switch_features_handler(self, ev):
        datapath = ev.msg.datapath
        dpid = datapath.id

        print("[INFO] Switch connected:", dpid)
        self.port_status.setdefault(dpid, {})

    # -----------------------------
    # PORT STATUS EVENT HANDLER
    # -----------------------------
    @set_ev_cls(ofp_event.EventOFPPortStatus, MAIN_DISPATCHER)
    def port_status_handler(self, ev):
        msg = ev.msg
        datapath = msg.datapath
        dpid = datapath.id

        reason = msg.reason
        port_no = msg.desc.port_no
        ofproto = datapath.ofproto

        # Determine state
        if reason == ofproto.OFPPR_ADD:
            state = "UP"
            alert = "PORT ADDED"
        elif reason == ofproto.OFPPR_DELETE:
            state = "DOWN"
            alert = "PORT REMOVED"
        elif reason == ofproto.OFPPR_MODIFY:
            if msg.desc.state == ofproto.OFPPS_LINK_DOWN:
                state = "DOWN"
                alert = "PORT DOWN"
            else:
                state = "UP"
                alert = "PORT UP"
        else:
            state = "UNKNOWN"
            alert = "UNKNOWN EVENT"

        # Store state
        self.port_status.setdefault(dpid, {})
        self.port_status[dpid][port_no] = state

        # Logging
        print("[LOG] Switch {} | Port {} | State {}".format(dpid, port_no, state))

        # Alert
        print("[ALERT] {} → Switch {} Port {}".format(alert, dpid, port_no))
