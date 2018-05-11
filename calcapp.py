# Cálculo de doses 

import kivy 
from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.button import Button 
from kivy.uix.screenmanager import ScreenManager, Screen  
from kivy.uix.scrollview import ScrollView 
from kivy.uix.textinput import TextInput 
from kivy.core.window import Window




class Manager(ScreenManager): 
	pass 

class Menu(Screen): 
	pass 

class Dipirona(Screen):
	def calc_dipirona(self):
		peso = self.ids.textinput.text 
		peso = float(peso)
		dose = peso * 0.8
		if dose >= 40 : 
			dose = 40
		dose = str(int(dose))
		self.ids.label_dose_dipirona.text = dose 
		return 0  

class Paracetamol(Screen):
	def calc_paracetamol(self):
		peso = self.ids.textinput.text 
		peso = float(peso)
		dose = peso * 1
		if dose >= 40 : 
			dose = 40
		dose = str(int(dose))
		self.ids.label_dose_paracetamol.text = dose 
		return 0 		

class Prednisolona(Screen): 
	def calc_prednisolona(self):
		peso = self.ids.textinput.text 
		peso = float(peso)
		dose = peso  / 3
		dose = str(int(dose))
		self.ids.label_dose_prednisolona.text = dose 
		return 0 		

class Dexclorferinamina(Screen):
	def calc_dexclorferinamina(self):
		peso = self.ids.textinput.text 
		peso = float(peso)
		dose = (peso  * 0.4) / 3  
		dose = str(int(dose))
		self.ids.label_dose_dexclorferinamina.text = dose 
		return 0 

class Hidroxizina(Screen):
	def calc_hidroxizina(self):
		peso = self.ids.textinput.text 
		peso = float(peso)
		dose = peso  / 3  
		dose = str(int(dose))
		self.ids.label_dose_hidroxizina.text = dose 
		return 0 

class Bromoprida(Screen): 
	def calc_bromoprida(self): 
		peso = self.ids.textinput.text 
		peso = float(peso)
		dose = peso 
		dose = str(int(dose))
		self.ids.label_dose_bromoprida.text = dose 
		return 0 

class SROP(Screen) : 
	def calc_srop(self): 
		peso = self.ids.textinput.text 
		peso = float(peso)
		dose = peso * 10 
		dose = str(int(dose))
		self.ids.label_dose_srop.text = dose 
		return 0 

class SROT(Screen) : 
	def calc_srot(self): 
		peso = self.ids.textinput.text 
		peso = float(peso)
		dose = (peso * 25 ) / 4 
		dose = str(int(dose))
		self.ids.label_dose_srot.text = dose 
		return 0

class Sulfato(Screen) : 
	def calc_sulfato(self): 
		peso = self.ids.textinput.text 
		peso = float(peso)
		dose = peso  
		dose = str(int(dose))
		self.ids.label_dose_sulfato.text = dose 
		return 0

class CalcApp(App): 
	def build(self): 
		return Manager()

if __name__ == '__main__':
	Window.clearcolor = (1,1,1,1)
	CalcApp().run()