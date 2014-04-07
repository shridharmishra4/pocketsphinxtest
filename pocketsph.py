#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pocketsph.py
#  
#  Copyright 2014 Shridhar Mishra <shridhar@shridhar>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import sys
from pocketsphinx import Decoder
 
if __name__ == "__main__":
 
   hmdir = "/usr/share/pocketsphinx/model/hmm/en_US/hub4wsj_sc_8k"
   lmdir = "/usr/share/pocketsphinx/model/lm/en_US/hub4.5000.DMP"
   dictd = "/usr/share/pocketsphinx/model/lm/en_US/cmu07a.dic"
   wavfile = "/home/shridhar/web/Java Tutorial for Beginners.wav"
 
   speechRec = Decoder(hmm = hmdir, lm = lmdir, dict = dictd)
   wavFile = file(wavfile,'rb')
   speechRec.decode_raw(wavFile)
   ##print speechRec
   result = speechRec.get_hyp()
   ##print "popat"
   print "Recognised text from the converted video file"
   
   print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
   
 
   print result[0]
   print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"

	
