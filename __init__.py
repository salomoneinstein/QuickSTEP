# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Step
                                 A QGIS plugin
 Accuracy assessment of object-based image classification
                             -------------------
        begin                : 2016-05-25
        copyright            : (C) 2016 by Salomón Ramírez; Ivan Lizarazo/Universidad Distrital Francisco José de Caldas, Colombia; Universidad Nacional, Colombia
        email                : seramirezf@correo.udistrital.edu.co, ializarazos@unal.edu.co
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load QuickSTEP class from file Step.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .step_geobia import QuickSTEP
    return QuickSTEP(iface)
