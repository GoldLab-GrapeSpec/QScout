# -*- coding: utf-8 -*-

"""
/***************************************************************************
 PinDropper
                                 A QGIS plugin
 Drops pins on semi-regular patterns
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2020-09-29
        copyright            : (C) 2020 by Joshua Evans
        email                : joshuaevanslowell@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

__author__ = 'Joshua Evans'
__date__ = '2020-09-29'
__copyright__ = '(C) 2020 by Joshua Evans'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

from qgis.core import QgsProcessingProvider
from .pin_dropper_algorithm import QScoutPinDropperAlgorithm
from .pin_locator_algorithm import QScoutPinLocatorAlgorithm
from .grid_aggregator_algorithm import QScoutGridAggregatorAlgorithm
from .drop_grab_aggregate_algorithm import QScoutDropGrabAggregateAlgoithm
from .locate_grab_aggregate_algorithm import QScoutLocateGrabAggregateAlgorithm
from .value_grabber_algorithm import QScoutValueGrabberAlgorithm

class QScoutProvider(QgsProcessingProvider):

    def __init__(self):
        """
        Default constructor.
        """
        QgsProcessingProvider.__init__(self)

    def unload(self):
        """
        Unloads the provider. Any tear-down steps required by the provider
        should be implemented here.
        """
        pass

    def loadAlgorithms(self):
        """
        Loads all algorithms belonging to this provider.
        """
        self.addAlgorithm(QScoutPinDropperAlgorithm())
        self.addAlgorithm(QScoutPinLocatorAlgorithm())
        self.addAlgorithm(QScoutGridAggregatorAlgorithm())
        self.addAlgorithm(QScoutValueGrabberAlgorithm())
        self.addAlgorithm(QScoutDropGrabAggregateAlgoithm())
        self.addAlgorithm(QScoutLocateGrabAggregateAlgorithm())
        # add additional algorithms here
        # self.addAlgorithm(MyOtherAlgorithm())

    def id(self):
        """
        Returns the unique provider id, used for identifying the provider. This
        string should be a unique, short, character only string, eg "qgis" or
        "gdal". This string should not be localised.
        """
        return 'QScout'

    def name(self):
        """
        Returns the provider name, which is used to describe the provider
        within the GUI.

        This string should be short (e.g. "Lastools") and localised.
        """
        return self.tr('QScout')

    def icon(self):
        """
        Should return a QIcon which is used for your provider inside
        the Processing toolbox.
        """
        return QgsProcessingProvider.icon(self)

    def longName(self):
        """
        Returns the a longer version of the provider name, which can include
        extra details such as version numbers. E.g. "Lastools LIDAR tools
        (version 2.2.1)". This string should be localised. The default
        implementation returns the same string as name().
        """
        return self.name()
