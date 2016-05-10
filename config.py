import sys
import os
import datetime

import pyauto
from keyhac import *

#入力はキーボードそのままのもの
#出力はDvorakJに渡すもの
#DvorakJを起動してからKeyhacを起動する

def configure(keymap):

    #モディファイアキーの追加
    #無変換
    keymap.defineModifier( 29, "LUser0" )
    #変換
    keymap.defineModifier( 28, "RUser0" )

    #キーマップの追加(グローバル)
    keymap_global = keymap.defineWindowKeymap()

    keymap_global[ "C-S-Z"   ] = keymap.command_ClipboardList
    keymap_global[ "C-S-X"   ] = keymap.command_ClipboardRotate   # Move the most recent history to tail


    #無変換、変換、カタカナひらがな
    keymap_global[ "O-(29)" ] = "Back"
    keymap_global[ "O-(28)" ] = "Tab"
    keymap_global[ "(242)"  ] = "Enter"

    #無変換→変換、変換→無変換
    keymap_global[ "LUser0-O-(28)" ] = "Tab"
    keymap_global[ "RUser0-O-(29)" ] = "Esc"

    #記号をホームポジションへ
    keymap_global[ "User0-A" ] = "S-1"
    keymap_global[ "User0-S" ] = "S-2"
    keymap_global[ "User0-D" ] = "S-3"
    keymap_global[ "User0-F" ] = "S-4"
    keymap_global[ "User0-G" ] = "S-5"
    keymap_global[ "User0-H" ] = "S-6"
    keymap_global[ "User0-J" ] = "S-7"
    keymap_global[ "User0-K" ] = "S-8"
    keymap_global[ "User0-L" ] = "S-9"
    keymap_global[ "User0-Semicolon" ] = "S-0"

    keymap_global[ "User0-Q" ] = "CloseBracket"
    keymap_global[ "User0-W" ] = "S-CloseBracket"
    keymap_global[ "User0-E" ] = "OpenBracket"
    keymap_global[ "User0-R" ] = "S-OpenBracket"
    keymap_global[ "User0-T" ] = "Yen"
    keymap_global[ "User0-Y" ] = "S-Yen"
    keymap_global[ "User0-U" ] = "S-Minus"
    keymap_global[ "User0-I" ] = "S-Caret"
    keymap_global[ "User0-O" ] = "Minus"
    keymap_global[ "User0-P" ] = "Caret"

    keymap_global[ "User0-M"      ] = "Left"
    keymap_global[ "User0-Comma"  ] = "Down"
    keymap_global[ "User0-Period" ] = "Up"
    keymap_global[ "User0-Slash"  ] = "Right"  

