#Before you run this code
#1. Download POEdit -https://poedit.en.softonic.com/download
#A tool to directly extract Unicode text from your source code and provide translations
#2. Save the .mo and .po files in '.\locale\hi_IN\LC_MESSAGES' as APPNAME.po
#3. Choose the source file -Piglatin_UI_Internationalized.py in my case
#  All the four strings are populated automatically, select the translations from "Translation Suggestions" on the right
#  save again
#5. Change the current locale from control panel to Hindi
#6. References-
#http://stackoverflow.com/questions/3837683/python-no-translation-file-found-for-domain-using-custom-locale-folder
#http://stackoverflow.com/questions/3191664/list-of-all-locales-and-their-short-codes

import Piglatin
import os
import locale
import gettext
from tkinter import *

os.environ.setdefault('LANG', 'en')

#http://www.isunshare.com/windows-10/change-system-locale-in-windows-10.html
#Since I am using windows 10
#I did not have Hindi language pack
#Control Panel -> Add a language-> Added Hindi by installing it 
#Get the current locale - I set it to 'Hindi' on the computer that you are working on
locale_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'locale\\')
APPNAME = 'Piglatin_UI_Internationalized'
current_locale, encoding = locale.getdefaultlocale()
print([current_locale])
print(locale_dir)
t = gettext.translation(APPNAME, locale_dir, [current_locale])
t.install()

#returns a unicode string
#whenever you use '_' prefixed to a string, you get a unicode string
#and gets the translations
_ = t.gettext

#Using the grid manager means that you create a widget,
#and use the grid method to tell the manager in which row
#and column to place them. The size of the grid doesn't have
#to be defined, because the manager automatically determines
#the best dimensions for the widgets used.
class GUIOutput(Frame):
    def __init__(self):
        #inherited from frame
        Frame.__init__(self)
        self.master.title(_('Piglatin Generator'))

        #If you want to make the widgets as wide as the parent widget, you have to use the fill=X option: 
        lengText = Label(self.master, text=_('English Text'))
        #Size of the label is 5 vertically - y and horizontally - x
        lengText.grid(row=0, column=0,  sticky = E)
        
        varToTranslate =  StringVar()
        #Enter the translated text
        text_sentencetotranslate = Entry(self.master, textvariable=varToTranslate) 
        text_sentencetotranslate.grid(row=0, column=1,  sticky = E)
        
        lpiglatinText = Label(self.master, text=_("Translated Text"))
        #sticky - expand the widget if the text is larger than widget
        lpiglatinText.grid(row=1, column=0, sticky=E)


        varTranslated =  StringVar()
        text_piglatinsentence = Entry(self.master, textvariable=varTranslated)
        text_piglatinsentence.grid(row=1, column=1, sticky = E)
        
        #Lambda to pass arguments
        translate = Button(self.master, text = _("Translate"), command = lambda: self.translate(varToTranslate, varTranslated))
        translate.grid(row=2, columnspan= 2, sticky = E)

        #Disable it so that the text cannot be changed
        text_piglatinsentence.config(state=DISABLED)
        
        quitpiglatin = Button(self.master, text = _("Quit"),  command = self.quitCallBack)
        quitpiglatin.grid(row=2, column=4, columnspan=4,  sticky = E)

        
        
    def translate(self, sentencetotranslate, piglatinsentence  ):
        #populate text box
        piglatinObject = Piglatin.PigLatinTranslate()
        piglatinsentence.set(piglatinObject.piglatinTranslateSentence(sentencetotranslate.get()))
        
        

    def quitCallBack(self):
        self.master.quit()
        self.master.destroy()




