import kivy

kivy.require('2.3.1')

import secrets
import string

from kivy.app import App
from kivy.clock import Clock
from kivy.core.clipboard import Clipboard
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_file('app/gui.kv')


class Root(BoxLayout):
	LETTERS = string.ascii_letters
	DIGITS = string.digits
	SIGNS = string.punctuation

	def __init__(self, **kwargs):
		super().__init__(**kwargs)

	def generate_password(self, length_text='8'):
		# Build symbol pool based on checkboxes defined in the KV file
		# Validate length_text (comes from TextInput.text)
		try:
			length = int(length_text)
		except Exception:
			length = 8

		# enforce sensible bounds
		if length < 4:
			length = 4
		if length > 64:
			length = 64

		# Access checkbox widgets by id from kv: ids.letters, ids.numbers, ids.symbols
		pool = ''
		try:
			if self.ids.letters.active:
				pool += self.LETTERS
		except Exception:
			# If ids.letters not found, include letters by default
			pool += self.LETTERS

		try:
			if self.ids.numbers.active:
				pool += self.DIGITS
		except Exception:
			pool += self.DIGITS

		try:
			if self.ids.symbols.active:
				pool += self.SIGNS
		except Exception:
			# don't add signs if not present
			pass

		if not pool:
			# If nothing selected, fallback to letters+digits
			pool = self.LETTERS + self.DIGITS

		# Keep generating until basic conditions met (if applicable)
		while True:
			password = ''.join(secrets.choice(pool) for _ in range(length))

			# If letters are in pool, ensure both cases exist when ascii_letters used
			cond_letters = True
			if any(c in self.LETTERS for c in pool):
				cond_letters = any(ch.isupper() for ch in password) and any(
					ch.islower() for ch in password
				)

			cond_digits = True
			if any(c in self.DIGITS for c in pool):
				cond_digits = sum(ch.isdigit() for ch in password) >= 1

			if cond_letters and cond_digits:
				break

		return password

	def condition(self, password):
		pass

	def copy_password(self, password, button_widget=None):
		"""Copy `password` to the clipboard and give brief feedback on the button.

		If `button_widget` is provided (the Copy button), its text will change to
		'Copied' for 1.5 seconds.
		"""
		if not password:
			return

		try:
			Clipboard.copy(password)
		except Exception:
			# Clipboard may fail on some platforms; just return silently
			return

		if button_widget is not None:
			orig = button_widget.text
			button_widget.text = 'Copied'
			# restore text after 1.5 seconds
			Clock.schedule_once(lambda dt: setattr(button_widget, 'text', orig), 1.5)


class Generator(App):
	def build(self):
		Window.size = (275 * 2, 183 * 2)
		return Root()
