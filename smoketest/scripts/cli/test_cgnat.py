#!/usr/bin/env python3
#
# Copyright (C) 2024 VyOS maintainers and contributors
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 or later as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import unittest

from base_vyostest_shim import VyOSUnitTestSHIM
from vyos.configsession import ConfigSessionError


base_path = ['nat', 'cgnat']
nftables_cgnat_config = '/run/nftables-cgnat.nft'


class TestCGNAT(VyOSUnitTestSHIM.TestCase):
    @classmethod
    def setUpClass(cls):
        super(TestCGNAT, cls).setUpClass()

        # ensure we can also run this test on a live system - so lets clean
        # out the current configuration :)
        cls.cli_delete(cls, base_path)

    def tearDown(self):
        self.cli_delete(base_path)
        self.cli_commit()
        self.assertFalse(os.path.exists(nftables_cgnat_config))

    def test_cgnat(self):
        internal_name = 'vyos-int-01'
        external_name = 'vyos-ext-01'
        internal_net = '100.64.0.0/29'
        external_net = '192.0.2.1-192.0.2.2'
        external_ports = '40000-60000'
        ports_per_subscriber = '5000'
        rule = '100'

        nftables_search = [
            ['map tcp_nat_map'],
            ['map udp_nat_map'],
            ['map icmp_nat_map'],
            ['map other_nat_map'],
            ['100.64.0.0 : 192.0.2.1 . 40000-44999'],
            ['100.64.0.1 : 192.0.2.1 . 45000-49999'],
            ['100.64.0.2 : 192.0.2.1 . 50000-54999'],
            ['100.64.0.3 : 192.0.2.1 . 55000-59999'],
            ['100.64.0.4 : 192.0.2.2 . 40000-44999'],
            ['100.64.0.5 : 192.0.2.2 . 45000-49999'],
            ['100.64.0.6 : 192.0.2.2 . 50000-54999'],
            ['100.64.0.7 : 192.0.2.2 . 55000-59999'],
            ['chain POSTROUTING'],
            ['type nat hook postrouting priority srcnat'],
            ['ip protocol tcp counter snat ip to ip saddr map @tcp_nat_map'],
            ['ip protocol udp counter snat ip to ip saddr map @udp_nat_map'],
            ['ip protocol icmp counter snat ip to ip saddr map @icmp_nat_map'],
            ['counter snat ip to ip saddr map @other_nat_map'],
        ]

        self.cli_set(base_path + ['pool', 'external', external_name, 'external-port-range', external_ports])
        self.cli_set(base_path + ['pool', 'external', external_name, 'range', external_net])

        # allocation out of the available ports
        with self.assertRaises(ConfigSessionError):
            self.cli_set(base_path + ['pool', 'external', external_name, 'per-user-limit', 'port', '8000'])
            self.cli_commit()
        self.cli_set(base_path + ['pool', 'external', external_name, 'per-user-limit', 'port', ports_per_subscriber])

        # internal pool not set
        with self.assertRaises(ConfigSessionError):
            self.cli_commit()
        self.cli_set(base_path + ['pool', 'internal', internal_name, 'range', internal_net])

        self.cli_set(base_path + ['rule', rule, 'source', 'pool', internal_name])
        # non-exist translation pool
        with self.assertRaises(ConfigSessionError):
            self.cli_set(base_path + ['rule', rule, 'translation', 'pool', 'fake-pool'])
            self.cli_commit()

        self.cli_set(base_path + ['rule', rule, 'translation', 'pool', external_name])
        self.cli_commit()

        self.verify_nftables(nftables_search, 'ip cgnat', inverse=False, args='-s')


if __name__ == '__main__':
    unittest.main(verbosity=2)
