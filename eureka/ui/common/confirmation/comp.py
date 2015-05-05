# -*- coding: utf-8 -*-
# =-
# Copyright Solocal Group (2015)
#
# eureka@solocal.com
#
# This software is a computer program whose purpose is to provide a full
# featured participative innovation solution within your organization.
#
# This software is governed by the CeCILL license under French law and
# abiding by the rules of distribution of free software.  You can  use,
# modify and/ or redistribute the software under the terms of the CeCILL
# license as circulated by CEA, CNRS and INRIA at the following URL
# "http://www.cecill.info".
#
# As a counterpart to the access to the source code and  rights to copy,
# modify and redistribute granted by the license, users are provided only
# with a limited warranty  and the software's author,  the holder of the
# economic rights,  and the successive licensors  have only  limited
# liability.
#
# In this respect, the user's attention is drawn to the risks associated
# with loading,  using,  modifying and/or developing or reproducing the
# software by the user in light of its specific status of free software,
# that may mean  that it is complicated to manipulate,  and  that  also
# therefore means  that it is reserved for developers  and  experienced
# professionals having in-depth computer knowledge. Users are therefore
# encouraged to load and test the software's suitability as regards their
# requirements in conditions enabling the security of their systems and/or
# data to be ensured and,  more generally, to use and operate it in the
# same conditions as regards security.
#
# The fact that you are presently reading this means that you have had
# knowledge of the CeCILL license and that you accept its terms.
# =-

class Confirmation(object):
    """A simple editor used to confirm an action.

    Its UI can be customized using the following CSS rules:
      - ``div.confirmation`` -- its root element
      - ``div.buttons`` -- the response buttons box
    """

    def __init__(self, message, confirm_text, cancel_text, kind='warning'):
        """Initializer.

        Parameters:
          - ``message`` -- the confirmation message
          - ``confirm_text`` -- the confirmation action text
          - ``cancel_text`` -- the cancel action text
          - ``kind`` -- the kind of confirmation message. Equivalent to the CSS class
            applied to the message.
        """
        self.message = message
        self.confirm_text = confirm_text
        self.cancel_text = cancel_text
        self.kind = kind