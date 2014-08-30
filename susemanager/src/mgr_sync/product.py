# -*- coding: utf-8 -*-
#
# Copyright (c) 2014 SUSE
#
# This software is licensed to you under the GNU General Public License,
# version 2 (GPLv2). There is NO WARRANTY for this software, express or
# implied, including the implied warranties of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. You should have received a copy of GPLv2
# along with this software; if not, see
# http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.
#
# SUSE trademarks are not licensed under GPLv2. No permission is
# granted to use or replicate SUSE trademarks that are incorporated
# in this software or its documentation.

from enum import Enum

from spacewalk.susemanager.mgr_sync.channel import Channel


class Product(object):

    class Status(str, Enum):
        INSTALLED = "INSTALLED"
        AVAILABLE = "AVAILABLE"

    def __init__(self, data):
        self.arch = data["arch"]
        self.friendly_name = data["friendly_name"]
        self.status = Product.Status(data["status"].upper())
        self.extensions = []
        self._parse_extensions(data["extensions"])
        self.channels = [Channel(channel) for channel in data['channels']]

    @property
    def short_status(self):
        # pylint: disable=E1101
        if self.status == Product.Status.AVAILABLE:
            return "[ ]"
        else:
            return "[%s]" % str(self.status.value)[0]

    def to_ascii_row(self):
        return "{0} {1} ({2})".format(self.short_status, self.friendly_name,
                                      self.arch)

    def to_stdout(self, indentation_level=0, filter=None,
                  interactive_number=[]):
        prefix = indentation_level * "  "
        if interactive_number:
            if self.status == Product.Status.INSTALLED:
                prefix = "     " + prefix
            else:
                prefix = "%.3d) %s" % (interactive_number[0], prefix)
                interactive_number[0] += 1

        if not filter or self.matches_filter(filter):
            print(prefix + self.to_ascii_row())
            indentation_level += 1
            for ext in self.extensions:
                ext.to_stdout(indentation_level=indentation_level,
                              filter=filter,
                              interactive_number=interactive_number)

    def _parse_extensions(self, data):
        for extension in data:
            self.extensions.append(Product(extension))

    def matches_filter(self, filter):
        if not self.extensions:
            return filter in self.to_ascii_row().lower()
        else:
            for ext in self.extensions:
                if ext.matches_filter(filter):
                    return True

        return False

def find_product_by_label(label, products):
    """
    Find a product with the specified label.
    """

    for product in products:
        if product.label == label:
            return product
        match = find_product_by_label(label, product.extension)
        if match:
            return match

    return None

def parse_products(data):
    """
    Parses the data returned by SUSE Manager list products API.
    Returns a list of the Products.
    """

    products = []

    for p in data:
        products.append(Product(p))

    return products

