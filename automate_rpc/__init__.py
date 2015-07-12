# -*- coding: utf-8 -*-
# (c) 2015 Tuomas Airaksinen
#
# This file is part of automate-rpc.
#
# automate-rpc is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# automate-rpc is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with automate-rpc.  If not, see <http://www.gnu.org/licenses/>.

__author__ = "Tuomas Airaksinen"
__copyright__ = "Copyright 2015, Tuomas Airaksinen"
__credits__ = []
__license__ = "GPL"
__version__ = '0.9.2'
__maintainer__ = "Tuomas Airaksinen"
__email__ = "tuomas.airaksinen@gmail.com"
__status__ = "Beta"

from .rpc import RpcService

extension_classes = [RpcService]
